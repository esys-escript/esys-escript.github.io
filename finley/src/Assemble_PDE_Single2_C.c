
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

/*    assembles a single PDEs into the stiffness matrix S right hand side F  */

/*      D u_m  and Y */

/*    in a 3D domain. The shape functions for test and solution must be identical  */
/*    and 2* row_NS == row_NN (contact elements)                                   */

/*    Shape of the coefficients: */

/*      D = scalar    */
/*      Y = scalar    */


/**************************************************************/


#include "Assemble.h"
#include "Util.h"
#ifdef _OPENMP
#include <omp.h>
#endif


/**************************************************************/

void  Finley_Assemble_PDE_Single2_C(Assemble_Parameters p, Finley_ElementFile* elements,
                                    Paso_SystemMatrix* Mat, escriptDataC* F, escriptDataC* D, escriptDataC* Y) {

    index_t color;
    dim_t e, isub;
    __const double *D_p, *Y_p, *D_q, *Y_q;
    double *EM_S, *EM_F, *Vol;
    index_t *row_index;
    register dim_t q, s,r;
    register double rtmp, rtmp_D;
    bool_t add_EM_F, add_EM_S;

    bool_t extendedD=isExpanded(D);
    bool_t extendedY=isExpanded(Y);
    double *F_p=(requireWrite(F), getSampleDataRW(F,0));	/* use comma, to get around the mixed code and declarations thing */
    double *S=p.row_jac->BasisFunctions->S;

    #pragma omp parallel private(color,EM_S, EM_F, Vol, D_p, Y_p, D_q, Y_q,row_index,q, s,r,rtmp, rtmp_D,add_EM_F, add_EM_S, isub)
    {
       EM_S=THREAD_MEMALLOC(p.row_numShapesTotal*p.col_numShapesTotal,double);
       EM_F=THREAD_MEMALLOC(p.row_numShapesTotal,double);
       row_index=THREAD_MEMALLOC(p.row_numShapesTotal,index_t);
                                                                                                                                                                                                     
       if (!Finley_checkPtr(EM_S) && !Finley_checkPtr(EM_F) && !Finley_checkPtr(row_index) ) {

          for (color=elements->minColor;color<=elements->maxColor;color++) {
             /*  open loop over all elements: */
             #pragma omp for private(e) schedule(static)
             for(e=0;e<elements->numElements;e++){
                if (elements->Color[e]==color) {
			
				 D_p=getSampleDataRO(D,e);
				 Y_p=getSampleDataRO(Y,e);
                   
				 for (isub=0; isub<p.numSub; isub++) {
                      
			   		 Vol=&(p.row_jac->volume[INDEX3(0,isub,e, p.numQuadSub,p.numSub)]);
                      add_EM_F=FALSE;
                      add_EM_S=FALSE;
		      
                      /************************************************************* */
                      /* process D */
                      /**************************************************************/

                      if (NULL!=D_p) {
                        add_EM_S=TRUE;
                        if (extendedD) {
							D_q=&(D_p[INDEX2(0,isub, p.numQuadSub)]);
                            for (s=0;s<p.row_numShapes;s++) {
                              for (r=0;r<p.col_numShapes;r++) {
                                 rtmp=0;
                                 for (q=0;q<p.numQuadSub;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_numShapes)]*D_q[q]*S[INDEX2(r,q,p.row_numShapes)];
                                 EM_S[INDEX4(0,0,s         ,r         ,p.numEqu,p.numComp,p.row_numShapesTotal)]= rtmp;
                                 EM_S[INDEX4(0,0,s         ,r+p.col_numShapes,p.numEqu,p.numComp,p.row_numShapesTotal)]=-rtmp;
                                 EM_S[INDEX4(0,0,s+p.row_numShapes,r         ,p.numEqu,p.numComp,p.row_numShapesTotal)]=-rtmp;
                                 EM_S[INDEX4(0,0,s+p.row_numShapes,r+p.col_numShapes,p.numEqu,p.numComp,p.row_numShapesTotal)]= rtmp;
                              }
                            }
                        } else {
                            for (s=0;s<p.row_numShapes;s++) {
                              for (r=0;r<p.col_numShapes;r++) {
                                  rtmp=0;
                                  for (q=0;q<p.numQuadSub;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_numShapes)]*S[INDEX2(r,q,p.row_numShapes)];
                                  rtmp_D=rtmp*D_p[0];
                                  EM_S[INDEX4(0,0,s         ,r         ,p.numEqu,p.numComp,p.row_numShapesTotal)]= rtmp_D;
                                  EM_S[INDEX4(0,0,s         ,r+p.col_numShapes,p.numEqu,p.numComp,p.row_numShapesTotal)]=-rtmp_D;
                                  EM_S[INDEX4(0,0,s+p.row_numShapes,r         ,p.numEqu,p.numComp,p.row_numShapesTotal)]=-rtmp_D;
                                  EM_S[INDEX4(0,0,s+p.row_numShapes,r+p.col_numShapes,p.numEqu,p.numComp,p.row_numShapesTotal)]= rtmp_D;
                              }
                            }
                        }
                      }
                     /**************************************************************/
                     /*   process Y: */
                     /**************************************************************/

                      if (NULL!=Y_p) {
                        add_EM_F=TRUE;
                        if (extendedY) {
							Y_q=&(Y_p[INDEX2(0,isub, p.numQuadSub)]);
                           for (s=0;s<p.row_numShapes;s++) {
                             rtmp=0;
                             for (q=0;q<p.numQuadSub;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_numShapes)]*Y_q[q];
                             EM_F[INDEX2(0,s         ,p.numEqu)]=-rtmp;
                             EM_F[INDEX2(0,s+p.row_numShapes,p.numEqu)]= rtmp;
                           }
                         } else {
                           for (s=0;s<p.row_numShapes;s++) {
                               rtmp=0;
                               for (q=0;q<p.numQuadSub;q++) rtmp+=Vol[q]*S[INDEX2(s,q,p.row_numShapes)];
                               rtmp_D=rtmp*Y_p[0];
                               EM_F[INDEX2(0,s         ,p.numEqu)]=-rtmp_D;
                               EM_F[INDEX2(0,s+p.row_numShapes,p.numEqu)]= rtmp_D;
                           }
                         }
                       }
                       /***********************************************************************************************/
                       /* add the element matrices onto the matrix and right hand side                                */
                       /***********************************************************************************************/
                       for (q=0;q<p.row_numShapesTotal;q++) row_index[q]=p.row_DOF[elements->Nodes[INDEX2(p.row_node[INDEX2(q,isub,p.row_numShapesTotal)],e,p.NN)]];
      
                       if (add_EM_F) Finley_Util_AddScatter(p.row_numShapesTotal,row_index,p.numEqu,EM_F,F_p, p.row_DOF_UpperBound);
                       if (add_EM_S) Finley_Assemble_addToSystemMatrix(Mat,p.row_numShapesTotal,row_index,p.numEqu,p.col_numShapesTotal,row_index,p.numComp,EM_S);

                   } /* end of isub */
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
