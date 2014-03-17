
##############################################################################
#
# Copyright (c) 2003-2014 by University of Queensland
# http://www.uq.edu.au
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
# Development until 2012 by Earth Systems Science Computational Center (ESSCC)
# Development 2012-2013 by School of Earth Sciences
# Development from 2014 by Centre for Geoscience Computing (GeoComp)
#
##############################################################################

"""Cost functions for inversions with one or more forward models"""

__copyright__="""Copyright (c) 2003-2014 by University of Queensland
http://www.uq.edu.au
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

__all__ = [ 'InversionCostFunction']

from .costfunctions import MeteredCostFunction
from .mappings import Mapping
from .forwardmodels import ForwardModel
from esys.escript.pdetools import ArithmeticTuple
from esys.escript import Data
import numpy as np


class InversionCostFunction(MeteredCostFunction):
    """
    Class to define cost function *J(m)* for inversion with one or more
    forward models based on a multi-valued level set function *m*:

    *J(m) = J_reg(m) + sum_f mu_f * J_f(p)*

    where *J_reg(m)* is the regularization and cross gradient component of the
    cost function applied to a level set function *m*, *J_f(p)* are the data
    defect cost functions involving a physical forward model using the
    physical parameter(s) *p* and *mu_f* is the trade-off factor for model f.

    A forward model depends on a set of physical parameters *p* which are
    constructed from components of the level set function *m* via mappings.

    Example 1 (single forward model):
         m=Mapping()
         f=ForwardModel()
         J=InversionCostFunction(Regularization(), m, f)

    Example 2 (two forward models on a single valued level set)
         m0=Mapping()
         m1=Mapping()
         f0=ForwardModel()
         f1=ForwardModel()

         J=InversionCostFunction(Regularization(), mappings=[m0, m1], forward_models=[(f0, 0), (f1,1)])

    Example 3 (two forward models on 2-valued level set)
         m0=Mapping()
         m1=Mapping()
         f0=ForwardModel()
         f1=ForwardModel()

         J=InversionCostFunction(Regularization(numLevelSets=2), mappings=[(m0,0), (m1,0)], forward_models=[(f0, 0), (f1,1)])

    :cvar provides_inverse_Hessian_approximation: if true the class provides an
          approximative inverse of the Hessian operator.
    """
    provides_inverse_Hessian_approximation=True

    def __init__(self, regularization, mappings, forward_models):
        """
        constructor for the cost function.
        Stores the supplied object references and sets default weights.

        :param regularization: the regularization part of the cost function
        :type regularization: `Regularization`
        :param mappings: the mappings to calculate physical parameters from the
                         regularization. This is a list of 2-tuples *(map, i)*
                         where the first component map defines a `Mapping` and
                         the second component *i* defines the index of the
                         component of level set function to be used to
                         calculate the mapping. Items in the list may also be
                         just `Mapping` objects in which case the entire level
                         set function is fed into the `Mapping` (typically used
                         for a single-component level set function.
        :type mappings: `Mapping` or ``list``
        :param forward_models: the forward models involved in the calculation
                               of the cost function. This is a list of 2-tuples
                               *(f, ii)* where the first component f defines a
                               `ForwardModel` and the second component *ii* a
                               list of indexes referring to the physical
                               parameters in the `mappings` list. The 2-tuple
                               can be replaced by a `ForwardModel` if the
                               `mappings` list has a single entry.
        :param forward_models: `ForwardModel` or ``list``
        """
        super(InversionCostFunction, self).__init__()
        self.regularization=regularization

        if isinstance(mappings, Mapping):
             self.mappings = [mappings ]
        else:
             self.mappings = mappings

        if isinstance(forward_models, ForwardModel):
            self.forward_models = [ forward_models ]
        else:
            self.forward_models=forward_models
    
        trafo = regularization.getCoordinateTransformation()
        for m in self.forward_models:
            if isinstance(m, ForwardModel):
                F=m
            else:
                F=m[0]
            if not F.getCoordinateTransformation() == trafo:
                raise ValueError("Coordinate transformation for regularization and model don't match.") 

        self.numMappings=len(self.mappings)
        self.numModels=len(self.forward_models)
        self.numLevelSets = self.regularization.getNumLevelSets()
        self.__num_tradeoff_factors = self.regularization.getNumTradeOffFactors() + self.numModels
        self.setTradeOffFactorsModels()

        
        self.__Q={}
        for i in range(self.numModels):
            # find the index of the physical parameters used to evaluate a model
            f=self.forward_models[i]
            if isinstance(f, ForwardModel):
               idx=[0]
            elif len(f) == 1:
               idx=[0]
            else:
               idx = f[1]
               if isinstance(idx, int):
                 idx=[idx]
               else:
                 pass
      
            q=[]
            for k in idx:
                mm=self.mappings[k]
                if isinstance(mm, Mapping):
                    q.append(0)
                elif len(mm) == 1:
                    q.append(0)
                else:
                     if isinstance(mm[1], int):
                         q.append(mm[1])
                     else:
                        q+=list(mm[1])
            self.__Q[i]=q
        # for each parameter find the component of the levelset function  beeing used to define it:
        self.__parameter_to_level_set={}
        for k in range(self.numMappings):
            mm=self.mappings[k]
            if isinstance(mm, Mapping):
                 q=0
            elif len(mm) == 1:
                 q=0
            else:
                if isinstance(mm[1], int):
                   q=mm[1]
            self.__parameter_to_level_set[k]=q
                                
    def getDomain(self):
        """
        returns the domain of the cost function
        
        :rtype: `Domain`
        """
        self.regularization.getDomain()

    def getNumTradeOffFactors(self):
        """
        returns the number of trade-off factors being used including the
        trade-off factors used in the regularization component.

        :rtype: ``int``
        """
        return self.__num_tradeoff_factors

    def getForwardModel(self, idx=None):
        """
        returns the *idx*-th forward model.

        :param idx: model index. If cost function contains one model only `idx`
                    can be omitted.
        :type idx: ``int``
        """
        if idx==None: idx=0
        f=self.forward_models[idx]
        if isinstance(f, ForwardModel):
            F=f
        else:
            F=f[0]
        return F

    def getRegularization(self):
        """
        returns the regularization

        :rtype: `Regularization`
        """
        return self.regularization

    def setTradeOffFactorsModels(self, mu=None):
        """
        sets the trade-off factors for the forward model components.

        :param mu: list of the trade-off factors. If not present ones are used.
        :type mu: ``float`` in case of a single model or a ``list`` of
                  ``float`` with the length of the number of models.
        """
        if mu==None:
            self.mu_model=np.ones((self.numModels, ))
        else:
            if self.numModels > 1:
                mu=np.asarray(mu)
                if min(mu) > 0:
                    self.mu_model= mu
                else:
                    raise ValueError("All values for trade-off factor mu must be positive.")
            else:
                mu=float(mu)
                if mu > 0:
                    self.mu_model= [mu, ]
                else:
                    raise ValueError("Trade-off factor must be positive.")

    def getTradeOffFactorsModels(self):
        """
        returns the trade-off factors for the forward models

        :rtype: ``float`` or ``list`` of ``float``
        """
        if self.numModels>1:
            return self.mu_model
        else:
            return self.mu_model[0]

    def setTradeOffFactorsRegularization(self, mu=None, mu_c=None):
        """
        sets the trade-off factors for the regularization component of the
        cost function, see `Regularization` for details.

        :param mu: trade-off factors for the level-set variation part
        :param mu_c: trade-off factors for the cross gradient variation part
        """
        self.regularization.setTradeOffFactorsForVariation(mu)
        self.regularization.setTradeOffFactorsForCrossGradient(mu_c)

    def setTradeOffFactors(self, mu=None):
        """
        sets the trade-off factors for the forward model and regularization
        terms.

        :param mu: list of trade-off factors.
        :type mu: ``list`` of ``float``
        """
        if mu is None:
            mu=np.ones((self.__num_tradeoff_factors,))
        self.setTradeOffFactorsModels(mu[:self.numModels])
        self.regularization.setTradeOffFactors(mu[self.numModels:])

    def getTradeOffFactors(self, mu=None):
        """
        returns a list of the trade-off factors.

        :rtype: ``list`` of ``float``
        """
        mu1=self.getTradeOffFactorsModels(mu[:self.numModels])
        mu2=self.regularization.getTradeOffFactors()
        return [ m for m in mu1] + [ m for m in mu2]

    def createLevelSetFunction(self, *props):
        """
        returns an instance of an object used to represent a level set function
        initialized with zeros. Components can be overwritten by physical
        properties `props`. If present entries must correspond to the
        `mappings` arguments in the constructor. Use ``None`` for properties
        for which no value is given.
        """
        m=self.regularization.getPDE().createSolution()
        if len(props) > 0:
            for i in range(self.numMappings):
                if props[i]:
                    mm=self.mappings[i]
                    if isinstance(mm, Mapping):
                        m=mm.getInverse(props[i])
                    elif len(mm) == 1:
                        m=mm[0].getInverse(props[i])
                    else:
                        m[mm[1]]=mm[0].getInverse(props[i])
        return m

    def getProperties(self, m, return_list=False):
        """
        returns a list of the physical properties from a given level set
        function *m* using the mappings of the cost function.

        :param m: level set function
        :type m: `Data`
        :param return_list: if ``True`` a list is returned.
        :type return_list: ``bool``
        :rtype: ``list`` of `Data`
        """
        props=[]
        for i in range(self.numMappings):
            mm=self.mappings[i]
            if isinstance(mm, Mapping):
                p=mm.getValue(m)
            elif len(mm) == 1:
                p=mm[0].getValue(m)
            else:
                p=mm[0].getValue(m[mm[1]])
            props.append(p)
        if self.numMappings > 1 or return_list:
            return props
        else:
            return props[0]

    def _getDualProduct(self, x, r):
        """
        Returns the dual product, see `Regularization.getDualProduct`

        :type x: `Data`
        :type r: `ArithmeticTuple`
        :rtype: ``float``
        """
        return self.regularization.getDualProduct(x, r)

    def _getArguments(self, m):
        """
        returns pre-computed values that are shared in the calculation of
        *J(m)* and *grad J(m)*. In this implementation returns a tuple with the
        mapped value of ``m``, the arguments from the forward model and the
        arguments from the regularization.

        :param m: current approximation of the level set function
        :type m: `Data`
        :return: tuple of of values of the parameters, pre-computed values
                 for the forward model and pre-computed values for the
                 regularization
        :rtype: ``tuple``
        """
        args_reg=self.regularization.getArguments(m)
        # cache for physical parameters:
        props=self.getProperties(m, return_list=True)
        args_f=[]
        for i in range(self.numModels):
            f=self.forward_models[i]
            if isinstance(f, ForwardModel):
                aa=f.getArguments(props[0])
            elif len(f) == 1:
                aa=f[0].getArguments(props[0])
            else:
                idx = f[1]
                f=f[0]
                if isinstance(idx, int):
                    aa=f.getArguments(props[idx])
                else:
                    pp=tuple( [ props[i] for i in idx] )
                    aa=f.getArguments(*pp)
            args_f.append(aa)

        return props, args_f, args_reg

    def _getValue(self, m, *args):
        """
        Returns the value *J(m)* of the cost function at *m*.
        If the pre-computed values are not supplied `getArguments()` is called.

        :param m: current approximation of the level set function
        :type m: `Data`
        :param args: tuple of values of the parameters, pre-computed values
                     for the forward model and pre-computed values for the
                     regularization
        :rtype: ``float``
        """
        if len(args)==0:
            args=self.getArguments(m)

        props=args[0]
        args_f=args[1]
        args_reg=args[2]

        J = self.regularization.getValue(m, *args_reg)

        for i in range(self.numModels):
            f=self.forward_models[i]
            if isinstance(f, ForwardModel):
                J_f = f.getDefect(props[0],*args_f[i])
            elif len(f) == 1:
                J_f=f[0].getDefect(props[0],*args_f[i])
            else:
                idx = f[1]
                f=f[0]
                if isinstance(idx, int):
                    J_f = f.getDefect(props[idx],*args_f[i])
                else:
                    args=tuple( [ props[j] for j in idx] + args_f[i])
                    J_f = f.getDefect(*args)
            self.logger.debug("J_f[%d] = %e, mu_model[%d] = %e"%(i, J_f, i, self.mu_model[i]))
            J += self.mu_model[i] * J_f

        return J

    def getComponentValues(self, m, *args):
        return self._getComponentValues(m, *args)

    def _getComponentValues(self, m, *args):
        """
        returns the values of the individual cost functions that make up *f(x)* 
        using the precalculated values for *x*.

        :param x: a solution approximation
        :type x: x-type
        :rtype: ``list<<float>>``
        """
        if len(args)==0:
            args=self.getArguments(m)

        props=args[0]
        args_f=args[1]
        args_reg=args[2]

        J_reg = self.regularization.getValue(m, *args_reg)
        result = [J_reg]

        for i in range(self.numModels):
            f=self.forward_models[i]
            if isinstance(f, ForwardModel):
                J_f = f.getValue(props[0],*args_f[i])
            elif len(f) == 1:
                J_f=f[0].getValue(props[0],*args_f[i])
            else:
                idx = f[1]
                f=f[0]
                if isinstance(idx, int):
                    J_f = f.getValue(props[idx],*args_f[i])
                else:
                    args=tuple( [ props[j] for j in idx] + args_f[i])
                    J_f = f.getValue(*args)
            self.logger.debug("J_f[%d] = %e, mu_model[%d] = %e"%(i, J_f, i, self.mu_model[i]))

            result += [J_f] # self.mu_model[i] * ?? 

        return result

         
    def _getGradient(self, m, *args):
        """
        returns the gradient of the cost function at *m*.
        If the pre-computed values are not supplied `getArguments()` is called.

        :param m: current approximation of the level set function
        :type m: `Data`
        :param args: tuple of values of the parameters, pre-computed values
                     for the forward model and pre-computed values for the
                     regularization

        :rtype: `ArithmeticTuple`
        
        :note: returns (Y^,X) where Y^ is gradient from regularisation plus gradients of fwd models.
               X is the gradient of the regularisation wrt gradient of m.
        """
        if len(args)==0:
            args = self.getArguments(m)

        props=args[0]
        args_f=args[1]
        args_reg=args[2]

        g_J = self.regularization.getGradient(m, *args_reg)
        p_diffs=[]
        for i in range(self.numMappings):
            mm=self.mappings[i]
            if isinstance(mm, Mapping):
                dpdm = mm.getDerivative(m)
            elif len(mm) == 1:
                dpdm = mm[0].getDerivative(m)
            else:
                dpdm = mm[0].getDerivative(m[mm[1]])
            p_diffs.append(dpdm)

        Y=g_J[0]      # Beacause g_J==(Y,X)  Y_k=dKer/dm_k
        for i in range(self.numModels):
            mu=self.mu_model[i]
            f=self.forward_models[i]
            if isinstance(f, ForwardModel):
                Ys= f.getGradient(props[0],*args_f[i]) * p_diffs[0] * mu
                if self.numLevelSets == 1 :
                    Y +=Ys
                else:
                    Y[self.__parameter_to_level_set[0]] +=Ys
            elif len(f) == 1:
                Ys=f[0].getGradient(props[0],*args_f[i]) * p_diffs[0]  * mu
                if self.numLevelSets == 1 :
                    Y +=Ys
                else:
                    Y[self.__parameter_to_level_set[0]] +=Ys
            else:
                idx = f[1]
                f = f[0]
                if isinstance(idx, int):
                    Ys = f.getGradient(props[idx],*args_f[i]) * p_diffs[idx] * mu
                    if self.numLevelSets == 1 :
                        Y+=Ys
                    else:
                        Y[self.__parameter_to_level_set[idx]] += Ys
                else:
                    args = tuple( [ props[j] for j in idx] + args_f[i])
                    Ys = f.getGradient(*args)
                    for j in range(idx):
                        if self.numLevelSets == 1 :
                           Y+=Ys[j]* p_diffs[idx[j]] * mu
                        else:
                           Y[self.__parameter_to_level_set[j]]+=Ys[j]* p_diffs[idx[j]] * mu
        return g_J

    def _getInverseHessianApproximation(self, m, r, *args):
        """
        returns an approximative evaluation *p* of the inverse of the Hessian
        operator of the cost function for a given gradient type *r* at a
        given location *m*: *H(m) p = r*

        :param m: level set approximation where to calculate Hessian inverse
        :type m: `Data`
        :param r: a given gradient
        :type r: `ArithmeticTuple`
        :param args: tuple of values of the parameters, pre-computed values
                     for the forward model and pre-computed values for the
                     regularization
        :rtype: `Data`
        :note: in the current implementation only the regularization term is
               considered in the inverse Hessian approximation.
        """
        m=self.regularization.getInverseHessianApproximation(m, r, *args[2])
        return m

    def updateHessian(self):
        """
        notifies the class that the Hessian operator needs to be updated.
        """
        self.regularization.updateHessian()

    def _getNorm(self, m):
        """
        returns the norm of `m`

        :param m: level set function
        :type m: `Data`
        :rtype: ``float``
        """
        return self.regularization.getNorm(m)
