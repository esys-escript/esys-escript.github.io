
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


/**************************************************************/

/*    assemblage routines: */

/*    calculates the minimum distance between two vertices of elements and assigns the value to each  */
/*    quadrature point in element_size                                                                         */


/**************************************************************/

#include "Assemble.h"
#include "Util.h"
#ifdef _OPENMP
#include <omp.h>
#endif

/**************************************************************/
void Finley_Assemble_getSize(Finley_NodeFile* nodes, Finley_ElementFile* elements, escriptDataC* element_size) {

  double *local_X=NULL,*element_size_array;
  dim_t e,n0,n1,q,i, NVertices, NN, NS, numQuad, numDim;
  index_t node_offset;
  double d,diff,min_diff;
  Finley_resetError();

  if (nodes==NULL || elements==NULL) return;
  NVertices=elements->ReferenceElement->Type->numVertices;
  NN=elements->ReferenceElement->Type->numNodes;
  NS=elements->ReferenceElement->Type->numShapes;
  numDim=nodes->numDim;
  
  if (Finley_Assemble_reducedIntegrationOrder(element_size)) {
      numQuad=elements->ReferenceElementReducedOrder->numQuadNodes;
  } else {
      numQuad=elements->ReferenceElement->numQuadNodes;
  }

  /* set a few more parameters */

  if (getFunctionSpaceType(element_size)==FINLEY_CONTACT_ELEMENTS_2) {
      node_offset=NN-NS;
  } else {
      node_offset=0;
  }

  /* check the dimensions of element_size */

  /* if (numDim!=elements->ReferenceElement->Type->numDim) {
     Finley_setError(TYPE_ERROR,"Finley_Assemble_getSize: Spatial and element dimension must match.");
  } else  */
  if (! numSamplesEqual(element_size,numQuad,elements->numElements)) {
       Finley_setError(TYPE_ERROR,"Finley_Assemble_getSize: illegal number of samples of element size Data object");
  } else if (! isDataPointShapeEqual(element_size,0,&(numDim))) {
       Finley_setError(TYPE_ERROR,"Finley_Assemble_getSize: illegal data point shape of element size Data object");
  }  else if (!isExpanded(element_size)) {
       Finley_setError(TYPE_ERROR,"Finley_Assemble_getSize: expanded Data object is expected for element size.");
  }
  /* now we can start: */

  if (Finley_noError()) {
	requireWrite(element_size);
        #pragma omp parallel private(local_X)
        {
	   /* allocation of work arrays */
	   local_X=THREAD_MEMALLOC(NN*numDim,double);
	   if (! Finley_checkPtr(local_X) ) {
	     /* open the element loop */
             #pragma omp for private(e,min_diff,diff,n0,n1,d,q,i,element_size_array) schedule(static)
	     for(e=0;e<elements->numElements;e++) {
	       /* gather local coordinates of nodes into local_X(numDim,NN): */
	       Finley_Util_Gather_double(NS,&(elements->Nodes[INDEX2(node_offset,e,NN)]),numDim,nodes->Coordinates,local_X);
	       /* calculate minimal differences */
	       min_diff=-1;
	       for (n0=0;n0<NVertices;n0++) {
	         for (n1=n0+1;n1<NVertices;n1++) {
		   diff=0;
		   for (i=0;i<numDim;i++) {
		     d=local_X[INDEX2(i,n0,numDim)]-local_X[INDEX2(i,n1,numDim)];
		     diff+=d*d;
		   }
		   if (min_diff<0) {
		     min_diff=diff;
		   } else {
		     min_diff=MIN(min_diff,diff);
		   }
	         }
	       }
	       min_diff=sqrt(MAX(min_diff,0));
	       /* set all values to min_diff */
               element_size_array=getSampleDataRW(element_size,e);
	       for (q=0;q<numQuad;q++) element_size_array[q]=min_diff;
	     }
	   }
	   THREAD_MEMFREE(local_X);
        }
  }
  return;
}
