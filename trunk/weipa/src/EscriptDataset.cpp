
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

#include <weipa/EscriptDataset.h>
#include <weipa/DataVar.h>
#include <weipa/ElementData.h>
#include <weipa/FileWriter.h>
#include <weipa/FinleyMesh.h>
#include <weipa/NodeData.h>

#ifndef VISIT_PLUGIN
#include <escript/Data.h>
#endif

#include <numeric> // for std::accumulate

#if USE_SILO
#include <silo.h>

#if HAVE_MPI
#include <pmpio.h>
#endif

#endif // USE_SILO

using namespace std;

namespace weipa {

const char* MESH_VARS = "mesh_vars/";
const int NUM_SILO_FILES = 1;

//
// Default constructor
//
EscriptDataset::EscriptDataset() :
    cycle(0),
    time(0.),
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
    cycle(0),
    time(0.),
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
// Sets the domain using an escript domain instance.
//
bool EscriptDataset::setDomain(const escript::AbstractDomain* domain)
{
#ifndef VISIT_PLUGIN
    int myError = 0, gError;

    // fail if the domain has already been set
    if (meshBlocks.size() > 0) {
        cerr << "Domain has already been set!" << endl;
        myError = 1;
    } else if (!domain) {
        cerr << "Domain is NULL!" << endl;
        myError = 1;
    } else {
#if HAVE_MPI
        mpiComm = domain->getMPIComm();
        mpiRank = domain->getMPIRank();
        mpiSize = domain->getMPISize();
#endif
        FinleyMesh_ptr mesh(new FinleyMesh());
        if (mesh->initFromEscript(domain)) {
            if (mpiSize > 1)
                mesh->reorderGhostZones(mpiRank);
            meshBlocks.push_back(mesh);
        } else {
            cerr << "Error initializing domain!" << endl;
            myError = 2;
        }
    }

    if (mpiSize > 1) {
#if HAVE_MPI
        MPI_Allreduce(&myError, &gError, 1, MPI_INT, MPI_MAX, mpiComm);
#else
        gError = myError;
#endif
    } else {
        gError = myError;
    }

    if (gError>1) {
        meshBlocks.clear();
    } else if (gError==0) {
        // Convert mesh data to variables
        convertMeshVariables();
    }
    return (gError==0);

#else // VISIT_PLUGIN
    return false;
#endif
}

//
//
//
bool EscriptDataset::addData(escript::Data& data, const string name,
                             const string units)
{
#ifndef VISIT_PLUGIN
    bool success = true;

    // fail if no domain has been set
    if (meshBlocks.size() == 0) {
        success = false;
    } else {
        // initialize variable
        VarInfo vi;
        vi.varName = name;
        vi.units = units;

        DataVar_ptr var(new DataVar(vi.varName));
        if (var->initFromEscript(data, meshBlocks[0])) {
            vi.dataBlocks.push_back(var);
            updateSampleDistribution(vi);
            vi.valid = true;
        } else {
            var.reset();
            vi.valid = false;
        }
        variables.push_back(vi);
    }
    return success;

#else // VISIT_PLUGIN
    return false;
#endif
}

//
//
//
bool EscriptDataset::loadNetCDF(const string meshFilePattern,
                                const StringVec& varFiles,
                                const StringVec& varNames, int nBlocks)
{
    // sanity check
    if (varFiles.size() != varNames.size()) {
        return false;
    }

    // load the domain files
    if (!loadDomain(meshFilePattern, nBlocks)) {
        return false;
    }

    // load the variables
    StringVec::const_iterator fileIt = varFiles.begin();
    StringVec::const_iterator nameIt = varNames.begin();
    for (; fileIt != varFiles.end(); fileIt++, nameIt++) {
        loadData(*fileIt, *nameIt, "");
    }

    return true;
}

//
// Load only variables using provided domain
//
bool EscriptDataset::loadNetCDF(const MeshBlocks& mesh,
                                const StringVec& varFiles,
                                const StringVec& varNames)
{
    // sanity check
    if (varFiles.size() != varNames.size()) {
        return false;
    }

    // set the domain
    if (!setExternalDomain(mesh)) {
        return false;
    }

    // load the variables
    StringVec::const_iterator fileIt = varFiles.begin();
    StringVec::const_iterator nameIt = varNames.begin();
    for (; fileIt != varFiles.end(); fileIt++, nameIt++) {
        loadData(*fileIt, *nameIt, "");
    }

    return true;
}

//
//
//
bool EscriptDataset::saveSilo(string fileName, bool useMultiMesh)
{
#if USE_SILO
    if (meshBlocks.size() == 0)
        return false;

    const char* blockDirFmt = "/block%04d";
    string siloPath;
    DBfile* dbfile = NULL;
    int driver = DB_HDF5; // prefer HDF5 if available
    //FIXME: Silo's HDF5 driver and NetCDF 4 are currently incompatible because
    //NetCDF calls H5close() when all its files are closed.
    //Unidata has been contacted, Ticket ID: YTC-894489.
    //When this issue is resolved, remove the following line.
    driver = DB_PDB;
#if HAVE_MPI
    PMPIO_baton_t* baton = NULL;
#endif

    if (mpiSize > 1) {
#if HAVE_MPI
        baton = PMPIO_Init(NUM_SILO_FILES, PMPIO_WRITE,
                    mpiComm, 0x1337, PMPIO_DefaultCreate, PMPIO_DefaultOpen,
                    PMPIO_DefaultClose, (void*)&driver);
        // try the fallback driver in case of error
        if (!baton && driver != DB_PDB) {
            driver = DB_PDB;
            baton = PMPIO_Init(NUM_SILO_FILES, PMPIO_WRITE,
                        mpiComm, 0x1337, PMPIO_DefaultCreate, PMPIO_DefaultOpen,
                        PMPIO_DefaultClose, (void*)&driver);
        }
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
                "escriptData", driver);
        // try the fallback driver in case of error
        if (!dbfile && driver != DB_PDB) {
            driver = DB_PDB;
            dbfile = DBCreate(fileName.c_str(), DB_CLOBBER, DB_LOCAL,
                    "escriptData", driver);
        }
    }

