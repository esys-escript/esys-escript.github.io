
/*******************************************************
*
* Copyright (c) 2003-2011 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


#ifndef INC_FINLEY_NODEFILE
#define INC_FINLEY_NODEFILE

#define MAX_numDim 3

#include "Finley.h"
#include "NodeMapping.h"
#include "escript/DataC.h"
#include "paso/Distribution.h"
#include "paso/Coupler.h"
#include "esysUtils/Esys_MPI.h"

struct Finley_NodeFile {
  Esys_MPIInfo *MPIInfo;              /* MPI information */

  dim_t numNodes;                      /* number of nodes */
  dim_t numDim;                        /* spatial dimension */
  index_t *Id;                         /* Id[i] is the id number of node i. It needs to be unique. */
  index_t *Tag;                        /* Tag[i] is the tag of node i. */
  index_t *tagsInUse;                  /* array of tags which are actually used */
  dim_t     numTagsInUse;               /* number of tags used */

  index_t* globalDegreesOfFreedom;      /* globalDegreesOfFreedom[i] is the global degree of freedom assigned to node i */
                                       /* this index is used to consider periodic boundary conditions by assigning */
                                       /* the same degreesOfFreedom to the same node */
  double *Coordinates;                 /* Coordinates[INDEX2(k,i,numDim)] is the k-th coordinate of the */
                                       /* node i. */
  index_t *globalReducedDOFIndex;    /* assigns each local node a global unique Id in a dens labeling of reduced DOF*/
                                     /* value <0 indicates that the DOF is not used */
  index_t *globalReducedNodesIndex;    /* assigns each local node a global unique Id in a dens labeling */
                                     /* value <0 indicates that the DOF is not used */
  index_t *globalNodesIndex;           /* assigns each local reduced node a global unique Id in a dens labeling */


 Finley_NodeMapping *nodesMapping;
 Finley_NodeMapping *reducedNodesMapping;
 Finley_NodeMapping *degreesOfFreedomMapping;
 Finley_NodeMapping *reducedDegreesOfFreedomMapping;
 
 Paso_Distribution *nodesDistribution;
 Paso_Distribution *reducedNodesDistribution;
 Paso_Distribution *degreesOfFreedomDistribution;
 Paso_Distribution *reducedDegreesOfFreedomDistribution;

 Paso_Connector* degreesOfFreedomConnector;
 Paso_Connector *reducedDegreesOfFreedomConnector;
  
                     /* these a the packed versions of Id */
 index_t *reducedNodesId;        
 index_t *degreesOfFreedomId;
 index_t *reducedDegreesOfFreedomId;


 int status; /* the status counts the updates done on the node coordinates */
              /* the value of status is increased by when the node coordinates are updated.*/
                                                                                                                                                                                                 
                                                                                                                                                                                                 
};

typedef struct Finley_NodeFile Finley_NodeFile;



Finley_NodeFile* Finley_NodeFile_alloc(dim_t, Esys_MPIInfo *MPIInfo);
index_t Finley_NodeFile_getFirstReducedNode(Finley_NodeFile* in);
index_t Finley_NodeFile_getLastReducedNode(Finley_NodeFile* in);
dim_t Finley_NodeFile_getGlobalNumReducedNodes(Finley_NodeFile* in);
index_t* Finley_NodeFile_borrowGlobalReducedNodesIndex(Finley_NodeFile* in);
index_t Finley_NodeFile_maxGlobalNodeIDIndex(Finley_NodeFile* in);
index_t Finley_NodeFile_maxGlobalReducedNodeIDIndex(Finley_NodeFile* in);
index_t Finley_NodeFile_GlobalDegreeOfFreedomIndex(Finley_NodeFile* in);
index_t Finley_NodeFile_GlobalReducedDegreeOfFreedomIndex(Finley_NodeFile* in);

index_t Finley_NodeFile_getFirstNode(Finley_NodeFile* in);
index_t Finley_NodeFile_getLastNode(Finley_NodeFile* in);
dim_t Finley_NodeFile_getGlobalNumNodes(Finley_NodeFile* in);
index_t* Finley_NodeFile_borrowGlobalNodesIndex(Finley_NodeFile* in);

/* returns the number of target */
dim_t Finley_NodeFile_getNumReducedNodes(Finley_NodeFile* in);
dim_t Finley_NodeFile_getNumDegreesOfFreedom(Finley_NodeFile* in);
dim_t Finley_NodeFile_getNumNodes(Finley_NodeFile* in);
dim_t Finley_NodeFile_getNumReducedDegreesOfFreedom(Finley_NodeFile* in);

