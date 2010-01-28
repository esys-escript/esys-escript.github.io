
/*******************************************************
*
* Copyright (c) 2003-2010 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/

#include <escriptexport/EscriptDataset.h>
#include <escriptexport/DataVar.h>
#include <escriptexport/ElementData.h>
#include <escriptexport/FinleyMesh.h>
#include <escriptexport/NodeData.h>
#include <escript/Data.h>

#include <iostream>
#include <numeric> // for std::accumulate

#if USE_SILO
#include <silo.h>

#if HAVE_MPI
#include <pmpio.h>
#endif

#endif // USE_SILO

using namespace std;

namespace escriptexport {

const char* MESH_VARS = "mesh_vars/";
const int NUM_SILO_FILES = 1;

//
// Default constructor
//
EscriptDataset::EscriptDataset() :
    numParts(0),
    cycle(0),
    time(0.),
    keepMesh(false),
    externalMesh(false),
    mpiRank(0),
    mpiSize(1)
{
}

//
// Constructor with communicator
//
#if HAVE_MPI
EscriptDataset::EscriptDataset(MPI_Comm comm) :
    numParts(0),
    cycle(0),
    time(0.),
    keepMesh(false),
    externalMesh(false),
    mpiComm(comm)
{
    MPI_Comm_rank(mpiComm, &mpiRank);
    MPI_Comm_size(mpiComm, &mpiSize);
}
#endif

//
// Destructor
//
EscriptDataset::~EscriptDataset()
{
}

//
//
//
bool EscriptDataset::initFromEscript(escript::const_Domain_ptr escriptDomain,
                                     DataVec& escriptVars,
                                     const StringVec& varNames)
{
    int myError;
    numParts = 1;
    FinleyMesh_ptr mesh(new FinleyMesh());
    if (mesh->initFromEscript(escriptDomain)) {
        if (mpiSize > 1)
            mesh->reorderGhostZones(mpiRank);
        meshBlocks.push_back(mesh);
        myError = false;
    } else {
        mesh.reset();
        myError = true;
    }

    int gError;
#if HAVE_MPI
    MPI_Allreduce(&myError, &gError, 1, MPI_LOGICAL, MPI_LOR, mpiComm);
#else
    gError = myError;
#endif

    if (!gError) {
        // initialize variables
        DataVec::iterator varIt = escriptVars.begin();
        StringVec::const_iterator nameIt = varNames.begin();
        for (; varIt != escriptVars.end(); varIt++, nameIt++) {
            VarInfo vi;
            vi.varName = *nameIt;

            DataVar_ptr var(new DataVar(vi.varName));
            if (var->initFromEscript(*varIt, mesh)) {
                vi.dataBlocks.push_back(var);
                updateSampleDistribution(vi);
                vi.valid = true;
            } else {
                var.reset();
                vi.valid = false;
            }
            variables.push_back(vi);
        }

        // Convert mesh data to variables
        convertMeshVariables();
    }

    return !gError;
}

//
//
//
bool EscriptDataset::loadNetCDF(const string meshFilePattern,
                                const StringVec& varFiles,
                                const StringVec& varNames, int nBlocks)
{
    if (mpiSize > 1 && nBlocks != mpiSize) {
        cerr << "Cannot load " << nBlocks << " chunks on " << mpiSize
            << " MPI ranks!" << endl;
        return false;
    }

    numParts = nBlocks;
    meshFmt = meshFilePattern;
    
    // Load the mesh files
    if (!loadMeshFromNetCDF()) {
        cerr << "Reading the domain failed." << endl;
        return false;
    }

    // Convert mesh data to variables
    convertMeshVariables();

    // Load the variables
    StringVec::const_iterator fileIt = varFiles.begin();
    StringVec::const_iterator nameIt = varNames.begin();
    for (; fileIt != varFiles.end(); fileIt++, nameIt++) {
        loadVarFromNetCDF(*fileIt, *nameIt);
    }

    return true;
}

//
// Load only variables using provided mesh
//
bool EscriptDataset::loadNetCDF(const MeshBlocks& mesh,
                                const StringVec& varFiles,
                                const StringVec& varNames)
{
    if (mpiSize > 1 && mesh.size() > 1) {
        cerr << "Can only read one mesh block per rank when using MPI!" << endl;
        return false;
    }

    externalMesh = true;
    meshBlocks = mesh;
    numParts = meshBlocks.size();
    keepMesh = true;

    // Load the variables
    StringVec::const_iterator fileIt = varFiles.begin();
    StringVec::const_iterator nameIt = varNames.begin();
    for (; fileIt != varFiles.end(); fileIt++, nameIt++) {
        loadVarFromNetCDF(*fileIt, *nameIt);
    }

    return true;
}

//
//
//
bool EscriptDataset::saveSilo(string fileName, bool useMultiMesh)
{
#if USE_SILO
    if (numParts == 0)
        return false;

    const char* blockDirFmt = "/block%04d";
    string siloPath;
    DBfile* dbfile = NULL;
#if HAVE_MPI
    PMPIO_baton_t* baton = NULL;
#endif

    if (mpiSize > 1) {
#if HAVE_MPI
        baton = PMPIO_Init(NUM_SILO_FILES, PMPIO_WRITE,
                    mpiComm, 0x1337, PMPIO_DefaultCreate, PMPIO_DefaultOpen,
                    PMPIO_DefaultClose, NULL);
        if (baton) {
            char str[64];
            snprintf(str, 64, blockDirFmt, PMPIO_RankInGroup(baton, mpiRank));
            siloPath = str;
            dbfile = (DBfile*) PMPIO_WaitForBaton(
                    baton, fileName.c_str(), siloPath.c_str());
        }
#endif
    } else {
        dbfile = DBCreate(fileName.c_str(), DB_CLOBBER, DB_LOCAL,
                "escriptData", DB_PDB);
    }

    if (!dbfile) {
        cerr << "Could not create Silo file." << endl;
        return false;
    }

    MeshBlocks::iterator meshIt;
    VarVector::iterator viIt;
    int idx = 0;
    for (meshIt = meshBlocks.begin(); meshIt != meshBlocks.end(); meshIt++, idx++) {
        if (mpiSize == 1) {
            char str[64];
            snprintf(str, 64, blockDirFmt, idx);
            siloPath = str;
            DBMkdir(dbfile, siloPath.c_str());
        }
        // write block of the mesh if we don't use an external mesh
        if (!externalMesh) {
            if (! (*meshIt)->writeToSilo(dbfile, siloPath)) {
                cerr << "Error writing block " << idx << " of mesh to Silo file!\n";
                break;
            }
        }

        // write variables for current mesh block
        for (viIt = variables.begin(); viIt != variables.end(); viIt++) {
            // do not attempt to write this variable if previous steps failed
            if (!(*viIt).valid) continue;
            DataVar_ptr var = (*viIt).dataBlocks[idx];
            if (!var->writeToSilo(dbfile, siloPath)) {
                cerr << "Error writing block " << idx << " of '"
                    << var->getName() << "' to Silo file!" << endl;
                (*viIt).valid = false;
            }
        }
    }

    // rank 0 writes additional data that describe how the parts fit together
    if (mpiRank == 0) {
        if (useMultiMesh) {
            const StringVec& meshNames = meshBlocks[0]->getMeshNames();
            StringVec::const_iterator it;
            for (it = meshNames.begin(); it != meshNames.end(); it++)
                putSiloMultiMesh(dbfile, *it);

            DBMkdir(dbfile, MESH_VARS);
            for (viIt = meshVariables.begin(); viIt != meshVariables.end(); viIt++)
                putSiloMultiVar(dbfile, *viIt, true);

            for (viIt = variables.begin(); viIt != variables.end(); viIt++) {
                if (!(*viIt).valid) continue;
                DataVar_ptr var = (*viIt).dataBlocks[0];
                if (var->getRank() < 2)
                    putSiloMultiVar(dbfile, *viIt);
                else
                    putSiloMultiTensor(dbfile, *viIt);
            }
        }

        vector<char*> tensorNames;
        vector<string> tensorDefStrings;
        vector<char*> tensorDefs;

        // collect tensors for their Silo definitions
        for (viIt = variables.begin(); viIt != variables.end(); viIt++) {
            if (!(*viIt).valid) continue;
            DataVar_ptr var = (*viIt).dataBlocks[0];
            if (var->getRank() == 2) {
                tensorDefStrings.push_back(var->getTensorDef());
                tensorDefs.push_back((char*)tensorDefStrings.back().c_str());
                tensorNames.push_back((char*)var->getName().c_str());
            }
        }

        if (tensorDefs.size()) {
            DBSetDir(dbfile, "/");
            DBoptlist* optList = DBMakeOptlist(2);
            DBAddOption(optList, DBOPT_CYCLE, &cycle);
            DBAddOption(optList, DBOPT_DTIME, &time);
            vector<DBoptlist*> defOpts(tensorDefs.size(), optList);
            vector<int> defTypes(tensorDefs.size(), DB_VARTYPE_TENSOR);
            DBPutDefvars(dbfile, "tensors", tensorDefs.size(), &tensorNames[0],
                    &defTypes[0], &tensorDefs[0], &defOpts[0]);
            DBFreeOptlist(optList);
        }
    }

    if (mpiSize > 1) {
#if HAVE_MPI
        PMPIO_HandOffBaton(baton, dbfile);
        PMPIO_Finish(baton);
#endif
    } else {
        DBClose(dbfile);
    }

    return true;

#else // !USE_SILO
    return false;
#endif
}

//
//
//
bool EscriptDataset::saveVTK(string fileName)
{
    if (numParts == 0)
        return false;

    string meshName;

    // determine mesh type and variables to write
    VarVector nodalVars, cellVars;
    VarVector::iterator viIt;
    for (viIt = variables.begin(); viIt != variables.end(); viIt++) {
        const DataBlocks& varBlocks = viIt->dataBlocks;
        // skip empty variable
        int numSamples = accumulate(viIt->sampleDistribution.begin(),
                viIt->sampleDistribution.end(), 0);
        if (numSamples == 0 || !viIt->valid) {
            continue;
        }
        string tmpName = varBlocks[0]->getMeshName();
        if (meshName != "") {
            if (meshName != tmpName) {
                cerr << "VTK supports only one mesh! Skipping variable "
                    << varBlocks[0]->getName() << " on " << tmpName << endl;
                continue;
            }
        } else {
            meshName = tmpName;
        }

        if (varBlocks[0]->isNodeCentered()) {
            nodalVars.push_back(*viIt);
        } else {
            cellVars.push_back(*viIt);
        }
    }

    // no valid variables so use default mesh
    if (meshName == "")
        meshName = "Elements";

    // add mesh variables
    for (viIt = meshVariables.begin(); viIt != meshVariables.end(); viIt++) {
        DataVar_ptr var = viIt->dataBlocks[0];
        if (meshName == var->getMeshName()) {
            VarInfo vi = *viIt;
            vi.varName = string(MESH_VARS)+vi.varName;
            if (var->isNodeCentered()) {
                nodalVars.push_back(vi);
            } else {
                cellVars.push_back(vi);
            }
        }
    }

    MeshBlocks::iterator meshIt;
    int gNumPoints;
    int gNumCells = 0;
    int gCellSizeAndType[2] = { 0, 0 };

#if HAVE_MPI
    // remove file first if it exists
    int error = 0;
    int mpiErr;
    if (mpiRank == 0) {
        ifstream f(fileName.c_str());
        if (f.is_open()) {
            f.close();
            if (remove(fileName.c_str())) {
                error=1;
            }
        }
    }
    MPI_Allreduce(&error, &mpiErr, 1, MPI_INT, MPI_MAX, mpiComm);
    if (mpiErr != 0) {
        cerr << "Error removing " << fileName << "!" << endl;
        return false;
    }

    MPI_File mpiFileHandle;
    MPI_Info mpiInfo = MPI_INFO_NULL;
    int amode = MPI_MODE_CREATE|MPI_MODE_WRONLY|MPI_MODE_UNIQUE_OPEN;
    mpiErr = MPI_File_open(mpiComm, const_cast<char*>(fileName.c_str()),
            amode, mpiInfo, &mpiFileHandle);
    if (mpiErr == MPI_SUCCESS) {
        mpiErr = MPI_File_set_view(mpiFileHandle, 0, MPI_CHAR, MPI_CHAR,
                const_cast<char*>("native"), mpiInfo);
    }
    if (mpiErr != MPI_SUCCESS) {
        cerr << "Error opening " << fileName << " for parallel writing!" << endl;
        return false;
    }

    int myNumCells;
    if (mpiSize > 1)
        meshBlocks[0]->removeGhostZones(mpiRank);
    ElementData_ptr elements = meshBlocks[0]->getElementsByName(meshName);
    myNumCells = elements->getNumElements();
    MPI_Reduce(&myNumCells, &gNumCells, 1, MPI_INT, MPI_SUM, 0, mpiComm);

    int myCellSizeAndType[2];
    myCellSizeAndType[0] = elements->getNodesPerElement();
    myCellSizeAndType[1] = elements->getType();

    // rank 0 needs to know element type and size but it's possible that this
    // information is only available on other ranks (value=0) so retrieve it
    MPI_Reduce(&myCellSizeAndType, &gCellSizeAndType, 2, MPI_INT, MPI_MAX, 0,
            mpiComm);

    // these definitions make the code more readable and life easier -
    // WRITE_ORDERED causes all ranks to write the contents of the stream while
    // WRITE_SHARED should only be called for rank 0.
#define WRITE_ORDERED(_stream) \
    do {\
        MPI_Status mpiStatus;\
        string contents = _stream.str();\
        mpiErr = MPI_File_write_ordered(\
            mpiFileHandle, const_cast<char*>(contents.c_str()),\
            contents.length(), MPI_CHAR, &mpiStatus);\
        _stream.str("");\
    } while(0)

#define WRITE_SHARED(_stream) \
    do {\
        MPI_Status mpiStatus;\
        string contents = _stream.str();\
        mpiErr = MPI_File_write_shared(\
            mpiFileHandle, const_cast<char*>(contents.c_str()),\
            contents.length(), MPI_CHAR, &mpiStatus);\
        _stream.str("");\
    } while(0)

#else /*********** non-MPI version follows ************/

    ofstream ofs(fileName.c_str());

    int idx = 0;
    for (meshIt = meshBlocks.begin(); meshIt != meshBlocks.end(); meshIt++, idx++) {
        if (numParts > 1)
            (*meshIt)->removeGhostZones(idx);
        ElementData_ptr elements = (*meshIt)->getElementsByName(meshName);
        gNumCells += elements->getNumElements();
        if (gCellSizeAndType[0] == 0)
            gCellSizeAndType[0] = elements->getNodesPerElement();
        if (gCellSizeAndType[1] == 0)
            gCellSizeAndType[1] = elements->getType();
    }

    // the non-MPI versions of WRITE_ORDERED and WRITE_SHARED are
    // identical.
