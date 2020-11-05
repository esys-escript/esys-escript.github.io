/*****************************************************************************
*
* Copyright (c) 2003-2019 by The University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Apache License, version 2.0
* http://www.apache.org/licenses/LICENSE-2.0
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development 2012-2013 by School of Earth Sciences
* Development from 2014 by Centre for Geoscience Computing (GeoComp)
*
*****************************************************************************/

#include <escript/DataTypes.h>

#include <oxley/Oxley.h>

#include <unordered_map>
#include <utility>

#include <boost/functional/hash.hpp>
#include <boost/python/numpy.hpp>

#include <p4est_iterate.h>
#include <p8est_iterate.h>

#ifndef __OXLEY_DATA_H__
#define __OXLEY_DATA_H__

// Macroes for array indexing
#define INDEX2(_X1_,_X2_,_N1_) ((_X1_)+(_N1_)*(_X2_))
#define INDEX3(_X1_,_X2_,_X3_,_N1_,_N2_) ((_X1_)+(_N1_)*INDEX2(_X2_,_X3_,_N2_))
#define INDEX4(_X1_,_X2_,_X3_,_X4_,_N1_,_N2_,_N3_) ((_X1_)+(_N1_)*INDEX3(_X2_,_X3_,_X4_,_N2_,_N3_))
#define INDEX5(_X1_,_X2_,_X3_,_X4_,_X5_,_N1_,_N2_,_N3_,_N4_) ((_X1_)+(_N1_)*INDEX4(_X2_,_X3_,_X4_,_X5_,_N2_,_N3_,_N4_))
#define INDEX6(_X1_,_X2_,_X3_,_X4_,_X5_,_X6_,_N1_,_N2_,_N3_,_N4_,_N5_) ((_X1_)+(_N1_)*INDEX5(_X2_,_X3_,_X4_,_X5_,_X6_,_N2_,_N3_,_N4_,_N5_))

////////////////////////////////////////////////////////////////////////
// This file contains the data structures used by Rectangle and Brick
////////////////////////////////////////////////////////////////////////

// Forward declarations
struct addSurfaceData;

//This structure describes the information that is stored at each
//quadrant / octant in the p4est / p8est
struct quadrantData
{
	double u = 0.0;

	// The quadrant's tag
	long quadTag = 0;

	// Node tag
	double nodeTag = 0;

	// Spatial coordinates of the corner node that defines the quadrant
	double xy[2] = {0.0,0.0};

	// treeid index
	long treeid = -1;

	// Number of the MPI process that owns this quadrant
	int owner = -1;

	// faceOffset[i]=-1 if face i is not an external face, otherwise it is
    // the index of that face (where i: 0=left, 1=right, 2=bottom, 3=top)
    // escript::DataTypes::IndexVector m_faceOffset;
    signed int m_faceOffset = {-1};
};

struct octantData
{
	double u = 0.0; // A Scalar variable

	// The octant's tag
	long octantTag = 0;

	// Node tag
	double nodeTag = 0;

	// Spatial coordinates of the corner node that defines the octant
	double xyz[3] = {0.0,0.0,0.0};
};

//This structure describes the information that is stored with the p4est
class p4estData
{
public:
	// origin of domain
    double m_origin[2] = {0.0};

    // extent of the domain
    double m_lxy[2] = {0.0};

    // side lengths of domain
    double m_length[2] = {0.0};

    // grid spacings / cell sizes of domain for each level of refinement
    double m_dx[2][P4EST_MAXLEVEL+1] = {{0}};

    // number of face elements per edge (left, right, bottom, top)
    escript::DataTypes::dim_t m_faceCount[4] = {-1};

    // vector that maps each node to a DOF index (used for the coupler)
    escript::DataTypes::IndexVector m_dofMap;

    // periodic boundary conditions
    bool periodic[2] {false, false};

	// maximum levels of recursion to use during refinement
	int max_levels_refinement = 0;


	void assign_info(addSurfaceData * tmp) {info=tmp;};

	addSurfaceData * borrow_info(){return info;};

