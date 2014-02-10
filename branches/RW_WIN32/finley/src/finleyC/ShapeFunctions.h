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

/*   Finley: Shape functions header file */

/**************************************************************/

/*   Author: gross@access.edu.au */
/*   Version: $Id$ */

/**************************************************************/

#ifndef INC_FINLEY_SHAPEFUNCTIONS
#define INC_FINLEY_SHAPEFUNCTIONS

/**************************************************************/

#include "Finley.h"
#ifdef __cplusplus
extern "C" {
#endif

/**************************************************************/

#define S_INDEX(_J_,_I_,_NUMNODES_)                INDEX2(_J_,_I_,_NUMNODES_)
#define DSDV_INDEX(_J_,_K_,_I_,_NUMNODES_,_DIM_)   INDEX3(_J_,_K_,_I_,_NUMNODES_,_DIM_)

/**************************************************************/
/*   Interfaces: */

typedef void (Finley_Shape_Function) (dim_t,double*,double*,double*);

Finley_Shape_Function Finley_Shape_Point1;
Finley_Shape_Function Finley_Shape_Line2;
Finley_Shape_Function Finley_Shape_Line3;
Finley_Shape_Function Finley_Shape_Line4;
Finley_Shape_Function Finley_Shape_Tri3;
Finley_Shape_Function Finley_Shape_Tri6;
Finley_Shape_Function Finley_Shape_Tri9;
Finley_Shape_Function Finley_Shape_Tri10;
Finley_Shape_Function Finley_Shape_Rec4;
Finley_Shape_Function Finley_Shape_Rec8;
Finley_Shape_Function Finley_Shape_Rec9;
Finley_Shape_Function Finley_Shape_Rec12;
Finley_Shape_Function Finley_Shape_Rec16;
Finley_Shape_Function Finley_Shape_Tet4;
Finley_Shape_Function Finley_Shape_Tet10;
Finley_Shape_Function Finley_Shape_Tet16;
Finley_Shape_Function Finley_Shape_Hex8;
Finley_Shape_Function Finley_Shape_Hex20;
Finley_Shape_Function Finley_Shape_Hex32;

#ifdef __cplusplus
}
#endif /* __cplusplus */


#endif /* #ifndef INC_FINLEY_SHAPEFUNCTIONS */

/*
 * $Log$
 * Revision 1.3  2005/09/15 03:44:23  jgs
 * Merge of development branch dev-02 back to main trunk on 2005-09-15
 *
 * Revision 1.2.2.1  2005/09/07 06:26:21  gross
 * the solver from finley are put into the standalone package paso now
 *
 * Revision 1.2  2005/07/08 04:07:56  jgs
 * Merge of development branch back to main trunk on 2005-07-08
 *
 * Revision 1.1.1.1.2.1  2005/06/29 02:34:55  gross
 * some changes towards 64 integers in finley
 *
 * Revision 1.1.1.1  2004/10/26 06:53:57  jgs
 * initial import of project esys2
 *
 * Revision 1.1.1.1  2004/06/24 04:00:40  johng
 * Initial version of eys using boost-python.
 *
 *
 */