#define WRITE_ORDERED(_stream) \
    do {\
        ofs << _stream.str();\
        _stream.str("");\
    } while(0)

#define WRITE_SHARED(_stream) \
    do {\
        ofs << _stream.str();\
        _stream.str("");\
    } while(0)

#endif

    gNumPoints = meshBlocks[0]->getNodes()->getGlobalNumNodes();

    ostringstream oss;
    oss.setf(ios_base::scientific, ios_base::floatfield);

    if (mpiRank == 0) {
#ifdef _DEBUG
        cout << meshName << ": pts=" << gNumPoints << ", cells=" << gNumCells
            << ", cellsize=" << gCellSizeAndType[0] << ", type="
            << gCellSizeAndType[1] << ", numNodalVars=" << nodalVars.size()
            << ", numCellVars=" << cellVars.size()
            << endl;
#endif

        oss << "<?xml version=\"1.0\"?>" << endl;
        oss << "<VTKFile type=\"UnstructuredGrid\" version=\"0.1\">" << endl;
        oss << "<UnstructuredGrid>" << endl;

        // write time and cycle values
        oss << "<FieldData>" << endl;
        oss << "<DataArray Name=\"TIME\" type=\"Float64\" format=\"ascii\" NumberOfTuples=\"1\">" << endl;
        oss << time << endl;
        oss << "</DataArray>" << endl << "</FieldData>" << endl;
        oss << "<FieldData>" << endl;
        oss << "<DataArray Name=\"CYCLE\" type=\"Int32\" format=\"ascii\" NumberOfTuples=\"1\">" << endl;
        oss << cycle << endl;
        oss << "</DataArray>" << endl << "</FieldData>" << endl;

        // write mesh header
        oss << "<Piece NumberOfPoints=\"" << gNumPoints
            << "\" NumberOfCells=\"" << gNumCells << "\">" << endl;
        oss << "<Points>" << endl;
        oss << "<DataArray NumberOfComponents=\"3\" type=\"Float64\" format=\"ascii\">" << endl;
    }

    //
    // coordinates (note that we are using the original nodes)
    // 
    for (meshIt = meshBlocks.begin(); meshIt != meshBlocks.end(); meshIt++) {
        (*meshIt)->getNodes()->writeCoordinatesVTK(oss, mpiRank);
    }

    WRITE_ORDERED(oss);

    if (mpiRank == 0) {
        oss << "</DataArray>" << endl << "</Points>" << endl;
        oss << "<Cells>" << endl;
        oss << "<DataArray Name=\"connectivity\" type=\"Int32\" format=\"ascii\">" << endl;
    }

    //
    // connectivity
    //
    for (meshIt = meshBlocks.begin(); meshIt != meshBlocks.end(); meshIt++) {
        ElementData_ptr el = (*meshIt)->getElementsByName(meshName);
        el->writeConnectivityVTK(oss);
    }

    WRITE_ORDERED(oss);

    //
    // offsets & types
    // 
    if (mpiRank == 0) {
        oss << "</DataArray>" << endl;
        oss << "<DataArray Name=\"offsets\" type=\"Int32\" format=\"ascii\">" << endl;
        for (int i=1; i < gNumCells+1; i++) {
            oss << i*gCellSizeAndType[0] << endl;
        }
        oss << "</DataArray>" << endl;
        oss << "<DataArray Name=\"types\" type=\"UInt8\" format=\"ascii\">" << endl;
        for (int i=1; i < gNumCells+1; i++) {
            oss << gCellSizeAndType[1] << endl;
        }
        oss << "</DataArray>" << endl << "</Cells>" << endl;
        WRITE_SHARED(oss);
    }

    // now write all variables - first the nodal data, then cell data

    // write nodal data if any
    if (nodalVars.size() > 0) {
        if (mpiRank == 0)
            oss << "<PointData>" << endl;
        for (viIt = nodalVars.begin(); viIt != nodalVars.end(); viIt++) {
            writeVarToVTK(*viIt, oss);
            WRITE_ORDERED(oss);
            if (mpiRank == 0)
                oss << "</DataArray>" << endl;
        }
        if (mpiRank == 0)
            oss << "</PointData>" << endl;
    }

    // write cell data if any
    if (cellVars.size() > 0) {
        if (mpiRank == 0)
            oss << "<CellData>" << endl;
        for (viIt = cellVars.begin(); viIt != cellVars.end(); viIt++) {
            writeVarToVTK(*viIt, oss);
            WRITE_ORDERED(oss);
            if (mpiRank == 0)
                oss << "</DataArray>" << endl;
        }
        if (mpiRank == 0)
            oss << "</CellData>" << endl;
    }

    if (mpiRank == 0) {
        oss << "</Piece>" << endl << "</UnstructuredGrid>" << endl
            << "</VTKFile>" << endl;
        WRITE_SHARED(oss);
    }

