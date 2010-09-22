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

#include "ShapeTable.h"
#include <stdlib.h>

// Joel Fenwick - derived from info in Finley's Quadrature and shape files

// This method is not threadsafe unless the initial call has completed
// Evaluates the shape functions at nodes (This is the S value from the finley ShapeFunctions
// The dim argument is the dimension of the element not the dimension of the embedding space.
// the reduced arg is whether the elements are reduced or not
bool_t getQuadShape(dim_t dim, bool_t reduced, const double** shapearr)
{
#define _dudley_s_alpha 0.58541019662496852
#define _dudley_s_beta  0.1381966011250105


// {Line, TRI, TET} X {single_quad_point, more} X max number of quadpoints
static const double _dudley_V[3*2][12] = {
{0.5,0,0,0,0,0,0,0,0,0,0,0},	// Line single
{(1.-.577350269189626)/2.,(1.+.577350269189626)/2.,0,0,0,0,0,0,0,0,0,0},	// Line 2 points
{1/3.,1/3.,0,0,0,0,0,0,0,0,0,0},	// Tri single
{0.5,0,0,0.5,0.5,0.5,0,0,0,0,0,0},		// Tri 3 points
{0.25,0.25,0.25,0,0,0,0,0,0,0,0,0},			// Tet single
{_dudley_s_beta, _dudley_s_beta, _dudley_s_beta, 
_dudley_s_alpha, _dudley_s_beta, _dudley_s_beta,
_dudley_s_beta, _dudley_s_alpha, _dudley_s_beta,
_dudley_s_beta, _dudley_s_beta, _dudley_s_alpha
}					// Tet 4 points			
};

#undef _dudley_s_alpha
#undef _dudley_s_beta

static double** arr=0;

if (arr==0)
{
arr=malloc(8*sizeof(double*));		// point occupies two slots to make things simpler
arr[0]=malloc(1*sizeof(double));
arr[0][0]=1.;				// point
arr[1]=arr[0];
arr[2]=malloc(4*sizeof(double));	// Line Single
arr[3]=malloc(4*sizeof(double));	// Line 2
arr[4]=malloc(4*sizeof(double));	// Tri single

for (int i=0;i<2;++i)	
{
arr[2][2*i]=1-_dudley_V[0][i];
arr[3][2*i]=1-_dudley_V[1][i];
arr[4][2*i]=1-_dudley_V[2][i];

arr[2][2*i+1]=_dudley_V[0][i];
arr[3][2*i+1]=_dudley_V[1][i];
arr[4][2*i+1]=_dudley_V[2][i];
}

arr[5]=malloc(9*sizeof(double));		// Tri 3
for (int i=0;i<3;++i)
{
arr[5][3*i]=1-_dudley_V[3][3*i] -_dudley_V[2][3*i+1];
arr[5][3*i+1]=_dudley_V[3][3*i];
arr[5][3*i+2]=_dudley_V[3][3*i+1];
}
arr[6]=malloc(3*sizeof(double));	// Tet single
arr[6][0]=1-_dudley_V[4][0] -_dudley_V[2][1] -_dudley_V[2][2];
arr[6][1]=_dudley_V[4][0];
arr[6][2]= _dudley_V[4][1];
arr[6][3]=_dudley_V[4][2];

arr[7]=malloc(16*sizeof(double));
for (int i=0;i<4;++i)
{
  double x=_dudley_V[5][0];
  double y=_dudley_V[5][1];
  double z=_dudley_V[5][2];
  arr[7][4*i]=1-x-y-z;
  arr[7][4*i+1]=x;
  arr[7][4*i+2]=y;
  arr[7][4*i+3]=z;
}
}	// end if 

    if ((dim>-1) && (dim<4))
    {
        *shapearr=arr[(!reduced)?(2*dim+1):(2*dim)];
	return 1;
    }
    *shapearr=0;
    return 0;
}