    if (!dbfile) {
        cerr << "Could not create Silo file." << endl;
        if (mpiSize > 1) {
#if HAVE_MPI
            PMPIO_HandOffBaton(baton, dbfile);
            PMPIO_Finish(baton);
#endif
        }
        return false;
    }

    if (driver==DB_HDF5) {
        // gzip level 1 already provides good compression with minimal
        // performance penalty. Some tests showed that gzip levels >3 performed
        // rather badly on escript data both in terms of time and space
        DBSetCompression("ERRMODE=FALLBACK METHOD=GZIP LEVEL=1");
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
            if (! (*meshIt)->writeToSilo(
                        dbfile, siloPath, meshLabels, meshUnits)) {
                cerr << "Error writing block " << idx
                    << " of mesh to Silo file!" << endl;
                break;
            }
        }

        // write variables for current mesh block
        for (viIt = variables.begin(); viIt != variables.end(); viIt++) {
            // do not attempt to write this variable if previous steps failed
            if (!viIt->valid) continue;
            DataVar_ptr var = viIt->dataBlocks[idx];
            if (!var->writeToSilo(dbfile, siloPath, viIt->units)) {
                cerr << "Error writing block " << idx << " of '"
                    << var->getName() << "' to Silo file!" << endl;
                viIt->valid = false;
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
                if (!viIt->valid) continue;
                DataVar_ptr var = viIt->dataBlocks[0];
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
            if (!viIt->valid) continue;
            DataVar_ptr var = viIt->dataBlocks[0];
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
    if (meshBlocks.size() == 0)
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

    FileWriter* fw = NULL;

    if (mpiSize > 1) {
#if HAVE_MPI
        fw = new FileWriter(mpiComm);
        meshBlocks[0]->removeGhostZones(mpiRank);
        ElementData_ptr elements = meshBlocks[0]->getElementsByName(meshName);
        int myNumCells = elements->getNumElements();
        MPI_Reduce(&myNumCells, &gNumCells, 1, MPI_INT, MPI_SUM, 0, mpiComm);

        int myCellSizeAndType[2];
        myCellSizeAndType[0] = elements->getNodesPerElement();
        myCellSizeAndType[1] = elements->getType();

        // rank 0 needs to know element type and size but it's possible that
        // this information is only available on other ranks (value=0) so
        // retrieve it
        MPI_Reduce(&myCellSizeAndType, &gCellSizeAndType, 2, MPI_INT, MPI_MAX,
                0, mpiComm);
#endif
    } else {
        fw = new FileWriter();
        int idx = 0;
        for (meshIt = meshBlocks.begin(); meshIt != meshBlocks.end(); meshIt++, idx++) {
            if (meshBlocks.size() > 1)
                (*meshIt)->removeGhostZones(idx);
            ElementData_ptr elements = (*meshIt)->getElementsByName(meshName);
            gNumCells += elements->getNumElements();
            if (gCellSizeAndType[0] == 0)
                gCellSizeAndType[0] = elements->getNodesPerElement();
            if (gCellSizeAndType[1] == 0)
                gCellSizeAndType[1] = elements->getType();
        }
    }

    gNumPoints = meshBlocks[0]->getNodes()->getGlobalNumNodes();

    ostringstream oss;
    oss.setf(ios_base::scientific, ios_base::floatfield);

    if (!fw->openFile(fileName)) {
        return false;
    }

    if (mpiRank == 0) {
#ifdef _DEBUG
        cout << meshName << ": pts=" << gNumPoints << ", cells=" << gNumCells
            << ", cellsize=" << gCellSizeAndType[0] << ", type="
            << gCellSizeAndType[1] << ", numNodalVars=" << nodalVars.size()
            << ", numCellVars=" << cellVars.size()
            << endl;
#endif

        oss << "<?xml version=\"1.0\"?>" << endl;
        oss << "<VTKFile type=\"UnstructuredGrid\" version=\"0.1\"";
        if (mdSchema.length()>0) {
            oss << " " << mdSchema;
        }
        oss << ">" << endl;
        if (mdString.length()>0) {
            oss << mdString << endl;
        }
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
    int blockNum = (mpiSize>1 ? mpiRank : 0);
    for (meshIt = meshBlocks.begin(); meshIt != meshBlocks.end(); meshIt++, blockNum++) {
        (*meshIt)->getNodes()->writeCoordinatesVTK(oss, blockNum);
    }

    if (!fw->writeOrdered(oss)) {
        cerr << "Warning, ignoring file write error!" << endl;
    }

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

    if (!fw->writeOrdered(oss)) {
        cerr << "Warning, ignoring file write error!" << endl;
    }

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
        if (!fw->writeShared(oss)) {
            cerr << "Warning, ignoring file write error!" << endl;
        }
    }

    // now write all variables - first the nodal data, then cell data

    // write nodal data if any
    if (!nodalVars.empty()) {
        if (mpiRank == 0)
            oss << "<PointData>" << endl;
        for (viIt = nodalVars.begin(); viIt != nodalVars.end(); viIt++) {
            writeVarToVTK(*viIt, oss);
            if (!fw->writeOrdered(oss)) {
                cerr << "Warning, ignoring file write error!" << endl;
            }
            if (mpiRank == 0)
                oss << "</DataArray>" << endl;
        }
        if (mpiRank == 0)
            oss << "</PointData>" << endl;
    }

    // write cell data if any
    if (!cellVars.empty()) {
        if (mpiRank == 0)
            oss << "<CellData>" << endl;
        for (viIt = cellVars.begin(); viIt != cellVars.end(); viIt++) {
            writeVarToVTK(*viIt, oss);
            if (!fw->writeOrdered(oss)) {
                cerr << "Warning, ignoring file write error!" << endl;
            }
            if (mpiRank == 0)
                oss << "</DataArray>" << endl;
        }
        if (mpiRank == 0)
            oss << "</CellData>" << endl;
    }

    if (mpiRank == 0) {
        oss << "</Piece>" << endl << "</UnstructuredGrid>" << endl
            << "</VTKFile>" << endl;
        if (!fw->writeShared(oss)) {
            cerr << "Warning, ignoring file write error!" << endl;
        }
    }

    fw->close();
    delete fw;
    return true;
}

//
//
//
void EscriptDataset::setMeshLabels(const string x, const string y, const string z)
{
    meshLabels.clear();
    meshLabels.push_back(x);
    meshLabels.push_back(y);
    if (z.length()>0)
        meshLabels.push_back(z);
}

//
//
//
void EscriptDataset::setMeshUnits(const string x, const string y, const string z)
{
    meshUnits.clear();
    meshUnits.push_back(x);
    meshUnits.push_back(y);
    if (z.length()>0)
        meshUnits.push_back(z);
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

    // this is required in case we read a dataset with more than one chunk on
    // one rank
    int blockNum = (mpiSize>1 ? mpiRank : 0);
    DataBlocks::const_iterator blockIt;
    for (blockIt = varBlocks.begin(); blockIt != varBlocks.end(); blockIt++, blockNum++) {
        (*blockIt)->writeToVTK(os, blockNum);
    }
}

//
// Sets the domain from dump files.
//
bool EscriptDataset::loadDomain(const string filePattern, int nBlocks)
{
    int myError = 0, gError;

    if (mpiSize > 1 && nBlocks != mpiSize) {
        cerr << "Cannot load " << nBlocks << " chunks on " << mpiSize
            << " MPI ranks!" << endl;
        myError = 1;

    } else if (meshBlocks.size() > 0) {
        cerr << "Domain has already been set!" << endl;
        myError = 1;

    } else {
        char* str = new char[filePattern.length()+10];
        if (mpiSize > 1) {
            FinleyMesh_ptr meshPart(new FinleyMesh());
            sprintf(str, filePattern.c_str(), mpiRank);
            string meshfile = str;
            if (meshPart->initFromNetCDF(meshfile)) {
                meshPart->reorderGhostZones(mpiRank);
                meshBlocks.push_back(meshPart);
            } else {
                cerr << "Error initializing domain!" << endl;
                myError = 1;
            }
        } else {
            for (int idx=0; idx < nBlocks; idx++) {
                FinleyMesh_ptr meshPart(new FinleyMesh());
                sprintf(str, filePattern.c_str(), idx);
                string meshfile = str;
                if (meshPart->initFromNetCDF(meshfile)) {
                    if (nBlocks > 1)
                        meshPart->reorderGhostZones(idx);
                    meshBlocks.push_back(meshPart);
                } else {
                    cerr << "Error initializing domain block " << idx << endl;
                    myError = 1;
                    break;
                }
            }
        }
        delete[] str;
    }

    if (mpiSize > 1) {
#if HAVE_MPI
        MPI_Allreduce(&myError, &gError, 1, MPI_INT, MPI_MAX, mpiComm);
#else
        gError = myError;
#endif
    } else {
        gError = myError;
    }

    if (gError) {
        meshBlocks.clear();
    } else {
        // Convert mesh data to variables
        convertMeshVariables();
    }

    return !gError;
}

//
// Sets an already converted domain.
//
bool EscriptDataset::setExternalDomain(const MeshBlocks& domain)
{
    int myError = 0, gError;

    if (mpiSize > 1 && domain.size() > 1) {
        cerr << "Can only add one domain block per rank when using MPI!"
            << endl;
        myError = 1;

    } else if (meshBlocks.size() > 0) {
        cerr << "Domain has already been set!" << endl;
        myError = 1;

    }

    if (mpiSize > 1) {
#if HAVE_MPI
        MPI_Allreduce(&myError, &gError, 1, MPI_INT, MPI_MAX, mpiComm);
#else
        gError = myError;
#endif
    } else {
        gError = myError;
    }

    if (!gError) {
        externalMesh = true;
        meshBlocks = domain;
    }

    return !gError;
}

//
//
//
bool EscriptDataset::loadData(const string filePattern, const string name,
                              const string units)
{
    int myError = 0, gError;

    // fail if no domain has been set
    if (meshBlocks.size() == 0) {
        gError = 1;

    } else {
        // initialize variable
        VarInfo vi;
        vi.varName = name;
        vi.units = units;
        vi.valid = true;
        char* str = new char[filePattern.length()+10];

        // read all parts of the variable
        MeshBlocks::iterator mIt;
        int idx = (mpiSize > 1) ? mpiRank : 0;
        for (mIt = meshBlocks.begin(); mIt != meshBlocks.end(); mIt++, idx++) {
            sprintf(str, filePattern.c_str(), idx);
            string dfile = str;
            DataVar_ptr var(new DataVar(name));
            if (var->initFromNetCDF(dfile, *mIt))
                vi.dataBlocks.push_back(var);
            else {
                cerr << "Error reading " << dfile << endl;
                myError = 1;
                break;
            }
        }
        delete[] str;

        if (mpiSize > 1) {
#if HAVE_MPI
            MPI_Allreduce(&myError, &gError, 1, MPI_INT, MPI_MAX, mpiComm);
#else
            gError = myError;
#endif
        } else {
            gError = myError;
        }

        if (!gError) {
            // only add variable if all chunks have been read without error
            updateSampleDistribution(vi);
            variables.push_back(vi);
        }
    }

    return !gError;
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
    if (!meshnames.empty()) {
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
    if (!varnames.empty()) {
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
            if (!varnames.empty()) {
                DBPutMultivar(dbfile, comp.str().c_str(), varnames.size(),
                        &varnames[0], &vartypes[0], optList);
            }
        }
    }
    DBFreeOptlist(optList);
#endif
}

} // namespace weipa