#if HAVE_MPI
    mpiErr = MPI_File_close(&mpiFileHandle);
#else
    ofs.close();
#endif

    return true;
}

//
//
//
void EscriptDataset::writeVarToVTK(const VarInfo& varInfo, ostream& os)
{
    const DataBlocks& varBlocks = varInfo.dataBlocks;
    int rank = varBlocks[0]->getRank();
    int numComps = 1;
    if (rank > 0)
        numComps *= 3;
    if (rank > 1)
        numComps *= 3;

    if (mpiRank == 0) {
        os << "<DataArray Name=\"" << varInfo.varName
            << "\" type=\"Float64\" NumberOfComponents=\"" << numComps
            << "\" format=\"ascii\">" << endl;
    }

    DataBlocks::const_iterator blockIt;
    for (blockIt = varBlocks.begin(); blockIt != varBlocks.end(); blockIt++) {
        (*blockIt)->writeToVTK(os, mpiRank);
    }
}

//
//
//
bool EscriptDataset::loadMeshFromNetCDF()
{
    bool ok = true;
    char* str = new char[meshFmt.length()+10];
    if (mpiSize > 1) {
        FinleyMesh_ptr meshPart(new FinleyMesh());
        sprintf(str, meshFmt.c_str(), mpiRank);
        string meshfile = str;
        if (meshPart->initFromNetCDF(meshfile)) {
            meshPart->reorderGhostZones(mpiRank);
            meshBlocks.push_back(meshPart);
        } else {
            meshPart.reset();
            ok = false;
        }
    } else {
        for (int idx=0; idx < numParts; idx++) {
            FinleyMesh_ptr meshPart(new FinleyMesh());
            sprintf(str, meshFmt.c_str(), idx);
            string meshfile = str;
            if (meshPart->initFromNetCDF(meshfile)) {
                if (numParts > 1)
                    meshPart->reorderGhostZones(idx);
                meshBlocks.push_back(meshPart);
            } else {
                meshPart.reset();
                ok = false;
                break;
            }
        }
    }
    delete[] str;
    return ok;
}

