
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

__copyright__="""Copyright (c) 2003-2014 by University of Queensland
http://www.uq.edu.au
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"


__author__="Lutz Gross, l.gross@uq.edu.au"

import unittest
from esys.escript import *
from esys.escript.linearPDEs import LinearPDE

class Test_assemblage_2Do1(unittest.TestCase):
  def setNormal(self,fs):
     out=Vector(0.,fs)
     out.setTaggedValue(2,[1,0])
     out.setTaggedValue(1,[-1,0])
     out.setTaggedValue(20, [0,1])
     out.setTaggedValue(10, [0,-1])
     return out
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=5-9*x[1]-7*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[0,0]=7
    Y_test=0
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[0]*((-49))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=(-2)-2*x[1]-7*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[0,1]=3
    Y_test=0
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[0]*((-6))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=(-2)-7*x[1]-4*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[1,0]=2
    Y_test=0
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[1]*((-8))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=1+3*x[1]+5*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[1,1]=5
    Y_test=0
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[1]*(15)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Const_typeStrong_comp0(self):
    x=self.domain.getX()
    u=5+5*x[1]+2*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[0]=3
    Y_test=(-6)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[0]*(15+15*x[1]+6*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Const_typeStrong_comp1(self):
    x=self.domain.getX()
    u=5-8*x[1]+3*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[1]=7
    Y_test=56
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[1]*(35-56*x[1]+21*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_C_Const_typeStrong_comp0(self):
    x=self.domain.getX()
    u=6-9*x[1]-3*x[0]
    C_test=Data(0.,(2,),Function(self.domain))
    C_test[0]=3
    Y_test=(-9)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_C_Const_typeStrong_comp1(self):
    x=self.domain.getX()
    u=(-6)+7*x[1]+5*x[0]
    C_test=Data(0.,(2,),Function(self.domain))
    C_test[1]=8
    Y_test=56
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_D_Const_typeStrong(self):
    x=self.domain.getX()
    u=1+2*x[1]-7*x[0]
    D_test=Data(6,(),Function(self.domain))
    Y_test=6+12*x[1]-42*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_d_Const_typeStrong(self):
    x=self.domain.getX()
    u=8-4*x[1]+4*x[0]
    d_test=Data(5,(),FunctionOnBoundary(self.domain))
    y_test=40-20*x[1]+20*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=6-2*x[1]+7*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[0,0]=x[0]
    Y_test=(-7)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[0]*(7*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=(-4)-1*x[1]+2*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[0,1]=x[0]
    Y_test=1
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[0]*((-1)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=2+2*x[1]+4*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[1,0]=x[1]
    Y_test=(-4)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[1]*(4*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=2-6*x[1]-2*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[1,1]=x[1]
    Y_test=6
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[1]*((-6)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Vario_typeStrong_comp0(self):
    x=self.domain.getX()
    u=(-7)+x[1]+6*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[0]=x[0]
    Y_test=7-1*x[1]-12*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[0]*((-7)*x[0]+x[0]*x[1]+6*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Vario_typeStrong_comp1(self):
    x=self.domain.getX()
    u=(-1)-1*x[1]+2*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[1]=x[1]
    Y_test=1+2*x[1]-2*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[1]*((-1)*x[1]-1*x[1]**2+2*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_C_Vario_typeStrong_comp0(self):
    x=self.domain.getX()
    u=8-5*x[1]-8*x[0]
    C_test=Data(0.,(2,),Function(self.domain))
    C_test[0]=x[0]
    Y_test=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_C_Vario_typeStrong_comp1(self):
    x=self.domain.getX()
    u=7+6*x[1]-9*x[0]
    C_test=Data(0.,(2,),Function(self.domain))
    C_test[1]=x[1]
    Y_test=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_D_Vario_typeStrong(self):
    x=self.domain.getX()
    u=7
    D_test=Function(self.domain).getX()[0]
    Y_test=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_d_Vario_typeStrong(self):
    x=self.domain.getX()
    u=3
    d_test=interpolate(x[0],FunctionOnBoundary(self.domain))
    y_test=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Const_typeWeak_comp00(self):
    x=self.domain.getX()
    u=4+3*x[1]-7*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[0,0]=1
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=(-7)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Const_typeWeak_comp01(self):
    x=self.domain.getX()
    u=(-7)-9*x[1]-8*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[0,1]=8
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=(-72)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Const_typeWeak_comp10(self):
    x=self.domain.getX()
    u=1+5*x[1]-3*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[1,0]=3
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=(-9)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Const_typeWeak_comp11(self):
    x=self.domain.getX()
    u=(-1)-7*x[1]+2*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[1,1]=8
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=(-56)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Const_typeWeak_comp0(self):
    x=self.domain.getX()
    u=7-5*x[1]-7*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[0]=7
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=49-35*x[1]-49*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Const_typeWeak_comp1(self):
    x=self.domain.getX()
    u=(-7)-4*x[1]-1*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[1]=4
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=(-28)-16*x[1]-4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Vario_typeWeak_comp00(self):
    x=self.domain.getX()
    u=1+x[1]+2*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[0,0]=x[0]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Vario_typeWeak_comp01(self):
    x=self.domain.getX()
    u=(-1)-3*x[1]-3*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[0,1]=x[0]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Vario_typeWeak_comp10(self):
    x=self.domain.getX()
    u=(-6)+5*x[1]+x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[1,0]=x[1]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_A_Vario_typeWeak_comp11(self):
    x=self.domain.getX()
    u=(-5)+3*x[1]-6*x[0]
    A_test=Data(0.,(2,2),Function(self.domain))
    A_test[1,1]=x[1]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=3*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Vario_typeWeak_comp0(self):
    x=self.domain.getX()
    u=(-8)
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[0]=x[0]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Vario_typeWeak_comp1(self):
    x=self.domain.getX()
    u=(-8)
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[1]=x[1]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=(-8)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)+7*x[1]-1*x[0]
    u[1]=(-4)+7*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,0,0]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-1))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8-6*x[1]-8*x[0]
    u[1]=(-3)+5*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,0,1]=5
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-30))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)-3*x[1]+2*x[0]
    u[1]=6+x[1]-1*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,1,0]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-4))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1+2*x[1]+6*x[0]
    u[1]=(-3)-3*x[1]-1*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,1,1]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-9))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4+2*x[1]+2*x[0]
    u[1]=(-1)+3*x[1]+2*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,0,0]=8
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(16)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+4*x[1]-1*x[0]
    u[1]=(-9)-5*x[1]-6*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,0,1]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(8)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3-4*x[1]+5*x[0]
    u[1]=(-9)+4*x[1]+5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,1,0]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(20)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+x[1]-6*x[0]
    u[1]=(-8)-7*x[1]+3*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,1,1]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-14))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+4*x[1]+5*x[0]
    u[1]=3+x[1]+3*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,0,0]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(10)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)+7*x[1]+3*x[0]
    u[1]=(-2)-1*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,0,1]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(49)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-7*x[1]-7*x[0]
    u[1]=5-8*x[1]-7*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,1,0]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-49))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)-5*x[1]+4*x[0]
    u[1]=(-4)+4*x[1]-8*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,1,1]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(16)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)-1*x[1]-2*x[0]
    u[1]=7+7*x[1]+6*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,0,0]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-12))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1+6*x[1]+6*x[0]
    u[1]=(-3)+4*x[1]+6*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,0,1]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(18)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)+2*x[1]+7*x[0]
    u[1]=(-2)-8*x[1]+2*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,1,0]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(12)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeStrong_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)+3*x[1]-9*x[0]
    u[1]=2+8*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,1,1]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(24)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)-9*x[1]-8*x[0]
    u[1]=(-6)-7*x[1]+8*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,0]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=24
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-15)-27*x[1]-24*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2-9*x[1]-8*x[0]
    u[1]=5+6*x[1]-5*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,1]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=30
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(30+36*x[1]-30*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)+6*x[1]-1*x[0]
    u[1]=(-9)-2*x[1]+8*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,0]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-42)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-35)+42*x[1]-7*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4-4*x[1]+4*x[0]
    u[1]=1+5*x[1]+8*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,1]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-30)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(6+30*x[1]+48*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-5*x[1]-8*x[0]
    u[1]=1-2*x[1]+5*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,0]=8
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=64
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(56-40*x[1]-64*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)+2*x[1]-9*x[0]
    u[1]=(-6)+4*x[1]+x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,1]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-3)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-18)+12*x[1]+3*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)+5*x[1]-5*x[0]
    u[1]=(-1)+7*x[1]-5*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,0]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-15)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-15)+15*x[1]-15*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+8*x[1]-5*x[0]
    u[1]=(-7)+7*x[1]-9*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,1]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-7)+7*x[1]-9*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Const_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-4*x[1]-8*x[0]
    u[1]=8+6*x[1]+x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[0,0,0]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-16)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Const_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2+3*x[1]-9*x[0]
    u[1]=(-7)+7*x[1]+4*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[0,0,1]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=3
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Const_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3-1*x[1]-7*x[0]
    u[1]=2+7*x[1]+7*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[0,1,0]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=21
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Const_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)+7*x[1]+7*x[0]
    u[1]=(-4)+7*x[1]+2*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[0,1,1]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=14
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Const_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5-2*x[1]-7*x[0]
    u[1]=(-8)+2*x[1]-4*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[1,0,0]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Const_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)+x[1]+8*x[0]
    u[1]=2+x[1]-9*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[1,0,1]=8
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=8
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Const_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8+6*x[1]+6*x[0]
    u[1]=(-6)-4*x[1]-1*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[1,1,0]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Const_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3-7*x[1]+7*x[0]
    u[1]=(-1)-5*x[1]+6*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[1,1,1]=8
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-40)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_D_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8-1*x[1]-6*x[0]
    u[1]=(-4)-3*x[1]-9*x[0]
    D_test=Data(0.,(2,2),Function(self.domain))
    D_test[0,0]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=24-3*x[1]-18*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_D_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)-8*x[1]+7*x[0]
    u[1]=(-2)+3*x[1]-5*x[0]
    D_test=Data(0.,(2,2),Function(self.domain))
    D_test[0,1]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-12)+18*x[1]-30*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_D_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+6*x[1]-8*x[0]
    u[1]=7+3*x[1]-9*x[0]
    D_test=Data(0.,(2,2),Function(self.domain))
    D_test[1,0]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=12+12*x[1]-16*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_D_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)-3*x[1]+4*x[0]
    u[1]=1+8*x[1]-8*x[0]
    D_test=Data(0.,(2,2),Function(self.domain))
    D_test[1,1]=5
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=5+40*x[1]-40*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)+3*x[1]+8*x[0]
    u[1]=7+6*x[1]+3*x[0]
    d_test=Data(0.,(2,2),FunctionOnBoundary(self.domain))
    d_test[0,0]=8
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[0]=(-72)+24*x[1]+64*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1+3*x[1]+3*x[0]
    u[1]=(-4)-2*x[1]+2*x[0]
    d_test=Data(0.,(2,2),FunctionOnBoundary(self.domain))
    d_test[0,1]=1
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[0]=(-4)-2*x[1]+2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)+6*x[1]-7*x[0]
    u[1]=4+4*x[1]-3*x[0]
    d_test=Data(0.,(2,2),FunctionOnBoundary(self.domain))
    d_test[1,0]=2
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[1]=(-4)+12*x[1]-14*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+x[1]-9*x[0]
    u[1]=(-8)+6*x[1]+3*x[0]
    d_test=Data(0.,(2,2),FunctionOnBoundary(self.domain))
    d_test[1,1]=3
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[1]=(-24)+18*x[1]+9*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6-7*x[1]-2*x[0]
    u[1]=(-7)+6*x[1]+2*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=2
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-2)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-2*x[1]+x[0]
    u[1]=5-5*x[1]+2*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=2
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-2)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+8*x[1]+2*x[0]
    u[1]=(-3)-7*x[1]+8*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-8)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(8*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)-3*x[1]-1*x[0]
    u[1]=(-9)-2*x[1]+5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,1,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=2
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-2)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3-5*x[1]-3*x[0]
    u[1]=6-1*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,0,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=3
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-3)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)+6*x[1]+6*x[0]
    u[1]=(-2)-4*x[1]+5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,0,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-6)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(6*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)+6*x[1]+6*x[0]
    u[1]=8-3*x[1]-2*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=2
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-2)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4-1*x[1]-1*x[0]
    u[1]=(-4)-6*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=6
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-6)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-5*x[1]-1*x[0]
    u[1]=(-6)-9*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=1
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-1)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2-3*x[1]-6*x[0]
    u[1]=(-3)+8*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=3
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-3)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8+6*x[1]+4*x[0]
    u[1]=(-5)-7*x[1]-1*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=1
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-1)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)-3*x[1]+4*x[0]
    u[1]=7-9*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,1,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=9
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-9)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6-5*x[1]+x[0]
    u[1]=(-7)-1*x[1]+x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,0,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-1)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)+2*x[1]+5*x[0]
    u[1]=5+2*x[1]+6*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,0,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-2)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(2*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)-2*x[1]-1*x[0]
    u[1]=(-5)+6*x[1]+5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-5)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(5*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeStrong_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-1*x[1]+4*x[0]
    u[1]=(-8)-8*x[1]-6*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=8
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-8)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)+8*x[1]-4*x[0]
    u[1]=(-4)+3*x[1]+7*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=1-8*x[1]+8*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-1)*x[0]+8*x[0]*x[1]-4*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4-1*x[1]+3*x[0]
    u[1]=2+x[1]-5*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-2)-1*x[1]+10*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(2*x[0]+x[0]*x[1]-5*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)+6*x[1]-7*x[0]
    u[1]=4+2*x[1]-9*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=3-12*x[1]+7*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-3)*x[1]+6*x[1]**2-7*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4-3*x[1]-7*x[0]
    u[1]=5-7*x[1]+8*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-5)+14*x[1]-8*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(5*x[1]-7*x[1]**2+8*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+8*x[1]+2*x[0]
    u[1]=(-1)+7*x[1]+6*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-6)-8*x[1]-4*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(6*x[0]+8*x[0]*x[1]+2*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)-2*x[1]-4*x[0]
    u[1]=3+4*x[1]+8*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-3)-4*x[1]-16*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(3*x[0]+4*x[0]*x[1]+8*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2+8*x[1]-3*x[0]
    u[1]=(-3)+5*x[1]+5*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-2)-16*x[1]+3*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(2*x[1]+8*x[1]**2-3*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4+4*x[1]-3*x[0]
    u[1]=(-3)-7*x[1]+7*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=3+14*x[1]-7*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-3)*x[1]-7*x[1]**2+7*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Vario_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)+4*x[1]+7*x[0]
    u[1]=6+7*x[1]-5*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[0,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Vario_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-8*x[1]-9*x[0]
    u[1]=(-3)+7*x[1]-9*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[0,0,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-8)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Vario_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3-2*x[1]+x[0]
    u[1]=3-7*x[1]-1*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[0,1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Vario_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)-5*x[1]+2*x[0]
    u[1]=(-8)+x[1]-1*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[0,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Vario_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8-5*x[1]+x[0]
    u[1]=4-5*x[1]-5*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[1,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Vario_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)+5*x[1]-4*x[0]
    u[1]=(-2)+x[1]-3*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[1,0,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Vario_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-1*x[1]+6*x[0]
    u[1]=2+4*x[1]-4*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[1,1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_C_Vario_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)+x[1]+2*x[0]
    u[1]=8-7*x[1]-8*x[0]
    C_test=Data(0.,(2,2,2),Function(self.domain))
    C_test[1,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_D_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=(-4)
    D_test=Data(0.,(2,2),Function(self.domain))
    D_test[0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_D_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=2
    D_test=Data(0.,(2,2),Function(self.domain))
    D_test[0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_D_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=(-3)
    D_test=Data(0.,(2,2),Function(self.domain))
    D_test[1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_D_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=6
    D_test=Data(0.,(2,2),Function(self.domain))
    D_test[1,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=(-9)
    d_test=Data(0.,(2,2),FunctionOnBoundary(self.domain))
    d_test[0,0]=x[0]
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=2
    d_test=Data(0.,(2,2),FunctionOnBoundary(self.domain))
    d_test[0,1]=x[0]
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=(-3)
    d_test=Data(0.,(2,2),FunctionOnBoundary(self.domain))
    d_test[1,0]=x[0]
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[1]=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=(-4)
    d_test=Data(0.,(2,2),FunctionOnBoundary(self.domain))
    d_test[1,1]=x[0]
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[1]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5-9*x[1]-8*x[0]
    u[1]=4-8*x[1]-5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,0,0]=3
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-24)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-6*x[1]+8*x[0]
    u[1]=7-2*x[1]-7*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,0,1]=7
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-42)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)-2*x[1]-5*x[0]
    u[1]=(-3)+4*x[1]-5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,1,0]=2
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-10)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+5*x[1]-4*x[0]
    u[1]=6-6*x[1]+x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,1,1]=8
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-48)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1+2*x[1]-4*x[0]
    u[1]=1-3*x[1]+5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,0,0]=7
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-28)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)-9*x[1]+x[0]
    u[1]=(-2)-9*x[1]+7*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,0,1]=5
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-45)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)-7*x[1]+6*x[0]
    u[1]=(-3)-7*x[1]+8*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,1,0]=7
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=56
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)-3*x[1]+4*x[0]
    u[1]=(-4)+2*x[1]-5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,1,1]=3
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=6
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)-7*x[1]-3*x[0]
    u[1]=(-5)+3*x[1]+7*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,0,0]=1
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-3)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)-9*x[1]-8*x[0]
    u[1]=2+6*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,0,1]=1
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-9)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)-1*x[1]-2*x[0]
    u[1]=7-4*x[1]-8*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,1,0]=2
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-16)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)-6*x[1]-7*x[0]
    u[1]=8-9*x[1]-8*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,1,1]=5
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-45)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5-7*x[1]-7*x[0]
    u[1]=(-9)-3*x[1]+7*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,0,0]=5
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-35)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)-3*x[1]-2*x[0]
    u[1]=4+7*x[1]+7*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,0,1]=8
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-24)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+2*x[1]-7*x[0]
    u[1]=4+4*x[1]-6*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,1,0]=4
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-24)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Const_typeWeak_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4-9*x[1]+x[0]
    u[1]=3-5*x[1]+3*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,1,1]=4
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-20)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeWeak_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5-7*x[1]-7*x[0]
    u[1]=(-5)+7*x[1]-1*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,0]=7
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=35-49*x[1]-49*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeWeak_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+2*x[1]-9*x[0]
    u[1]=(-6)-5*x[1]-8*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,1]=7
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-42)-35*x[1]-56*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeWeak_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)-3*x[1]+7*x[0]
    u[1]=(-8)-8*x[1]+7*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,0]=3
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-12)-9*x[1]+21*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeWeak_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)+3*x[1]+7*x[0]
    u[1]=(-7)-6*x[1]+x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,1]=4
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-28)-24*x[1]+4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeWeak_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)-1*x[1]-2*x[0]
    u[1]=(-8)-3*x[1]+6*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,0]=6
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-12)-6*x[1]-12*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeWeak_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4+4*x[1]-4*x[0]
    u[1]=(-3)-5*x[1]+3*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,1]=1
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-3)-5*x[1]+3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeWeak_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8-5*x[1]+2*x[0]
    u[1]=6-8*x[1]+8*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,0]=2
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=16-10*x[1]+4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeWeak_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)-8*x[1]-9*x[0]
    u[1]=(-6)-9*x[1]+4*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,1]=5
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-30)-45*x[1]+20*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)-2*x[1]-5*x[0]
    u[1]=(-8)+8*x[1]+2*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,0,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+6*x[1]-2*x[0]
    u[1]=4-7*x[1]-5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,0,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-1*x[1]-7*x[0]
    u[1]=(-1)+2*x[1]-2*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,1,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-2)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)+4*x[1]-1*x[0]
    u[1]=(-7)+4*x[1]-5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,0,1,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)+5*x[1]-5*x[0]
    u[1]=5-3*x[1]+x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,0,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-5)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8+5*x[1]-3*x[0]
    u[1]=6+8*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,0,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8+2*x[1]+5*x[0]
    u[1]=1+7*x[1]-2*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,1,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-2)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2-6*x[1]+x[0]
    u[1]=(-1)-7*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[0,1,1,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-7)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)+3*x[1]+7*x[0]
    u[1]=(-2)+2*x[1]+5*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,0,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7+8*x[1]+5*x[0]
    u[1]=2+x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,0,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)-5*x[1]-8*x[0]
    u[1]=(-9)+3*x[1]+2*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,1,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)-9*x[1]+5*x[0]
    u[1]=(-5)-8*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,0,1,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8+7*x[1]-4*x[0]
    u[1]=6-3*x[1]+x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,0,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-4)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)-3*x[1]+4*x[0]
    u[1]=(-9)-9*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,0,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-3)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)+3*x[1]+3*x[0]
    u[1]=6-7*x[1]+7*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,1,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=7*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_A_Vario_typeWeak_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3-3*x[1]-6*x[0]
    u[1]=3+2*x[1]+3*x[0]
    A_test=Data(0.,(2,2,2,2),Function(self.domain))
    A_test[1,1,1,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=2*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeWeak_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=(-7)
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeWeak_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=(-4)
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeWeak_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=3
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeWeak_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=5
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeWeak_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=(-4)
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeWeak_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=(-5)
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeWeak_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=2
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-7)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeWeak_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=(-4)
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-4)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+5*x[1]+7*x[0]
    u[1]=8-1*x[1]+8*x[0]
    u[2]=(-1)-9*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,0,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(28)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5+x[1]+2*x[0]
    u[1]=8+4*x[1]-1*x[0]
    u[2]=(-9)-8*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,0,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(6)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+5*x[1]-1*x[0]
    u[1]=7+2*x[1]-3*x[0]
    u[2]=(-1)-5*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,1,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-6))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-4*x[1]+3*x[0]
    u[1]=(-1)+3*x[1]+3*x[0]
    u[2]=8+4*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,1,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(21)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-1*x[1]+8*x[0]
    u[1]=(-9)+7*x[1]+4*x[0]
    u[2]=(-7)+4*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,2,0]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(56)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+x[1]+5*x[0]
    u[1]=3+8*x[1]+4*x[0]
    u[2]=(-1)+8*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,2,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(16)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-6*x[1]+2*x[0]
    u[1]=2+5*x[1]+7*x[0]
    u[2]=8+6*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,0,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(8)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+5*x[1]+7*x[0]
    u[1]=(-4)-2*x[1]+x[0]
    u[2]=5+x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,0,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(10)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+4*x[1]-7*x[0]
    u[1]=6-3*x[1]-2*x[0]
    u[2]=(-7)-9*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,1,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-12))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-2*x[1]+3*x[0]
    u[1]=5-8*x[1]-9*x[0]
    u[2]=8+7*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,1,1]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-32))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-2*x[1]-5*x[0]
    u[1]=(-6)-9*x[1]+4*x[0]
    u[2]=(-5)-4*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,2,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(9)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp0121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-9*x[1]+4*x[0]
    u[1]=(-2)+8*x[1]+7*x[0]
    u[2]=8+x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,2,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(2)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-9*x[1]-3*x[0]
    u[1]=7-5*x[1]+x[0]
    u[2]=(-6)-8*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,0,0]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-21))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-1*x[1]+x[0]
    u[1]=(-6)+7*x[1]+8*x[0]
    u[2]=3+6*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,0,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-3))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-4*x[1]-5*x[0]
    u[1]=6-1*x[1]-9*x[0]
    u[2]=(-5)-5*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,1,0]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-45))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-2*x[1]-3*x[0]
    u[1]=(-3)-5*x[1]-6*x[0]
    u[2]=(-4)+8*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,1,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-30))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-4*x[1]-2*x[0]
    u[1]=(-5)-3*x[1]+8*x[0]
    u[2]=1+7*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,2,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-12))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+4*x[1]-7*x[0]
    u[1]=(-1)+6*x[1]-7*x[0]
    u[2]=1+x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,2,1]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(4)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+2*x[1]+6*x[0]
    u[1]=(-6)+8*x[1]+4*x[0]
    u[2]=5+2*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,0,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(24)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-7*x[1]-8*x[0]
    u[1]=1+4*x[1]-1*x[0]
    u[2]=(-2)-8*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,0,1]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-28))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+8*x[1]-6*x[0]
    u[1]=(-2)-7*x[1]-2*x[0]
    u[2]=1-6*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,1,0]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-14))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+x[1]-3*x[0]
    u[1]=(-4)-8*x[1]+x[0]
    u[2]=6-7*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,1,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-48))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+7*x[1]-1*x[0]
    u[1]=(-6)+6*x[1]-7*x[0]
    u[2]=5+4*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,2,0]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-7))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp1121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-2*x[1]-7*x[0]
    u[1]=7+6*x[1]-9*x[0]
    u[2]=8-7*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,2,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-14))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-8*x[1]-7*x[0]
    u[1]=8-1*x[1]-6*x[0]
    u[2]=4+5*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,0,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-21))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-6*x[1]+3*x[0]
    u[1]=1+3*x[1]+8*x[0]
    u[2]=(-2)-2*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,0,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-36))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-1*x[1]-3*x[0]
    u[1]=(-9)+7*x[1]-8*x[0]
    u[2]=(-9)-2*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,1,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-32))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-4*x[1]+6*x[0]
    u[1]=(-3)-2*x[1]-7*x[0]
    u[2]=3+8*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,1,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-4))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-8*x[1]+4*x[0]
    u[1]=(-1)-9*x[1]-4*x[0]
    u[2]=5-1*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,2,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-4))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+4*x[1]+7*x[0]
    u[1]=1+4*x[1]+3*x[0]
    u[2]=4-2*x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,2,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-16))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+x[1]-1*x[0]
    u[1]=(-7)+3*x[1]-8*x[0]
    u[2]=(-9)+6*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,0,0]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-8))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+6*x[1]-4*x[0]
    u[1]=(-7)-6*x[1]-9*x[0]
    u[2]=(-9)-2*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,0,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(36)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-4*x[1]+8*x[0]
    u[1]=(-7)+8*x[1]+7*x[0]
    u[2]=4+3*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,1,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(28)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-8*x[1]+8*x[0]
    u[1]=8+3*x[1]-1*x[0]
    u[2]=(-2)+4*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,1,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(9)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5+4*x[1]-7*x[0]
    u[1]=5+2*x[1]+4*x[0]
    u[2]=4-1*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,2,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-6))
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeStrong_comp2121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-1*x[1]-6*x[0]
    u[1]=(-1)-3*x[1]-9*x[0]
    u[2]=(-3)+5*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,2,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(15)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-6*x[1]-3*x[0]
    u[1]=(-2)-8*x[1]-3*x[0]
    u[2]=8-5*x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=18
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-36)-36*x[1]-18*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+4*x[1]+6*x[0]
    u[1]=2-2*x[1]+x[0]
    u[2]=(-2)+8*x[1]+8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,1]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(8-8*x[1]+4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+5*x[1]+5*x[0]
    u[1]=(-9)+6*x[1]+3*x[0]
    u[2]=5+7*x[1]+3*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,2]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-21)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(35+49*x[1]+21*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-8*x[1]-6*x[0]
    u[1]=5-1*x[1]+6*x[0]
    u[2]=(-1)+8*x[1]-3*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=48
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-18)-48*x[1]-36*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-5*x[1]+3*x[0]
    u[1]=(-6)+x[1]-9*x[0]
    u[2]=(-9)+7*x[1]-8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-3)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-18)+3*x[1]-27*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-4*x[1]+7*x[0]
    u[1]=(-8)-1*x[1]+2*x[0]
    u[2]=(-9)-8*x[1]-4*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,2]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=8
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-9)-8*x[1]-4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-9*x[1]-9*x[0]
    u[1]=(-5)+7*x[1]-6*x[0]
    u[2]=(-4)-5*x[1]-2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=18
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-12)-18*x[1]-18*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+3*x[1]-9*x[0]
    u[1]=(-4)-9*x[1]-9*x[0]
    u[2]=8-6*x[1]+6*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,1]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=45
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-20)-45*x[1]-45*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-9*x[1]-6*x[0]
    u[1]=2+6*x[1]-9*x[0]
    u[2]=5+3*x[1]-2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,2]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=16
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(40+24*x[1]-16*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-8*x[1]+x[0]
    u[1]=(-5)-9*x[1]+2*x[0]
    u[2]=1+3*x[1]+5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=16
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(12-16*x[1]+2*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+4*x[1]-6*x[0]
    u[1]=(-6)+5*x[1]+7*x[0]
    u[2]=1+8*x[1]-3*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-15)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-18)+15*x[1]+21*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-3*x[1]-1*x[0]
    u[1]=(-1)-8*x[1]-3*x[0]
    u[2]=(-8)+8*x[1]+4*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,2]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-48)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-48)+48*x[1]+24*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-3*x[1]-5*x[0]
    u[1]=(-6)+6*x[1]+5*x[0]
    u[2]=(-2)+5*x[1]-2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,0]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=5
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(4-3*x[1]-5*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-2*x[1]+3*x[0]
    u[1]=(-2)-3*x[1]-5*x[0]
    u[2]=3+8*x[1]-6*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,1]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=25
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-10)-15*x[1]-25*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-6*x[1]+5*x[0]
    u[1]=5+8*x[1]+3*x[0]
    u[2]=5-9*x[1]+8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,2]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-64)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(40-72*x[1]+64*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-6*x[1]-1*x[0]
    u[1]=6+7*x[1]-3*x[0]
    u[2]=7+6*x[1]-3*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=12
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-6)-12*x[1]-2*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+8*x[1]+3*x[0]
    u[1]=2-9*x[1]-8*x[0]
    u[2]=(-6)-6*x[1]-9*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=9
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(2-9*x[1]-8*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeStrong_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+2*x[1]+8*x[0]
    u[1]=2+7*x[1]-1*x[0]
    u[2]=(-3)+4*x[1]+3*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,2]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-20)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-15)+20*x[1]+15*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-7*x[1]+x[0]
    u[1]=(-7)+5*x[1]-8*x[0]
    u[2]=4-4*x[1]-6*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,0,0]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=7
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-6*x[1]-9*x[0]
    u[1]=(-3)-6*x[1]-8*x[0]
    u[2]=4-2*x[1]-3*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,0,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-6)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-6*x[1]+4*x[0]
    u[1]=(-3)+4*x[1]-6*x[0]
    u[2]=5-4*x[1]+2*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,1,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-36)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+8*x[1]+7*x[0]
    u[1]=1+3*x[1]+8*x[0]
    u[2]=5+x[1]-3*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,1,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=9
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+5*x[1]+5*x[0]
    u[1]=(-4)+7*x[1]-9*x[0]
    u[2]=1+3*x[1]-3*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,2,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-9)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-4*x[1]+x[0]
    u[1]=3-8*x[1]+5*x[0]
    u[2]=(-1)+7*x[1]+2*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,2,1]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=35
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-6*x[1]-7*x[0]
    u[1]=(-8)-8*x[1]+8*x[0]
    u[2]=4+6*x[1]-8*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,0,0]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-35)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-3*x[1]+2*x[0]
    u[1]=2+5*x[1]-2*x[0]
    u[2]=(-3)-4*x[1]-4*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,0,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-24)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-7*x[1]-7*x[0]
    u[1]=6-2*x[1]-5*x[0]
    u[2]=(-5)+4*x[1]-2*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,1,0]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-5)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-3*x[1]-5*x[0]
    u[1]=3+5*x[1]-4*x[0]
    u[2]=7-7*x[1]+2*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,1,1]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=25
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3-4*x[1]-1*x[0]
    u[1]=5-2*x[1]-2*x[0]
    u[2]=(-5)+x[1]+3*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,2,0]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=15
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-7*x[1]+4*x[0]
    u[1]=(-1)+x[1]-6*x[0]
    u[2]=(-8)+4*x[1]-5*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,2,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=4
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-2*x[1]+7*x[0]
    u[1]=(-3)+2*x[1]-7*x[0]
    u[2]=(-7)+4*x[1]+8*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,0,0]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=56
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+3*x[1]-4*x[0]
    u[1]=(-6)+3*x[1]+4*x[0]
    u[2]=(-1)+4*x[1]+8*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,0,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=18
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+x[1]+2*x[0]
    u[1]=(-2)-3*x[1]+2*x[0]
    u[2]=(-1)-9*x[1]+4*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,1,0]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=14
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-7*x[1]-5*x[0]
    u[1]=(-7)-4*x[1]+x[0]
    u[2]=(-6)-4*x[1]+7*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,1,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-28)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp220(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-4*x[1]-9*x[0]
    u[1]=6+7*x[1]-9*x[0]
    u[2]=8-1*x[1]+3*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,2,0]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=24
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Const_typeStrong_comp221(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-4*x[1]-7*x[0]
    u[1]=(-9)+4*x[1]+3*x[0]
    u[2]=8-5*x[1]+6*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,2,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-5)
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-6*x[1]-6*x[0]
    u[1]=4+6*x[1]-5*x[0]
    u[2]=2+4*x[1]+8*x[0]
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[0,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-24)-24*x[1]-24*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+7*x[1]+4*x[0]
    u[1]=4-1*x[1]-4*x[0]
    u[2]=8+2*x[1]-4*x[0]
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[0,1]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=20-5*x[1]-20*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Const_typeStrong_comp02(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-5*x[1]+7*x[0]
    u[1]=(-7)+x[1]+6*x[0]
    u[2]=(-7)-3*x[1]+7*x[0]
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[0,2]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-14)-6*x[1]+14*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+6*x[1]+7*x[0]
    u[1]=6+6*x[1]-1*x[0]
    u[2]=8+x[1]+6*x[0]
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[1,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=14+12*x[1]+14*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+5*x[1]+2*x[0]
    u[1]=(-7)+5*x[1]-9*x[0]
    u[2]=4-1*x[1]+5*x[0]
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[1,1]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-28)+20*x[1]-36*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Const_typeStrong_comp12(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-9*x[1]-8*x[0]
    u[1]=8+5*x[1]+4*x[0]
    u[2]=(-3)-6*x[1]+5*x[0]
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[1,2]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-15)-30*x[1]+25*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Const_typeStrong_comp20(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+2*x[1]-1*x[0]
    u[1]=(-4)+x[1]+7*x[0]
    u[2]=(-6)+7*x[1]-3*x[0]
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[2,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-24)+12*x[1]-6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Const_typeStrong_comp21(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+5*x[1]+8*x[0]
    u[1]=(-4)-4*x[1]-5*x[0]
    u[2]=(-5)+2*x[1]-5*x[0]
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[2,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-4)-4*x[1]-5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Const_typeStrong_comp22(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-8*x[1]-4*x[0]
    u[1]=7-5*x[1]-3*x[0]
    u[2]=(-4)+5*x[1]+6*x[0]
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[2,2]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-16)+20*x[1]+24*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+2*x[1]+3*x[0]
    u[1]=(-4)-8*x[1]-5*x[0]
    u[2]=7-1*x[1]-6*x[0]
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[0,0]=7
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=42+14*x[1]+21*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+4*x[1]+8*x[0]
    u[1]=(-1)+6*x[1]+4*x[0]
    u[2]=(-5)+7*x[1]+2*x[0]
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[0,1]=3
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=(-3)+18*x[1]+12*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Const_typeStrong_comp02(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+5*x[1]+7*x[0]
    u[1]=(-9)-8*x[1]-1*x[0]
    u[2]=7+4*x[1]-4*x[0]
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[0,2]=4
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=28+16*x[1]-16*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-4*x[1]+2*x[0]
    u[1]=(-3)+4*x[1]+2*x[0]
    u[2]=(-8)+2*x[1]-7*x[0]
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[1,0]=1
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=1-4*x[1]+2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+5*x[1]+8*x[0]
    u[1]=4-5*x[1]+6*x[0]
    u[2]=(-1)-5*x[1]-9*x[0]
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[1,1]=1
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=4-5*x[1]+6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Const_typeStrong_comp12(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+7*x[1]-8*x[0]
    u[1]=3+5*x[1]-4*x[0]
    u[2]=(-7)+6*x[1]-1*x[0]
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[1,2]=2
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=(-14)+12*x[1]-2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Const_typeStrong_comp20(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+6*x[1]-8*x[0]
    u[1]=(-5)-7*x[1]+4*x[0]
    u[2]=(-2)+7*x[1]+3*x[0]
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[2,0]=6
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=24+36*x[1]-48*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Const_typeStrong_comp21(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+2*x[1]-8*x[0]
    u[1]=4-9*x[1]-5*x[0]
    u[2]=1+3*x[1]+6*x[0]
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[2,1]=1
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=4-9*x[1]-5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Const_typeStrong_comp22(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+8*x[1]-2*x[0]
    u[1]=(-1)+3*x[1]+6*x[0]
    u[2]=(-8)-5*x[1]-3*x[0]
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[2,2]=5
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=(-40)-25*x[1]-15*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-6*x[1]-3*x[0]
    u[1]=5+5*x[1]-8*x[0]
    u[2]=6+8*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=3
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-3)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+3*x[1]-9*x[0]
    u[1]=8-6*x[1]+4*x[0]
    u[2]=(-8)+x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-3)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(3*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-9*x[1]+3*x[0]
    u[1]=(-9)-5*x[1]+4*x[0]
    u[2]=6+4*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+2*x[1]+8*x[0]
    u[1]=(-5)-8*x[1]+7*x[0]
    u[2]=2-8*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,1,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=8
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-8)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-7*x[1]-8*x[0]
    u[1]=(-4)-3*x[1]-1*x[0]
    u[2]=4+2*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=2
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-2)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+4*x[1]+8*x[0]
    u[1]=7+3*x[1]+3*x[0]
    u[2]=7-9*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,2,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=9
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-9)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+3*x[1]-8*x[0]
    u[1]=(-2)-4*x[1]-8*x[0]
    u[2]=2+5*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,0,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=8
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-8)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+4*x[1]-3*x[0]
    u[1]=3-6*x[1]+x[0]
    u[2]=2+5*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(4*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-6*x[1]-4*x[0]
    u[1]=8+8*x[1]+2*x[0]
    u[2]=8-7*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-2)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(2*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+6*x[1]-4*x[0]
    u[1]=5+5*x[1]-5*x[0]
    u[2]=(-6)+8*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-5)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(5*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-2*x[1]+4*x[0]
    u[1]=8+7*x[1]-9*x[0]
    u[2]=7-8*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,2,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-3)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(3*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp0121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+5*x[1]+2*x[0]
    u[1]=1-1*x[1]+6*x[0]
    u[2]=6-3*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=3
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-3)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-7*x[1]-7*x[0]
    u[1]=(-4)-2*x[1]+8*x[0]
    u[2]=2-2*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=7
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-7)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-1*x[1]-8*x[0]
    u[1]=(-8)-7*x[1]+2*x[0]
    u[2]=3-5*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=1
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-1)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3-9*x[1]+x[0]
    u[1]=3+x[1]-4*x[0]
    u[2]=8+8*x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=4
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-4)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+7*x[1]-7*x[0]
    u[1]=(-4)-1*x[1]-8*x[0]
    u[2]=6+2*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,1,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=1
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-1)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5+3*x[1]-6*x[0]
    u[1]=(-2)+4*x[1]+5*x[0]
    u[2]=(-4)-3*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-4)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3-9*x[1]+2*x[0]
    u[1]=(-5)-1*x[1]+5*x[0]
    u[2]=7-3*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,2,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=3
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-3)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5+8*x[1]-3*x[0]
    u[1]=5-1*x[1]+x[0]
    u[2]=(-8)+4*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,0,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=3
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-3)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-9*x[1]+x[0]
    u[1]=3+x[1]-4*x[0]
    u[2]=(-6)-1*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=9
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-9)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+7*x[1]+5*x[0]
    u[1]=4-8*x[1]+4*x[0]
    u[2]=(-5)+3*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-4)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(4*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-4*x[1]-9*x[0]
    u[1]=3+6*x[1]+7*x[0]
    u[2]=6+x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-6)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(6*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+x[1]-2*x[0]
    u[1]=(-4)+5*x[1]-6*x[0]
    u[2]=(-5)+3*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,2,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=2
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-2)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp1121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-7*x[1]+4*x[0]
    u[1]=(-6)+5*x[1]-7*x[0]
    u[2]=(-4)-8*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=8
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-8)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-9*x[1]-5*x[0]
    u[1]=4-7*x[1]-2*x[0]
    u[2]=5-7*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=5
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-5)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-3*x[1]-8*x[0]
    u[1]=4-9*x[1]-7*x[0]
    u[2]=6+7*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=3
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-3)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+6*x[1]+7*x[0]
    u[1]=(-7)+7*x[1]+4*x[0]
    u[2]=1-6*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-4)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-6*x[1]+x[0]
    u[1]=(-1)-9*x[1]-3*x[0]
    u[2]=(-7)-2*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,1,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=9
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-9)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+6*x[1]-8*x[0]
    u[1]=(-1)+2*x[1]-6*x[0]
    u[2]=3-1*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=5
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-5)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)+x[1]-9*x[0]
    u[1]=(-7)-6*x[1]+4*x[0]
    u[2]=(-5)+3*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,2,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-3)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(3*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-3*x[1]+7*x[0]
    u[1]=1+5*x[1]+5*x[0]
    u[2]=8+6*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,0,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-7)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(7*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+7*x[1]+x[0]
    u[1]=4-3*x[1]-6*x[0]
    u[2]=(-2)-3*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-7)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(7*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+2*x[1]-5*x[0]
    u[1]=8-2*x[1]+4*x[0]
    u[2]=6+6*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-4)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(4*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-2*x[1]-8*x[0]
    u[1]=(-4)-5*x[1]-2*x[0]
    u[2]=(-6)-8*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=5
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-5)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+3*x[1]+5*x[0]
    u[1]=2-1*x[1]+7*x[0]
    u[2]=6+2*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,2,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-5)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(5*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeStrong_comp2121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-1*x[1]-1*x[0]
    u[1]=6+x[1]-4*x[0]
    u[2]=3+4*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-4)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(4*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+3*x[1]+x[0]
    u[1]=6+8*x[1]-2*x[0]
    u[2]=3-2*x[1]+2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=5-3*x[1]-2*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-5)*x[0]+3*x[0]*x[1]+x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-7*x[1]+8*x[0]
    u[1]=(-5)-1*x[1]-6*x[0]
    u[2]=7+6*x[1]-4*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=5+x[1]+12*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-5)*x[0]-1*x[0]*x[1]-6*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+2*x[1]+2*x[0]
    u[1]=6+x[1]+4*x[0]
    u[2]=6+2*x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-6)-2*x[1]+14*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(6*x[0]+2*x[0]*x[1]-7*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5+3*x[1]-9*x[0]
    u[1]=1-8*x[1]-7*x[0]
    u[2]=1+7*x[1]+x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-5)-6*x[1]+9*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(5*x[1]+3*x[1]**2-9*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+8*x[1]-4*x[0]
    u[1]=1-4*x[1]+4*x[0]
    u[2]=(-3)-5*x[1]-3*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-1)+8*x[1]-4*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(x[1]-4*x[1]**2+4*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+8*x[1]-1*x[0]
    u[1]=(-8)+5*x[1]+2*x[0]
    u[2]=(-1)+3*x[1]-5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,2]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=1-6*x[1]+5*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-1)*x[1]+3*x[1]**2-5*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-4*x[1]+6*x[0]
    u[1]=7-6*x[1]+3*x[0]
    u[2]=(-2)-3*x[1]+8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=9+4*x[1]-12*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-9)*x[0]-4*x[0]*x[1]+6*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+3*x[1]-1*x[0]
    u[1]=5+x[1]-5*x[0]
    u[2]=7-3*x[1]-3*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-5)-1*x[1]+10*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(5*x[0]+x[0]*x[1]-5*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-5*x[1]-5*x[0]
    u[1]=(-9)-7*x[1]-7*x[0]
    u[2]=5-9*x[1]-9*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-5)+9*x[1]+18*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(5*x[0]-9*x[0]*x[1]-9*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+7*x[1]+6*x[0]
    u[1]=(-6)-4*x[1]-2*x[0]
    u[2]=3-8*x[1]-9*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=1-14*x[1]-6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-1)*x[1]+7*x[1]**2+6*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-3*x[1]-5*x[0]
    u[1]=(-9)+2*x[1]+x[0]
    u[2]=1+6*x[1]-5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=9-4*x[1]-1*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-9)*x[1]+2*x[1]**2+x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+3*x[1]-1*x[0]
    u[1]=(-1)-9*x[1]+6*x[0]
    u[2]=7+4*x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,2]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)-8*x[1]+7*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(7*x[1]+4*x[1]**2-7*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-1*x[1]+x[0]
    u[1]=(-5)-7*x[1]-2*x[0]
    u[2]=(-4)+6*x[1]+4*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=3+x[1]-2*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-3)*x[0]-1*x[0]*x[1]+x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+2*x[1]-2*x[0]
    u[1]=8+8*x[1]+3*x[0]
    u[2]=(-5)+8*x[1]+8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-8)-8*x[1]-6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(8*x[0]+8*x[0]*x[1]+3*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+4*x[1]+4*x[0]
    u[1]=5+2*x[1]-7*x[0]
    u[2]=1-2*x[1]+8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-1)+2*x[1]-16*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(x[0]-2*x[0]*x[1]+8*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+3*x[1]+2*x[0]
    u[1]=3-3*x[1]-9*x[0]
    u[2]=1+x[1]+2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-8)-6*x[1]-2*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(8*x[1]+3*x[1]**2+2*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-8*x[1]-2*x[0]
    u[1]=6+7*x[1]-5*x[0]
    u[2]=6+x[1]-1*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-6)-14*x[1]+5*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(6*x[1]+7*x[1]**2-5*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeStrong_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-9*x[1]-3*x[0]
    u[1]=1+8*x[1]+8*x[0]
    u[2]=(-5)+x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,2]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=5-2*x[1]+7*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-5)*x[1]+x[1]**2-7*x[0]*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-3*x[1]-9*x[0]
    u[1]=(-1)+6*x[1]-6*x[0]
    u[2]=(-3)+8*x[1]-5*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+x[1]+5*x[0]
    u[1]=5+2*x[1]-1*x[0]
    u[2]=2-3*x[1]-4*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-9*x[1]+5*x[0]
    u[1]=4-2*x[1]+7*x[0]
    u[2]=(-6)-5*x[1]-6*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-3*x[1]+7*x[0]
    u[1]=5+5*x[1]+8*x[0]
    u[2]=6-2*x[1]-7*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-6*x[1]+8*x[0]
    u[1]=(-1)-8*x[1]-7*x[0]
    u[2]=(-8)+2*x[1]+7*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+8*x[1]+3*x[0]
    u[1]=(-5)+2*x[1]-4*x[0]
    u[2]=4-7*x[1]+8*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[0,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-7)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+8*x[1]-9*x[0]
    u[1]=(-4)+7*x[1]-9*x[0]
    u[2]=5+3*x[1]+8*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+5*x[1]-4*x[0]
    u[1]=(-4)+6*x[1]+6*x[0]
    u[2]=(-2)-2*x[1]-6*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3-5*x[1]+5*x[0]
    u[1]=7-1*x[1]-5*x[0]
    u[2]=2-3*x[1]+8*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+4*x[1]+3*x[0]
    u[1]=8+6*x[1]-5*x[0]
    u[2]=5-3*x[1]-3*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+3*x[1]-1*x[0]
    u[1]=(-7)-2*x[1]+4*x[0]
    u[2]=6-3*x[1]+5*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+2*x[1]-1*x[0]
    u[1]=(-9)+2*x[1]+6*x[0]
    u[2]=(-2)+5*x[1]+4*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[1,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-7*x[1]+5*x[0]
    u[1]=7+6*x[1]+5*x[0]
    u[2]=(-8)-8*x[1]-1*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+3*x[1]-1*x[0]
    u[1]=(-8)+5*x[1]+5*x[0]
    u[2]=8+6*x[1]-4*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=3*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-1*x[1]+4*x[0]
    u[1]=6-1*x[1]+x[0]
    u[2]=(-4)+3*x[1]+2*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+7*x[1]-7*x[0]
    u[1]=(-8)+x[1]-8*x[0]
    u[2]=5-5*x[1]+7*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp220(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-2*x[1]-5*x[0]
    u[1]=5-3*x[1]+7*x[0]
    u[2]=1-5*x[1]-1*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_C_Vario_typeStrong_comp221(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+3*x[1]+x[0]
    u[1]=5-3*x[1]-4*x[0]
    u[2]=6-4*x[1]-2*x[0]
    C_test=Data(0.,(3,3,2),Function(self.domain))
    C_test[2,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-4)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C=C_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=4
    u[2]=(-5)
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2
    u[1]=2
    u[2]=(-2)
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Vario_typeStrong_comp02(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=(-5)
    u[2]=(-9)
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=7
    u[2]=5
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=1
    u[2]=7
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[1,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Vario_typeStrong_comp12(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=(-7)
    u[2]=6
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[1,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Vario_typeStrong_comp20(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=3
    u[2]=3
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-6)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Vario_typeStrong_comp21(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=7
    u[2]=(-3)
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[2,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_D_Vario_typeStrong_comp22(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5
    u[1]=(-8)
    u[2]=(-2)
    D_test=Data(0.,(3,3),Function(self.domain))
    D_test[2,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-2)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D=D_test, Y=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=(-9)
    u[2]=(-9)
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[0,0]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=(-5)
    u[2]=(-3)
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[0,1]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Vario_typeStrong_comp02(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=(-8)
    u[2]=2
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[0,2]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=(-6)
    u[2]=3
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[1,0]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=2
    u[2]=7
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[1,1]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Vario_typeStrong_comp12(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)
    u[1]=1
    u[2]=4
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[1,2]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Vario_typeStrong_comp20(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=3
    u[2]=(-3)
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[2,0]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Vario_typeStrong_comp21(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=8
    u[2]=4
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[2,1]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_Vario_typeStrong_comp22(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=8
    u[2]=(-4)
    d_test=Data(0.,(3,3),FunctionOnBoundary(self.domain))
    d_test[2,2]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d=d_test, y=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-3*x[1]+7*x[0]
    u[1]=7+7*x[1]-2*x[0]
    u[2]=1-6*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,0,0]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=56
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-6*x[1]-5*x[0]
    u[1]=(-9)-7*x[1]-9*x[0]
    u[2]=7-6*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,0,1]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-12)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+4*x[1]-6*x[0]
    u[1]=(-6)+5*x[1]+6*x[0]
    u[2]=(-2)-8*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,1,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=30
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+x[1]-7*x[0]
    u[1]=(-4)-7*x[1]-9*x[0]
    u[2]=(-8)-4*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,1,1]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-21)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-7*x[1]-9*x[0]
    u[1]=(-3)-2*x[1]-4*x[0]
    u[2]=(-1)+6*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,2,0]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-6)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-6*x[1]+8*x[0]
    u[1]=(-8)-5*x[1]-6*x[0]
    u[2]=2+5*x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,2,1]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=10
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-1*x[1]-1*x[0]
    u[1]=5+2*x[1]+4*x[0]
    u[2]=(-8)-2*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,0,0]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-3)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+7*x[1]-8*x[0]
    u[1]=5-4*x[1]+x[0]
    u[2]=2+2*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,0,1]=7
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=49
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+5*x[1]+7*x[0]
    u[1]=(-2)-2*x[1]-4*x[0]
    u[2]=7-2*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,1,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-20)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+5*x[1]-6*x[0]
    u[1]=2+2*x[1]+6*x[0]
    u[2]=5+8*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,1,1]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=4
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5+7*x[1]-2*x[0]
    u[1]=(-4)-2*x[1]-2*x[0]
    u[2]=7-6*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,2,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=35
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp0121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-3*x[1]+4*x[0]
    u[1]=(-8)+4*x[1]-8*x[0]
    u[2]=(-5)-8*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,2,1]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-8)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-5*x[1]+4*x[0]
    u[1]=(-1)-1*x[1]-5*x[0]
    u[2]=(-1)+8*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,0,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=20
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-1*x[1]+2*x[0]
    u[1]=2+3*x[1]-9*x[0]
    u[2]=3+7*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,0,1]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-2)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+8*x[1]-6*x[0]
    u[1]=5-9*x[1]-8*x[0]
    u[2]=4-8*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,1,0]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-16)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+5*x[1]+2*x[0]
    u[1]=(-9)+x[1]-7*x[0]
    u[2]=(-4)-5*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,1,1]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=3
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+5*x[1]-9*x[0]
    u[1]=2-9*x[1]-9*x[0]
    u[2]=(-4)+7*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,2,0]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=6
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-1*x[1]-5*x[0]
    u[1]=2+7*x[1]-4*x[0]
    u[2]=(-2)-6*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,2,1]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-30)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-6*x[1]-5*x[0]
    u[1]=3+3*x[1]-9*x[0]
    u[2]=3+7*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,0,0]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-30)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+5*x[1]+x[0]
    u[1]=8+4*x[1]+6*x[0]
    u[2]=(-1)+8*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,0,1]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=25
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+2*x[1]-1*x[0]
    u[1]=(-8)+5*x[1]-1*x[0]
    u[2]=4-7*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,1,0]=7
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-7)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-6*x[1]+8*x[0]
    u[1]=(-6)-9*x[1]+8*x[0]
    u[2]=5+x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,1,1]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-36)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+2*x[1]+2*x[0]
    u[1]=(-9)+6*x[1]-3*x[0]
    u[2]=6-1*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,2,0]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-72)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp1121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-5*x[1]-2*x[0]
    u[1]=5+2*x[1]+6*x[0]
    u[2]=(-7)+8*x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,2,1]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=32
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-5*x[1]-8*x[0]
    u[1]=2-9*x[1]+5*x[0]
    u[2]=4-3*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,0,0]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-64)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-5*x[1]-1*x[0]
    u[1]=1+2*x[1]+5*x[0]
    u[2]=(-7)-4*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,0,1]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-30)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-1*x[1]-3*x[0]
    u[1]=(-3)+8*x[1]-6*x[0]
    u[2]=(-6)-7*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,1,0]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-18)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+7*x[1]-6*x[0]
    u[1]=3+x[1]-7*x[0]
    u[2]=(-9)-9*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,1,1]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=1
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-7*x[1]-9*x[0]
    u[1]=(-1)-9*x[1]-5*x[0]
    u[2]=(-7)+8*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,2,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=40
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+5*x[1]+x[0]
    u[1]=8+5*x[1]-9*x[0]
    u[2]=2+2*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,2,1]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=4
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+6*x[1]-4*x[0]
    u[1]=(-7)-4*x[1]+2*x[0]
    u[2]=8+4*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,0,0]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-24)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-8*x[1]-9*x[0]
    u[1]=8+3*x[1]+7*x[0]
    u[2]=7+3*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,0,1]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-32)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-4*x[1]-6*x[0]
    u[1]=(-5)+7*x[1]-4*x[0]
    u[2]=6-2*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,1,0]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-32)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-2*x[1]+4*x[0]
    u[1]=6-7*x[1]-2*x[0]
    u[2]=4+5*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,1,1]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-7)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+4*x[1]+2*x[0]
    u[1]=3+x[1]+5*x[0]
    u[2]=(-1)-3*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,2,0]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=18
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Const_typeWeak_comp2121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-2*x[1]-1*x[0]
    u[1]=(-9)-3*x[1]+6*x[0]
    u[2]=(-1)-4*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,2,1]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-32)
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+6*x[1]-6*x[0]
    u[1]=1+8*x[1]-4*x[0]
    u[2]=6-8*x[1]-5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-30)+30*x[1]-30*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+4*x[1]-1*x[0]
    u[1]=(-4)-9*x[1]+5*x[0]
    u[2]=(-5)-7*x[1]+5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,1]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-20)-45*x[1]+25*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-8*x[1]+3*x[0]
    u[1]=3+5*x[1]+8*x[0]
    u[2]=5+4*x[1]-1*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,2]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=30+24*x[1]-6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-3*x[1]+2*x[0]
    u[1]=1-2*x[1]+2*x[0]
    u[2]=(-8)+2*x[1]+x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,0]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=10-6*x[1]+4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+8*x[1]-8*x[0]
    u[1]=(-7)+4*x[1]+7*x[0]
    u[2]=3-5*x[1]-9*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,1]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-42)+24*x[1]+42*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+4*x[1]-3*x[0]
    u[1]=2-3*x[1]+6*x[0]
    u[2]=(-7)+3*x[1]-4*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,2]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-7)+3*x[1]-4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-8*x[1]-4*x[0]
    u[1]=(-8)+5*x[1]-1*x[0]
    u[2]=(-7)+5*x[1]+5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,0]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-3)-24*x[1]-12*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+x[1]+6*x[0]
    u[1]=5-1*x[1]+6*x[0]
    u[2]=6-3*x[1]+7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,1]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=15-3*x[1]+18*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-7*x[1]-2*x[0]
    u[1]=3+4*x[1]-9*x[0]
    u[2]=4-2*x[1]+8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,2]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=16-8*x[1]+32*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+4*x[1]+2*x[0]
    u[1]=4+7*x[1]-7*x[0]
    u[2]=3-6*x[1]-8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,0]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-2)+8*x[1]+4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-9*x[1]+4*x[0]
    u[1]=8-7*x[1]-4*x[0]
    u[2]=(-2)-7*x[1]+7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,1]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=64-56*x[1]-32*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+6*x[1]+4*x[0]
    u[1]=(-1)-1*x[1]-2*x[0]
    u[2]=(-7)+3*x[1]-8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,2]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-7)+3*x[1]-8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-3*x[1]-2*x[0]
    u[1]=(-1)+4*x[1]+6*x[0]
    u[2]=(-3)-7*x[1]+5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,0]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=20-12*x[1]-8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-6*x[1]-8*x[0]
    u[1]=(-8)+4*x[1]-4*x[0]
    u[2]=8+x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,1]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-48)+24*x[1]-24*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-9*x[1]+8*x[0]
    u[1]=3+6*x[1]-9*x[0]
    u[2]=6-3*x[1]+8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,2]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=36-18*x[1]+48*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-7*x[1]+3*x[0]
    u[1]=(-5)-4*x[1]+6*x[0]
    u[2]=6+3*x[1]-5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,0]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=1-7*x[1]+3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+2*x[1]-7*x[0]
    u[1]=1-2*x[1]-7*x[0]
    u[2]=7-4*x[1]+x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,1]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=3-6*x[1]-21*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeWeak_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+4*x[1]+4*x[0]
    u[1]=(-8)-6*x[1]-9*x[0]
    u[2]=(-4)-6*x[1]-9*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,2]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-16)-24*x[1]-36*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-3*x[1]-3*x[0]
    u[1]=7-6*x[1]+6*x[0]
    u[2]=8-6*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-1*x[1]-8*x[0]
    u[1]=6-5*x[1]-1*x[0]
    u[2]=(-6)-7*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+4*x[1]-5*x[0]
    u[1]=(-9)+2*x[1]+5*x[0]
    u[2]=(-1)+8*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,1,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-1*x[1]-9*x[0]
    u[1]=5+4*x[1]+5*x[0]
    u[2]=(-8)+3*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,1,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-3*x[1]+4*x[0]
    u[1]=(-5)+x[1]+4*x[0]
    u[2]=(-3)+x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,2,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-2)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+5*x[1]+x[0]
    u[1]=8-9*x[1]-5*x[0]
    u[2]=2-6*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,0,2,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-6)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+2*x[1]-5*x[0]
    u[1]=(-8)+2*x[1]-1*x[0]
    u[2]=(-9)-3*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,0,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-5)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-1*x[1]-3*x[0]
    u[1]=(-1)-3*x[1]-9*x[0]
    u[2]=(-2)+6*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,0,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-1)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+6*x[1]-6*x[0]
    u[1]=2+7*x[1]-2*x[0]
    u[2]=7+3*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-2)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-7*x[1]+2*x[0]
    u[1]=1-4*x[1]-5*x[0]
    u[2]=2-7*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-4)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+8*x[1]-4*x[0]
    u[1]=(-4)-1*x[1]+4*x[0]
    u[2]=(-6)-3*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,2,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=8*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp0121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+6*x[1]-4*x[0]
    u[1]=2-7*x[1]-9*x[0]
    u[2]=(-2)-5*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[0,1,2,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-5)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-8*x[1]-1*x[0]
    u[1]=4+3*x[1]-8*x[0]
    u[2]=(-7)-8*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-7*x[1]+8*x[0]
    u[1]=2-1*x[1]-9*x[0]
    u[2]=3+5*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+x[1]-9*x[0]
    u[1]=1+3*x[1]+2*x[0]
    u[2]=1-3*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,1,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-2*x[1]-4*x[0]
    u[1]=7-9*x[1]-9*x[0]
    u[2]=(-5)-2*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,1,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+5*x[1]-9*x[0]
    u[1]=(-6)+6*x[1]-3*x[0]
    u[2]=3+8*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,2,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5+5*x[1]-8*x[0]
    u[1]=7+6*x[1]-3*x[0]
    u[2]=(-8)-4*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,0,2,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+4*x[1]-3*x[0]
    u[1]=(-2)+5*x[1]-5*x[0]
    u[2]=1-4*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,0,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-3)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-4*x[1]-9*x[0]
    u[1]=8-8*x[1]-2*x[0]
    u[2]=7+5*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,0,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-4)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-6*x[1]+7*x[0]
    u[1]=(-7)+6*x[1]+5*x[0]
    u[2]=7+2*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-8*x[1]-7*x[0]
    u[1]=6+7*x[1]+8*x[0]
    u[2]=(-2)+8*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=7*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-7*x[1]+4*x[0]
    u[1]=7-3*x[1]-5*x[0]
    u[2]=(-1)+5*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,2,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-8)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp1121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-3*x[1]+5*x[0]
    u[1]=7+6*x[1]-9*x[0]
    u[2]=(-1)-4*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[1,1,2,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-4)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-8*x[1]-9*x[0]
    u[1]=(-8)-4*x[1]-8*x[0]
    u[2]=1-4*x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+7*x[1]+3*x[0]
    u[1]=7-2*x[1]+6*x[0]
    u[2]=4+8*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+6*x[1]+3*x[0]
    u[1]=(-2)+8*x[1]+8*x[0]
    u[2]=(-1)+8*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,1,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+5*x[1]-8*x[0]
    u[1]=5+8*x[1]+6*x[0]
    u[2]=(-1)-4*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,1,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+3*x[1]-4*x[0]
    u[1]=(-1)-2*x[1]+8*x[0]
    u[2]=(-9)-6*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,2,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-2*x[1]-7*x[0]
    u[1]=(-9)+4*x[1]+7*x[0]
    u[2]=6+4*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,0,2,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+x[1]-5*x[0]
    u[1]=(-4)-7*x[1]+7*x[0]
    u[2]=(-2)+6*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,0,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-5)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-1*x[1]+7*x[0]
    u[1]=8+8*x[1]+2*x[0]
    u[2]=6+4*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,0,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-1)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-8*x[1]+4*x[0]
    u[1]=6+8*x[1]-9*x[0]
    u[2]=(-4)-4*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-9)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-7*x[1]-7*x[0]
    u[1]=2+8*x[1]+5*x[0]
    u[2]=(-8)-6*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=8*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+2*x[1]+5*x[0]
    u[1]=(-5)+8*x[1]-4*x[0]
    u[2]=(-1)+2*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,2,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_A_Vario_typeWeak_comp2121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+5*x[1]-7*x[0]
    u[1]=(-2)+6*x[1]+5*x[0]
    u[2]=2-1*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),Function(self.domain))
    A_test[2,1,2,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-1)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A=A_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=4
    u[2]=2
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)
    u[1]=1
    u[2]=4
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)
    u[1]=(-8)
    u[2]=6
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,2]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2
    u[1]=(-7)
    u[2]=(-2)
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=2*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=7
    u[2]=(-9)
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=7*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=1
    u[2]=5
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,2]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=(-8)
    u[2]=7
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=(-6)
    u[2]=4
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-6)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=4
    u[2]=(-8)
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,2]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=1
    u[2]=3
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=8*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=(-4)
    u[2]=(-6)
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-4)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2
    u[1]=(-5)
    u[2]=7
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,2]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=7*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)
    u[1]=4
    u[2]=7
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)
    u[1]=5
    u[2]=(-9)
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=(-9)
    u[2]=(-9)
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,2]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=(-3)
    u[2]=7
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=8*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=(-6)
    u[2]=5
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-6)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeWeak_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=(-3)
    u[2]=(-8)
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,2]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-8)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, X=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=(-1)+2*x[1]+6*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[0,0]=5
    Y_test=0
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[0]*(30)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=7-1*x[1]-8*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[0,1]=6
    Y_test=0
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[0]*((-6))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=(-7)+3*x[1]+3*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[1,0]=5
    Y_test=0
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[1]*(15)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=(-8)+7*x[1]+3*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[1,1]=2
    Y_test=0
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[1]*(14)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_B_Const_typeStrong_comp0(self):
    x=self.domain.getX()
    u=(-5)
    B_test=Data(0.,(2,),ReducedFunction(self.domain))
    B_test[0]=1
    Y_test=0
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[0]*((-5))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_B_Const_typeStrong_comp1(self):
    x=self.domain.getX()
    u=(-7)
    B_test=Data(0.,(2,),ReducedFunction(self.domain))
    B_test[1]=7
    Y_test=0
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[1]*((-49))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_C_Const_typeStrong_comp0(self):
    x=self.domain.getX()
    u=(-2)-4*x[1]+2*x[0]
    C_test=Data(0.,(2,),ReducedFunction(self.domain))
    C_test[0]=3
    Y_test=6
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_C_Const_typeStrong_comp1(self):
    x=self.domain.getX()
    u=(-6)+4*x[1]-2*x[0]
    C_test=Data(0.,(2,),ReducedFunction(self.domain))
    C_test[1]=2
    Y_test=8
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_D_Const_typeStrong(self):
    x=self.domain.getX()
    u=(-8)-7*x[1]+4*x[0]
    D_test=Data(5,(),ReducedFunction(self.domain))
    Y_test=(-40)-35*x[1]+20*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_d_Const_typeStrong(self):
    x=self.domain.getX()
    u=4+7*x[1]+3*x[0]
    d_test=Data(8,(),ReducedFunctionOnBoundary(self.domain))
    y_test=32+56*x[1]+24*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=(-5)+5*x[1]-1*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[0,0]=x[0]
    Y_test=1
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[0]*((-1)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=2-7*x[1]+2*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[0,1]=x[0]
    Y_test=7
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[0]*((-7)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=8-4*x[1]-1*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[1,0]=x[1]
    Y_test=1
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[1]*((-1)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=(-6)+8*x[1]-2*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[1,1]=x[1]
    Y_test=(-8)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[1]*(8*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_B_Vario_typeStrong_comp0(self):
    x=self.domain.getX()
    u=(-7)
    B_test=Data(0.,(2,),ReducedFunction(self.domain))
    B_test[0]=x[0]
    Y_test=7
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[0]*((-7)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_B_Vario_typeStrong_comp1(self):
    x=self.domain.getX()
    u=(-7)
    B_test=Data(0.,(2,),ReducedFunction(self.domain))
    B_test[1]=x[1]
    Y_test=7
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=n[1]*((-7)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_C_Vario_typeStrong_comp0(self):
    x=self.domain.getX()
    u=5-7*x[1]-8*x[0]
    C_test=Data(0.,(2,),ReducedFunction(self.domain))
    C_test[0]=x[0]
    Y_test=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_C_Vario_typeStrong_comp1(self):
    x=self.domain.getX()
    u=8-2*x[1]+2*x[0]
    C_test=Data(0.,(2,),ReducedFunction(self.domain))
    C_test[1]=x[1]
    Y_test=(-2)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_D_Vario_typeStrong(self):
    x=self.domain.getX()
    u=(-8)
    D_test=ReducedFunction(self.domain).getX()[0]
    Y_test=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_d_Vario_typeStrong(self):
    x=self.domain.getX()
    u=3
    d_test=interpolate(x[0],ReducedFunctionOnBoundary(self.domain))
    y_test=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Const_typeWeak_comp00(self):
    x=self.domain.getX()
    u=8-1*x[1]-6*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[0,0]=1
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=(-6)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Const_typeWeak_comp01(self):
    x=self.domain.getX()
    u=(-1)+5*x[1]-3*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[0,1]=4
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=20
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Const_typeWeak_comp10(self):
    x=self.domain.getX()
    u=6+3*x[1]-2*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[1,0]=7
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=(-14)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Const_typeWeak_comp11(self):
    x=self.domain.getX()
    u=7-9*x[1]-2*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[1,1]=7
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=(-63)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_B_Const_typeWeak_comp0(self):
    x=self.domain.getX()
    u=6
    B_test=Data(0.,(2,),ReducedFunction(self.domain))
    B_test[0]=1
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=6
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_B_Const_typeWeak_comp1(self):
    x=self.domain.getX()
    u=(-6)
    B_test=Data(0.,(2,),ReducedFunction(self.domain))
    B_test[1]=2
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=(-12)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Vario_typeWeak_comp00(self):
    x=self.domain.getX()
    u=6-8*x[1]-9*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[0,0]=x[0]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Vario_typeWeak_comp01(self):
    x=self.domain.getX()
    u=7-5*x[1]-1*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[0,1]=x[0]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Vario_typeWeak_comp10(self):
    x=self.domain.getX()
    u=7-5*x[1]+2*x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[1,0]=x[1]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=2*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_A_Vario_typeWeak_comp11(self):
    x=self.domain.getX()
    u=6-8*x[1]+x[0]
    A_test=Data(0.,(2,2),ReducedFunction(self.domain))
    A_test[1,1]=x[1]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=(-8)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_B_Vario_typeWeak_comp0(self):
    x=self.domain.getX()
    u=(-4)
    B_test=Data(0.,(2,),ReducedFunction(self.domain))
    B_test[0]=x[0]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[0]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_B_Vario_typeWeak_comp1(self):
    x=self.domain.getX()
    u=4
    B_test=Data(0.,(2,),ReducedFunction(self.domain))
    B_test[1]=x[1]
    X_test=Data(0.,(2,),ContinuousFunction(self.domain))
    X_test[1]=4*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)-4*x[1]+8*x[0]
    u[1]=1+5*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,0,0]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(48)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2-5*x[1]-1*x[0]
    u[1]=(-5)-5*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,0,1]=8
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-40))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)-1*x[1]+8*x[0]
    u[1]=(-2)-2*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,1,0]=5
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(20)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)-8*x[1]-8*x[0]
    u[1]=(-3)-6*x[1]+6*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,1,1]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-6))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8+3*x[1]+7*x[0]
    u[1]=(-8)+2*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,0,0]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(28)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)-9*x[1]-8*x[0]
    u[1]=7-7*x[1]+8*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,0,1]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-9))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1-8*x[1]+4*x[0]
    u[1]=6-6*x[1]-2*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,1,0]=5
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-10))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+5*x[1]+8*x[0]
    u[1]=(-3)+3*x[1]-4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,1,1]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(3)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1-1*x[1]-5*x[0]
    u[1]=4+2*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,0,0]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-10))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)+6*x[1]-7*x[0]
    u[1]=8+8*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,0,1]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(36)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)+6*x[1]+x[0]
    u[1]=(-7)-9*x[1]-4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,1,0]=8
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-32))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)+x[1]-4*x[0]
    u[1]=5-1*x[1]+5*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,1,1]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-4))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)+4*x[1]+5*x[0]
    u[1]=2+8*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,0,0]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(5)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-5*x[1]+6*x[0]
    u[1]=4+4*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,0,1]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-20))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)+3*x[1]+x[0]
    u[1]=1-8*x[1]-1*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,1,0]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-3))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeStrong_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-1*x[1]+5*x[0]
    u[1]=6+6*x[1]+x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,1,1]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(42)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=2
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,0,0]=8
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(48)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=(-5)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,0,1]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-35))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)
    u[1]=(-2)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,1,0]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-54))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=5
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,1,1]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(30)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=(-6)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,0,0]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-12))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=(-7)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,0,1]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-21))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=7
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,1,0]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-32))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=(-4)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,1,1]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-16))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Const_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)-1*x[1]-4*x[0]
    u[1]=(-5)+x[1]+8*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[0,0,0]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-8)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Const_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)+3*x[1]-5*x[0]
    u[1]=4-3*x[1]+4*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[0,0,1]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=21
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Const_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)+4*x[1]+8*x[0]
    u[1]=1+8*x[1]-1*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[0,1,0]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-7)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Const_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1-1*x[1]+3*x[0]
    u[1]=6+4*x[1]-6*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[0,1,1]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=8
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Const_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5-3*x[1]+6*x[0]
    u[1]=(-7)-3*x[1]-9*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[1,0,0]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=36
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Const_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)-2*x[1]-2*x[0]
    u[1]=(-1)-2*x[1]+8*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[1,0,1]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-6)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Const_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)-8*x[1]+2*x[0]
    u[1]=3+7*x[1]-6*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[1,1,0]=6
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-36)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Const_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7+4*x[1]+4*x[0]
    u[1]=(-8)+8*x[1]+8*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[1,1,1]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=32
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_D_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3-9*x[1]+6*x[0]
    u[1]=(-3)+6*x[1]-3*x[0]
    D_test=Data(0.,(2,2),ReducedFunction(self.domain))
    D_test[0,0]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=9-27*x[1]+18*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_D_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)+2*x[1]-5*x[0]
    u[1]=(-5)-8*x[1]-2*x[0]
    D_test=Data(0.,(2,2),ReducedFunction(self.domain))
    D_test[0,1]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-10)-16*x[1]-4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_D_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)+5*x[1]+x[0]
    u[1]=(-5)+x[1]+3*x[0]
    D_test=Data(0.,(2,2),ReducedFunction(self.domain))
    D_test[1,0]=3
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-9)+15*x[1]+3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_D_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)+4*x[1]-8*x[0]
    u[1]=(-7)-7*x[1]+4*x[0]
    D_test=Data(0.,(2,2),ReducedFunction(self.domain))
    D_test[1,1]=4
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-28)-28*x[1]+16*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1-8*x[1]-1*x[0]
    u[1]=6-1*x[1]+2*x[0]
    d_test=Data(0.,(2,2),ReducedFunctionOnBoundary(self.domain))
    d_test[0,0]=3
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[0]=3-24*x[1]-3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)-3*x[1]+8*x[0]
    u[1]=(-3)+7*x[1]-5*x[0]
    d_test=Data(0.,(2,2),ReducedFunctionOnBoundary(self.domain))
    d_test[0,1]=2
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[0]=(-6)+14*x[1]-10*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)-6*x[1]-7*x[0]
    u[1]=(-2)+6*x[1]+8*x[0]
    d_test=Data(0.,(2,2),ReducedFunctionOnBoundary(self.domain))
    d_test[1,0]=3
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[1]=(-24)-18*x[1]-21*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)+8*x[1]-4*x[0]
    u[1]=6+7*x[1]+6*x[0]
    d_test=Data(0.,(2,2),ReducedFunctionOnBoundary(self.domain))
    d_test[1,1]=7
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[1]=42+49*x[1]+42*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)-9*x[1]+3*x[0]
    u[1]=(-5)-7*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-3)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(3*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+7*x[1]+7*x[0]
    u[1]=(-1)+x[1]+3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-7)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(7*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8+x[1]+6*x[0]
    u[1]=(-3)+3*x[1]+2*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-2)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(2*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)+x[1]-2*x[0]
    u[1]=(-8)-6*x[1]-2*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,1,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=6
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-6)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)-5*x[1]-8*x[0]
    u[1]=5-1*x[1]-5*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,0,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=8
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-8)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4-1*x[1]+8*x[0]
    u[1]=5-4*x[1]-2*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,0,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=1
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-1)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)-5*x[1]-1*x[0]
    u[1]=(-6)-7*x[1]-7*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=7
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-7)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4-2*x[1]-1*x[0]
    u[1]=8-2*x[1]-8*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=2
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-2)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)+2*x[1]-5*x[0]
    u[1]=(-8)-4*x[1]-4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=5
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-5)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)+7*x[1]-6*x[0]
    u[1]=(-6)-5*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(7*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)-5*x[1]+7*x[0]
    u[1]=(-8)-3*x[1]-6*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=6
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-6)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8+2*x[1]+7*x[0]
    u[1]=8+8*x[1]-4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,1,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-8)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(8*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)-8*x[1]-1*x[0]
    u[1]=(-1)-4*x[1]-5*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,0,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=1
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-1)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)-2*x[1]+x[0]
    u[1]=3+4*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,0,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=2
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-2)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)-4*x[1]-6*x[0]
    u[1]=8-8*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=9
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-9)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeStrong_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4-8*x[1]+x[0]
    u[1]=(-6)-4*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=4
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-4)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=(-7)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-1)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=(-6)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=6
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-6)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)
    u[1]=(-9)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=5
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-5)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=3
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-3)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(3*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=(-8)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-8)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(8*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)
    u[1]=(-3)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=3
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-3)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=(-1)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-1)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2
    u[1]=(-4)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=4
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-4)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Vario_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)+4*x[1]-2*x[0]
    u[1]=(-3)-8*x[1]+x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[0,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-2)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Vario_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4+8*x[1]-5*x[0]
    u[1]=(-1)+4*x[1]+4*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[0,0,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=8*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Vario_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)-2*x[1]+x[0]
    u[1]=(-3)+3*x[1]-4*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[0,1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Vario_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1-8*x[1]-1*x[0]
    u[1]=(-9)+7*x[1]-8*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[0,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=7*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Vario_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)-7*x[1]-9*x[0]
    u[1]=(-4)-9*x[1]-2*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[1,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Vario_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2+3*x[1]-5*x[0]
    u[1]=6+5*x[1]+4*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[1,0,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=3*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Vario_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2+3*x[1]-2*x[0]
    u[1]=4-7*x[1]-7*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[1,1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_C_Vario_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+4*x[1]-2*x[0]
    u[1]=2-5*x[1]-8*x[0]
    C_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    C_test[1,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-5)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_D_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=3
    D_test=Data(0.,(2,2),ReducedFunction(self.domain))
    D_test[0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_D_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=4
    D_test=Data(0.,(2,2),ReducedFunction(self.domain))
    D_test[0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_D_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=(-7)
    D_test=Data(0.,(2,2),ReducedFunction(self.domain))
    D_test[1,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_D_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=(-2)
    D_test=Data(0.,(2,2),ReducedFunction(self.domain))
    D_test[1,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-2)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=4
    d_test=Data(0.,(2,2),ReducedFunctionOnBoundary(self.domain))
    d_test[0,0]=x[0]
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[0]=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=(-3)
    d_test=Data(0.,(2,2),ReducedFunctionOnBoundary(self.domain))
    d_test[0,1]=x[0]
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=1
    d_test=Data(0.,(2,2),ReducedFunctionOnBoundary(self.domain))
    d_test[1,0]=x[0]
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[1]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=1
    d_test=Data(0.,(2,2),ReducedFunctionOnBoundary(self.domain))
    d_test[1,1]=x[0]
    y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_test[1]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2+8*x[1]+8*x[0]
    u[1]=1-9*x[1]-2*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,0,0]=2
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=16
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3-8*x[1]+6*x[0]
    u[1]=(-4)-3*x[1]-8*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,0,1]=5
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-40)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5-4*x[1]+4*x[0]
    u[1]=(-6)+3*x[1]+x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,1,0]=4
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=4
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5+3*x[1]-8*x[0]
    u[1]=(-9)+6*x[1]+6*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,1,1]=1
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=6
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1-8*x[1]-7*x[0]
    u[1]=(-7)-3*x[1]+5*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,0,0]=5
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-35)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-7*x[1]+8*x[0]
    u[1]=4-9*x[1]+7*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,0,1]=3
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-21)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-4)-7*x[1]-8*x[0]
    u[1]=(-7)+x[1]+6*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,1,0]=3
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=18
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6-6*x[1]+5*x[0]
    u[1]=8-5*x[1]+x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,1,1]=8
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-40)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2-5*x[1]+6*x[0]
    u[1]=(-2)-9*x[1]+2*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,0,0]=6
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=36
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)+5*x[1]-5*x[0]
    u[1]=6-9*x[1]-6*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,0,1]=1
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=5
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+6*x[1]+5*x[0]
    u[1]=(-7)+x[1]+3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,1,0]=4
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=12
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5+x[1]-1*x[0]
    u[1]=(-7)-5*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,1,1]=4
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-20)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)+x[1]+3*x[0]
    u[1]=1+7*x[1]-2*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,0,0]=5
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=15
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)-7*x[1]-6*x[0]
    u[1]=6-8*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,0,1]=6
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-42)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)+6*x[1]-1*x[0]
    u[1]=(-9)-4*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,1,0]=7
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-21)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Const_typeWeak_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)-8*x[1]-6*x[0]
    u[1]=(-9)+8*x[1]-5*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,1,1]=6
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=48
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeWeak_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)
    u[1]=(-3)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,0,0]=1
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-9)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeWeak_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=3
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,0,1]=6
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=18
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeWeak_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5
    u[1]=6
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,1,0]=5
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=25
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeWeak_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=1
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,1,1]=3
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=3
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeWeak_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=6
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,0,0]=6
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=6
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeWeak_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=(-4)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,0,1]=1
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-4)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeWeak_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=8
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,1,0]=2
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-12)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Const_typeWeak_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=(-9)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,1,1]=3
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-27)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1-1*x[1]+x[0]
    u[1]=7+4*x[1]+7*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,0,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8-3*x[1]-6*x[0]
    u[1]=3-2*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,0,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7+7*x[1]-2*x[0]
    u[1]=(-1)+5*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,1,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+7*x[1]-9*x[0]
    u[1]=(-4)-8*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,0,1,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6+5*x[1]-3*x[0]
    u[1]=(-1)+3*x[1]-4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,0,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-3)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)-1*x[1]-9*x[0]
    u[1]=8+5*x[1]+6*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,0,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-1)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-7*x[1]+6*x[0]
    u[1]=8+2*x[1]-5*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,1,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-5)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5+4*x[1]+x[0]
    u[1]=2+4*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[0,1,1,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=4*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-9)-9*x[1]-3*x[0]
    u[1]=8-4*x[1]-6*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,0,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2-9*x[1]-6*x[0]
    u[1]=(-9)-6*x[1]-9*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,0,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)-3*x[1]-9*x[0]
    u[1]=(-7)+6*x[1]+6*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,1,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=2-5*x[1]-8*x[0]
    u[1]=(-9)-5*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,0,1,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7-1*x[1]-9*x[0]
    u[1]=5+7*x[1]+4*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,0,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-9)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)+4*x[1]-2*x[0]
    u[1]=7+4*x[1]-3*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,0,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=4*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-2)-5*x[1]+4*x[0]
    u[1]=3+7*x[1]+5*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,1,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_A_Vario_typeWeak_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)+2*x[1]+x[0]
    u[1]=(-6)-8*x[1]+8*x[0]
    A_test=Data(0.,(2,2,2,2),ReducedFunction(self.domain))
    A_test[1,1,1,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-8)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeWeak_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=7
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,0,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-6)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeWeak_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=5
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,0,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,0]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeWeak_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=(-2)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,1,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeWeak_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=7
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[0,1,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[0,1]=7*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeWeak_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-1)
    u[1]=3
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,0,0]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeWeak_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=(-7)
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,0,1]=x[0]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeWeak_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=5
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,1,0]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_B_Vario_typeWeak_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=7
    B_test=Data(0.,(2,2,2),ReducedFunction(self.domain))
    B_test[1,1,1]=x[1]
    X_test=Data(0.,(2, 2),ContinuousFunction(self.domain))
    X_test[1,1]=7*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+4*x[1]+3*x[0]
    u[1]=3-1*x[1]-2*x[0]
    u[2]=(-3)-4*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,0,0]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(21)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-7*x[1]+3*x[0]
    u[1]=1-8*x[1]+8*x[0]
    u[2]=7-1*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,0,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-56))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+3*x[1]+5*x[0]
    u[1]=4-6*x[1]+8*x[0]
    u[2]=(-4)+x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,1,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(24)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-6*x[1]-4*x[0]
    u[1]=6+x[1]-4*x[0]
    u[2]=4-5*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,1,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(7)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-2*x[1]+7*x[0]
    u[1]=(-7)-6*x[1]+4*x[0]
    u[2]=(-5)-8*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,2,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(3)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-4*x[1]-7*x[0]
    u[1]=(-7)-6*x[1]+4*x[0]
    u[2]=2+7*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,2,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(49)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-2*x[1]-8*x[0]
    u[1]=5+8*x[1]+5*x[0]
    u[2]=4+5*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,0,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-16))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)+3*x[1]-6*x[0]
    u[1]=(-1)-9*x[1]-1*x[0]
    u[2]=(-2)+x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,0,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(9)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-9*x[1]+2*x[0]
    u[1]=7+x[1]-2*x[0]
    u[2]=8-3*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,1,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-12))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+2*x[1]+5*x[0]
    u[1]=(-8)+8*x[1]-7*x[0]
    u[2]=(-4)+7*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,1,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(64)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-2*x[1]-1*x[0]
    u[1]=(-3)-8*x[1]-2*x[0]
    u[2]=7-8*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,2,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-12))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp0121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+5*x[1]-8*x[0]
    u[1]=(-4)+7*x[1]+x[0]
    u[2]=7-4*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,2,1]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-20))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-9*x[1]+4*x[0]
    u[1]=(-8)-4*x[1]-6*x[0]
    u[2]=3-3*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,0,0]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(4)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+8*x[1]-8*x[0]
    u[1]=(-6)-4*x[1]+x[0]
    u[2]=(-2)+8*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,0,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(64)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-4*x[1]-2*x[0]
    u[1]=5+2*x[1]-9*x[0]
    u[2]=4-9*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,1,0]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-45))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-8*x[1]-3*x[0]
    u[1]=7+2*x[1]+6*x[0]
    u[2]=1-3*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,1,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(2)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+8*x[1]+4*x[0]
    u[1]=(-4)-4*x[1]-7*x[0]
    u[2]=8-2*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,2,0]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(14)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-2*x[1]+2*x[0]
    u[1]=4-5*x[1]-3*x[0]
    u[2]=1+7*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,2,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(56)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)+8*x[1]+2*x[0]
    u[1]=(-1)-8*x[1]-1*x[0]
    u[2]=(-5)-2*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,0,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(12)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-1*x[1]-1*x[0]
    u[1]=(-2)+x[1]-3*x[0]
    u[2]=3+5*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,0,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-3))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+2*x[1]+5*x[0]
    u[1]=1+6*x[1]+5*x[0]
    u[2]=6+8*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,1,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(30)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-9*x[1]+8*x[0]
    u[1]=2+3*x[1]-1*x[0]
    u[2]=7-6*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,1,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(3)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-8*x[1]+8*x[0]
    u[1]=5-2*x[1]-8*x[0]
    u[2]=(-8)-6*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,2,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(16)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp1121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+5*x[1]-6*x[0]
    u[1]=5-2*x[1]-2*x[0]
    u[2]=1+6*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,2,1]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(30)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-9*x[1]+7*x[0]
    u[1]=(-1)+8*x[1]-8*x[0]
    u[2]=4-9*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,0,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(21)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)+2*x[1]+x[0]
    u[1]=6-3*x[1]+4*x[0]
    u[2]=2+2*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,0,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(14)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+x[1]-8*x[0]
    u[1]=6+6*x[1]-3*x[0]
    u[2]=(-3)-3*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,1,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-9))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+3*x[1]+7*x[0]
    u[1]=(-1)-3*x[1]+7*x[0]
    u[2]=(-8)+2*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,1,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-3))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-2*x[1]+5*x[0]
    u[1]=(-3)+2*x[1]-6*x[0]
    u[2]=(-4)+4*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,2,0]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(20)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+6*x[1]-8*x[0]
    u[1]=(-3)-4*x[1]-1*x[0]
    u[2]=(-3)+7*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,2,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(21)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3-4*x[1]+3*x[0]
    u[1]=3+6*x[1]-6*x[0]
    u[2]=(-1)+x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,0,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(18)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-5*x[1]+6*x[0]
    u[1]=(-3)+6*x[1]-1*x[0]
    u[2]=(-5)-5*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,0,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-10))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+7*x[1]+6*x[0]
    u[1]=(-2)-7*x[1]-8*x[0]
    u[2]=(-7)-4*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,1,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-32))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-8*x[1]+2*x[0]
    u[1]=(-1)-5*x[1]-7*x[0]
    u[2]=5+6*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,1,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-35))
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+8*x[1]-6*x[0]
    u[1]=1-4*x[1]+7*x[0]
    u[2]=2-9*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,2,0]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(5)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeStrong_comp2121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+6*x[1]-6*x[0]
    u[1]=(-1)+7*x[1]-2*x[0]
    u[2]=8+4*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,2,1]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(16)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=1
    u[2]=(-6)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,0]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-35))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)
    u[1]=(-8)
    u[2]=7
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-56))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2
    u[1]=1
    u[2]=(-1)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,2]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-3))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=2
    u[2]=(-6)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(24)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=8
    u[2]=(-8)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(64)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=(-3)
    u[2]=(-2)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,2]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-2))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=(-5)
    u[2]=8
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(36)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=5
    u[2]=2
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(30)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=(-2)
    u[2]=4
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,2]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(12)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)
    u[1]=(-6)
    u[2]=4
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-12))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=8
    u[2]=(-3)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(48)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=4
    u[2]=5
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,2]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(10)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=7
    u[2]=(-3)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-12))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=2
    u[2]=(-3)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(14)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=2
    u[2]=(-5)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,2]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-30))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=(-2)
    u[2]=4
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,0]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(48)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5
    u[1]=6
    u[2]=(-7)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,1]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(18)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeStrong_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=7
    u[2]=(-7)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,2]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-42))
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-2*x[1]+3*x[0]
    u[1]=4-3*x[1]-7*x[0]
    u[2]=2+7*x[1]-9*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,0,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=6
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3-9*x[1]-9*x[0]
    u[1]=(-5)-3*x[1]+2*x[0]
    u[2]=6-6*x[1]-1*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,0,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-72)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-4*x[1]-2*x[0]
    u[1]=3+2*x[1]+7*x[0]
    u[2]=(-4)-3*x[1]+7*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,1,0]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=7
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+8*x[1]+3*x[0]
    u[1]=2-8*x[1]-5*x[0]
    u[2]=(-8)+7*x[1]+4*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,1,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-8)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-4*x[1]+8*x[0]
    u[1]=(-3)+x[1]-1*x[0]
    u[2]=3-2*x[1]+6*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,2,0]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=48
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-2*x[1]-4*x[0]
    u[1]=(-7)-4*x[1]+6*x[0]
    u[2]=4-2*x[1]-8*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,2,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-9*x[1]-2*x[0]
    u[1]=(-3)-4*x[1]+8*x[0]
    u[2]=6-3*x[1]-1*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,0,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-12)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5+8*x[1]-5*x[0]
    u[1]=1-3*x[1]+2*x[0]
    u[2]=5+3*x[1]-1*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,0,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=48
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+7*x[1]-2*x[0]
    u[1]=3+4*x[1]+6*x[0]
    u[2]=2+7*x[1]-4*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,1,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=24
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+4*x[1]+8*x[0]
    u[1]=5-8*x[1]-6*x[0]
    u[2]=(-2)-5*x[1]+x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,1,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-56)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-8*x[1]-6*x[0]
    u[1]=4+8*x[1]+5*x[0]
    u[2]=5-9*x[1]-2*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,2,0]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-16)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+5*x[1]-8*x[0]
    u[1]=6-8*x[1]+2*x[0]
    u[2]=(-7)-5*x[1]+8*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,2,1]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-25)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+6*x[1]-2*x[0]
    u[1]=(-8)+6*x[1]+5*x[0]
    u[2]=(-8)+7*x[1]+3*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,0,0]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-6)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+3*x[1]-7*x[0]
    u[1]=(-9)+7*x[1]+3*x[0]
    u[2]=(-4)-9*x[1]+2*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,0,1]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=3
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+7*x[1]+4*x[0]
    u[1]=(-4)-8*x[1]+4*x[0]
    u[2]=(-3)-6*x[1]+8*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,1,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=24
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+2*x[1]+7*x[0]
    u[1]=(-3)-1*x[1]-9*x[0]
    u[2]=(-8)-9*x[1]+7*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,1,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-6)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp220(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+7*x[1]+5*x[0]
    u[1]=(-4)-4*x[1]+3*x[0]
    u[2]=5-6*x[1]-8*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,2,0]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-48)
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Const_typeStrong_comp221(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+x[1]-8*x[0]
    u[1]=2-1*x[1]-7*x[0]
    u[2]=(-2)+3*x[1]-2*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,2,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=24
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-8*x[1]-2*x[0]
    u[1]=(-5)+7*x[1]-3*x[0]
    u[2]=(-4)+7*x[1]+8*x[0]
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[0,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=4-16*x[1]-4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-7*x[1]+3*x[0]
    u[1]=4-8*x[1]-2*x[0]
    u[2]=3-9*x[1]+2*x[0]
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[0,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=8-16*x[1]-4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Const_typeStrong_comp02(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-1*x[1]-1*x[0]
    u[1]=8+2*x[1]+x[0]
    u[2]=3-1*x[1]+2*x[0]
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[0,2]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=9-3*x[1]+6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+x[1]-6*x[0]
    u[1]=6+8*x[1]+7*x[0]
    u[2]=6-1*x[1]+8*x[0]
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[1,0]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=56+7*x[1]-42*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+3*x[1]-1*x[0]
    u[1]=(-4)-8*x[1]-5*x[0]
    u[2]=3+3*x[1]-5*x[0]
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[1,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-24)-48*x[1]-30*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Const_typeStrong_comp12(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+2*x[1]-9*x[0]
    u[1]=(-4)-9*x[1]+5*x[0]
    u[2]=(-9)-3*x[1]+3*x[0]
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[1,2]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-54)-18*x[1]+18*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Const_typeStrong_comp20(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-8*x[1]+8*x[0]
    u[1]=(-8)-9*x[1]+8*x[0]
    u[2]=(-9)+5*x[1]+4*x[0]
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[2,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-2)-16*x[1]+16*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Const_typeStrong_comp21(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-6*x[1]-1*x[0]
    u[1]=(-2)+8*x[1]+6*x[0]
    u[2]=1+8*x[1]+3*x[0]
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[2,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-4)+16*x[1]+12*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Const_typeStrong_comp22(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-4*x[1]-2*x[0]
    u[1]=7-7*x[1]-7*x[0]
    u[2]=4+6*x[1]-2*x[0]
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[2,2]=3
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=12+18*x[1]-6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Const_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-1*x[1]+7*x[0]
    u[1]=7-4*x[1]-9*x[0]
    u[2]=(-2)-9*x[1]+5*x[0]
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[0,0]=7
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=(-56)-7*x[1]+49*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Const_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-9*x[1]+8*x[0]
    u[1]=(-6)-3*x[1]-9*x[0]
    u[2]=7+6*x[1]+2*x[0]
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[0,1]=2
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=(-12)-6*x[1]-18*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Const_typeStrong_comp02(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+7*x[1]-7*x[0]
    u[1]=(-4)-8*x[1]+2*x[0]
    u[2]=(-3)-8*x[1]+3*x[0]
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[0,2]=5
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=(-15)-40*x[1]+15*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Const_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+4*x[1]+x[0]
    u[1]=(-2)-5*x[1]-9*x[0]
    u[2]=(-7)-7*x[1]-8*x[0]
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[1,0]=2
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=(-18)+8*x[1]+2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Const_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+5*x[1]+5*x[0]
    u[1]=(-5)-8*x[1]-1*x[0]
    u[2]=(-1)-2*x[1]-5*x[0]
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[1,1]=2
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=(-10)-16*x[1]-2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Const_typeStrong_comp12(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-2*x[1]-3*x[0]
    u[1]=(-2)+5*x[1]+x[0]
    u[2]=(-8)-5*x[1]+5*x[0]
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[1,2]=6
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=(-48)-30*x[1]+30*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Const_typeStrong_comp20(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-2*x[1]-8*x[0]
    u[1]=1+x[1]-7*x[0]
    u[2]=(-3)-7*x[1]+7*x[0]
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[2,0]=4
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=(-36)-8*x[1]-32*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Const_typeStrong_comp21(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-6*x[1]-2*x[0]
    u[1]=(-1)-9*x[1]-6*x[0]
    u[2]=(-7)-1*x[1]+4*x[0]
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[2,1]=5
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=(-5)-45*x[1]-30*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Const_typeStrong_comp22(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+5*x[1]-6*x[0]
    u[1]=(-4)-7*x[1]-4*x[0]
    u[2]=7-4*x[1]-6*x[0]
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[2,2]=8
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=56-32*x[1]-48*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+7*x[1]+4*x[0]
    u[1]=(-4)-5*x[1]-3*x[0]
    u[2]=8-7*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+7*x[1]-9*x[0]
    u[1]=(-2)+4*x[1]+2*x[0]
    u[2]=(-4)+8*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-7)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(7*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+3*x[1]-6*x[0]
    u[1]=2+5*x[1]+7*x[0]
    u[2]=(-2)-8*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-7)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(7*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-3*x[1]-6*x[0]
    u[1]=(-9)+2*x[1]-9*x[0]
    u[2]=(-8)-6*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,1,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-2)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(2*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-9*x[1]-7*x[0]
    u[1]=(-9)+7*x[1]-5*x[0]
    u[2]=1-3*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-6)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(6*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+2*x[1]-2*x[0]
    u[1]=(-2)+4*x[1]+8*x[0]
    u[2]=6+6*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,2,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-6)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(6*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-9*x[1]+5*x[0]
    u[1]=1-2*x[1]+x[0]
    u[2]=3-9*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,0,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-5)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(5*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-3*x[1]+2*x[0]
    u[1]=7-1*x[1]+5*x[0]
    u[2]=(-3)-6*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=3
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-3)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-1*x[1]-4*x[0]
    u[1]=(-3)-7*x[1]+x[0]
    u[2]=4+x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-1)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-2*x[1]-2*x[0]
    u[1]=4-9*x[1]-5*x[0]
    u[2]=(-8)-9*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=9
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-9)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+x[1]-3*x[0]
    u[1]=(-7)-6*x[1]+x[0]
    u[2]=(-3)-9*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,2,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=6
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-6)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp0121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+3*x[1]-7*x[0]
    u[1]=(-8)+4*x[1]+4*x[0]
    u[2]=3-4*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=4
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-4)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+6*x[1]-4*x[0]
    u[1]=8-9*x[1]+3*x[0]
    u[2]=(-4)+8*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=4
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-4)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+6*x[1]+6*x[0]
    u[1]=(-1)-2*x[1]+4*x[0]
    u[2]=(-8)+x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-6)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(6*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+2*x[1]+x[0]
    u[1]=(-1)-5*x[1]+3*x[0]
    u[2]=4+7*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-3)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(3*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+8*x[1]-6*x[0]
    u[1]=8+8*x[1]+6*x[0]
    u[2]=(-8)+3*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,1,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-8)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(8*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-6*x[1]+5*x[0]
    u[1]=(-7)+3*x[1]-1*x[0]
    u[2]=7-9*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-2)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(2*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+8*x[1]-7*x[0]
    u[1]=3-4*x[1]+4*x[0]
    u[2]=3-5*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,2,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=5
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-5)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+8*x[1]+5*x[0]
    u[1]=1-3*x[1]+7*x[0]
    u[2]=1-7*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,0,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-5)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(5*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-1*x[1]-9*x[0]
    u[1]=4+x[1]+4*x[0]
    u[2]=(-2)+7*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=1
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-1)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-3*x[1]-6*x[0]
    u[1]=4-2*x[1]+3*x[0]
    u[2]=(-8)+7*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-3)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(3*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-4*x[1]-8*x[0]
    u[1]=(-5)-6*x[1]-2*x[0]
    u[2]=8-1*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=6
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-6)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-3*x[1]-5*x[0]
    u[1]=(-7)-5*x[1]-5*x[0]
    u[2]=(-8)-7*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,2,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-6)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(6*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp1121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-8*x[1]-9*x[0]
    u[1]=(-7)+5*x[1]+6*x[0]
    u[2]=(-4)-9*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=9
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-9)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+6*x[1]+4*x[0]
    u[1]=8-7*x[1]+6*x[0]
    u[2]=(-2)+x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-4)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-5*x[1]-5*x[0]
    u[1]=3-4*x[1]+8*x[0]
    u[2]=(-2)+6*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=5
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-5)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+5*x[1]-9*x[0]
    u[1]=(-9)-9*x[1]-1*x[0]
    u[2]=(-7)+2*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=1
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-1)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-5*x[1]+8*x[0]
    u[1]=5-5*x[1]-3*x[0]
    u[2]=2+7*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,1,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=5
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-5)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-9*x[1]-4*x[0]
    u[1]=7+8*x[1]-1*x[0]
    u[2]=1+6*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=9
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-9)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+4*x[1]+2*x[0]
    u[1]=(-7)-2*x[1]-9*x[0]
    u[2]=(-1)-7*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,2,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=7
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-7)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-4*x[1]-9*x[0]
    u[1]=(-2)+7*x[1]-8*x[0]
    u[2]=(-3)+3*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,0,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=9
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-9)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+6*x[1]-8*x[0]
    u[1]=8+x[1]+3*x[0]
    u[2]=(-4)-2*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-6)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(6*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-5*x[1]-3*x[0]
    u[1]=8-6*x[1]+8*x[0]
    u[2]=(-5)+3*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-8)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(8*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-8*x[1]-8*x[0]
    u[1]=5-1*x[1]+x[0]
    u[2]=8+6*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=1
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-1)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+7*x[1]+8*x[0]
    u[1]=4-6*x[1]-1*x[0]
    u[2]=(-1)-3*x[1]-8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,2,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=8
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-8)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeStrong_comp2121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-8*x[1]-6*x[0]
    u[1]=8+2*x[1]-1*x[0]
    u[2]=1-6*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=6
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-6)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=(-1)
    u[2]=1
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=3
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-3)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=(-5)
    u[2]=8
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=5
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-5)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=(-8)
    u[2]=(-9)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=9
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-9)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=6
    u[2]=4
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-8)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(8*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=7
    u[2]=6
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-7)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(7*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=(-2)
    u[2]=(-1)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,2]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=1
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-1)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=(-7)
    u[2]=5
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=8
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-8)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=(-7)
    u[2]=2
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=7
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-7)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)
    u[1]=1
    u[2]=(-6)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=6
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-6)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=(-8)
    u[2]=5
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-4)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(4*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=(-4)
    u[2]=(-4)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=4
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-4)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=(-4)
    u[2]=(-2)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,2]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=2
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-2)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=6
    u[2]=6
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-4)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=(-2)
    u[2]=(-2)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=2
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-2)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=2
    u[2]=(-6)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=6
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-6)*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)
    u[1]=4
    u[2]=(-5)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=2
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-2)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=(-2)
    u[2]=(-2)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=2
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-2)*x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeStrong_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=(-3)
    u[2]=1
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,2]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-1)
    n=self.setNormal(ReducedFunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),ReducedFunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(x[1])
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, Y_reduced=Y_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-2*x[1]-4*x[0]
    u[1]=(-1)-7*x[1]+x[0]
    u[2]=(-9)+5*x[1]-7*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-4*x[1]-4*x[0]
    u[1]=5+x[1]-3*x[0]
    u[2]=(-3)-4*x[1]-7*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+4*x[1]-4*x[0]
    u[1]=3+4*x[1]+2*x[0]
    u[2]=(-6)+8*x[1]-7*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-1*x[1]+3*x[0]
    u[1]=7+3*x[1]-2*x[0]
    u[2]=(-4)+5*x[1]+7*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=3*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-4*x[1]+8*x[0]
    u[1]=7-6*x[1]-3*x[0]
    u[2]=6-9*x[1]-5*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+x[1]+4*x[0]
    u[1]=(-8)-8*x[1]+2*x[0]
    u[2]=(-3)+5*x[1]-7*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[0,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-6*x[1]-7*x[0]
    u[1]=4+3*x[1]+3*x[0]
    u[2]=6-6*x[1]+8*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-7*x[1]+5*x[0]
    u[1]=(-6)-7*x[1]-4*x[0]
    u[2]=(-9)+2*x[1]-1*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-2*x[1]-1*x[0]
    u[1]=7+7*x[1]+5*x[0]
    u[2]=(-1)-3*x[1]-7*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-3*x[1]+4*x[0]
    u[1]=4+2*x[1]-8*x[0]
    u[2]=6-6*x[1]-5*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=2*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+x[1]+2*x[0]
    u[1]=(-5)+3*x[1]-7*x[0]
    u[2]=(-6)+2*x[1]+5*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+4*x[1]-7*x[0]
    u[1]=4-2*x[1]+4*x[0]
    u[2]=3-2*x[1]-5*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[1,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-2)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+6*x[1]-7*x[0]
    u[1]=(-4)+2*x[1]+5*x[0]
    u[2]=(-3)-9*x[1]-8*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-4*x[1]+8*x[0]
    u[1]=(-5)+5*x[1]+x[0]
    u[2]=4+x[1]-1*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,0,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-4)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-6*x[1]+x[0]
    u[1]=(-1)+x[1]+4*x[0]
    u[2]=5+3*x[1]-4*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-7*x[1]-8*x[0]
    u[1]=(-3)+x[1]+8*x[0]
    u[2]=(-2)-2*x[1]-5*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp220(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+6*x[1]-1*x[0]
    u[1]=7+7*x[1]-9*x[0]
    u[2]=1-5*x[1]-3*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_C_Vario_typeStrong_comp221(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+7*x[1]+5*x[0]
    u[1]=(-6)+2*x[1]+5*x[0]
    u[2]=2-8*x[1]-6*x[0]
    C_test=Data(0.,(3,3,2),ReducedFunction(self.domain))
    C_test[2,2,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-8)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(C_reduced=C_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=3
    u[2]=4
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=3
    u[2]=(-9)
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Vario_typeStrong_comp02(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=(-5)
    u[2]=(-3)
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)
    u[1]=(-8)
    u[2]=7
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[1,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=1
    u[2]=(-2)
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[1,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Vario_typeStrong_comp12(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2
    u[1]=(-9)
    u[2]=6
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[1,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Vario_typeStrong_comp20(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)
    u[1]=(-5)
    u[2]=(-2)
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[2,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Vario_typeStrong_comp21(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=3
    u[2]=(-3)
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[2,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_D_Vario_typeStrong_comp22(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=(-8)
    u[2]=8
    D_test=Data(0.,(3,3),ReducedFunction(self.domain))
    D_test[2,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(D_reduced=D_test, Y_reduced=Y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Vario_typeStrong_comp00(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2
    u[1]=(-3)
    u[2]=(-2)
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[0,0]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Vario_typeStrong_comp01(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=5
    u[2]=3
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[0,1]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Vario_typeStrong_comp02(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=(-6)
    u[2]=2
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[0,2]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Vario_typeStrong_comp10(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=4
    u[2]=6
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[1,0]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Vario_typeStrong_comp11(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)
    u[1]=1
    u[2]=5
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[1,1]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Vario_typeStrong_comp12(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=(-8)
    u[2]=(-2)
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[1,2]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[1]=(-2)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Vario_typeStrong_comp20(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5
    u[1]=(-2)
    u[2]=(-3)
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[2,0]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Vario_typeStrong_comp21(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)
    u[1]=2
    u[2]=8
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[2,1]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_Vario_typeStrong_comp22(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)
    u[1]=2
    u[2]=(-1)
    d_test=Data(0.,(3,3),ReducedFunctionOnBoundary(self.domain))
    d_test[2,2]=x[0]
    y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_test[2]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_reduced=d_test, y_reduced=y_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-5*x[1]-2*x[0]
    u[1]=1-1*x[1]-7*x[0]
    u[2]=(-3)-8*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,0,0]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-4)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-4*x[1]-7*x[0]
    u[1]=5-4*x[1]-6*x[0]
    u[2]=(-1)+2*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,0,1]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-24)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+3*x[1]-7*x[0]
    u[1]=(-5)+x[1]-4*x[0]
    u[2]=4-5*x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,1,0]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-4)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3-5*x[1]-7*x[0]
    u[1]=(-7)+3*x[1]+x[0]
    u[2]=8-5*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,1,1]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=3
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+3*x[1]+3*x[0]
    u[1]=1+4*x[1]+3*x[0]
    u[2]=(-2)-1*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,2,0]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=56
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-3*x[1]-9*x[0]
    u[1]=(-2)+8*x[1]-7*x[0]
    u[2]=(-7)+5*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,2,1]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=20
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)-2*x[1]+6*x[0]
    u[1]=5+3*x[1]+8*x[0]
    u[2]=(-4)-6*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,0,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=30
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-5*x[1]-5*x[0]
    u[1]=7+7*x[1]+2*x[0]
    u[2]=(-9)-3*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,0,1]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-40)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-5*x[1]+7*x[0]
    u[1]=1+2*x[1]-9*x[0]
    u[2]=(-5)-9*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,1,0]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-27)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-6*x[1]-5*x[0]
    u[1]=(-7)+6*x[1]+6*x[0]
    u[2]=1-8*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,1,1]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=48
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+8*x[1]-2*x[0]
    u[1]=7-9*x[1]-4*x[0]
    u[2]=4-4*x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,2,0]=7
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-21)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp0121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+3*x[1]-3*x[0]
    u[1]=6+x[1]+7*x[0]
    u[2]=(-7)+3*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,2,1]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=18
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-4*x[1]-5*x[0]
    u[1]=8+7*x[1]-6*x[0]
    u[2]=7-1*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,0,0]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-30)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+8*x[1]+5*x[0]
    u[1]=7+x[1]+4*x[0]
    u[2]=(-5)+4*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,0,1]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=48
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-1*x[1]+x[0]
    u[1]=(-8)-1*x[1]-6*x[0]
    u[2]=4-6*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,1,0]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-36)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-9*x[1]-1*x[0]
    u[1]=8+8*x[1]+4*x[0]
    u[2]=(-4)-5*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,1,1]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=16
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-4*x[1]+6*x[0]
    u[1]=6+8*x[1]+4*x[0]
    u[2]=5+2*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,2,0]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=3
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-9*x[1]+7*x[0]
    u[1]=7+5*x[1]-4*x[0]
    u[2]=7-4*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,2,1]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-20)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-8*x[1]-8*x[0]
    u[1]=(-7)-8*x[1]+7*x[0]
    u[2]=4+2*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,0,0]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-8)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+8*x[1]+x[0]
    u[1]=(-2)-9*x[1]+2*x[0]
    u[2]=(-1)-8*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,0,1]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=32
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-7*x[1]+2*x[0]
    u[1]=2+x[1]-1*x[0]
    u[2]=8+4*x[1]+5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,1,0]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-8)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+3*x[1]+5*x[0]
    u[1]=8+8*x[1]+7*x[0]
    u[2]=1+5*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,1,1]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=40
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+5*x[1]+4*x[0]
    u[1]=(-4)-7*x[1]+5*x[0]
    u[2]=8-7*x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,2,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-15)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp1121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+2*x[1]-7*x[0]
    u[1]=(-8)+2*x[1]-3*x[0]
    u[2]=(-2)+8*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,2,1]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=16
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-5*x[1]-2*x[0]
    u[1]=(-9)+4*x[1]+8*x[0]
    u[2]=1-8*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,0,0]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-6)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-8*x[1]+4*x[0]
    u[1]=(-4)-3*x[1]-3*x[0]
    u[2]=(-8)-1*x[1]-3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,0,1]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-48)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-6*x[1]+8*x[0]
    u[1]=8+8*x[1]+8*x[0]
    u[2]=(-9)-9*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,1,0]=7
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=56
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+7*x[1]-3*x[0]
    u[1]=4-7*x[1]+6*x[0]
    u[2]=(-7)+5*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,1,1]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-28)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+4*x[1]-3*x[0]
    u[1]=3+4*x[1]-6*x[0]
    u[2]=(-5)-5*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,2,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=40
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-7*x[1]+x[0]
    u[1]=(-3)-3*x[1]-4*x[0]
    u[2]=6+x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,2,1]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=6
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-8*x[1]+3*x[0]
    u[1]=3-8*x[1]+x[0]
    u[2]=(-7)+5*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,0,0]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=9
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)+7*x[1]-3*x[0]
    u[1]=4-2*x[1]+7*x[0]
    u[2]=(-3)+5*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,0,1]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=35
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-1*x[1]-2*x[0]
    u[1]=1+x[1]-8*x[0]
    u[2]=6-6*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,1,0]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-48)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)+2*x[1]-4*x[0]
    u[1]=(-7)-9*x[1]+6*x[0]
    u[2]=(-9)-7*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,1,1]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-27)
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5+6*x[1]-7*x[0]
    u[1]=5+2*x[1]-5*x[0]
    u[2]=(-9)+4*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,2,0]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=6
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Const_typeWeak_comp2121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+5*x[1]-4*x[0]
    u[1]=3-4*x[1]-7*x[0]
    u[2]=1+3*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,2,1]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=9
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=1
    u[2]=(-5)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,0]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=5
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)
    u[1]=(-2)
    u[2]=(-4)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,1]=7
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-14)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=7
    u[2]=6
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,2]=7
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=42
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2
    u[1]=(-1)
    u[2]=6
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,0]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=2
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=5
    u[2]=6
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,1]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=15
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=6
    u[2]=(-4)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,2]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-32)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=8
    u[2]=1
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,0]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=24
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=6
    u[2]=(-5)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,1]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=12
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=(-4)
    u[2]=(-6)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,2]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-12)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)
    u[1]=(-1)
    u[2]=4
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,0]=1
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-9)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5
    u[1]=(-1)
    u[2]=1
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,1]=6
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-6)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=(-9)
    u[2]=(-5)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,2]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-40)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)
    u[1]=(-2)
    u[2]=(-1)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,0]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-18)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=4
    u[2]=6
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,1]=2
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=8
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=(-5)
    u[2]=(-7)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,2]=8
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-56)
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=(-3)
    u[2]=5
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,0]=3
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=18
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=7
    u[2]=(-7)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,1]=5
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=35
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Const_typeWeak_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=(-2)
    u[2]=5
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,2]=4
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=20
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-4*x[1]+4*x[0]
    u[1]=1-8*x[1]+4*x[0]
    u[2]=(-9)+8*x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+5*x[1]+x[0]
    u[1]=2-7*x[1]+5*x[0]
    u[2]=4-3*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+4*x[1]+x[0]
    u[1]=3-3*x[1]+5*x[0]
    u[2]=(-4)+x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,1,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+2*x[1]-6*x[0]
    u[1]=2-5*x[1]-8*x[0]
    u[2]=3+x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,1,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+8*x[1]+x[0]
    u[1]=2-7*x[1]-3*x[0]
    u[2]=(-7)+6*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,2,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+5*x[1]-4*x[0]
    u[1]=(-8)+6*x[1]+2*x[0]
    u[2]=(-6)-1*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,0,2,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)+x[1]+6*x[0]
    u[1]=(-4)-8*x[1]-9*x[0]
    u[2]=3-8*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,0,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+5*x[1]-7*x[0]
    u[1]=(-8)-3*x[1]+3*x[0]
    u[2]=7-5*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,0,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+2*x[1]+8*x[0]
    u[1]=(-3)+3*x[1]+5*x[0]
    u[2]=(-8)-3*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=5*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2+5*x[1]-1*x[0]
    u[1]=3+3*x[1]+x[0]
    u[2]=1-1*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=3*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+7*x[1]-5*x[0]
    u[1]=(-1)+4*x[1]+6*x[0]
    u[2]=7-1*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,2,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp0121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-5*x[1]-4*x[0]
    u[1]=3-3*x[1]-8*x[0]
    u[2]=(-8)-5*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[0,1,2,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-5)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+6*x[1]+5*x[0]
    u[1]=6-7*x[1]+7*x[0]
    u[2]=(-3)-8*x[1]-2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)+2*x[1]-7*x[0]
    u[1]=6-4*x[1]-1*x[0]
    u[2]=(-9)+3*x[1]+7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-6*x[1]-2*x[0]
    u[1]=(-4)-4*x[1]-1*x[0]
    u[2]=3+6*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,1,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-6*x[1]-5*x[0]
    u[1]=(-3)-7*x[1]+2*x[0]
    u[2]=2+5*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,1,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-6*x[1]-8*x[0]
    u[1]=(-3)+4*x[1]-7*x[0]
    u[2]=2-7*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,2,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=4*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+4*x[1]+8*x[0]
    u[1]=2+8*x[1]-7*x[0]
    u[2]=5+7*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,0,2,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-6*x[1]+6*x[0]
    u[1]=6+x[1]+7*x[0]
    u[2]=8+6*x[1]-4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,0,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)-3*x[1]-6*x[0]
    u[1]=3+8*x[1]-8*x[0]
    u[2]=(-9)+7*x[1]-1*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,0,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-3)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)-6*x[1]+8*x[0]
    u[1]=(-2)-4*x[1]+6*x[0]
    u[2]=1+2*x[1]+4*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-3*x[1]-1*x[0]
    u[1]=4+x[1]-8*x[0]
    u[2]=(-7)-1*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-1*x[1]+8*x[0]
    u[1]=(-8)-6*x[1]-4*x[0]
    u[2]=(-3)-6*x[1]-9*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,2,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-9)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp1121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-9*x[1]+3*x[0]
    u[1]=(-5)-3*x[1]-5*x[0]
    u[2]=(-2)-7*x[1]-5*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[1,1,2,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-7)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+4*x[1]-3*x[0]
    u[1]=(-9)+5*x[1]+3*x[0]
    u[2]=2-9*x[1]+8*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+3*x[1]+6*x[0]
    u[1]=8+8*x[1]-3*x[0]
    u[2]=(-1)+x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+8*x[1]+5*x[0]
    u[1]=2+5*x[1]-4*x[0]
    u[2]=(-8)+x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,1,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+8*x[1]-3*x[0]
    u[1]=(-8)-6*x[1]-2*x[0]
    u[2]=3+x[1]+3*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,1,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-6)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2020(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+x[1]+2*x[0]
    u[1]=(-2)-7*x[1]+2*x[0]
    u[2]=(-4)-4*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,2,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2021(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-7*x[1]+5*x[0]
    u[1]=1+6*x[1]-9*x[0]
    u[2]=2-7*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,0,2,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+4*x[1]-6*x[0]
    u[1]=4-4*x[1]+7*x[0]
    u[2]=2-3*x[1]+x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,0,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-6)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3+6*x[1]+2*x[0]
    u[1]=7+8*x[1]+8*x[0]
    u[2]=(-8)+4*x[1]+2*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,0,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+6*x[1]+x[0]
    u[1]=4+7*x[1]+7*x[0]
    u[2]=(-7)-6*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=7*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+7*x[1]+x[0]
    u[1]=(-7)+8*x[1]-9*x[0]
    u[2]=(-9)-6*x[1]+6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=8*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2120(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1-9*x[1]+3*x[0]
    u[1]=(-5)-6*x[1]+6*x[0]
    u[2]=(-7)+5*x[1]-6*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,2,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-6)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_A_Vario_typeWeak_comp2121(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-6*x[1]-5*x[0]
    u[1]=(-5)-7*x[1]-3*x[0]
    u[2]=(-5)-9*x[1]-7*x[0]
    A_test=Data(0.,(3,2,3,2),ReducedFunction(self.domain))
    A_test[2,1,2,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-9)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(A_reduced=A_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=7
    u[2]=7
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)
    u[1]=7
    u[2]=5
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=3
    u[2]=6
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,0,2]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,0]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=(-7)
    u[2]=(-4)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1
    u[1]=(-7)
    u[2]=(-3)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-7)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)
    u[1]=5
    u[2]=(-7)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[0,1,2]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[0,1]=(-7)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=8
    u[2]=(-2)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4
    u[1]=2
    u[2]=(-6)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)
    u[1]=5
    u[2]=(-3)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,0,2]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,0]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6
    u[1]=6
    u[2]=(-4)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=6*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)
    u[1]=(-6)
    u[2]=(-2)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=(-6)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5
    u[1]=8
    u[2]=7
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[1,1,2]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[1,1]=7*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=3
    u[1]=3
    u[2]=(-8)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,0]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)
    u[1]=(-5)
    u[2]=(-3)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,1]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8
    u[1]=(-2)
    u[2]=5
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,0,2]=x[0]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,0]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-8)
    u[1]=1
    u[2]=6
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,0]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-8)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7
    u[1]=(-1)
    u[2]=7
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,1]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-1)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_B_Vario_typeWeak_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)
    u[1]=(-4)
    u[2]=(-5)
    B_test=Data(0.,(3,2,3),ReducedFunction(self.domain))
    B_test[2,1,2]=x[1]
    X_test=Data(0.,(3, 2),ContinuousFunction(self.domain))
    X_test[2,1]=(-5)*x[1]
    pde=LinearPDE(self.domain)
    pde.setValue(B_reduced=B_test, X_reduced=X_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")

class Test_assemblage_2Do1_Contact(unittest.TestCase):
  def setNormal(self,fs):
     out=Vector(0.,fs)
     out.setTaggedValue(2,[1,0])
     out.setTaggedValue(1,[-1,0])
     out.setTaggedValue(20, [0,1])
     out.setTaggedValue(10, [0,-1])
     return out
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Const_typeContact_comp0(self):
    x=self.domain.getX()
    u=(-6)+4*x[1]+7*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[0]=3
    Y_test=(-21)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[0]*((-18)+12*x[1]+21*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=n_contact[0]*(18-12*x[1]-21*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Const_typeContact_comp1(self):
    x=self.domain.getX()
    u=(-4)-3*x[1]+5*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[1]=5
    Y_test=15
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[1]*((-20)-15*x[1]+25*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=0
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_d_contact_Const_typeContact(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=((-6)+x[1]-6*x[0])*jump
    d_contact_test=Data(4,(),FunctionOnContactZero(self.domain))
    y_contact_test=(-24)+4*x[1]-24*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Vario_typeContact_comp0(self):
    x=self.domain.getX()
    u=4+6*x[1]+2*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[0]=x[0]
    Y_test=(-4)-6*x[1]-4*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[0]*(4*x[0]+6*x[0]*x[1]+2*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=n_contact[0]*((-4)*x[0]-6*x[0]*x[1]-2*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_B_Vario_typeContact_comp1(self):
    x=self.domain.getX()
    u=7+5*x[1]+8*x[0]
    B_test=Data(0.,(2,),Function(self.domain))
    B_test[1]=x[1]
    Y_test=(-7)-10*x[1]-8*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=n[1]*(7*x[1]+5*x[1]**2+8*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=0
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu1_d_contact_Vario_typeContact(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=(8)*jump
    d_contact_test=interpolate(x[0],FunctionOnContactZero(self.domain))
    y_contact_test=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeContact_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=6-1*x[1]-4*x[0]
    u[1]=(-7)-1*x[1]+8*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,0]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=4
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(6-1*x[1]-4*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*((-6)+x[1]+4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeContact_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-6)-4*x[1]+7*x[0]
    u[1]=4+6*x[1]-6*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,1]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=42
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(28+42*x[1]-42*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*((-28)-42*x[1]+42*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeContact_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1+6*x[1]+3*x[0]
    u[1]=(-4)-5*x[1]-6*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,0]=7
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-42)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(7+42*x[1]+21*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeContact_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1+3*x[1]-3*x[0]
    u[1]=7-2*x[1]+4*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,1]=2
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=4
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(14-4*x[1]+8*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeContact_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-5)+8*x[1]+2*x[0]
    u[1]=1+5*x[1]+7*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,0]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-2)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-5)+8*x[1]+2*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*(5-8*x[1]-2*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeContact_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=8+2*x[1]+2*x[0]
    u[1]=(-8)-3*x[1]+5*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,1]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-5)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-8)-3*x[1]+5*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*(8+3*x[1]-5*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeContact_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=1-5*x[1]-2*x[0]
    u[1]=(-1)+5*x[1]+3*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,0]=8
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=40
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(8-40*x[1]-16*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Const_typeContact_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=5+5*x[1]-4*x[0]
    u[1]=(-2)-7*x[1]+4*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,1]=1
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=7
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-2)-7*x[1]+4*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_contact_Const_typeContact_comp00(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(8-3*x[1]+6*x[0])*jump
    u[1]=(2-6*x[1]+7*x[0])*jump
    d_contact_test=Data(0.,(2,2),FunctionOnContactZero(self.domain))
    d_contact_test[0,0]=7
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[0]=56-21*x[1]+42*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_contact_Const_typeContact_comp01(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=((-6)-7*x[1]+3*x[0])*jump
    u[1]=((-8)-5*x[1]+x[0])*jump
    d_contact_test=Data(0.,(2,2),FunctionOnContactZero(self.domain))
    d_contact_test[0,1]=6
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[0]=(-48)-30*x[1]+6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_contact_Const_typeContact_comp10(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(2-6*x[1]-7*x[0])*jump
    u[1]=((-3)-3*x[1]+3*x[0])*jump
    d_contact_test=Data(0.,(2,2),FunctionOnContactZero(self.domain))
    d_contact_test[1,0]=7
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[1]=14-42*x[1]-49*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_contact_Const_typeContact_comp11(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(3+8*x[1]+3*x[0])*jump
    u[1]=((-6)-7*x[1]+3*x[0])*jump
    d_contact_test=Data(0.,(2,2),FunctionOnContactZero(self.domain))
    d_contact_test[1,1]=6
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[1]=(-36)-42*x[1]+18*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeContact_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4+3*x[1]-3*x[0]
    u[1]=(-8)-3*x[1]+7*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)-3*x[1]+6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(4*x[0]+3*x[0]*x[1]-3*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*((-4)*x[0]-3*x[0]*x[1]+3*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeContact_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+6*x[1]-9*x[0]
    u[1]=4+7*x[1]-5*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-4)-7*x[1]+10*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(4*x[0]+7*x[0]*x[1]-5*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*((-4)*x[0]-7*x[0]*x[1]+5*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeContact_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-7)-2*x[1]-1*x[0]
    u[1]=(-3)-8*x[1]+x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=7+4*x[1]+x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-7)*x[1]-2*x[1]**2-1*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeContact_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)+5*x[1]-1*x[0]
    u[1]=3+5*x[1]-2*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[0,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[0]=(-3)-10*x[1]+2*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(3*x[1]+5*x[1]**2-2*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeContact_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-8)+3*x[1]-1*x[0]
    u[1]=(-3)+6*x[1]-8*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,0]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=8-3*x[1]+2*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-8)*x[0]+3*x[0]*x[1]-1*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*(8*x[0]-3*x[0]*x[1]+x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeContact_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=3+6*x[1]-2*x[0]
    u[1]=7-4*x[1]-4*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,0,1]=x[0]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)+4*x[1]+8*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(7*x[0]-4*x[0]*x[1]-4*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*((-7)*x[0]+4*x[0]*x[1]+4*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeContact_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=4+8*x[1]+7*x[0]
    u[1]=7-7*x[1]-6*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,0]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=(-4)-16*x[1]-7*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(4*x[1]+8*x[1]**2+7*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_B_Vario_typeContact_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(-3)+3*x[1]-5*x[0]
    u[1]=(-8)-6*x[1]-2*x[0]
    B_test=Data(0.,(2,2,2),Function(self.domain))
    B_test[1,1,1]=x[1]
    Y_test=Data(0.,(2,),ContinuousFunction(self.domain))
    Y_test[1]=8+12*x[1]+2*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(2,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-8)*x[1]-6*x[1]**2-2*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(2,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_contact_Vario_typeContact_comp00(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=((-5))*jump
    u[1]=((-4))*jump
    d_contact_test=Data(0.,(2,2),FunctionOnContactZero(self.domain))
    d_contact_test[0,0]=x[0]
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[0]=(-5)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_contact_Vario_typeContact_comp01(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=((-6))*jump
    u[1]=(8)*jump
    d_contact_test=Data(0.,(2,2),FunctionOnContactZero(self.domain))
    d_contact_test[0,1]=x[0]
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[0]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_contact_Vario_typeContact_comp10(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=((-6))*jump
    u[1]=((-3))*jump
    d_contact_test=Data(0.,(2,2),FunctionOnContactZero(self.domain))
    d_contact_test[1,0]=x[0]
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[1]=(-6)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu2_d_contact_Vario_typeContact_comp11(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=((-4))*jump
    u[1]=((-3))*jump
    d_contact_test=Data(0.,(2,2),FunctionOnContactZero(self.domain))
    d_contact_test[1,1]=x[0]
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[1]=(-3)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+5*x[1]-1*x[0]
    u[1]=2+8*x[1]-3*x[0]
    u[2]=(-9)+2*x[1]+4*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,0]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=4
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-20)+20*x[1]-4*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*(20-20*x[1]+4*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)+2*x[1]+x[0]
    u[1]=2-9*x[1]-5*x[0]
    u[2]=(-8)+6*x[1]+7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=35
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(14-63*x[1]-35*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*((-14)+63*x[1]+35*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-6*x[1]-5*x[0]
    u[1]=(-5)-9*x[1]+8*x[0]
    u[2]=5-9*x[1]-2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,2]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=2
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(5-9*x[1]-2*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*((-5)+9*x[1]+2*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+x[1]-3*x[0]
    u[1]=(-1)+8*x[1]+5*x[0]
    u[2]=(-4)-4*x[1]+x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,0]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-5)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(30+5*x[1]-15*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-4*x[1]+4*x[0]
    u[1]=(-8)+6*x[1]-1*x[0]
    u[2]=(-6)-1*x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,1]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-30)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-40)+30*x[1]-5*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)+7*x[1]+x[0]
    u[1]=(-2)+7*x[1]+7*x[0]
    u[2]=(-1)+8*x[1]-5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,2]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-56)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-7)+56*x[1]-35*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-1)+2*x[1]+3*x[0]
    u[1]=6-5*x[1]-3*x[0]
    u[2]=(-7)-6*x[1]+5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,0]=1
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-3)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-1)+2*x[1]+3*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*(1-2*x[1]-3*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-7*x[1]+5*x[0]
    u[1]=2+2*x[1]-4*x[0]
    u[2]=(-5)-9*x[1]-3*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,1]=6
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=24
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(12+12*x[1]-24*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*((-12)-12*x[1]+24*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=1+6*x[1]-3*x[0]
    u[1]=2-8*x[1]+x[0]
    u[2]=5+7*x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,2]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=28
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*(20+28*x[1]-28*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*((-20)-28*x[1]+28*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-2*x[1]+2*x[0]
    u[1]=8-4*x[1]-9*x[0]
    u[2]=8-8*x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,0]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=16
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-16)-16*x[1]+16*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8-2*x[1]-1*x[0]
    u[1]=8-6*x[1]+4*x[0]
    u[2]=7+3*x[1]+7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,1]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=48
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(64-48*x[1]+32*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+5*x[1]+2*x[0]
    u[1]=5-1*x[1]+8*x[0]
    u[2]=2+8*x[1]-9*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,2]=4
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-32)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(8+32*x[1]-36*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4-9*x[1]+5*x[0]
    u[1]=2-1*x[1]+x[0]
    u[2]=(-1)+4*x[1]+4*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,0]=8
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-40)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(32-72*x[1]+40*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[2]=n_contact[0]*((-32)+72*x[1]-40*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+3*x[1]+8*x[0]
    u[1]=5-4*x[1]-9*x[0]
    u[2]=(-8)+6*x[1]-5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,1]=7
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=63
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(35-28*x[1]-63*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[2]=n_contact[0]*((-35)+28*x[1]+63*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-3)-8*x[1]-3*x[0]
    u[1]=4+7*x[1]+4*x[0]
    u[2]=3-5*x[1]-1*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,2]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=5
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(15-25*x[1]-5*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[2]=n_contact[0]*((-15)+25*x[1]+5*x[0])
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+5*x[1]-6*x[0]
    u[1]=3+x[1]+x[0]
    u[2]=(-5)-4*x[1]-2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,0]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-10)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(8+10*x[1]-12*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-9)-2*x[1]+5*x[0]
    u[1]=(-8)+7*x[1]+8*x[0]
    u[2]=8+x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,1]=2
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-14)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-16)+14*x[1]+16*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Const_typeContact_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+4*x[1]+5*x[0]
    u[1]=(-5)-6*x[1]-3*x[0]
    u[2]=7+8*x[1]+7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,2]=5
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-40)
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(35+40*x[1]+35*x[0])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Const_typeContact_comp00(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(5+8*x[1]+4*x[0])*jump
    u[1]=((-9)+3*x[1]+7*x[0])*jump
    u[2]=((-9)-5*x[1]+5*x[0])*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[0,0]=6
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=30+48*x[1]+24*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Const_typeContact_comp01(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(6-9*x[1]+8*x[0])*jump
    u[1]=((-2)+8*x[1]-2*x[0])*jump
    u[2]=(4-7*x[1]-9*x[0])*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[0,1]=5
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=(-10)+40*x[1]-10*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Const_typeContact_comp02(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(4-9*x[1]+2*x[0])*jump
    u[1]=(4-9*x[1]+7*x[0])*jump
    u[2]=(8-7*x[1]+8*x[0])*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[0,2]=2
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=16-14*x[1]+16*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Const_typeContact_comp10(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(2-4*x[1]+6*x[0])*jump
    u[1]=(5+6*x[1]-5*x[0])*jump
    u[2]=((-3)-4*x[1]-4*x[0])*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[1,0]=3
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=6-12*x[1]+18*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Const_typeContact_comp11(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(7+5*x[1]-6*x[0])*jump
    u[1]=(2-5*x[1]+7*x[0])*jump
    u[2]=((-2)+3*x[1]+8*x[0])*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[1,1]=1
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=2-5*x[1]+7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Const_typeContact_comp12(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-6)-6*x[1]+2*x[0])*jump
    u[1]=((-8)-6*x[1]-9*x[0])*jump
    u[2]=(2+8*x[1]+x[0])*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[1,2]=6
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=12+48*x[1]+6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Const_typeContact_comp20(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-4)-4*x[1]-4*x[0])*jump
    u[1]=(1-3*x[1]-7*x[0])*jump
    u[2]=((-6)-5*x[1]+2*x[0])*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[2,0]=7
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=(-28)-28*x[1]-28*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Const_typeContact_comp21(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(3+4*x[1]+8*x[0])*jump
    u[1]=(7+8*x[1]+6*x[0])*jump
    u[2]=((-7)-6*x[1]+4*x[0])*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[2,1]=4
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=28+32*x[1]+24*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Const_typeContact_comp22(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-8)-2*x[1]-3*x[0])*jump
    u[1]=(3+4*x[1]+3*x[0])*jump
    u[2]=(8+6*x[1]-8*x[0])*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[2,2]=5
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=40+30*x[1]-40*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp000(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+5*x[1]-1*x[0]
    u[1]=(-7)+x[1]+2*x[0]
    u[2]=3-8*x[1]+2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-8)-5*x[1]+2*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*(8*x[0]+5*x[0]*x[1]-1*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*((-8)*x[0]-5*x[0]*x[1]+x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp001(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7+8*x[1]+2*x[0]
    u[1]=(-6)-7*x[1]-8*x[0]
    u[2]=8-1*x[1]+x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=6+7*x[1]+16*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-6)*x[0]-7*x[0]*x[1]-8*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*(6*x[0]+7*x[0]*x[1]+8*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp002(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-3*x[1]-5*x[0]
    u[1]=4+7*x[1]+2*x[0]
    u[2]=(-7)+7*x[1]+7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=7-7*x[1]-14*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[0]*((-7)*x[0]+7*x[0]*x[1]+7*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[0]=n_contact[0]*(7*x[0]-7*x[0]*x[1]-7*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp010(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6+4*x[1]+2*x[0]
    u[1]=(-7)+2*x[1]-1*x[0]
    u[2]=8+4*x[1]-8*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=(-6)-8*x[1]-2*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*(6*x[1]+4*x[1]**2+2*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp011(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)-4*x[1]-3*x[0]
    u[1]=(-2)-5*x[1]+6*x[0]
    u[2]=(-5)-4*x[1]-2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=2+10*x[1]-6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-2)*x[1]-5*x[1]**2+6*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp012(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=4+5*x[1]+6*x[0]
    u[1]=4-2*x[1]-2*x[0]
    u[2]=(-3)+8*x[1]+6*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[0,1,2]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[0]=3-16*x[1]-6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[0]=n[1]*((-3)*x[1]+8*x[1]**2+6*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp100(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+4*x[1]+2*x[0]
    u[1]=(-1)-9*x[1]-4*x[0]
    u[2]=5+8*x[1]+3*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=6-4*x[1]-4*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-6)*x[0]+4*x[0]*x[1]+2*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*(6*x[0]-4*x[0]*x[1]-2*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp101(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)-6*x[1]-7*x[0]
    u[1]=(-7)+8*x[1]-9*x[0]
    u[2]=(-2)+3*x[1]-7*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=7-8*x[1]+18*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-7)*x[0]+8*x[0]*x[1]-9*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*(7*x[0]-8*x[0]*x[1]+9*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp102(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-2)-1*x[1]-7*x[0]
    u[1]=(-5)-4*x[1]+4*x[0]
    u[2]=(-8)-4*x[1]-4*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=8+4*x[1]+8*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[0]*((-8)*x[0]-4*x[0]*x[1]-4*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[1]=n_contact[0]*(8*x[0]+4*x[0]*x[1]+4*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp110(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=7-7*x[1]+8*x[0]
    u[1]=1+6*x[1]-3*x[0]
    u[2]=(-6)+3*x[1]-9*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=(-7)+14*x[1]-8*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*(7*x[1]-7*x[1]**2+8*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp111(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-5)+6*x[1]+7*x[0]
    u[1]=(-3)+4*x[1]+6*x[0]
    u[2]=(-4)-1*x[1]+5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=3-8*x[1]-6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-3)*x[1]+4*x[1]**2+6*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp112(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=5-3*x[1]+5*x[0]
    u[1]=(-1)-9*x[1]-7*x[0]
    u[2]=(-3)+x[1]-6*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[1,1,2]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[1]=3-2*x[1]+6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[1]=n[1]*((-3)*x[1]+x[1]**2-6*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp200(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=2-5*x[1]-3*x[0]
    u[1]=7+x[1]+4*x[0]
    u[2]=(-9)+2*x[1]-6*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,0]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-2)+5*x[1]+6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(2*x[0]-5*x[0]*x[1]-3*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[2]=n_contact[0]*((-2)*x[0]+5*x[0]*x[1]+3*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp201(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-6)+5*x[1]-3*x[0]
    u[1]=(-8)+4*x[1]-3*x[0]
    u[2]=2-7*x[1]+2*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,1]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=8-4*x[1]+6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*((-8)*x[0]+4*x[0]*x[1]-3*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[2]=n_contact[0]*(8*x[0]-4*x[0]*x[1]+3*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp202(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=6-3*x[1]+8*x[0]
    u[1]=6-4*x[1]-6*x[0]
    u[2]=5-1*x[1]+5*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,0,2]=x[0]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-5)+x[1]-10*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[0]*(5*x[0]-1*x[0]*x[1]+5*x[0]**2)
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    y_contact_test[2]=n_contact[0]*((-5)*x[0]+x[0]*x[1]-5*x[0]**2)
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp210(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-7)+8*x[1]+3*x[0]
    u[1]=(-2)+5*x[1]-4*x[0]
    u[2]=(-7)+7*x[1]-1*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,0]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=7-16*x[1]-3*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*((-7)*x[1]+8*x[1]**2+3*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp211(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=8+x[1]-8*x[0]
    u[1]=5-4*x[1]-4*x[0]
    u[2]=(-1)-2*x[1]+4*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,1]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-5)+8*x[1]+4*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(5*x[1]-4*x[1]**2-4*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_B_Vario_typeContact_comp212(self):
    x=self.domain.getX()
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(-4)-4*x[1]-9*x[0]
    u[1]=5-6*x[1]+7*x[0]
    u[2]=7-6*x[1]+6*x[0]
    B_test=Data(0.,(3,2,3),Function(self.domain))
    B_test[2,1,2]=x[1]
    Y_test=Data(0.,(3,),ContinuousFunction(self.domain))
    Y_test[2]=(-7)+12*x[1]-6*x[0]
    n=self.setNormal(FunctionOnBoundary(self.domain))
    y_test=Data(0.,(3,),FunctionOnBoundary(self.domain))
    y_test[2]=n[1]*(7*x[1]-6*x[1]**2+6*x[0]*x[1])
    n_contact=FunctionOnContactZero(self.domain).getNormal()
    y_contact_test=Data(0.,(3,),FunctionOnContactZero(self.domain))
    pde=LinearPDE(self.domain)
    pde.setValue(B=B_test, Y=Y_test, y=y_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Vario_typeContact_comp00(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(2)*jump
    u[1]=(7)*jump
    u[2]=((-2))*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[0,0]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Vario_typeContact_comp01(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-6))*jump
    u[1]=(5)*jump
    u[2]=((-5))*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[0,1]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Vario_typeContact_comp02(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(8)*jump
    u[1]=(8)*jump
    u[2]=(7)*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[0,2]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=7*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Vario_typeContact_comp10(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(6)*jump
    u[1]=((-1))*jump
    u[2]=((-5))*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[1,0]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=6*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Vario_typeContact_comp11(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-8))*jump
    u[1]=(8)*jump
    u[2]=(4)*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[1,1]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Vario_typeContact_comp12(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(4)*jump
    u[1]=((-6))*jump
    u[2]=((-9))*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[1,2]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Vario_typeContact_comp20(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-7))*jump
    u[1]=((-3))*jump
    u[2]=(6)*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[2,0]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Vario_typeContact_comp21(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(1)*jump
    u[1]=((-9))*jump
    u[2]=((-3))*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[2,1]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=(-9)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOFull_NEqu3_d_contact_Vario_typeContact_comp22(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(6)*jump
    u[1]=(8)*jump
    u[2]=((-4))*jump
    d_contact_test=Data(0.,(3,3),FunctionOnContactZero(self.domain))
    d_contact_test[2,2]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact=d_contact_test, y_contact=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_d_contact_Const_typeContact(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=(4+3*x[1]-9*x[0])*jump
    d_contact_test=Data(2,(),ReducedFunctionOnContactZero(self.domain))
    y_contact_test=8+6*x[1]-18*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu1_d_contact_Vario_typeContact(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=((-6))*jump
    d_contact_test=interpolate(x[0],ReducedFunctionOnContactZero(self.domain))
    y_contact_test=(-6)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_contact_Const_typeContact_comp00(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(1+6*x[1]+4*x[0])*jump
    u[1]=(3-3*x[1]-5*x[0])*jump
    d_contact_test=Data(0.,(2,2),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,0]=2
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[0]=2+12*x[1]+8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_contact_Const_typeContact_comp01(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=((-4)-8*x[1]-5*x[0])*jump
    u[1]=((-4)+6*x[1]+5*x[0])*jump
    d_contact_test=Data(0.,(2,2),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,1]=8
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[0]=(-32)+48*x[1]+40*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_contact_Const_typeContact_comp10(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(6+3*x[1]-7*x[0])*jump
    u[1]=((-8)-5*x[1]+3*x[0])*jump
    d_contact_test=Data(0.,(2,2),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,0]=6
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[1]=36+18*x[1]-42*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_contact_Const_typeContact_comp11(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(6-2*x[1]-4*x[0])*jump
    u[1]=(5-5*x[1]+6*x[0])*jump
    d_contact_test=Data(0.,(2,2),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,1]=2
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[1]=10-10*x[1]+12*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_contact_Vario_typeContact_comp00(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(3)*jump
    u[1]=((-5))*jump
    d_contact_test=Data(0.,(2,2),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,0]=x[0]
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[0]=3*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_contact_Vario_typeContact_comp01(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(5)*jump
    u[1]=((-8))*jump
    d_contact_test=Data(0.,(2,2),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,1]=x[0]
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[0]=(-8)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_contact_Vario_typeContact_comp10(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=((-4))*jump
    u[1]=(7)*jump
    d_contact_test=Data(0.,(2,2),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,0]=x[0]
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[1]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu2_d_contact_Vario_typeContact_comp11(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(2,),ContinuousFunction(self.domain))
    u[0]=(8)*jump
    u[1]=(8)*jump
    d_contact_test=Data(0.,(2,2),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,1]=x[0]
    y_contact_test=Data(0.,(2,),ContinuousFunction(self.domain))
    y_contact_test[1]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Const_typeContact_comp00(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-8)-5*x[1]+4*x[0])*jump
    u[1]=(2+6*x[1]-6*x[0])*jump
    u[2]=((-6)-4*x[1]-2*x[0])*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,0]=3
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=(-24)-15*x[1]+12*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Const_typeContact_comp01(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-5)+5*x[1]+8*x[0])*jump
    u[1]=(5+7*x[1]-9*x[0])*jump
    u[2]=(2+6*x[1]+3*x[0])*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,1]=5
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=25+35*x[1]-45*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Const_typeContact_comp02(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(5-1*x[1]-6*x[0])*jump
    u[1]=((-1)-3*x[1]-7*x[0])*jump
    u[2]=((-6)+7*x[1]+5*x[0])*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,2]=1
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=(-6)+7*x[1]+5*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Const_typeContact_comp10(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-1)-1*x[1]-3*x[0])*jump
    u[1]=(6+4*x[1]-3*x[0])*jump
    u[2]=((-4)-2*x[1]-9*x[0])*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,0]=8
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=(-8)-8*x[1]-24*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Const_typeContact_comp11(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(4+4*x[1]-9*x[0])*jump
    u[1]=((-5)-4*x[1]-9*x[0])*jump
    u[2]=(2+8*x[1]-8*x[0])*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,1]=6
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=(-30)-24*x[1]-54*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Const_typeContact_comp12(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-7)-3*x[1]-3*x[0])*jump
    u[1]=((-9)-7*x[1]+7*x[0])*jump
    u[2]=((-2)-9*x[1]-3*x[0])*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,2]=3
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=(-6)-27*x[1]-9*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Const_typeContact_comp20(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(3-9*x[1]-9*x[0])*jump
    u[1]=(4+4*x[1]-4*x[0])*jump
    u[2]=((-6)-5*x[1]+3*x[0])*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[2,0]=8
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=24-72*x[1]-72*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Const_typeContact_comp21(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-6)-9*x[1]+6*x[0])*jump
    u[1]=((-4)-3*x[1]-9*x[0])*jump
    u[2]=(2+7*x[1]-1*x[0])*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[2,1]=4
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=(-16)-12*x[1]-36*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Const_typeContact_comp22(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-8)+6*x[1]-3*x[0])*jump
    u[1]=(1+7*x[1]-8*x[0])*jump
    u[2]=((-1)+x[1]+3*x[0])*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[2,2]=8
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=(-8)+8*x[1]+24*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Vario_typeContact_comp00(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-6))*jump
    u[1]=((-8))*jump
    u[2]=(5)*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,0]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=(-6)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Vario_typeContact_comp01(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-2))*jump
    u[1]=(2)*jump
    u[2]=((-3))*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,1]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Vario_typeContact_comp02(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-5))*jump
    u[1]=((-5))*jump
    u[2]=((-7))*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[0,2]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[0]=(-7)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Vario_typeContact_comp10(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-1))*jump
    u[1]=(4)*jump
    u[2]=((-1))*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,0]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Vario_typeContact_comp11(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-7))*jump
    u[1]=(2)*jump
    u[2]=((-6))*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,1]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Vario_typeContact_comp12(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(5)*jump
    u[1]=((-9))*jump
    u[2]=(2)*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[1,2]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[1]=2*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Vario_typeContact_comp20(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-4))*jump
    u[1]=((-5))*jump
    u[2]=(4)*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[2,0]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=(-4)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Vario_typeContact_comp21(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=(3)*jump
    u[1]=(8)*jump
    u[2]=(5)*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[2,1]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=8*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")
  #==================================================
  def test_assemblage_2D_solO1_coeffOReduced_NEqu3_d_contact_Vario_typeContact_comp22(self):
    x=self.domain.getX()
    jump=Data(0.,(),ContinuousFunction(self.domain))
    jump.setTaggedValue(2,1.)
    u=Data(0.,(3,),ContinuousFunction(self.domain))
    u[0]=((-3))*jump
    u[1]=((-2))*jump
    u[2]=((-1))*jump
    d_contact_test=Data(0.,(3,3),ReducedFunctionOnContactZero(self.domain))
    d_contact_test[2,2]=x[0]
    y_contact_test=Data(0.,(3,),ContinuousFunction(self.domain))
    y_contact_test[2]=(-1)*x[0]
    pde=LinearPDE(self.domain)
    pde.setValue(d_contact_reduced=d_contact_test, y_contact_reduced=y_contact_test)
    r=pde.getResidual(u)
    rhs=pde.getRightHandSide()
    self.assertTrue(Lsup(rhs)>0,"right hand side is zero")
    self.assertTrue(Lsup(r)<=self.RES_TOL*Lsup(rhs),"residual is too big")

