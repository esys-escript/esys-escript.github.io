/* $Id$ */

#ifndef INC_FINLEY_MESH
#define INC_FINLEY_MESH

/**************************************************************/

/* Finley: Mesh */

/* A mesh is built from nodes and elements which are describing the
   domain, the surface and point sources. (the latter are needed to
   establish links with other codes, in particular to particle
   codes). The nodes are stored a Finley_NodeFile and elements in a
   Finley_ElementFile. A Finley_NodeFile and three Finley_ElementFile
   containing the elements describing the domain, surface and point
   sources respectively. Notice that the surface elements do not
   necessaryly cover the entire surface of the domain. */

/* The element type is fixed by the reference element, see
   ReferenceElement.h. The numbering of the nodes starts with 0. */

/* Important: it is assumed that every node is appearing in at least
   one element or surface element and that any node used in an
   element, surface element or as a point is specified in the
   Finley_Node, see also Finley_resolveNodeIds. */

/* In some cases it is useful to refer to a mesh entirly built from
   order 1 (=linear) elements. The linear version of the mesh can be
   accessed by referning to the first few nodes of each element
   (thanks to the way the nodes are ordered). As the numbering of
   these nodes is not continuous a relabeling vectors are introduced
   in the Finley_NodeFile. This feature is not fully implemented
   yet. */

/* allnodes and elements are tagged. the tag allows to group nodes and
   elements. A typical application is to mark surface elements on a
   certain portion of the domain with the same tag. All these surface
   elements can then assigned the same value eg. for the pressure. */

/* Thespacial dimension is determined by the type of elements
   used. The spacial dimension should be accessed by the function
   Finley_Mesh_getDim. Notice that the element type also determines
   the type of surface elements to be used. */

/**************************************************************/

#include "NodeFile.h"
#include "ElementFile.h"
#include "escript/Data/DataC.h"

/**************************************************************/

/*  this struct holds a mesh: */

struct Finley_Mesh {
  char* Name;                           /* the name of the mesh */
  int order;                            /* integration order */
  int reference_counter;                /* counts the number of references to the mesh; */
  Finley_NodeFile* Nodes;               /* the table of the nodes */
  Finley_ElementFile* Elements;         /* the table of the elements */
  Finley_ElementFile* FaceElements;     /* the table of the face elements */
  Finley_ElementFile* ContactElements;  /* the table of the contact elements */
  Finley_ElementFile* Points;           /* the table of points (treated as elements of dimension 0) */
};

typedef struct Finley_Mesh Finley_Mesh;

/* these structures are used for matching surfaces elements: */

struct Finley_Mesh_findMatchingFaces_center{
   int refId;
   double x[MAX_numDim];
};
typedef struct Finley_Mesh_findMatchingFaces_center Finley_Mesh_findMatchingFaces_center;

/**************************************************************/

/*  interfaces: */

Finley_Mesh* Finley_Mesh_alloc(char*,int,int);
void Finley_Mesh_dealloc(Finley_Mesh*);
int Finley_Mesh_getDim(Finley_Mesh*);
int Finley_Mesh_getNumNodes(Finley_Mesh*);
int Finley_Mesh_getNumDegreesOfFreedom(Finley_Mesh*);
int Finley_Mesh_getReducedNumDegreesOfFreedom(Finley_Mesh*);
void Finley_Mesh_write(Finley_Mesh*,char*);
Finley_Mesh* Finley_Mesh_read(char*,int);

void Finley_Mesh_prepare(Finley_Mesh* in);
void Finley_Mesh_prepareNodes(Finley_Mesh* in);
void Finley_Mesh_improveColoring(Finley_Mesh* in);
void Finley_Mesh_optimizeElementDistribution(Finley_Mesh* in);
void  Finley_Mesh_resolveNodeIds(Finley_Mesh*);
Finley_Mesh* Finley_Mesh_merge(int, Finley_Mesh**);

void Finley_Mesh_relableElementNodes(int*,int,Finley_Mesh*);
void Finley_Mesh_markNodes(int*,int,Finley_Mesh*,int);

void Finley_Mesh_glueFaces(Finley_Mesh* self,double safety_factor,double tolerance);
void Finley_Mesh_joinFaces(Finley_Mesh* self,double safety_factor,double tolerance);

int Finley_Mesh_findMatchingFaces_compar(const void*,const void*);
void Finley_Mesh_findMatchingFaces(Finley_NodeFile*,Finley_ElementFile *,double,double, int*, int*,int*,int*);
void Finley_Mesh_print(Finley_Mesh *in);
void Finley_Mesh_saveDX(const char *, Finley_Mesh *, escriptDataC*);

#endif /* #ifndef INC_FINLEY_MESH */

/*
 * $Log$
 * Revision 1.1  2004/10/26 06:53:57  jgs
 * Initial revision
 *
 * Revision 1.5  2004/07/27 08:26:45  gross
 * Finley: saveDX added: now it is possible to write data on boundary and contact elements
 *
 * Revision 1.4  2004/07/26 04:27:15  gross
 * it allmost compiles now
 *
 * Revision 1.3  2004/07/02 04:21:13  gross
 * Finley C code has been included
 *
 * Revision 1.2  2004/07/02 00:03:29  gross
 * interface for saveDX added
 *
 * Revision 1.1.1.1  2004/06/24 04:00:40  johng
 * Initial version of eys using boost-python.
 *
 *
 */