//
//
//
bool EscriptDataset::loadVarFromNetCDF(const string& fileName,
                                       const string& varName)
{
    int myError = false;
    char* str = new char[fileName.length()+10];
    VarInfo vi;

    vi.varName = varName;
    vi.valid = true;

    // read all parts of the variable
    MeshBlocks::iterator mIt;
    int idx = (mpiSize > 1) ? mpiRank : 0;
    for (mIt = meshBlocks.begin(); mIt != meshBlocks.end(); mIt++, idx++) {
        sprintf(str, fileName.c_str(), idx);
        string dfile = str;
        DataVar_ptr var(new DataVar(varName));
        if (var->initFromNetCDF(dfile, *mIt))
            vi.dataBlocks.push_back(var);
        else {
            cerr << "Error reading " << dfile << endl;
            var.reset();
            myError = true;
            break;
        }
    }
    delete[] str;

    int gError;
#if HAVE_MPI
    MPI_Allreduce(&myError, &gError, 1, MPI_LOGICAL, MPI_LOR, mpiComm);
#else
    gError = myError;
#endif

    if (gError) {
        // at least one chunk was not read correctly
        vi.dataBlocks.clear();
        vi.valid = false;
    }

    updateSampleDistribution(vi);
    variables.push_back(vi);
    return vi.valid;
}

