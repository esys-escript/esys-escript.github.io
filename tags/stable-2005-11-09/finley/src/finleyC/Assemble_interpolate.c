/*
 ******************************************************************************
 *                                                                            *
 *       COPYRIGHT  ACcESS 2003,2004,2005 -  All Rights Reserved              *
 *                                                                            *
 * This software is the property of ACcESS. No part of this code              *
 * may be copied in any form or by any means without the expressed written    *
 * consent of ACcESS.  Copying, use or modification of this software          *
 * by any unauthorised person is illegal unless that person has a software    *
 * license agreement with ACcESS.                                             *
 *                                                                            *
 ******************************************************************************
*/

/**************************************************************/

/*    assemblage routines: interpolates nodal data in a data array onto elements (=integration points) */

/**************************************************************/

/*  Author: gross@access.edu.au */
/*  Version: $Id$ */

/**************************************************************/

#include "Assemble.h"
#include "Util.h"
#ifdef _OPENMP
#include <omp.h>
#endif

/**************************************************************/


void Finley_Assemble_interpolate(Finley_NodeFile *nodes, Finley_ElementFile* elements,escriptDataC* data,escriptDataC* interpolated_data) {
  double* local_data=NULL,*S=NULL,*data_array; 
  index_t dof_offset,*resort_nodes;
  dim_t q,i,NS_DOF,NN_DOF,numNodes,e;
  type_t type;
  #define NODES 0
  #define DOF 1
  #define REDUCED_DOF 2
  if (nodes==NULL || elements==NULL) return;
  dim_t NN=elements->ReferenceElement->Type->numNodes;
  dim_t NS=elements->ReferenceElement->Type->numShapes;
  dim_t numComps=getDataPointSize(data);
  type_t data_type=getFunctionSpaceType(data);
  dim_t numQuad=elements->ReferenceElement->numQuadNodes;
  index_t id[NN];
  for (i=0;i<NN;i++) id[i]=i;
  Finley_resetError();

  /* set some parameter */

  if (data_type==FINLEY_NODES) {
       type=NODES;
       resort_nodes=id;
       NN_DOF=elements->ReferenceElement->Type->numNodes;
       NS_DOF=elements->ReferenceElement->Type->numShapes;
       S=elements->ReferenceElement->S;
       numNodes=nodes->numNodes;
  } else if (data_type==FINLEY_DEGREES_OF_FREEDOM) {
       type=DOF;
       resort_nodes=id;
       NN_DOF=elements->ReferenceElement->Type->numNodes;
       NS_DOF=elements->ReferenceElement->Type->numShapes;
       S=elements->ReferenceElement->S;
       numNodes=nodes->numDegreesOfFreedom;
  } else if (data_type==FINLEY_REDUCED_DEGREES_OF_FREEDOM) {
       type=REDUCED_DOF;
       resort_nodes=elements->ReferenceElement->Type->linearNodes;
       NN_DOF=elements->LinearReferenceElement->Type->numNodes;
       NS_DOF=elements->LinearReferenceElement->Type->numShapes;
       S=elements->LinearReferenceElement->S;
       numNodes=nodes->reducedNumDegreesOfFreedom;
   } else {
       Finley_setError(TYPE_ERROR,"__FILE__: Cannot interpolate data");
  }

  if (getFunctionSpaceType(interpolated_data)==FINLEY_CONTACT_ELEMENTS_2) {
       dof_offset=NN_DOF-NS_DOF;
  } else {
       dof_offset=0;
  }

  /* check the dimensions of interpolated_data and data */

  if (! numSamplesEqual(interpolated_data,numQuad,elements->numElements)) {
       Finley_setError(TYPE_ERROR,"__FILE__: illegal number of samples of output Data object");
  } else if (! numSamplesEqual(data,1,numNodes)) {
       Finley_setError(TYPE_ERROR,"__FILE__: illegal number of samples of input Data object");
  } else if (numComps!=getDataPointSize(interpolated_data)) {
       Finley_setError(TYPE_ERROR,"__FILE__: number of components of input and interpolated Data do not match.");
  }  else if (!isExpanded(interpolated_data)) {
       Finley_setError(TYPE_ERROR,"__FILE__: expanded Data object is expected for output data.");
  }

  /* now we can start */

  if (Finley_noError()) {
       #pragma omp parallel private(local_data)
       {
          local_data=NULL; 
          /* allocation of work arrays */
          local_data=THREAD_MEMALLOC(NS*numComps,double); 
          if (! Finley_checkPtr(local_data)) {

	    /* open the element loop */

            #pragma omp for private(e,q,i,data_array) schedule(static)
	    for(e=0;e<elements->numElements;e++) {
   	      /* gather local data into local_data(numComps,NS_DOF): */
              switch (type) {
                 case NODES:
                        for (q=0;q<NS_DOF;q++) {
                           i=elements->Nodes[INDEX2(resort_nodes[dof_offset+q],e,NN)];
                           data_array=getSampleData(data,i);
                           Finley_copyDouble(numComps,data_array,local_data+q*numComps);
                        }
                        break;
                 case DOF:
                        for (q=0;q<NS_DOF;q++) {
                           i=elements->Nodes[INDEX2(resort_nodes[dof_offset+q],e,NN)];
                           data_array=getSampleData(data,nodes->degreeOfFreedom[i]);
                           Finley_copyDouble(numComps,data_array,local_data+q*numComps);
                        }
                        break;
                 case REDUCED_DOF:
                        for (q=0;q<NS_DOF;q++) {
                           i=elements->Nodes[INDEX2(resort_nodes[dof_offset+q],e,NN)];
                           data_array=getSampleData(data,nodes->reducedDegreeOfFreedom[i]);
                           Finley_copyDouble(numComps,data_array,local_data+q*numComps);
                        }
                        break;
              }

	      /*  calculate interpolated_data=local_data*S */

	      Finley_Util_SmallMatMult(numComps,numQuad,getSampleData(interpolated_data,e),NS_DOF,local_data,S);

	    } /* end of element loop */

          }
	  THREAD_MEMFREE(local_data);
     } /* end of parallel region */
  }
  #undef NODES 
  #undef DOF 
  #undef REDUCED_DOF 
}
/*
 * $Log$
 * Revision 1.6  2005/09/15 03:44:21  jgs
 * Merge of development branch dev-02 back to main trunk on 2005-09-15
 *
 * Revision 1.5.2.1  2005/09/07 06:26:18  gross
 * the solver from finley are put into the standalone package paso now
 *
 * Revision 1.5  2005/07/08 04:07:48  jgs
 * Merge of development branch back to main trunk on 2005-07-08
 *
 * Revision 1.4  2004/12/15 07:08:32  jgs
 * *** empty log message ***
 * Revision 1.1.1.1.2.3  2005/06/29 02:34:48  gross
 * some changes towards 64 integers in finley
 *
 * Revision 1.1.1.1.2.2  2004/11/24 01:37:12  gross
 * some changes dealing with the integer overflow in memory allocation. Finley solves 4M unknowns now
 *
 *
 *
 */