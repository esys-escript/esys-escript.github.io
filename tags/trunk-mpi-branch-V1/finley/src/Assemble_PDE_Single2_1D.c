/*
 ************************************************************
 *          Copyright 2006 by ACcESS MNRF                   *
 *                                                          *
 *              http://www.access.edu.au                    *
 *       Primary Business: Queensland, Australia            *
 *  Licensed under the Open Software License version 1.0    *
 *     http://www.opensource.org/licenses/osl-3.0.php       *
 *                                                          *
 ************************************************************
*/

/**************************************************************/

/*    assembles the system of numEq PDEs into the stiffness matrix S right hand side F  */
/*    the shape functions for test and solution must be identical */


/*      -(A_{i,j} u_,j)_i-(B_{i} u)_i+C_{j} u_,j-D u_m  and -(X_,i)_i + Y */

/*    in a 1D domain. The shape functions for test and solution must be identical  */
/*    and row_NS == row_NN                                                         */

/*    Shape of the coefficients: */

/*      A = 1 x 1 */
/*      B = 1   */
/*      C = 1   */
/*      D = scalar  */
/*      X = 1  */
/*      Y = scalar   */


/**************************************************************/

/*  Author: gross@access.edu.au */
/*  Version: $Id:$ */

/**************************************************************/


#include "Assemble.h"
#include "Util.h"
#ifdef _OPENMP
#include <omp.h>
#endif


/**************************************************************/