//
//
//
void EscriptDataset::convertMeshVariables()
{
    const StringVec& varNames = meshBlocks[0]->getVarNames();
    StringVec::const_iterator it;
    for (it = varNames.begin(); it != varNames.end(); it++) {
        VarInfo vi;
        vi.varName = *it;
        vi.valid = true;
        // get all parts of current variable
        MeshBlocks::iterator mIt;
        for (mIt = meshBlocks.begin(); mIt != meshBlocks.end(); mIt++) {
            DataVar_ptr var(new DataVar(*it));
            if (var->initFromMesh(*mIt)) {
                vi.dataBlocks.push_back(var);
            } else {
                cerr << "Error converting mesh variable " << *it << endl;
                vi.valid = false;
                break;
            }
        }
        updateSampleDistribution(vi);
        meshVariables.push_back(vi);
    }
}

// retrieves the number of samples at each block - used to determine which
// blocks contribute to given variable if any.
void EscriptDataset::updateSampleDistribution(VarInfo& vi)
{
    IntVec sampleDist;
    const DataBlocks& varBlocks = vi.dataBlocks;

    if (mpiSize > 1) {
#if HAVE_MPI
        int myNumSamples = varBlocks[0]->getNumberOfSamples();
        sampleDist.insert(sampleDist.end(), mpiSize, 0);
        MPI_Allgather(
            &myNumSamples, 1, MPI_INT, &sampleDist[0], 1, MPI_INT, mpiComm);
#endif
    } else {
        DataBlocks::const_iterator it;
        for (it = varBlocks.begin(); it != varBlocks.end(); it++) {
            sampleDist.push_back((*it)->getNumberOfSamples());
        }
    }
    vi.sampleDistribution = sampleDist;
}

