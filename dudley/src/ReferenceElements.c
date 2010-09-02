
/*******************************************************
*
* Copyright (c) 2003-2010 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


/**************************************************************/

/*   Dudley: Reference elements */

/**************************************************************/

#include "ReferenceElements.h"

/**************************************************************

    this list has been generated by generateReferenceElementList.py:.
*/
Dudley_ReferenceElementInfo Dudley_ReferenceElement_InfoList[]={
{ Point1, "Point1", 1,  { 0, 1 }, Point1,
    { 0 }, PointQuad, Point1Shape, Point1Shape,
    { 0 },
  1, { 0 },
  1, { 0 },
    { 0 },
    { -1 } },
{ Line2, "Line2", 2,  { 0, 2 }, Line2,
    { 0, 1 }, LineQuad, Line2Shape, Line2Shape,
    { 0, 1 },
  2, { 0, 1 },
  2, { 0, 1 },
    { 1, 0 },
    { -1 } },
{ Tri3, "Tri3", 3,  { 0, 3 }, Tri3,
    { 0, 1, 2 }, TriQuad, Tri3Shape, Tri3Shape,
    { 0, 1, 2 },
  3, { 0, 1, 2 },
  3, { 0, 1, 2 },
    { 1, 2, 0 },
    { 0, 2, 1 } },
{ Tet4, "Tet4", 4, { 0, 4 }, Tet4,
    { 0, 1, 2, 3 }, TetQuad, Tet4Shape, Tet4Shape,
    { 0, 1, 2, 3 },
  4, { 0, 1, 2, 3 },
  4, { 0, 1, 2, 3 },
    { -1 },
    { -1 } },
{ Line2Face, "Line2Face", 2, { 0, 2 }, Line2Face,
    { 0, 1 }, PointQuad, Line2Shape, Line2Shape,
    { 0, 1 },
  1, { 0 },
  1, { 0 },
    { 0, 1, 2 },
    { -1 } },
{ Tri3Face, "Tri3Face", 3, { 0, 3 }, Tri3Face,
    { 0, 1, 2 }, LineQuad, Tri3Shape, Tri3Shape,
    { 0, 1, 2 },
  2, { 0, 1 },
  2, { 0, 1 },
    { 1, 0, 2 },
    { -1 } },
{ Tet4Face, "Tet4Face", 4, { 0, 4 }, Tet4Face,
    { 0, 1, 2, 3 }, TriQuad, Tet4Shape, Tet4Shape,
    { 0, 1, 2, 3 },
  3, { 0, 1, 2 },
  4, { 0, 1, 2, 3 },
    { 1, 2, 0, 3 },
    { 0, 2, 1, 3 } },
{ NoRef, "noElement", 0, { 0 }, NoRef,
    { 0 }, NoQuad, NoShape, NoShape,
    { 0 },
  -1, { 0 },
  -1, { 0 },
    { 0 },
    { 0 } }

};

/**************************************************************
  
  creates a ReferenceElement of type id and a given integration order 

  */


