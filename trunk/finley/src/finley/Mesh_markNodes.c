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

/*   Finley: Mesh */

/*   mark the used nodes with offeset: */

/**************************************************************/

/*  Author: gross@access.edu.au */
/*  Version: $Id$ */

/**************************************************************/

#include "Mesh.h"

/**************************************************************/

void Finley_Mesh_markNodes(index_t* mask,index_t offset,Finley_Mesh* in,bool_t useLinear) {
          Finley_ElementFile_markNodes(mask,offset,in->Elements,useLinear);
          Finley_ElementFile_markNodes(mask,offset,in->FaceElements,useLinear);
          Finley_ElementFile_markNodes(mask,offset,in->ContactElements,useLinear);
          Finley_ElementFile_markNodes(mask,offset,in->Points,useLinear);
}
/*
* $Log$
* Revision 1.3  2005/09/15 03:44:22  jgs
* Merge of development branch dev-02 back to main trunk on 2005-09-15
*
* Revision 1.2.2.1  2005/09/07 06:26:19  gross
* the solver from finley are put into the standalone package paso now
*
* Revision 1.2  2005/07/08 04:07:53  jgs
* Merge of development branch back to main trunk on 2005-07-08
*
* Revision 1.1.1.1.2.1  2005/06/29 02:34:52  gross
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

