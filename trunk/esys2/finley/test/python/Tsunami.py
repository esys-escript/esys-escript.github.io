# $Id$

from esys.escript import *
from esys.linearPDEs import *
from esys import finley

g=9.81 * 1e-3 # km/sec
C=2           # sqrt(km)/sec
g_c=1e-5      # Hz 
H_level=1
#=====================================
L=1000. #km
mydomain=finley.Rectangle(l0=L,l1=L,n0=100,n1=100)
#mydomain=finley.ReadMesh("test.msh")
e_size=mydomain.getSize()
#====================================
#  profile:
#===================================
x=mydomain.getX()
H=H_level # *(1.-exp(-2.*x[0]/L))
#====================================
h_pde=LinearPDE(mydomain)
h_pde.setValue(D=1.)
h_pde.setSymmetryOn()
hv_pde=LinearPDE(mydomain)
hv_pde.setValue(D=kronecker(mydomain))
hv_pde.setSymmetryOn()
#====================================

def getDh(h_pde,h,v,hv,H):
   h_pde.setValue(Y=-trace(grad(hv)))
   return h_pde.getSolution()

def getDhv(hv_pde,h,v,hv,H):
   F=trace(grad(outer(hv,v)+0.5*g*(h**2-H**2)*kronecker(hv_pde.getDomain())))
   Q=h*g_c*matrixmult(numarray.array([[0,-1],[1,0]]),v)-g*(h-H)*grad(H)+g*length(v)/(C*h**2)*v 
   hv_pde.setValue(Y=-F-Q)
   return hv_pde.getSolution()


x=mydomain.getX()
h=H-0.015*exp(-0.1*length(x-[L/2.,L/2.]))
v=Vector(0.,ContinuousFunction(mydomain))
hv=h*v

t=0
dt=0.01
t_count=0
while t_count<200:
  t_count+=1
  t+=dt
  print "@ ",t_count,"-th time step t =",t," (step size = ",dt,")"  
  # Taylor Galerkin method
  h_half=h+dt/2*getDh(h_pde,h,v,hv,H)
  hv_half=hv+dt/2*getDhv(hv_pde,h,v,hv,H)
  v_half=hv_half/(h_half+1.e-15)
  h=h+dt*getDh(h_pde,h_half,v_half,hv_half,H)
  hv=hv+dt*getDhv(hv_pde,h_half,v_half,hv_half,H)
  v=hv/(h+1.e-15)

  if t_count%10==0:
      print "save ",t_count
  
  dt=min(inf(e_size/(sqrt(g*h)+length(v)+1.e-15)),10.)
  print "@v =",sup(v),inf(v)
  print "@h =",sup(h),inf(h)
  print "@c =",Lsup(sqrt(g*h))
  print "@dt  =",inf(e_size/(sqrt(g*h)+length(v)+1.e-15))
