/*
 ************************************************************
 *          Copyright 2006 by ACcESS MNRF                   *
 *                                                          *
 *              http://www.access.edu.au                    *
 *       Primary Business: Queensland, Australia            *
 *  Licensed under the Open Software License version 3.0    *
 *     http://www.opensource.org/licenses/osl-3.0.php       *
 *                                                          *
 ************************************************************
*/

/**************************************************************/

/*    assemblage rjacines: calculate the gradient of nodal data at quadrature points */

/**************************************************************/

/*   Copyrights by ACcESS Australia, 2003,2004,2005 */
/*   author: gross@access.edu.au */
/*   version: $Id$ */

/**************************************************************/

#include "Assemble.h"
#include "Util.h"
#ifdef _OPENMP
#include <omp.h>
#endif
/*****************************************************************/


void Finley_Assemble_gradient(Finley_NodeFile* nodes, Finley_ElementFile* elements,
                              escriptDataC* grad_data,escriptDataC* data) {

  dim_t numNodes, numShapes, numLocalNodes, numComps, NN;
  type_t data_type=getFunctionSpaceType(data);
  bool_t reducedShapefunction=FALSE, reducedIntegrationOrder=FALSE;
  Finley_NodeMapping *mapping=NULL;
  index_t dof_offset, s_offset;
  Finley_ElementFile_Jacobeans* jac=NULL;
  type_t grad_data_type=getFunctionSpaceType(grad_data);
  Finley_resetError();
  if (nodes==NULL || elements==NULL) return;
  numComps=getDataPointSize(data);
  NN=elements->ReferenceElement->Type->numNodes;
  reducedIntegrationOrder=Finley_Assemble_reducedIntegrationOrder(grad_data);

  if (data_type==FINLEY_NODES) {
       reducedShapefunction=FALSE;
       mapping=nodes->nodesMapping;
  } else if (data_type==FINLEY_REDUCED_NODES) { 
       reducedShapefunction=TRUE;
       mapping=nodes->reducedNodesMapping;
  } else if (data_type==FINLEY_DEGREES_OF_FREEDOM) {
       if (elements->MPIInfo->size>1) {
          Finley_setError(TYPE_ERROR,"Finley_Assemble_gradient: for more than one processor DEGREES_OF_FREEDOM data are not accepted as input.");
          return;
       }
       reducedShapefunction=FALSE;
       mapping=nodes->degreesOfFreedomMapping;
  } else if (data_type==FINLEY_REDUCED_DEGREES_OF_FREEDOM) {
       if (elements->MPIInfo->size>1) {
          Finley_setError(TYPE_ERROR,"Finley_Assemble_gradient: for more than one processor REDUCED_DEGREES_OF_FREEDOM data are not accepted as input.");
          return;
       }
       reducedShapefunction=TRUE;
       mapping=nodes->reducedDegreesOfFreedomMapping;
  } else {
       Finley_setError(TYPE_ERROR,"Finley_Assemble_gradient: Cannot calculate gradient of data because of unsuitable input data representation.");
  }

  jac=Finley_ElementFile_borrowJacobeans(elements,nodes,reducedShapefunction,reducedIntegrationOrder);
  if (Finley_noError()) {

      numShapes=jac->ReferenceElement->Type->numShapes;
      numLocalNodes=jac->ReferenceElement->Type->numNodes;
      if (grad_data_type==FINLEY_CONTACT_ELEMENTS_2 || grad_data_type== FINLEY_REDUCED_CONTACT_ELEMENTS_2)  {
       dof_offset=numShapes;
       s_offset=jac->ReferenceElement->Type->numShapes;
      } else {
       dof_offset=0;
       s_offset=0;
      }

      /* check the dimensions of data */

      if (! numSamplesEqual(grad_data,jac->ReferenceElement->numQuadNodes,elements->numElements)) {
           Finley_setError(TYPE_ERROR,"Finley_Assemble_gradient: illegal number of samples in gradient Data object");
      } else if (! numSamplesEqual(data,1,mapping->numTargets)) {
           Finley_setError(TYPE_ERROR,"Finley_Assemble_gradient: illegal number of samples of input Data object");
      } else if (jac->numDim*numComps!=getDataPointSize(grad_data)) {
           Finley_setError(TYPE_ERROR,"Finley_Assemble_gradient: illegal number of components in gradient data object.");
      }  else if (!isExpanded(grad_data)) {
           Finley_setError(TYPE_ERROR,"Finley_Assemble_gradient: expanded Data object is expected for output data.");
      } else if (! (dof_offset+jac->ReferenceElement->Type->numShapes <= numLocalNodes)) {
           Finley_setError(SYSTEM_ERROR,"Finley_Assemble_gradient: nodes per element is inconsistent with number of jacobeans.");
      } else if (! (s_offset+jac->ReferenceElement->Type->numShapes <= jac->ReferenceElement->Type->numNodes)) {
           Finley_setError(SYSTEM_ERROR,"Finley_Assemble_gradient: offset test failed.");
      }
  }
  /* now we can start */

  if (Finley_noError()) {
      register dim_t e,q,l,s,n;
      register double* data_array,  *grad_data_e;
      #pragma omp parallel private(e,q,l,s,n,data_array,grad_data_e)
      {
         if (jac->numDim==1) {
                #define DIM 1
                #pragma omp for schedule(static)
   	        for (e=0;e<elements->numElements;e++) {
                    grad_data_e=getSampleData(grad_data,e);
                    for (q=0;q<DIM*(jac->ReferenceElement->numQuadNodes)*numComps; q++) grad_data_e[q]=0;
                    for (s=0;s<jac->ReferenceElement->Type->numShapes;s++) {
                       n=mapping->target[elements->Nodes[INDEX2(dof_offset+s,e,NN)]];
                       data_array=getSampleData(data,n);
                       for (q=0;q<jac->ReferenceElement->numQuadNodes;q++) {
                           for (l=0;l<numComps;l++) {
                                grad_data_e[INDEX3(l,0,q,numComps,DIM)]+=data_array[l]* 
                                      jac->DSDX[INDEX4(s_offset+s,0,q,e,jac->ReferenceElement->Type->numNodes,DIM,jac->ReferenceElement->numQuadNodes)];
                           }
                       }
                    }
                }

                #undef DIM
         } else if (jac->numDim==2) {
                #define DIM 2
                #pragma omp for schedule(static)
   	        for (e=0;e<elements->numElements;e++) {
                    grad_data_e=getSampleData(grad_data,e);
                    for (q=0;q<DIM*(jac->ReferenceElement->numQuadNodes)*numComps; q++) grad_data_e[q]=0;
                    for (s=0;s<jac->ReferenceElement->Type->numShapes;s++) {
                       n=mapping->target[elements->Nodes[INDEX2(dof_offset+s,e,NN)]];
                       data_array=getSampleData(data,n);
                       for (q=0;q<jac->ReferenceElement->numQuadNodes;q++) {
                           for (l=0;l<numComps;l++) {
                               grad_data_e[INDEX3(l,0,q,numComps,DIM)]+=data_array[l]* 
                                        jac->DSDX[INDEX4(s_offset+s,0,q,e,jac->ReferenceElement->Type->numNodes,DIM,jac->ReferenceElement->numQuadNodes)];
                               grad_data_e[INDEX3(l,1,q,numComps,DIM)]+=data_array[l]* 
                                        jac->DSDX[INDEX4(s_offset+s,1,q,e,jac->ReferenceElement->Type->numNodes,DIM,jac->ReferenceElement->numQuadNodes)];
                           }
                       }
                    }
                }
                #undef DIM
         } else if (jac->numDim==3) {
                #define DIM 3
                #pragma omp for private(e,grad_data_e,s,n,data_array,q,l) schedule(static)
   	        for (e=0;e<elements->numElements;e++) {
                    grad_data_e=getSampleData(grad_data,e); 
                    for (q=0;q<DIM*(jac->ReferenceElement->numQuadNodes)*numComps; q++) grad_data_e[q]=0;
                    for (s=0;s<jac->ReferenceElement->Type->numShapes;s++) {
                       n=mapping->target[elements->Nodes[INDEX2(dof_offset+s,e,NN)]];
                       data_array=getSampleData(data,n);
                       for (q=0;q<jac->ReferenceElement->numQuadNodes;q++) {
                           for (l=0;l<numComps;l++) {
                               grad_data_e[INDEX3(l,0,q,numComps,DIM)]+=data_array[l]*
                                    jac->DSDX[INDEX4(s_offset+s,0,q,e,jac->ReferenceElement->Type->numNodes,DIM,jac->ReferenceElement->numQuadNodes)];
                               grad_data_e[INDEX3(l,1,q,numComps,DIM)]+=data_array[l]*
                                    jac->DSDX[INDEX4(s_offset+s,1,q,e,jac->ReferenceElement->Type->numNodes,DIM,jac->ReferenceElement->numQuadNodes)];
                               grad_data_e[INDEX3(l,2,q,numComps,DIM)]+=data_array[l]*
                                    jac->DSDX[INDEX4(s_offset+s,2,q,e,jac->ReferenceElement->Type->numNodes,DIM,jac->ReferenceElement->numQuadNodes)];
                           }
                       }
                    }
                }
                #undef DIM
         }
      } /* end parallel region */
  }
}