//
//
//
void EscriptDataset::putSiloMultiMesh(DBfile* dbfile, const string& meshName)
{
#if USE_SILO
    vector<int> meshtypes;
    vector<string> tempstrings;
    vector<char*> meshnames;
    string pathPrefix;

    int ppIndex = meshBlocks[0]->getSiloPath().find(':');
    if (ppIndex != string::npos) {
        pathPrefix = meshBlocks[0]->getSiloPath().substr(0, ppIndex+1);
    }

    // find a variable belonging to this mesh to get the sample
    // distribution (which tells us which ranks contribute to this mesh).
    // Try mesh variables first, then regular ones.
    VarVector::const_iterator viIt;
    for (viIt = meshVariables.begin(); viIt != meshVariables.end(); viIt++) {
        if (meshName == viIt->dataBlocks[0]->getMeshName())
            break;
    }

    if (viIt == meshVariables.end()) {
        for (viIt = variables.begin(); viIt != variables.end(); viIt++) {
            if (meshName == viIt->dataBlocks[0]->getMeshName())
                break;
        }
    }
    // this probably means that the mesh is empty
    if (viIt == variables.end()) {
        return;
    }

    for (size_t idx = 0; idx < viIt->sampleDistribution.size(); idx++) {
        if (viIt->sampleDistribution[idx] > 0) {
            stringstream siloPath;
            siloPath << pathPrefix << "/block";
            int prevWidth = siloPath.width(4);
            char prevFill = siloPath.fill('0');
            siloPath << right << idx;
            siloPath.width(prevWidth);
            siloPath.fill(prevFill);
            siloPath << "/";
            siloPath << meshName;
            tempstrings.push_back(siloPath.str());
            meshnames.push_back((char*)tempstrings.back().c_str());
            meshtypes.push_back(DB_UCDMESH);
        }
    }

    // ignore empty mesh
    if (meshnames.size() > 0) {
        DBSetDir(dbfile, "/");
        DBoptlist* optList = DBMakeOptlist(2);
        DBAddOption(optList, DBOPT_CYCLE, &cycle);
        DBAddOption(optList, DBOPT_DTIME, &time);
        DBPutMultimesh(dbfile, meshName.c_str(), meshnames.size(),
                &meshnames[0], &meshtypes[0], optList);
        DBFreeOptlist(optList);
    }
#endif
}

