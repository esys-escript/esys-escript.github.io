/*
 ************************************************************
 *          Copyright 2006,2007 by ACcENULLNULL MNRF              *
 *                                                          *
 *              http://www.access.edu.au                    *
 *       Primary Business: Queensland, Australia            *
 *  Licensed under the Open NULLoftware License version 3.0    *
 *     http://www.opensource.org/licenses/osl-3.0.php       *
 *                                                          *
 ************************************************************
*/


/**************************************************************/

/*    assembles the mass matrix in lumped form                */

/*    The coefficient D has to be defined on the integration points or not present. */

/*    lumpedMat has to be initialized before the routine is called. */

/**************************************************************/

/*  Author: gross@access.edu.au */
/*  Version: $Id: Assemble_LumpedSystem.c 1204 2007-06-23 11:43:12Z gross $ */

/**************************************************************/

#include "Assemble.h"
#include "Util.h"
#ifdef _OPENMP
#include <omp.h>
#endif


/**************************************************************/

void Finley_Assemble_LumpedSystem(Finley_NodeFile* nodes,Finley_ElementFile* elements, escriptDataC* lumpedMat, escriptDataC* D) 
{

  bool_t reducedIntegrationOrder=FALSE, expandedD;
  char error_msg[LenErrorMsg_MAX];
  Assemble_Parameters p;
  double time0;
  dim_t dimensions[ESCRIPT_MAX_DATA_RANK], k, e, len_EM_lumpedMat, q, s;
  type_t funcspace;
  index_t color,*row_index=NULL;
  double *S=NULL, *EM_lumpedMat=NULL, *Vol=NULL, *D_p=NULL, *lumpedMat_p=NULL;
  register double rtmp;
  size_t len_EM_lumpedMat_size;

  Finley_resetError();

  if (nodes==NULL || elements==NULL) return;
  if (isEmpty(lumpedMat) || isEmpty(D)) return;
  if (isEmpty(lumpedMat) && !isEmpty(D)) { 
        Finley_setError(TYPE_ERROR,"Assemble_LumpedSystem: coefficients are non-zero but no lumped matrix is given.");
        return;
  }
  funcspace=getFunctionSpaceType(D);
  /* check if all function spaces are the same */
  if (funcspace==FINLEY_ELEMENTS) {
       reducedIntegrationOrder=FALSE;
  } else if (funcspace==FINLEY_FACE_ELEMENTS)  {
       reducedIntegrationOrder=FALSE;
  } else if (funcspace==FINLEY_REDUCED_ELEMENTS) {
       reducedIntegrationOrder=TRUE;
  } else if (funcspace==FINLEY_REDUCED_FACE_ELEMENTS)  {
       reducedIntegrationOrder=TRUE;
  } else {
       Finley_setError(TYPE_ERROR,"Assemble_LumpedSystem: assemblage failed because of illegal function space.");
  }
  if (! Finley_noError()) return;

  /* set all parameters in p*/
  Assemble_getAssembleParameters(nodes,elements,NULL,lumpedMat, reducedIntegrationOrder, &p);
  if (! Finley_noError()) return;

  /* check if all function spaces are the same */

  if (! numSamplesEqual(D,p.numQuad,elements->numElements) ) {
        sprintf(error_msg,"Assemble_LumpedSystem: sample points of coefficient D don't match (%d,%d)",p.numQuad,elements->numElements);
        Finley_setError(TYPE_ERROR,error_msg);
  }

  /*  check the dimensions: */
  
  if (p.numEqu==1) {
    if (!isEmpty(D)) {
       if (!isDataPointShapeEqual(D,0,dimensions)) {
          Finley_setError(TYPE_ERROR,"Assemble_LumpedSystem: coefficient D, rank 0 expected.");
       }

    }
  } else {
    if (!isEmpty(D)) {
      dimensions[0]=p.numEqu;
      if (!isDataPointShapeEqual(D,1,dimensions)) {
          sprintf(error_msg,"Assemble_LumpedSystem: coefficient D, expected shape (%d,)",dimensions[0]);
          Finley_setError(TYPE_ERROR,error_msg);
      }
    }
  }

  if (Finley_noError()) {
    lumpedMat_p=getSampleData(lumpedMat,0);
    len_EM_lumpedMat=p.row_NN*p.numEqu;
    len_EM_lumpedMat_size=len_EM_lumpedMat*sizeof(double);
    expandedD=isExpanded(D);
    S=p.row_jac->ReferenceElement->S;

    #pragma omp parallel private(color, EM_lumpedMat, row_index, Vol, D_p, s, q, k, rtmp)
    {
       EM_lumpedMat=THREAD_MEMALLOC(len_EM_lumpedMat,double);
       row_index=THREAD_MEMALLOC(p.row_NN,index_t);
       if ( !Finley_checkPtr(EM_lumpedMat) && !Finley_checkPtr(row_index) ) {
          if (p.numEqu == 1) {
             if (expandedD) {
                 #ifndef PASO_MPI
                 for (color=elements->minColor;color<=elements->maxColor;color++) {
                    /*  open loop over all elements: */
                    #pragma omp for private(e) schedule(static)
                    for(e=0;e<elements->numElements;e++){
                       if (elements->Color[e]==color) {
                 #else
                 {
                    for(e=0;e<elements->numElements;e++) {
                       {
                 #endif
                          Vol=&(p.row_jac->volume[INDEX2(0,e,p.numQuad)]);
                          memset(EM_lumpedMat,0,len_EM_lumpedMat_size);
                          D_p=getSampleData(D,e);
                          for (s=0;s<p.row_NS;s++) {
                              rtmp=0;
                              for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)]*D_p[q];
                              EM_lumpedMat[INDEX2(0,s,p.numEqu)]+=rtmp;
                          }
                          for (q=0;q<p.row_NN;q++) row_index[q]=p.row_DOF[elements->Nodes[INDEX2(p.row_node[q],e,p.NN)]];
                          Finley_Util_AddScatter(p.row_NN,row_index,p.numEqu,EM_lumpedMat,lumpedMat_p, p.row_DOF_UpperBound);
                       } /* end color check */
                    } /* end element loop */
                  } /* end color loop */
             } else  {
                 #ifndef PASO_MPI
                 for (color=elements->minColor;color<=elements->maxColor;color++) {
                 /*  open loop over all elements: */
                 #pragma omp for private(e) schedule(static)
                 for(e=0;e<elements->numElements;e++){
                    if (elements->Color[e]==color) {
                 #else
                 {
                    for(e=0;e<elements->numElements;e++) {
                       {
                 #endif
                           Vol=&(p.row_jac->volume[INDEX2(0,e,p.numQuad)]);
                           memset(EM_lumpedMat,0,len_EM_lumpedMat_size);
                           D_p=getSampleData(D,e);
                           for (s=0;s<p.row_NS;s++) {
                               rtmp=0;
                               for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)];
                               EM_lumpedMat[INDEX2(0,s,p.numEqu)]+=rtmp*D_p[0];
                           }
                           for (q=0;q<p.row_NN;q++) row_index[q]=p.row_DOF[elements->Nodes[INDEX2(p.row_node[q],e,p.NN)]];
                           Finley_Util_AddScatter(p.row_NN,row_index,p.numEqu,EM_lumpedMat,lumpedMat_p, p.row_DOF_UpperBound);
                      } /* end color check */
                    } /* end element loop */
                 } /* end color loop */
             }
          } else {
             if (expandedD) {
                 #ifndef PASO_MPI
                 for (color=elements->minColor;color<=elements->maxColor;color++) {
                    /*  open loop over all elements: */
                    #pragma omp for private(e) schedule(static)
                    for(e=0;e<elements->numElements;e++){
                       if (elements->Color[e]==color) {
                 #else
                 {
                    for(e=0;e<elements->numElements;e++) {
                       {
                 #endif
                          Vol=&(p.row_jac->volume[INDEX2(0,e,p.numQuad)]);
                          memset(EM_lumpedMat,0,len_EM_lumpedMat_size);
                          D_p=getSampleData(D,e);
                          for (s=0;s<p.row_NS;s++) {
                              for (k=0;k<p.numEqu;k++) {
                                  rtmp=0.;
                                  for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)]*D_p[INDEX2(k,q,p.numEqu)];
                                  EM_lumpedMat[INDEX2(k,s,p.numEqu)]+=rtmp;
                              }
                          }
                          for (q=0;q<p.row_NN;q++) row_index[q]=p.row_DOF[elements->Nodes[INDEX2(p.row_node[q],e,p.NN)]];
                          Finley_Util_AddScatter(p.row_NN,row_index,p.numEqu,EM_lumpedMat,lumpedMat_p, p.row_DOF_UpperBound);
                       } /* end color check */
                    } /* end element loop */
                } /* end color loop */
             } else {
                 #ifndef PASO_MPI
                 for (color=elements->minColor;color<=elements->maxColor;color++) {
                    /*  open loop over all elements: */
                    #pragma omp for private(e) schedule(static)
                    for(e=0;e<elements->numElements;e++){
                       if (elements->Color[e]==color) {
                 #else
                 {
                    for(e=0;e<elements->numElements;e++) {
                       {
                 #endif
                          Vol=&(p.row_jac->volume[INDEX2(0,e,p.numQuad)]);
                          memset(EM_lumpedMat,0,len_EM_lumpedMat_size);
                          D_p=getSampleData(D,e);
                          for (s=0;s<p.row_NS;s++) {
                              rtmp=0;
                              for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)];
                              for (k=0;k<p.numEqu;k++) EM_lumpedMat[INDEX2(k,s,p.numEqu)]+=rtmp*D_p[k];
                          }
                          for (q=0;q<p.row_NN;q++) row_index[q]=p.row_DOF[elements->Nodes[INDEX2(p.row_node[q],e,p.NN)]];
                          Finley_Util_AddScatter(p.row_NN,row_index,p.numEqu,EM_lumpedMat,lumpedMat_p, p.row_DOF_UpperBound);
                       } /* end color check */
                    } /* end element loop */
                } /* end color loop */
             }
          }
       } /* end of pointer check */
       THREAD_MEMFREE(EM_lumpedMat);
       THREAD_MEMFREE(row_index);
    } /* end parallel region */
  }
  #ifdef Finley_TRACE
  printf("timing: assemblage lumped PDE: %.4e sec\n",Finley_timer()-time0);
  #endif
}