Dudley_ReferenceElement* Dudley_ReferenceElement_alloc(ElementTypeId id, int order) 
{
	dim_t numQuadNodes;
	double *quadWeights=NULL, *quadNodes=NULL;
	Dudley_ReferenceElement *out=NULL;
	Dudley_QuadInfo* quadscheme;
	Dudley_ShapeFunctionInfo* parametrization, *basisfunction, *linearbasisfunction;
	Dudley_ReferenceElementInfo *type, *linear_type;

        type=Dudley_ReferenceElement_getInfo(id);
        if (type == NULL)
	{ 
             Dudley_setError(VALUE_ERROR,"Dudley_ReferenceElement_alloc: unable to identify element type.");
            return NULL;
        }
        linear_type=Dudley_ReferenceElement_getInfo(type->LinearTypeId);
        if (linear_type == NULL)
	{
            Dudley_setError(VALUE_ERROR,"Dudley_ReferenceElement_alloc: unable to identify linear element type.");
            return NULL;
        }
	out=MEMALLOC(1,Dudley_ReferenceElement);
	if (Dudley_checkPtr(out)) return NULL;
	out->reference_counter=0;
	out->Parametrization=NULL;
	out->BasisFunctions=NULL;
	out->LinearBasisFunctions=NULL;
	out->Type=type;
	out->numNodes=out->Type->numNodes;
	out->LinearType=linear_type;
	out->numLinearNodes=out->LinearType->numNodes;
        out->integrationOrder=-1;
        out->DBasisFunctionDv=NULL;
        out->DBasisFunctionDvShared=TRUE;

	quadscheme=Dudley_QuadInfo_getInfo(out->Type->Quadrature);
	parametrization=Dudley_ShapeFunction_getInfo(out->Type->Parametrization);
	basisfunction=Dudley_ShapeFunction_getInfo(out->Type->BasisFunctions);
	linearbasisfunction=Dudley_ShapeFunction_getInfo(Dudley_ReferenceElement_InfoList[out->Type->LinearTypeId].BasisFunctions);
        out->numLocalDim=quadscheme->numDim;
	
	/*  set up the basic integration scheme 
	    note that quadscheme->numDim is not necessarily the diemnsion of the element 
	*/
	
	if (order<0) order=MAX(2*basisfunction->numOrder,0);
        out->integrationOrder=order;
	numQuadNodes=quadscheme->getNumQuadNodes(order);
	
	quadNodes=MEMALLOC(numQuadNodes*quadscheme->numDim,double);
	quadWeights=MEMALLOC(numQuadNodes,double);	
	if ( !( Dudley_checkPtr(quadNodes) || Dudley_checkPtr(quadWeights) ) )
	{
		quadscheme->getQuadNodes(numQuadNodes, quadNodes, quadWeights);
	
		/*  set the basis functions on the quadrature points:
		 *  note: Dudley_ShapeFunction_alloc will introduce 0. if the dimensions of the quadrature scheme 
		 * and the dimension of the element don;t match.
		 */
		/*
	         * before we can set the shape function for the parametrization the quadrature scheme needs to be replicated :
		 */
	
		out->Parametrization=Dudley_ShapeFunction_alloc(parametrization->TypeId, quadscheme->numDim, numQuadNodes, quadNodes, quadWeights);
		out->BasisFunctions=Dudley_ShapeFunction_alloc(basisfunction->TypeId, quadscheme->numDim, numQuadNodes, quadNodes, quadWeights);
		out->LinearBasisFunctions=Dudley_ShapeFunction_alloc(linearbasisfunction->TypeId, quadscheme->numDim, numQuadNodes, quadNodes, quadWeights);
		out->DBasisFunctionDv=out->BasisFunctions->dSdv;
		out->DBasisFunctionDvShared=TRUE;
	}
	MEMFREE(quadNodes);
	MEMFREE(quadWeights);
	if (Dudley_noError())
	{
		return Dudley_ReferenceElement_reference(out);
	} else	
	{
		Dudley_ReferenceElement_dealloc(out);
		return NULL;
	} 
}

/**************************************************************/

void Dudley_ReferenceElement_dealloc(Dudley_ReferenceElement* in) {
	if (in!=NULL) {
		in->reference_counter--;
		if (in->reference_counter<1) {
			Dudley_ShapeFunction_dealloc(in->Parametrization);
			Dudley_ShapeFunction_dealloc(in->BasisFunctions);
			Dudley_ShapeFunction_dealloc(in->LinearBasisFunctions);
                        if (! in->DBasisFunctionDvShared) MEMFREE(in->DBasisFunctionDv);
			MEMFREE(in);
		}
	}

}

/**************************************************************/

ElementTypeId Dudley_ReferenceElement_getTypeId(char* element_type) {
    int ptr=0;
    ElementTypeId out=NoRef;
    while (Dudley_ReferenceElement_InfoList[ptr].TypeId!=NoRef && out==NoRef) {
       if (strcmp(element_type,Dudley_ReferenceElement_InfoList[ptr].Name)==0) out=Dudley_ReferenceElement_InfoList[ptr].TypeId;
       ptr++;
    }
    return out;
}

Dudley_ReferenceElement* Dudley_ReferenceElement_reference(Dudley_ReferenceElement* in) {
     if (in!=NULL) ++(in->reference_counter);
     return in;
}

Dudley_ReferenceElementInfo* Dudley_ReferenceElement_getInfo(ElementTypeId id)
{
    int ptr=0;
    Dudley_ReferenceElementInfo* out=NULL;
    while (Dudley_ReferenceElement_InfoList[ptr].TypeId!=NoRef && out==NULL) {
       if (Dudley_ReferenceElement_InfoList[ptr].TypeId==id) out=&(Dudley_ReferenceElement_InfoList[ptr]);
       ptr++;
    }
    if (out==NULL) {
        Dudley_setError(VALUE_ERROR,"Dudley_ReferenceElement_getInfo: cannot find requested reference element.");
    }
    return out;
}


