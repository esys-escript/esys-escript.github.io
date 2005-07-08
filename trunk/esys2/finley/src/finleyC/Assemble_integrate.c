/* $Id$ */

/**************************************************************/

/*    assemblage routines: integrates data on quadrature points   */

/**************************************************************/

/*   Copyrights by ACcESS Australia, 2003,2004 */
/*   author: gross@access.edu.au */
/*   Version: $Id$ */

/**************************************************************/

#include "escript/Data/DataC.h"
#include "Finley.h"
#include "Assemble.h"
#include "NodeFile.h"
#include "ElementFile.h"
#include "Util.h"
#ifdef _OPENMP
#include <omp.h>
#endif

/**************************************************************/

void Finley_Assemble_integrate(Finley_NodeFile* nodes, Finley_ElementFile* elements,escriptDataC* data,double* out) {
    type_t datacase;
    index_t node_offset;
    dim_t q,e,i;
    double *local_X, *dVdv, *Vol,*out_local,*data_array,rtmp;
    if (nodes==NULL || elements==NULL) return;
    dim_t NN=elements->ReferenceElement->Type->numNodes;
    dim_t NS=elements->ReferenceElement->Type->numShapes;
    type_t data_type=getFunctionSpaceType(data);
    dim_t numComps=getDataPointSize(data);
    dim_t numQuad=elements->ReferenceElement->numQuadNodes;
    dim_t numDim=nodes->numDim;
    dim_t numDim_local=elements->ReferenceElement->Type->numDim;
                                                                                                                                               
    /* set some parameter */
                                                                                                                                               
    if (data_type==FINLEY_ELEMENTS) {
        datacase=0;
        node_offset=0;
    } else if (data_type==FINLEY_FACE_ELEMENTS)  {
        datacase=1;
        node_offset=0;
    } else if (data_type==FINLEY_CONTACT_ELEMENTS_1)  {
        datacase=1;
        node_offset=0;
    } else if (data_type==FINLEY_CONTACT_ELEMENTS_2)  {
        datacase=1;
        node_offset=NN-NS;
    } else {
       Finley_ErrorCode=TYPE_ERROR;
       sprintf(Finley_ErrorMsg,"integration of data is not possible.");
    }

    /* check the shape of the data  */

    if (! numSamplesEqual(data,numQuad,elements->numElements)) {
       Finley_ErrorCode=TYPE_ERROR;
       sprintf(Finley_ErrorMsg,"illegal number of samples of integrant kernel Data object");
    }

    /* now we can start */

    if (Finley_ErrorCode==NO_ERROR) {
        for (q=0;q<numComps;q++) out[q]=0;
        #pragma omp parallel private(local_X,dVdv,Vol,out_local,i)
        {

            /* allocation of work arrays */

            local_X=dVdv=Vol=out_local=NULL;
            out_local=THREAD_MEMALLOC(numComps,double); 
            dVdv=THREAD_MEMALLOC(numQuad*numDim_local*numDim,double);
            Vol=THREAD_MEMALLOC(numQuad,double);
            local_X=THREAD_MEMALLOC(NS*numDim,double); 

            if (! (Finley_checkPtr(Vol) || Finley_checkPtr(local_X) || Finley_checkPtr(dVdv)  || Finley_checkPtr(out_local))) {

               /* initialize local result */

	       for (i=0;i<numComps;i++) out_local[i]=0;

               /* open the element loop */

               #pragma omp for private(e,q,data_array,rtmp) schedule(static)
               for(e=0;e<elements->numElements;e++) {
                    /* gather local coordinates of nodes into local_X: */
                    Finley_Util_Gather_double(NS,&(elements->Nodes[INDEX2(node_offset,e,NN)]),numDim,nodes->Coordinates,local_X);
                    /*  calculate dVdv(i,j,q)=V(i,k)*DSDv(k,j,q) */
                    Finley_Util_SmallMatMult(numDim,numDim_local*numQuad,dVdv,NS,local_X,elements->ReferenceElement->dSdv);
                    /* calculate volume /area elements */
                    switch (datacase) {
                        case 0:
                           Finley_Util_DetOfSmallMat(numQuad,numDim,dVdv,Vol);
                           break;
                        case 1:
                           Finley_LengthOfNormalVector(numQuad,numDim,numDim_local,dVdv,Vol);
                           break;
                    }
                    /* out=out+ integrals */
                    data_array=getSampleData(data,e);
                    if (isExpanded(data)) {
                         for (q=0;q<numQuad;q++) {
                            rtmp=ABS(Vol[q])*elements->ReferenceElement->QuadWeights[q];
                            for (i=0;i<numComps;i++) out_local[i]+=data_array[INDEX2(i,q,numComps)]*rtmp;
                         }
                    } else {
                         rtmp=0.;
                         for (q=0;q<numQuad;q++) rtmp+=ABS(Vol[q])*elements->ReferenceElement->QuadWeights[q];
                         for (i=0;i<numComps;i++) out_local[i]+=data_array[i]*rtmp;
                    }
               }

               /* add local results to global result */
               #pragma omp critical
               for (i=0;i<numComps;i++) out[i]+=out_local[i];

           }
           THREAD_MEMFREE(local_X);
           THREAD_MEMFREE(dVdv);
           THREAD_MEMFREE(Vol);
           THREAD_MEMFREE(out_local);
       }
    }
}

/*
 * $Log$
 * Revision 1.5  2005/07/08 04:07:48  jgs
 * Merge of development branch back to main trunk on 2005-07-08
 *
 * Revision 1.4  2004/12/15 07:08:32  jgs
 * *** empty log message ***
 * Revision 1.1.1.1.2.2  2005/06/29 02:34:48  gross
 * some changes towards 64 integers in finley
 *
 * Revision 1.1.1.1.2.1  2004/11/24 01:37:12  gross
 * some changes dealing with the integer overflow in memory allocation. Finley solves 4M unknowns now
 *
 *
 *
 */
