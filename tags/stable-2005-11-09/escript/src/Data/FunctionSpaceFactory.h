/* 
 ******************************************************************************
 *                                                                            *
 *       COPYRIGHT  ACcESS 2004 -  All Rights Reserved                        *
 *                                                                            *
 * This software is the property of ACcESS. No part of this code              *
 * may be copied in any form or by any means without the expressed written    *
 * consent of ACcESS.  Copying, use or modification of this software          *
 * by any unauthorised person is illegal unless that person has a software    *
 * license agreement with ACcESS.                                             *
 *                                                                            *
 ******************************************************************************
*/
                                                                           
#if !defined  escript_FunctionSpaceFactory_20040604_H
#define escript_FunctionSpaceFactory_20040604_H

#include "escript/Data/AbstractDomain.h"
#include "escript/Data/FunctionSpace.h"

namespace escript {

  /**
     \brief
     Create function space objects.

     Description:
     Create function space objects.

  */

  /**
     \brief
     Return a continuous FunctionSpace
  */
  FunctionSpace continuousFunction(const AbstractDomain& domain);

  /**
     \brief
     Return a functon FunctionSpace
  */
  FunctionSpace function(const AbstractDomain& domain);
  /**
     \brief
     Return a function on boundary FunctionSpace
  */
  FunctionSpace functionOnBoundary(const AbstractDomain& domain);
  /**
     \brief
     Return a FunctionSpace
  */
  FunctionSpace functionOnContactZero(const AbstractDomain& domain);
  /**
     \brief
     Return a FunctionSpace
  */
  FunctionSpace functionOnContactOne(const AbstractDomain& domain);
  /**
     \brief
     Return a FunctionSpace
  */
  FunctionSpace solution(const AbstractDomain& domain);
  /**
     \brief
     Return a FunctionSpace
  */
  FunctionSpace reducedSolution(const AbstractDomain& domain);
  /**
     \brief
     Return a FunctionSpace
  */
  FunctionSpace diracDeltaFunction(const AbstractDomain& domain);

} // end of namespace
#endif