	// This is here to temporarily store information
private:
	addSurfaceData * info;
};

class p8estData
{
public:
	// origin of domain
    double m_origin[3] = {0.0,0.0,0.0};

    // side lengths of domain
    double m_length[3] = {0.0,0.0,0.0};

    // number of spatial subdivisions
    int m_NX[3] = {0,0,0};

    // total number of elements in each dimension
    escript::DataTypes::dim_t m_gNE[3] = {0,0,0};

    // number of elements for this rank in each dimension including shared
    escript::DataTypes::dim_t m_NE[3] = {0,0,0};

    // periodic boundary conditions
    bool periodic[3] {false, false, false};

	// maximum levels of recursion to use during refinement
	int max_levels_refinement = 0;

	void assign_info(addSurfaceData * tmp) {info=tmp;};

	addSurfaceData * borrow_info(){return info;};

	// This is here to temporarily store information
private:
	addSurfaceData * info;
};

// This structure temporarily stores information used by the addSurface function
struct addSurfaceData {

	int oldTag = -1;
	int newTag = -1;
	std::vector<double> x;
	std::vector<double> y;
	std::vector<double> z;

	// The domain in which the function z[x,y] is defined
	double xmin,xmax,ymin,ymax;

};

struct update_RC_data {

	std::unordered_map<DoublePair,long,boost::hash<DoublePair>> * pNodeIDs; 
	// std::unordered_map<long,bool> * phangingNodeIDs; 
	p4est_t * p4est;
	std::vector< std::vector<long> > * indices;

};

struct getConnections_data {

	const std::unordered_map<DoublePair,long,boost::hash<DoublePair>> * pNodeIDs; 
	p4est_t * p4est;
	std::vector< std::vector<escript::DataTypes::index_t> > * indices;

};

// Tracks information used by the assembler
template<class Scalar>
struct assembly_data_d {

	std::vector<Scalar> * EM_S;
	std::vector<Scalar> * EM_F;
};

// bool operator==(const p4estData A, const p4estData B)
// {
	
// 	return (A.m_origin[0] == B.m_origin[0])
// 		&& (A.m_origin[1] == B.m_origin[1])
// 		&& (A.m_length[0] == B.m_length[0])
// 		&& (A.m_length[1] == B.m_length[1]);
// };

// bool operator==(const p8estData A, const p8estData B)
// {
	
// 	return (A.m_origin[0] == B.m_origin[0])
// 		&& (A.m_origin[1] == B.m_origin[1])
// 		&& (A.m_origin[2] == B.m_origin[2])
// 		&& (A.m_length[0] == B.m_length[0])
// 		&& (A.m_length[1] == B.m_length[1])
// 		&& (A.m_length[2] == B.m_length[2]);
// };

template <typename S> 
struct interpolateNodesOnElementsWorker_Data {

	S sentinel;
	int offset;
	double * fxx;

};

template <typename S> 
struct interpolateNodesOnFacesWorker_Data {

	S sentinel;
	int offset;
	double * fxx;
	int direction=-1;
	bool shared=false;

};

namespace oxley {

// Call back function that copies quadrant tags onto tagVector
void getQuadTagVector(p4est_iter_volume_info_t * info, void *tagVector);
void getQuadTagVector(p8est_iter_volume_info_t * info, void *tagVector);

// Call back function that copies coordinate info onto tagVector
void getXCoordVector(p4est_iter_volume_info_t * info, void *tagVector);
void getYCoordVector(p4est_iter_volume_info_t * info, void *tagVector);
void getXCoordVector(p8est_iter_volume_info_t * info, void *tagVector);
void getYCoordVector(p8est_iter_volume_info_t * info, void *tagVector);
void getZCoordVector(p8est_iter_volume_info_t * info, void *tagVector);

// Call back function that copies node information onto tagVector
void getNodeTagVector(p4est_iter_volume_info_t * info, void *tagVector);
void getNodeTagVector(p8est_iter_volume_info_t * info, void *tagVector);

} //namespace oxley

#endif