//
//
//
void EscriptDataset::putSiloMultiVar(DBfile* dbfile, const VarInfo& vi,
                                     bool useMeshFile)
{
#if USE_SILO
    vector<int> vartypes;
    vector<string> tempstrings;
    vector<char*> varnames;
    string pathPrefix;
    if (useMeshFile) {
        int ppIndex = meshBlocks[0]->getSiloPath().find(':');
        if (ppIndex != string::npos) {
            pathPrefix = meshBlocks[0]->getSiloPath().substr(0, ppIndex+1);
        }
    }

    for (size_t idx = 0; idx < vi.sampleDistribution.size(); idx++) {
        if (vi.sampleDistribution[idx] > 0) {
            stringstream siloPath;
            siloPath << pathPrefix << "/block";
            int prevWidth = siloPath.width(4);
            char prevFill = siloPath.fill('0');
            siloPath << right << idx;
            siloPath.width(prevWidth);
            siloPath.fill(prevFill);
            siloPath << "/";
            siloPath << vi.varName;
            tempstrings.push_back(siloPath.str());
            varnames.push_back((char*)tempstrings.back().c_str());
            vartypes.push_back(DB_UCDVAR);
        }
    }

    // ignore empty variables
    if (varnames.size() > 0) {
        DBSetDir(dbfile, "/");
        DBoptlist* optList = DBMakeOptlist(2);
        DBAddOption(optList, DBOPT_CYCLE, &cycle);
        DBAddOption(optList, DBOPT_DTIME, &time);
        if (useMeshFile) {
            string vpath = string(MESH_VARS)+vi.varName;
            DBPutMultivar(dbfile, vpath.c_str(), varnames.size(),
                    &varnames[0], &vartypes[0], optList);
        } else {
            DBPutMultivar(dbfile, vi.varName.c_str(), varnames.size(),
                    &varnames[0], &vartypes[0], optList);
        }
        DBFreeOptlist(optList);
    }
#endif
}

