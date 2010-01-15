
/*******************************************************
*
* Copyright (c) 2003-2009 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/

#include <escriptexport/ElementData.h>
#include <escriptexport/NodeData.h>

extern "C" {
#include <finley/ElementFile.h>
}

#include <iostream>

#if USE_NETCDF
#include <netcdf.hh>
#endif

#if USE_SILO
#include <silo.h>
#endif

using namespace std;

// The following arrays contain indices to convert unsupported element
// types into supported ones (lines, triangles, quads, hexahedrons)

static const size_t line3indices[2*2] = {
    0, 2,
    2, 1
};
static const size_t tri6indices[4*3] = {
    0, 3, 5,
    3, 1, 4,
    5, 4, 2,
    3, 4, 5
};
static const size_t rec8indices[6*3] = {
    0, 4, 7,
    4, 1, 5,
    5, 2, 6,
    6, 3, 7,
    7, 5, 6,
    7, 4, 5
};
static const size_t rec9indices[4*4] = {
    0, 4, 8, 7,
    4, 1, 5, 8,
    7, 8, 6, 3,
    8, 5, 2, 6
};
static const size_t tet10indices[8*4] = {
    6, 0, 7, 4,
    2, 6, 9, 5,
    9, 7, 3, 8,
    4, 1, 8, 5,
    6, 7, 9, 8,
    5, 6, 9, 8,
    6, 5, 4, 8,
    7, 6, 4, 8
};
static const size_t hex20indices[36*3] = {
     0,  8, 12,   8,  1, 13,  13,  5, 16,
    16,  4, 12,   8, 13, 16,   8, 16, 12,
     1,  9, 13,   9,  2, 14,  14,  6, 17,
    17,  5, 13,   9, 14, 17,   9, 17, 13,
     2, 10, 14,  10,  3, 15,  15,  7, 18,
    18, 14,  6,  10, 15, 18,  10, 18, 14,
     3, 11, 15,  11,  0, 12,  12,  4, 19,
    19,  7, 15,  11, 12, 19,  11, 19, 15,
     4, 16, 19,  16,  5, 17,  17,  6, 18,
    18,  7, 19,  16, 17, 18,  16, 18, 19,
     3, 10, 11,  10,  2,  9,   9,  1,  8,
     8,  0, 11,  10,  9,  8,  10,  8, 11
};
static const size_t hex27indices[8*8] = {
     0,  8, 20, 11, 12, 21, 26, 24,
     8,  1,  9, 20, 21, 13, 22, 26,
    11, 20, 10,  3, 24, 26, 23, 15,
    20,  9,  2, 10, 26, 22, 14, 23,
    12, 21, 26, 24,  4, 16, 25, 19,
    21, 13, 22, 26, 16,  5, 17, 25,
    24, 26, 23, 15, 19, 25, 18,  7,
    26, 22, 14, 23, 25, 17,  6, 18
};

namespace escriptexport {
    
//
// Constructor
//
ElementData::ElementData(const string& elementName, NodeData_ptr nodeData)
    : originalMesh(nodeData), name(elementName), numElements(0),
      numGhostElements(0), numDims(0), nodesPerElement(0),
      type(ZONETYPE_UNKNOWN)
{
}

//
// Copy constructor
//
ElementData::ElementData(const ElementData& e)
{
    name = e.name;
    numElements = e.numElements;
    numGhostElements = e.numGhostElements;
    numDims = e.numDims;
    type = e.type;
    nodesPerElement = e.nodesPerElement;
    originalMesh = e.originalMesh;
    if (e.nodeMesh)
        nodeMesh.reset(new NodeData(*e.nodeMesh));

    nodes = e.nodes;
    ID = e.ID;
    color = e.color;
    tag = e.tag;
    owner = e.owner;

    if (e.reducedElements)
        reducedElements = ElementData_ptr(new ElementData(*e.reducedElements));
}

//
// Destructor
//
ElementData::~ElementData()
{
}

bool ElementData::initFromFinley(const Finley_ElementFile* finleyFile)
{
    numElements = finleyFile->numElements;

    if (numElements > 0) {
        nodesPerElement = finleyFile->numNodes;

        int* iPtr;
   
        iPtr = finleyFile->Nodes;
        nodes.clear();
        nodes.insert(nodes.end(), numElements*nodesPerElement, 0);
        copy(iPtr, iPtr+numElements*nodesPerElement, nodes.begin());

        iPtr = finleyFile->Color;
        color.clear();
        color.insert(color.end(), numElements, 0);
        copy(iPtr, iPtr+numElements, color.begin());

        iPtr = finleyFile->Id;
        ID.clear();
        ID.insert(ID.end(), numElements, 0);
        copy(iPtr, iPtr+numElements, ID.begin());

        iPtr = finleyFile->Owner;
        owner.clear();
        owner.insert(owner.end(), numElements, 0);
        copy(iPtr, iPtr+numElements, owner.begin());

        iPtr = finleyFile->Tag;
        tag.clear();
        tag.insert(tag.end(), numElements, 0);
        copy(iPtr, iPtr+numElements, tag.begin());

        ElementTypeId tid = finleyFile->referenceElementSet->
            referenceElement->Type->TypeId;
        FinleyElementInfo f = getFinleyTypeInfo(tid);
        type = f.elementType;
        if (f.elementFactor > 1 || f.reducedElementSize != nodesPerElement)
            buildReducedElements(f);

        buildMeshes();
    }
    return true;
}

StringVec ElementData::getMeshNames() const
{
    StringVec res;
    if (nodeMesh)
        res.push_back(nodeMesh->getName());
    if (reducedElements) {
        StringVec rNames = reducedElements->getMeshNames();
        if (rNames.size() > 0)
            res.insert(res.end(), rNames.begin(), rNames.end());
    }
    return res;
}

StringVec ElementData::getVarNames() const
{
    StringVec res;
    if (numElements > 0) {
        res.push_back(name + string("_Color"));
        res.push_back(name + string("_Id"));
        res.push_back(name + string("_Owner"));
        res.push_back(name + string("_Tag"));
    }
    if (reducedElements) {
        StringVec rNames = reducedElements->getVarNames();
        if (rNames.size() > 0)
            res.insert(res.end(), rNames.begin(), rNames.end());
    }
    return res;
}

const IntVec& ElementData::getVarDataByName(const string varName) const
{
    if (varName == name+string("_Color"))
        return color;
    else if (varName == name+string("_Id"))
        return ID;
    else if (varName == name+string("_Owner")) {
        return owner;
    } else if (varName == name+string("_Tag"))
        return tag;
    else if (reducedElements)
        return reducedElements->getVarDataByName(varName);
    else
        throw "Invalid variable name";
}

//
// Reads element data from given NetCDF file
//
bool ElementData::readFromNc(NcFile* ncfile)
{
#if USE_NETCDF
    string num_str("num_");
    num_str += name;

    NcAtt* att = ncfile->get_att(num_str.c_str());
    numElements = att->as_int(0);

    // Only attempt to read further if there are any elements.
    // Having no elements is not an error.
    if (numElements > 0) {
        att = ncfile->get_att((num_str + string("_numNodes")).c_str());
        nodesPerElement = att->as_int(0);

        nodes.insert(nodes.end(), numElements*nodesPerElement, 0);
        NcVar* var = ncfile->get_var((name + string("_Nodes")).c_str());
        var->get(&nodes[0], numElements, nodesPerElement);

        color.insert(color.end(), numElements, 0);
        var = ncfile->get_var((name + string("_Color")).c_str());
        var->get(&color[0], numElements);

        ID.insert(ID.end(), numElements, 0);
        var = ncfile->get_var((name + string("_Id")).c_str());
        var->get(&ID[0], numElements);

        owner.insert(owner.end(), numElements, 0);
        var = ncfile->get_var((name + string("_Owner")).c_str());
        var->get(&owner[0], numElements);

        tag.insert(tag.end(), numElements, 0);
        var = ncfile->get_var((name + string("_Tag")).c_str());
        var->get(&tag[0], numElements);

        att = ncfile->get_att((name + string("_TypeId")).c_str());
        FinleyElementInfo f = getFinleyTypeInfo((ElementTypeId)att->as_int(0));
        type = f.elementType;

        if (f.elementFactor > 1 || f.reducedElementSize != nodesPerElement)
            buildReducedElements(f);

        buildMeshes();
    }

    return true; 
#else // !USE_NETCDF
    return false;
#endif
}

//
//
//
void ElementData::reorderArray(IntVec& v, const IntVec& idx,
                               int elementsPerIndex)
{
    IntVec newArray(v.size());
    IntVec::iterator arrIt = newArray.begin();
    IntVec::const_iterator idxIt;
    if (elementsPerIndex == 1) {
        for (idxIt=idx.begin(); idxIt!=idx.end(); idxIt++) {
            *arrIt++ = v[*idxIt];
        }
    } else {
        for (idxIt=idx.begin(); idxIt!=idx.end(); idxIt++) {
            int i = *idxIt;
            copy(&v[i*elementsPerIndex], &v[(i+1)*elementsPerIndex], arrIt);
            arrIt += elementsPerIndex;
        }
    }
    v.swap(newArray);
}

//
//
//
void ElementData::buildReducedElements(const FinleyElementInfo& f)
{
    // create the node list for the new element type
    IntVec reducedNodes(f.reducedElementSize*numElements, 0);

    IntVec::iterator reducedIt = reducedNodes.begin();
    IntVec::const_iterator origIt;
    for (origIt=nodes.begin(); origIt!=nodes.end();
         origIt+=nodesPerElement)
    {
        copy(origIt, origIt+f.reducedElementSize, reducedIt);
        reducedIt += f.reducedElementSize;
    }

    if (f.elementFactor > 1) {
        // replace each element by multiple smaller ones which will be the
        // new 'full' elements, whereas the original ones are the reduced
        // elements, e.g.:
        //
        // new reduced:         new full:
        //   _________           _________
        //  |         |         |    |    |
        //  |         |    >    |____|____|
        //  |         |    >    |    |    |
        //  |_________|         |____|____|
        //

        // create the reduced elements which are basically a copy of the
        // current elements
        reducedElements = ElementData_ptr(new ElementData(
                    "Reduced"+name, originalMesh));
        reducedElements->nodes = reducedNodes;
        reducedElements->numElements = numElements;
        reducedElements->type = f.reducedElementType;
        reducedElements->nodesPerElement = f.reducedElementSize;
        reducedElements->owner = owner;
        reducedElements->color = color;
        reducedElements->ID = ID;
        reducedElements->tag = tag;

        // now update full element data
        IntVec fullNodes(f.elementSize*f.elementFactor*numElements);
        IntVec::iterator cellIt = fullNodes.begin();

        owner.clear();
        color.clear();
        ID.clear();
        tag.clear();
        for (int i=0; i < numElements; i++) {
            owner.insert(owner.end(), f.elementFactor, reducedElements->owner[i]);
            color.insert(color.end(), f.elementFactor, reducedElements->color[i]);
            ID.insert(ID.end(), f.elementFactor, reducedElements->ID[i]);
            tag.insert(tag.end(), f.elementFactor, reducedElements->tag[i]);
            for (int j=0; j < f.elementFactor*f.elementSize; j++)
                *cellIt++ = nodes[nodesPerElement*i+f.multiCellIndices[j]];
        }

        nodes.swap(fullNodes);
        nodesPerElement = f.elementSize;
        numElements *= f.elementFactor;

    } else {
        // we merely converted element types and don't need reduced elements
        // so just replace node list and type
        nodes.swap(reducedNodes);
        nodesPerElement = f.reducedElementSize;
        type = f.reducedElementType;
    }
}

//
//
//
IntVec ElementData::prepareGhostIndices(int ownIndex)
{
    IntVec indexArray;
    numGhostElements = 0;
    
    // move indices of "ghost zones" to the end to be able to reorder
    // data accordingly
    for (int i=0; i<numElements; i++) {
        if (owner[i] == ownIndex)
            indexArray.push_back(i);
    }

    for (int i=0; i<numElements; i++) {
        if (owner[i] != ownIndex) {
            numGhostElements++;
            indexArray.push_back(i);
        }
    }
    return indexArray;
}

//
//
//
void ElementData::reorderGhostZones(int ownIndex)
{
    IntVec indexArray = prepareGhostIndices(ownIndex);

    // move "ghost data" to the end of the arrays
    if (numGhostElements > 0) {
        reorderArray(nodes, indexArray, nodesPerElement);
        reorderArray(owner, indexArray, 1);
        reorderArray(color, indexArray, 1);
        reorderArray(ID, indexArray, 1);
        reorderArray(tag, indexArray, 1);
    }

    if (reducedElements)
        reducedElements->reorderGhostZones(ownIndex);
}

//
//
//
void ElementData::removeGhostZones(int ownIndex)
{
    reorderGhostZones(ownIndex);

    if (numGhostElements > 0) {
        numElements -= numGhostElements;
        nodes.resize(numElements*nodesPerElement);
        owner.resize(numElements);
        color.resize(numElements);
        ID.resize(numElements);
        tag.resize(numElements);
        numGhostElements = 0;
    }

    if (reducedElements)
        reducedElements->removeGhostZones(ownIndex);
}

//
//
//
void ElementData::buildMeshes()
{
    // build a new mesh containing only the required nodes
    if (numElements > 0) {
        if (nodeMesh) {
            NodeData_ptr newMesh(new NodeData(nodeMesh, nodes, name));
            nodeMesh.swap(newMesh);
        } else {
            nodeMesh.reset(new NodeData(originalMesh, nodes, name));
        }
#ifdef _DEBUG
        cout << nodeMesh->getName() << " has " << nodeMesh->getNumNodes()
            << " nodes and " << numElements << " elements" << endl;
#endif
    }

    if (reducedElements)
        reducedElements->buildMeshes();
}

#if USE_SILO
//
//
//
inline int toSiloElementType(int type)
{
    switch (type) {
        case ZONETYPE_BEAM: return DB_ZONETYPE_BEAM;
        case ZONETYPE_HEX: return DB_ZONETYPE_HEX;
        case ZONETYPE_POLYGON: return DB_ZONETYPE_POLYGON;
        case ZONETYPE_QUAD: return DB_ZONETYPE_QUAD;
        case ZONETYPE_TET: return DB_ZONETYPE_TET;
        case ZONETYPE_TRIANGLE: return DB_ZONETYPE_TRIANGLE;
    }
    return 0;
}
#endif

//
//
//
bool ElementData::writeToSilo(DBfile* dbfile, const string& siloPath)
{
#if USE_SILO
    if (numElements == 0)
        return true;

    int ret;

    if (siloPath != "") {
        ret = DBSetDir(dbfile, siloPath.c_str());
        if (ret != 0)
            return false;
    }

    // write out the full mesh in any case
    nodeMesh->setSiloPath(siloPath);
    string siloMeshNameStr = nodeMesh->getFullSiloName();
    const char* siloMeshName = siloMeshNameStr.c_str();
    int arraylen = numElements * nodesPerElement;
    int eltype = toSiloElementType(type);

    string varName = name + string("_zones");
    ret = DBPutZonelist2(dbfile, varName.c_str(), numElements,
            nodeMesh->getNumDims(), &nodes[0], arraylen, 0, 0,
            numGhostElements, &eltype, &nodesPerElement, &numElements, 1, NULL);
    if (ret == 0) {
        CoordArray& coordbase = const_cast<CoordArray&>(nodeMesh->getCoords());
        ret = DBPutUcdmesh(dbfile, siloMeshName,
                nodeMesh->getNumDims(), NULL, &coordbase[0],
                nodeMesh->getNumNodes(), numElements, varName.c_str(),
                /*"facelist"*/NULL, DB_FLOAT, NULL);
    }
    
    // Point mesh is useful for debugging
    if (0) {
        CoordArray& coordbase = const_cast<CoordArray&>(nodeMesh->getCoords());
        DBPutPointmesh(dbfile, "/pointmesh", nodeMesh->getNumDims(),
                &coordbase[0], nodeMesh->getNumNodes(), DB_FLOAT, NULL);
    }

    if (ret != 0)
        return false;

    // write out the element-centered variables
    varName = name + string("_Color");
    ret = DBPutUcdvar1(dbfile, varName.c_str(), siloMeshName,
            (float*)&color[0], numElements, NULL, 0, DB_INT, DB_ZONECENT,
            NULL);
    if (ret == 0) {
        varName = name + string("_Id");
        ret = DBPutUcdvar1(dbfile, varName.c_str(), siloMeshName,
            (float*)&ID[0], numElements, NULL, 0, DB_INT, DB_ZONECENT,
            NULL);
    }
    if (ret == 0) {
        varName = name + string("_Owner");
        ret = DBPutUcdvar1(dbfile, varName.c_str(), siloMeshName,
            (float*)&owner[0], numElements, NULL, 0, DB_INT, DB_ZONECENT,
            NULL);
    }
    if (ret == 0) {
        varName = name + string("_Tag");
        ret = DBPutUcdvar1(dbfile, varName.c_str(), siloMeshName,
            (float*)&tag[0], numElements, NULL, 0, DB_INT, DB_ZONECENT,
            NULL);
    }

    if (reducedElements) {
        reducedElements->writeToSilo(dbfile, siloPath);
    }

    // "Elements" is a special case
    if (name == "Elements") {
        nodeMesh->writeToSilo(dbfile);
    }

    return (ret == 0);

