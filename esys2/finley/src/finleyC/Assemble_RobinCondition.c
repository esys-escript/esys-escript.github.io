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

/*    assembles a system of numEq natural boundary condition into the stiffness matrix S and right hand side F: */

/*     d*u = y */

/*    u has numComp components. */

/*    Shape of the coefficients: */

/*      d = numEqu x numComp  */
/*      y = numEqu */

/*    The coefficients d and y have to be defined on the integartion points on face elements or not present (=NULL). */

/*    S and F have to be initialized before the routine is called. S or F can be NULL. In this case the left or */
/*    the right hand side of the natural boundary conditions is not processed. */


/**************************************************************/

/*   author: gross@access.edu.au */
/*   Version: $Id$ */

/**************************************************************/

#include "Assemble.h"
#include "Util.h"
#ifdef _OPENMP
#include <omp.h>
#endif

/**************************************************************/

void Finley_Assemble_RobinCondition(Finley_NodeFile* nodes,Finley_ElementFile* elements,Paso_SystemMatrix* S, escriptDataC* F, escriptDataC* d, escriptDataC* y, Finley_Assemble_handelShapeMissMatch handelShapeMissMatchForEM) {
  char error_msg[LenErrorMsg_MAX];
  double *EM_S=NULL,*EM_F=NULL,*V=NULL,*dVdv=NULL,*dSdV=NULL,*Area=NULL;
  double time0;
  Assemble_Parameters p;
  index_t *index_row=NULL,*index_col=NULL,color;
  dim_t dimensions[ESCRIPT_MAX_DATA_RANK],e,q;
  Finley_resetError();

  if (nodes==NULL || elements==NULL) return;
  if (S==NULL && isEmpty(F)) return;

  /* set all parameters in p*/
  Assemble_getAssembleParameters(nodes,elements,S,F,&p);
  if (! Finley_noError()) return;

  /*  get a functionspace */
  type_t funcspace=UNKNOWN;
  updateFunctionSpaceType(funcspace,d);
  updateFunctionSpaceType(funcspace,y);
  if (funcspace==UNKNOWN) return; /* all  data are empty */

  /* check if all function spaces are the same */

  if (! functionSpaceTypeEqual(funcspace,d) ) {
        Finley_setError(TYPE_ERROR,"__FILE__: unexpected function space type for coefficient d");
  }
  if (! functionSpaceTypeEqual(funcspace,y) ) {
        Finley_setError(TYPE_ERROR,"__FILE__: unexpected function space type for coefficient y");
  }

  /* check if all function spaces are the same */

  if (! numSamplesEqual(d,p.numQuad,elements->numElements) ) {
        sprintf(error_msg,"__FILE__: sample points of coefficient d don't match (%d,%d)",p.numQuad,elements->numElements);
        Finley_setError(TYPE_ERROR,error_msg);
  }

  if (! numSamplesEqual(y,p.numQuad,elements->numElements) ) {
        sprintf(error_msg,"__FILE__: sample points of coefficient y don't match (%d,%d)",p.numQuad,elements->numElements);
        Finley_setError(TYPE_ERROR,error_msg);
  }

  
  /*  check coefficient */
  
  if (p.numEqu==1 && p.numComp==1) {
    if (!isEmpty(d)) {
      if (! isDataPointShapeEqual(d,0,dimensions)) {
          Finley_setError(TYPE_ERROR,"__FILE__: coefficient d, rank 0 expected.");
      }
    }
    if (!isEmpty(y)) {
      if (! isDataPointShapeEqual(y,0,dimensions)) {
          Finley_setError(TYPE_ERROR,"__FILE__: coefficient y, rank 0 expected.");
      }
    }
  } else {
    if (!isEmpty(d)) {
      dimensions[0]=p.numEqu;
      dimensions[1]=p.numComp;
      if (! isDataPointShapeEqual(d,2,dimensions)) {
          sprintf(error_msg,"__FILE__: coefficient d, expected shape (%d,%d)",dimensions[0],dimensions[1]);
          Finley_setError(TYPE_ERROR,error_msg);
      }
    }
    if (!isEmpty(y)) {
      dimensions[0]=p.numEqu;
      if (! isDataPointShapeEqual(y,1,dimensions)) {
          sprintf(error_msg,"__FILE__: coefficient y, expected shape (%d,)",dimensions[0]);
          Finley_setError(TYPE_ERROR,error_msg);
      }
    }
  }
  
  if (Finley_noError()) {
     time0=Finley_timer();
     #pragma omp parallel private(index_row,index_col,EM_S,EM_F,V,dVdv,dSdV,Area,color)
     {
        EM_S=EM_F=V=dVdv=dSdV=Area=NULL;
        index_row=index_col=NULL;
        /* allocate work arrays: */
        EM_S=THREAD_MEMALLOC(p.NN_col*p.NN_row*p.numEqu*p.numComp,double);
        EM_F=THREAD_MEMALLOC(p.NN_row*p.numEqu,double);
        V=THREAD_MEMALLOC(p.NN*p.numDim,double);
        dVdv=THREAD_MEMALLOC(p.numDim*p.numElementDim*p.numQuad,double);
        Area=THREAD_MEMALLOC(p.numQuad,double);
        index_row=THREAD_MEMALLOC(p.NN_row,index_t);
        index_col=THREAD_MEMALLOC(p.NN_col,index_t);
        if (! ( Finley_checkPtr(EM_S) || Finley_checkPtr(EM_F) || Finley_checkPtr(index_row) || Finley_checkPtr(index_col) || 
                Finley_checkPtr(V) || Finley_checkPtr(dVdv) || Finley_checkPtr(Area))) {
           /*  open loop over all colors: */
           for (color=elements->minColor;color<=elements->maxColor;color++) {
              /*  open loop over all elements: */
              #pragma omp for private(e,q) schedule(static)
              for(e=0;e<elements->numElements;e++){
                if (elements->Color[e]==color) {
                   for (q=0;q<p.NN_row;q++) index_row[q]=p.label_row[elements->Nodes[INDEX2(p.row_node[q],e,p.NN)]];
                   /* gather V-coordinates of nodes into V: */
                   Finley_Util_Gather_double(p.NN,&(elements->Nodes[INDEX2(0,e,p.NN)]),p.numDim,nodes->Coordinates,V);
                   /* handel the case where NS!=p.NN (contact elements) */
                   Finley_Assemble_handelShapeMissMatch_Mean_in(p.numDim,p.NN,1,V,p.NS,1);
                   /*  calculate dVdv(i,j,q)=V(i,k)*DSDv(k,j,q) */
                   Finley_Util_SmallMatMult(p.numDim,p.numElementDim*p.numQuad,dVdv,p.NS,V,p.referenceElement->dSdv);
                   /*  */
                   Finley_LengthOfNormalVector(p.numQuad,p.numDim,p.numElementDim,dVdv,Area);
                   /*  scale area: */
                   for (q=0;q<p.numQuad;q++) Area[q]=ABS(Area[q]*p.referenceElement->QuadWeights[q]);
                   /*   integration for the stiffness matrix: */
                   /*   in order to optimze the number of operations the case of constants coefficience needs a bit more work */
                   /*   to make use of some symmetry. */
                   if (S!=NULL) {
                       for (q=0;q<p.NN_col*p.NN_row*p.numEqu*p.numComp;q++) EM_S[q]=0;
                       if (p.numEqu==1 && p.numComp==1) {
                           Finley_Assemble_PDEMatrix_Single2(p.NS_row,p.numElementDim,p.numQuad,
                                                                     p.referenceElement_row->S,dSdV,Area,p.NN_row,EM_S,
                                                                     NULL,TRUE,
                                                                     NULL,TRUE,
                                                                     NULL,TRUE,
                                                                     getSampleData(d,e),isExpanded(d));
                       } else {
                           Finley_Assemble_PDEMatrix_System2(p.NS_row,p.numElementDim,p.numQuad,
                                                                     p.numEqu,p.numComp,p.referenceElement_row->S,dSdV,Area,p.NN_row,EM_S,
                                                                     NULL,TRUE,
                                                                     NULL,TRUE,
                                                                     NULL,TRUE,
                                                                     getSampleData(d,e),isExpanded(d));
                       }
                       /* handel the case of p.NS<NN */
                       handelShapeMissMatchForEM(p.numEqu*p.numComp,p.NN_row,p.NN_col,EM_S,p.NS_row,p.NS_col);
                  /*
                       {int g;
	               for(g=0;g<p.NN*p.NN*p.numEqu*p.numComp;g++) printf("%f ",EM_S[g]);
	               printf("\n");
                       }
                     */
                       /* add  */
                       for (q=0;q<p.NN_col;q++) index_col[q]=p.label_col[elements->Nodes[INDEX2(p.col_node[q],e,p.NN)]];
                       Finley_Assemble_addToSystemMatrix(S,p.NN_row,index_row,p.numEqu,p.NN_col,index_col,p.numComp,EM_S);
                   }
                   if (!isEmpty(F)) {
                     for (q=0;q<p.NN_row*p.numEqu;q++) EM_F[q]=0;
                     if (p.numEqu==1) {
	                Finley_Assemble_RHSMatrix_Single(p.NS_row,p.numElementDim,p.numQuad,
                                                              p.referenceElement_row->S,dSdV,Area,p.NN_row,EM_F,
                                                              NULL,TRUE,
                                                              getSampleData(y,e),isExpanded(y));
                     } else {
	                Finley_Assemble_RHSMatrix_System(p.NS_row,p.numElementDim,p.numQuad,
                                                              p.numEqu,p.referenceElement_row->S,dSdV,Area,p.NN_row,EM_F,
                                                              NULL,TRUE,
                                                              getSampleData(y,e),isExpanded(y));
                     }
                     /* handel the case of NS<NN */
                     handelShapeMissMatchForEM(p.numEqu,p.NN_row,1,EM_F,p.NS_row,1);
                     /*
                       {int g;
	               for(g=0;g<p.NN*p.numEqu;g++) printf("%f ",EM_F[g]);
	               printf("\n");
                       }
                     */
                     /* add  */
                     Finley_Util_AddScatter(p.NN_row,index_row,p.numEqu,EM_F,getSampleData(F,0));
                   }
                 }
              } /*  end of element loop: */
           } /*  end of color loop: */
        }
        THREAD_MEMFREE(EM_S);
        THREAD_MEMFREE(EM_F);
        THREAD_MEMFREE(V);
        THREAD_MEMFREE(dVdv);
        THREAD_MEMFREE(dSdV);
        THREAD_MEMFREE(Area);
        THREAD_MEMFREE(index_row);
        THREAD_MEMFREE(index_col);
     }
     #ifdef Finley_TRACE
     printf("timing: assemblage natural BC: %.4e sec\n",Finley_timer()-time0);
     #endif
  }
}
/*
 * $Log$
 * Revision 1.8  2005/09/15 03:44:21  jgs
 * Merge of development branch dev-02 back to main trunk on 2005-09-15
 *
 * Revision 1.7  2005/09/01 03:31:35  jgs
 * Merge of development branch dev-02 back to main trunk on 2005-09-01
 *
 * Revision 1.6  2005/08/12 01:45:43  jgs
 * erge of development branch dev-02 back to main trunk on 2005-08-12
 *
 * Revision 1.5.2.4  2005/09/07 06:26:17  gross
 * the solver from finley are put into the standalone package paso now
 *
 * Revision 1.5.2.3  2005/08/24 02:02:18  gross
 * timing output switched off. solver output can be swiched through getSolution(verbose=True) now.
 *
 * Revision 1.5.2.2  2005/08/04 22:41:11  gross
 * some extra routines for finley that might speed-up RHS assembling in some cases (not actived right now)
 *
 * Revision 1.5.2.1  2005/08/03 08:55:46  gross
 * typo fixed
 *
 * Revision 1.5  2005/07/08 04:07:46  jgs
 * Merge of development branch back to main trunk on 2005-07-08
 *
 * Revision 1.4  2004/12/15 07:08:32  jgs
 * *** empty log message ***
 * Revision 1.1.1.1.2.2  2005/06/29 02:34:47  gross
 * some changes towards 64 integers in finley
 *
 * Revision 1.1.1.1.2.1  2004/11/24 01:37:12  gross
 * some changes dealing with the integer overflow in memory allocation. Finley solves 4M unknowns now
 *
 *
 *
 */