//
//
//
void EscriptDataset::putSiloMultiTensor(DBfile* dbfile, const VarInfo& vi)
{
#if USE_SILO
    string tensorDir = vi.varName+string("_comps/");
    DBSetDir(dbfile, "/");
    DBMkdir(dbfile, tensorDir.c_str());
    int one = 1;
    DBoptlist* optList = DBMakeOptlist(3);
    DBAddOption(optList, DBOPT_CYCLE, &cycle);
    DBAddOption(optList, DBOPT_DTIME, &time);
    DBAddOption(optList, DBOPT_HIDE_FROM_GUI, &one);
    const IntVec& shape = vi.dataBlocks[0]->getShape();

    for (int i=0; i<shape[1]; i++) {
        for (int j=0; j<shape[0]; j++) {
            vector<string> tempstrings;
            vector<char*> varnames;
            vector<int> vartypes;
            stringstream comp;
            comp << vi.varName << "_comps/a_";
            comp << i;
            comp << j;
            for (size_t idx = 0; idx < vi.sampleDistribution.size(); idx++) {
                if (vi.sampleDistribution[idx] > 0) {
                    stringstream siloPath;
                    siloPath << "/block";
                    int prevWidth = siloPath.width(4);
                    char prevFill = siloPath.fill('0');
                    siloPath << right << idx;
                    siloPath.width(prevWidth);
                    siloPath.fill(prevFill);
                    siloPath << "/" << comp.str();
                    tempstrings.push_back(siloPath.str());
                    varnames.push_back((char*)tempstrings.back().c_str());
                    vartypes.push_back(DB_UCDVAR);
                }
            }
            if (varnames.size() > 0) {
                DBPutMultivar(dbfile, comp.str().c_str(), varnames.size(),
                        &varnames[0], &vartypes[0], optList);
            }
        }
    }
    DBFreeOptlist(optList);
#endif
}

} // namespace escriptexport