void  Finley_Assemble_PDE_Single2_1D(Assemble_Parameters p, Finley_ElementFile* elements,
                                     Paso_SystemMatrix* Mat, escriptDataC* F,
                                     escriptDataC* A, escriptDataC* B, escriptDataC* C, escriptDataC* D, escriptDataC* X, escriptDataC* Y) {

    #define DIM 1
    index_t color;
    dim_t e;
    double *EM_S, *EM_F, *Vol, *DSDX, *A_p, *B_p, *C_p, *D_p, *X_p, *Y_p;
    index_t *row_index;
    register dim_t q, s,r;
    register double rtmp;
    bool_t add_EM_F, add_EM_S;

    bool_t extendedA=isExpanded(A);
    bool_t extendedB=isExpanded(B);
    bool_t extendedC=isExpanded(C);
    bool_t extendedD=isExpanded(D);
    bool_t extendedX=isExpanded(X);
    bool_t extendedY=isExpanded(Y);
    double *F_p=getSampleData(F,0);
    double *S=p.row_jac->ReferenceElement->S;
    dim_t len_EM_S=p.row_NN*p.col_NN;
    dim_t len_EM_F=p.row_NN;


    #pragma omp parallel private(color, EM_S, EM_F, Vol, DSDX, A_p, B_p, C_p, D_p, X_p, Y_p, row_index, q, s,r,rtmp,add_EM_F, add_EM_S)
    {
       EM_S=THREAD_MEMALLOC(len_EM_S,double);
       EM_F=THREAD_MEMALLOC(len_EM_F,double);
       row_index=THREAD_MEMALLOC(p.row_NN,index_t);

       if (!Finley_checkPtr(EM_S) && !Finley_checkPtr(EM_F) && !Finley_checkPtr(row_index) ) {

          #ifndef PASO_MPI
          for (color=elements->minColor;color<=elements->maxColor;color++) {
             /*  open loop over all elements: */
             #pragma omp for private(e) schedule(static)
             for(e=0;e<elements->numElements;e++){
                if (elements->Color[e]==color) {
          #else
          {  /* Open curly brace to match the one closing the color loop */
             for(e=0;e<elements->numElements;e++) {
                {
          #endif
                   Vol=&(p.row_jac->volume[INDEX2(0,e,p.numQuad)]);
                   DSDX=&(p.row_jac->DSDX[INDEX4(0,0,0,e,p.row_NN,DIM,p.numQuad)]);
                   for (q=0;q<len_EM_S;++q) EM_S[q]=0;
                   for (q=0;q<len_EM_F;++q) EM_F[q]=0;
                   add_EM_F=FALSE;
                   add_EM_S=FALSE;
                   /**************************************************************/
                   /*   process A: */
                   /**************************************************************/
                   A_p=getSampleData(A,e);
                   if (NULL!=A_p) {
                      add_EM_S=TRUE;
                      if (extendedA) {
                         for (s=0;s<p.row_NS;s++) {
                           for (r=0;r<p.col_NS;r++) {
                              rtmp=0;
                              for (q=0;q<p.numQuad;q++) {
                                 rtmp+=Vol[q]*DSDX[INDEX3(s,0,q,p.row_NN,DIM)]*A_p[INDEX3(0,0,q,DIM,DIM)]*DSDX[INDEX3(r,0,q,p.row_NN,DIM)];
                             }
                             EM_S[INDEX4(0,0,s,r,p.numEqu,p.numComp,p.row_NN)]+=rtmp;
                           }
                         }
                      } else {
                         for (s=0;s<p.row_NS;s++) {
                           for (r=0;r<p.col_NS;r++) {
                               rtmp=0;
                               for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*DSDX[INDEX3(s,0,q,p.row_NN,DIM)]*DSDX[INDEX3(r,0,q,p.row_NN,DIM)];
                               EM_S[INDEX4(0,0,s,r,p.numEqu,p.numComp,p.row_NN)]+=rtmp*A_p[INDEX2(0,0,DIM)];
                           }
                         }
                       }
                   }
                   /**************************************************************/
                   /*   process B: */
                   /**************************************************************/
                   B_p=getSampleData(B,e);
                   if (NULL!=B_p) {
                      add_EM_S=TRUE;
                      if (extendedB) {
                         for (s=0;s<p.row_NS;s++) {
                           for (r=0;r<p.col_NS;r++) {
                             rtmp=0;
                             for (q=0;q<p.numQuad;q++) {
                                rtmp+=Vol[q]*DSDX[INDEX3(s,0,q,p.row_NN,DIM)]*B_p[INDEX2(0,q,DIM)]*S[INDEX2(r,q,p.row_NS)];
                             }
                             EM_S[INDEX4(0,0,s,r,p.numEqu,p.numComp,p.row_NN)]+=rtmp;
                           }
                         }
                      } else {
                         for (s=0;s<p.row_NS;s++) {
                           for (r=0;r<p.col_NS;r++) {
                               rtmp=0;
                               for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*DSDX[INDEX3(s,0,q,p.row_NN,DIM)]*S[INDEX2(r,q,p.row_NS)];
                               EM_S[INDEX4(0,0,s,r,p.numEqu,p.numComp,p.row_NN)]+=rtmp*B_p[0];
                           }
                         }
                      }
                   }
                   /**************************************************************/
                   /*   process C: */
                   /**************************************************************/
                   C_p=getSampleData(C,e);
                   if (NULL!=C_p) {
                      add_EM_S=TRUE;
                     if (extendedC) {
                         for (s=0;s<p.row_NS;s++) {
                           for (r=0;r<p.col_NS;r++) {
                             rtmp=0;
                             for (q=0;q<p.numQuad;q++) {
                                rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)]*C_p[INDEX2(0,q,DIM)]*DSDX[INDEX3(r,0,q,p.row_NN,DIM)];
                             }
                             EM_S[INDEX4(0,0,s,r,p.numEqu,p.numComp,p.row_NN)]+=rtmp;
                           }
                         }
                     } else {
                         for (s=0;s<p.row_NS;s++) {
                           for (r=0;r<p.col_NS;r++) {
                              rtmp=0;
                              for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)]*DSDX[INDEX3(r,0,q,p.row_NN,DIM)];
                              EM_S[INDEX4(0,0,s,r,p.numEqu,p.numComp,p.row_NN)]+=rtmp*C_p[0];
                           }
                         }
                     }
                   }
                   /************************************************************* */
                   /* process D */
                   /**************************************************************/
                   D_p=getSampleData(D,e);
                   if (NULL!=D_p) {
                     add_EM_S=TRUE;
                     if (extendedD) {
                         for (s=0;s<p.row_NS;s++) {
                           for (r=0;r<p.col_NS;r++) {
                              rtmp=0;
                              for (q=0;q<p.numQuad;q++) {
                                 rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)]*D_p[q]*S[INDEX2(r,q,p.row_NS)];
                             }
                             EM_S[INDEX4(0,0,s,r,p.numEqu,p.numComp,p.row_NN)]+=rtmp;
                           }
                         }
                     } else {
                         for (s=0;s<p.row_NS;s++) {
                           for (r=0;r<p.col_NS;r++) {
                               rtmp=0;
                               for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)]*S[INDEX2(r,q,p.row_NS)];
                               EM_S[INDEX4(0,0,s,r,p.numEqu,p.numComp,p.row_NN)]+=rtmp*D_p[0];
                           }
                         }
                     }
                   }
                   /**************************************************************/
                   /*   process X: */
                   /**************************************************************/
                   X_p=getSampleData(X,e);
                   if (NULL!=X_p) {
                     add_EM_F=TRUE;
                     if (extendedX) {
                        for (s=0;s<p.row_NS;s++) {
                          rtmp=0;
                          for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*DSDX[INDEX3(s,0,q,p.row_NN,DIM)]*X_p[INDEX2(0,q,DIM)];
                          EM_F[INDEX2(0,s,p.numEqu)]+=rtmp;
                        }
                     } else {
                        for (s=0;s<p.row_NS;s++) {
                          rtmp=0;
                          for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*DSDX[INDEX3(s,0,q,p.row_NN,DIM)];
                          EM_F[INDEX2(0,s,p.numEqu)]+=rtmp*X_p[0];
                        }
                     }
                  }
                  /**************************************************************/
                  /*   process Y: */
                  /**************************************************************/
                   Y_p=getSampleData(Y,e);
                   if (NULL!=Y_p) {
                     add_EM_F=TRUE;
                     if (extendedY) {
                        for (s=0;s<p.row_NS;s++) {
                           rtmp=0;
                           for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)]*Y_p[q];
                           EM_F[INDEX2(0,s,p.numEqu)]+=rtmp;
                        }
                      } else {
                        for (s=0;s<p.row_NS;s++) {
                            rtmp=0;
                            for (q=0;q<p.numQuad;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_NS)];
                            EM_F[INDEX2(0,s,p.numEqu)]+=rtmp*Y_p[0];
                        }
                      }
                    }
                    /***********************************************************************************************/
                    /* add the element matrices onto the matrix and right hand side                                */
                    /***********************************************************************************************/
                    for (q=0;q<p.row_NN;q++) row_index[q]=p.row_DOF[elements->Nodes[INDEX2(p.row_node[q],e,p.NN)]];
                    if (add_EM_F) Finley_Util_AddScatter(p.row_NN,row_index,p.numEqu,EM_F,F_p, p.row_DOF_UpperBound);
                    if (add_EM_S) Finley_Assemble_addToSystemMatrix(Mat,p.row_NN,row_index,p.numEqu,p.col_NN,row_index,p.numComp,EM_S);
   
                } /* end color check */
             } /* end element loop */
         } /* end color loop */
           
         THREAD_MEMFREE(EM_S);
         THREAD_MEMFREE(EM_F);
         THREAD_MEMFREE(row_index);

      } /* end of pointer check */
   } /* end parallel region */
}
/*
 * $Log$
 */