#else // !USE_SILO
    return false;
#endif
}

//
//
//
FinleyElementInfo ElementData::getFinleyTypeInfo(ElementTypeId typeId)
{
    FinleyElementInfo ret;
    ret.multiCellIndices = NULL;
    ret.elementFactor = 1;

    switch (typeId) {
        case Point1_Contact://untested
        case Line2Face_Contact://untested
        case Line3Face_Contact://untested
        case Line2Face://untested
        case Line3Face://untested
        case Point1://untested
            cerr << "WARNING: Finley type " <<typeId<< " is untested!" << endl;
            ret.elementSize = 1;
            ret.elementType = ZONETYPE_POLYGON;
            break;

        case Tri3Face_Contact://untested
        case Tri3Face://untested
            cerr << "WARNING: Finley type " <<typeId<< " is untested!" << endl;
        case Line2_Contact:
        case Rec4Face_Contact:
        case Rec4Face:
        case Line2:
            ret.elementSize = ret.reducedElementSize = 2;
            ret.elementType = ret.reducedElementType = ZONETYPE_BEAM;
            break;

        case Line3:
            ret.multiCellIndices = line3indices;
            ret.elementFactor = 2;
            // fall through
        case Line3_Contact:
        case Tri6Face_Contact://untested
        case Rec8Face_Contact:
        case Tri6Face://untested
        case Rec8Face:
            //VTK_QUADRATIC_EDGE
            ret.elementSize = ret.reducedElementSize = 2;
            ret.elementType = ret.reducedElementType = ZONETYPE_BEAM;
            break;

        case Tet4Face_Contact://untested
        case Tet4Face://untested
            cerr << "WARNING: Finley type " <<typeId<< " is untested!" << endl;
        case Tri3_Contact:
        case Tri3:
            ret.elementSize = ret.reducedElementSize = 3;
            ret.elementType = ret.reducedElementType = ZONETYPE_TRIANGLE;
            break;

        case Rec4_Contact:
        case Hex8Face_Contact:
        case Hex8Face:
        case Rec4:
            ret.elementSize = ret.reducedElementSize = 4;
            ret.elementType = ret.reducedElementType = ZONETYPE_QUAD;
            break;

        case Rec9:
            ret.multiCellIndices = rec9indices;
            ret.elementFactor = 4;
            // fall through
        case Rec9_Contact:
            ret.elementSize = ret.reducedElementSize = 4;
            ret.elementType = ret.reducedElementType = ZONETYPE_QUAD;
            break;

        case Tet4:
            ret.elementSize = ret.reducedElementSize = 4;
            ret.elementType = ret.reducedElementType = ZONETYPE_TET;
            break;

        case Tri6:
            ret.multiCellIndices = tri6indices;
            ret.elementFactor = 4;
            // fall through
        case Tri6_Contact:
        case Tet10Face_Contact://untested
        case Tet10Face://untested
            //VTK_QUADRATIC_TRIANGLE
            ret.elementSize = ret.reducedElementSize = 3;
            ret.elementType = ret.reducedElementType = ZONETYPE_TRIANGLE;
            break;

        case Rec8:
            ret.multiCellIndices = rec8indices;
            ret.elementFactor = 6;
            // fall through
        case Hex20Face:
        case Rec8_Contact:
        case Hex20Face_Contact:
            //VTK_QUADRATIC_QUAD
            ret.elementSize = 3;
            ret.elementType = ZONETYPE_TRIANGLE; 
            ret.reducedElementSize = 4;
            ret.reducedElementType = ZONETYPE_QUAD;
            break;

        case Tet10:
            //VTK_QUADRATIC_TETRA
            ret.multiCellIndices = tet10indices;
            ret.elementFactor = 8;
            ret.elementSize = ret.reducedElementSize = 4;
            ret.elementType = ret.reducedElementType = ZONETYPE_TET;
            break;

        case Hex20:
            //VTK_QUADRATIC_HEXAHEDRON
            ret.multiCellIndices = hex20indices;
            ret.elementFactor = 36;
            ret.elementSize = 3;
            ret.elementType = ZONETYPE_TRIANGLE;
            ret.reducedElementSize = 8;
            ret.reducedElementType = ZONETYPE_HEX;
            break;

        case Hex27:
            ret.multiCellIndices = hex27indices;
            ret.elementFactor = 8;
            // fall through
        case Hex8:
            ret.elementSize = ret.reducedElementSize = 8;
            ret.elementType = ret.reducedElementType = ZONETYPE_HEX;
            break;

        default:
            cerr << "WARNING: Unknown Finley Type " << typeId << endl;
            break;
    }
    return ret;
}

} // namespace escriptexport

