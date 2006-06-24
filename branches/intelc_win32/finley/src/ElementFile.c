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

/*   Finley: ElementFile */

/*   allocates an element file to hold elements of type id and with integration order order. */
/*   use Finley_Mesh_allocElementTable to allocate the element table (Id,Nodes,Tag). */

/**************************************************************/

/*   Author: gross@access.edu.au */
/*   Version: $Id$ */

/**************************************************************/

#include "ElementFile.h"

/**************************************************************/

#ifndef PASO_MPI
Finley_ElementFile* Finley_ElementFile_alloc(ElementTypeId id,index_t order)
#else
Finley_ElementFile* Finley_ElementFile_alloc(ElementTypeId id,index_t order, Paso_MPIInfo *MPIInfo)
#endif
{
  extern Finley_RefElementInfo Finley_RefElement_InfoList[];
  dim_t NQ;
  Finley_ElementFile *out;
  
  /*   get the number of quadrature nodes needed to achieve integration order order: */
  
  if (order<0) order=2*Finley_RefElement_InfoList[id].numOrder;
  NQ= Finley_RefElement_InfoList[id].getNumQuadNodes(order);
  if (! Finley_noError()) return NULL;
  
  /*  allocate the return value */
  
  out=MEMALLOC(1,Finley_ElementFile);
  if (Finley_checkPtr(out)) return NULL;
  out->ReferenceElement=NULL;
  out->LinearReferenceElement=NULL;
  out->numElements=0;
  out->Id=NULL;
  out->Nodes=NULL;
  out->Tag=NULL;
  out->Color=NULL;
  out->minColor=0;
  out->maxColor=-1;
  out->order = order;
  out->volume_is_valid=FALSE;  
  out->volume=NULL;          
  out->DvDV=NULL;             
  out->DSDV_is_valid=FALSE;
  out->DSDV=NULL;             
  out->DSLinearDV_is_valid=FALSE; 
  out->DSLinearDV=NULL;         
  out->X_is_valid=FALSE;        
  out->X=NULL;                

#ifdef PASO_MPI
  out->MPIInfo = Paso_MPIInfo_getReference( MPIInfo );
  out->elementDistribution = Finley_ElementDistribution_alloc( MPIInfo );
#endif

  /*  allocate the reference element: */
  
  out->ReferenceElement=Finley_RefElement_alloc(id,NQ);
  if (! Finley_noError()) {
     Finley_ElementFile_dealloc(out);
     return NULL;
  }
  out->LinearReferenceElement=Finley_RefElement_alloc(Finley_RefElement_InfoList[id].LinearTypeId,NQ);
  if (! Finley_noError()) {
     Finley_ElementFile_dealloc(out);
     return NULL;
  }
  return out;
}

/*  deallocates an element file: */

void Finley_ElementFile_dealloc(Finley_ElementFile* in) {
  if (in!=NULL) {
     #ifdef Finley_TRACE
     if (in->ReferenceElement!=NULL) printf("element file for %s is deallocated.\n",in->ReferenceElement->Type->Name);
     #endif
     Finley_RefElement_dealloc(in->ReferenceElement);
     Finley_RefElement_dealloc(in->LinearReferenceElement);
     Finley_ElementFile_deallocTable(in);   
     MEMFREE(in->volume);          
     MEMFREE(in->DvDV);             
     MEMFREE(in->DSDV);             
     MEMFREE(in->DSLinearDV);         
     MEMFREE(in->X);     
#ifdef PASO_MPI
     Paso_MPIInfo_dealloc( in->MPIInfo );
     Finley_ElementDistribution_dealloc( in->elementDistribution );
#endif           
     MEMFREE(in);      
  }
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
* Revision 1.1.1.1.2.2  2005/06/29 02:34:49  gross
* some changes towards 64 integers in finley
*
* Revision 1.1.1.1.2.1  2004/11/24 01:37:13  gross
* some changes dealing with the integer overflow in memory allocation. Finley solves 4M unknowns now
*
*
*
*/