/* returns the mapping from local nodes to a target */
index_t* Finley_NodeFile_borrowTargetReducedNodes(Finley_NodeFile* in);
index_t* Finley_NodeFile_borrowTargetDegreesOfFreedom(Finley_NodeFile* in);
index_t* Finley_NodeFile_borrowTargetNodes(Finley_NodeFile* in);
index_t* Finley_NodeFile_borrowTargetReducedDegreesOfFreedom(Finley_NodeFile* in);
/* returns the mapping from target to the local nodes */
index_t* Finley_NodeFile_borrowReducedNodesTarget(Finley_NodeFile* in);
index_t* Finley_NodeFile_borrowDegreesOfFreedomTarget(Finley_NodeFile* in);
index_t* Finley_NodeFile_borrowNodesTarget(Finley_NodeFile* in);
index_t* Finley_NodeFile_borrowReducedDegreesOfFreedomTarget(Finley_NodeFile* in);

void Finley_NodeFile_allocTable(Finley_NodeFile*,dim_t);
void Finley_NodeFile_free(Finley_NodeFile*);
void Finley_NodeFile_freeTable(Finley_NodeFile*);
void Finley_NodeFile_setIdGlobalRange(index_t*,index_t*,Finley_NodeFile*);
void Finley_NodeFile_setIdRange(index_t*,index_t*,Finley_NodeFile*);
void Finley_NodeFile_setDOFGlobalRange(index_t*,index_t*,Finley_NodeFile*);
void Finley_NodeFile_setDOFRange(index_t*,index_t*,Finley_NodeFile*);


void Finley_NodeFile_setGlobalDOFRange(index_t*,index_t*,Finley_NodeFile*);
void Finley_NodeFile_setGlobalIdRange(index_t*,index_t*,Finley_NodeFile*);
index_t Finley_NodeFile_maxGlobalDegreeOfFreedomIndex(Finley_NodeFile*);
index_t Finley_NodeFile_maxGlobalReducedDegreeOfFreedomIndex(Finley_NodeFile*);

void Finley_NodeFile_setReducedDOFRange(index_t*,index_t*,Finley_NodeFile*);
dim_t Finley_NodeFile_createDenseDOFLabeling(Finley_NodeFile*);
dim_t Finley_NodeFile_createDenseNodeLabeling(Finley_NodeFile* in, index_t* node_distribution, const index_t* dof_distribution);
dim_t Finley_NodeFile_createDenseReducedNodeLabeling(Finley_NodeFile* in, index_t* reducedNodeMask);
dim_t Finley_NodeFile_createDenseReducedDOFLabeling(Finley_NodeFile* in, index_t* reducedNodeMask);
void Finley_NodeFile_assignMPIRankToDOFs(Finley_NodeFile* in,Esys_MPI_rank* mpiRankOfDOF, index_t *distribution);
void Finley_NodeFile_gather(index_t*,Finley_NodeFile*,Finley_NodeFile*);
void Finley_NodeFile_gather_global(index_t*,Finley_NodeFile*,Finley_NodeFile*);
void Finley_NodeFile_gatherEntries(dim_t, index_t*, index_t, index_t, index_t*, index_t*, index_t*, index_t*, index_t*, index_t*, dim_t numDim, double*, double*);
void Finley_NodeFile_copyTable(dim_t,Finley_NodeFile*,dim_t,dim_t,Finley_NodeFile*);
void Finley_NodeFile_scatter(index_t*,Finley_NodeFile*,Finley_NodeFile*);
void Finley_NodeFile_scatterEntries(dim_t, index_t*, index_t, index_t, index_t*, index_t*, index_t*, index_t*, index_t*, index_t*, dim_t numDim, double*, double*);
void Finley_NodeFile_copyTable(dim_t,Finley_NodeFile*,dim_t,dim_t,Finley_NodeFile*);
void Finley_NodeFile_setGlobalReducedDegreeOfFreedomRange(index_t* min_id,index_t* max_id,Finley_NodeFile* in);
void Finley_NodeFile_setGlobalNodeIDIndexRange(index_t* min_id,index_t* max_id,Finley_NodeFile* in);
void Finley_NodeFile_setGlobalReducedNodeIDIndexRange(index_t* min_id,index_t* max_id,Finley_NodeFile* in);

/* ===================== */
void Finley_NodeFile_setCoordinates(Finley_NodeFile*,escriptDataC*);
void Finley_NodeFile_setTags(Finley_NodeFile*,const int,escriptDataC*);
void Finley_NodeFile_setTagsInUse(Finley_NodeFile* in);

#endif

