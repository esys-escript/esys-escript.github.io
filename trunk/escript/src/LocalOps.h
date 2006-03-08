// $Id$
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

#if !defined escript_LocalOps_H
#define escript_LocalOps_H
#include <math.h>
namespace escript {


/**
   \brief
   solves a 1x1 eigenvalue A*V=ev*V problem

   \param A00 Input - A_00 
   \param ev0 Output - eigenvalue
*/
inline
void eigenvalues1(const double A00,double* ev0) {

   *ev0=A00;

}
/**
   \brief
   solves a 2x2 eigenvalue A*V=ev*V problem for symmetric A

   \param A00 Input - A_00 
   \param A01 Input - A_01 
   \param A11 Input - A_11
   \param ev0 Output - smallest eigenvalue
   \param ev1 Output - largest eigenvalue
*/
inline
void eigenvalues2(const double A00,const double A01
                                 ,const double A11,
                 double* ev0, double* ev1) {
      const register double trA=(A00+A11)/2.;
      const register double A_00=A00-trA;
      const register double A_11=A11-trA;
      const register double s=sqrt(A01*A01-A_00*A_11);
      *ev0=trA-s;
      *ev1=trA+s;
}
/**
   \brief
   solves a 3x3 eigenvalue A*V=ev*V problem for symmetric A

   \param A00 Input - A_00 
   \param A01 Input - A_01 
   \param A02 Input - A_02 
   \param A11 Input - A_11 
   \param A12 Input - A_12 
   \param A22 Input - A_22 
   \param ev0 Output - smallest eigenvalue
   \param ev1 Output - eigenvalue
   \param ev2 Output - largest eigenvalue
*/
inline
void eigenvalues3(const double A00, const double A01, const double A02,
                                   const double A11, const double A12,
                                                     const double A22,
                 double* ev0, double* ev1,double* ev2) {

      const register double trA=(A00+A11+A22)/3.;
      const register double A_00=A00-trA;
      const register double A_11=A11-trA;
      const register double A_22=A22-trA;
      const register double A01_2=A01*A01;
      const register double A02_2=A02*A02;
      const register double A12_2=A12*A12;
      const register double p=A02_2+A12_2+A01_2+(A_00*A_00+A_11*A_11+A_22*A_22)/2.;
      const register double q=(A02_2*A_11+A12_2*A_00+A01_2*A_22)-(A_00*A_11*A_22+2*A01*A12*A02);
      const register double sq_p=sqrt(p/3.);
      register double z=-q/(2*pow(sq_p,3));
      if (z<-1.) {
         z=-1.;
      } else if (z>1.) {
         z=1.;
      }
      const register double alpha_3=acos(z)/3.;
      *ev2=trA+2.*sq_p*cos(alpha_3);
      *ev1=trA-2.*sq_p*cos(alpha_3+M_PI/3.);
      *ev0=trA-2.*sq_p*cos(alpha_3-M_PI/3.);
}
} // end of namespace
#endif
