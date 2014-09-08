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

#include "FunctionSpaceFactory.h"
#include "AbstractContinuousDomain.h"

namespace escript {

FunctionSpace continuousFunction(const AbstractDomain& domain) 
{
  const AbstractContinuousDomain& temp=AbstractContinuousDomain::asAbstractContinuousDomain(domain);
  return FunctionSpace(domain,temp.getContinuousFunctionCode());
}
 
FunctionSpace function(const AbstractDomain& domain) 
{
  const AbstractContinuousDomain& temp=AbstractContinuousDomain::asAbstractContinuousDomain(domain);
  return FunctionSpace(domain,temp.getFunctionCode());
}

FunctionSpace functionOnBoundary(const AbstractDomain& domain) 
{
  const AbstractContinuousDomain& temp=AbstractContinuousDomain::asAbstractContinuousDomain(domain);
  return FunctionSpace(domain,temp.getFunctionOnBoundaryCode());
}

FunctionSpace functionOnContactZero(const AbstractDomain& domain) 
{
  const AbstractContinuousDomain& temp=AbstractContinuousDomain::asAbstractContinuousDomain(domain);
  return FunctionSpace(domain,temp.getFunctionOnContactZeroCode());
}
 
FunctionSpace functionOnContactOne(const AbstractDomain& domain) 
{
  const AbstractContinuousDomain& temp=AbstractContinuousDomain::asAbstractContinuousDomain(domain);
  return FunctionSpace(domain,temp.getFunctionOnContactOneCode());
}

FunctionSpace solution(const AbstractDomain& domain) 
{
  const AbstractContinuousDomain& temp=AbstractContinuousDomain::asAbstractContinuousDomain(domain);
  return FunctionSpace(domain,temp.getSolutionCode());
}

FunctionSpace reducedSolution(const AbstractDomain& domain) 
{
  const AbstractContinuousDomain& temp=AbstractContinuousDomain::asAbstractContinuousDomain(domain);
  return FunctionSpace(domain,temp.getReducedSolutionCode());
}

FunctionSpace diracDeltaFunction(const AbstractDomain& domain)
{
  const AbstractContinuousDomain& temp=AbstractContinuousDomain::asAbstractContinuousDomain(domain);
  return FunctionSpace(domain,temp.getDiracDeltaFunctionCode());
}

}  // end of namespace