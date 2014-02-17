
/*****************************************************************************
*
* Copyright (c) 2003-2013 by University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development since 2012 by School of Earth Sciences
*
*****************************************************************************/


/************************************************************************************/

/*    assembles the system of numEq PDEs into the stiffness matrix S and right hand side F  */

/*      d_dirac_{k,m} u_m and y_dirac_k */

/*    u has p.numComp components in a 3D domain. The shape functions for test and solution must be identical  */
/*    and row_NS == row_NN                                                                                  */

/*    Shape of the coefficients: */

/*      d_dirac = p.numEqu x p.numComp  */
/*      y_dirac = p.numEqu   */


/************************************************************************************/


#include "Assemble.h"
#include "Util.h"
#ifdef _OPENMP
#include <omp.h>
#endif


/************************************************************************************/

void  Finley_Assemble_PDE_Points(Finley_Assemble_Parameters p,
                                 Finley_ElementFile* elements,
                                 Paso_SystemMatrix* Mat, escriptDataC* F,
                                 escriptDataC* d_dirac, escriptDataC* y_dirac) {

    index_t color, e, row_index;
    __const double  *d_dirac_p, *y_dirac_p;
    
    double *F_p=(requireWrite(F), getSampleDataRW(F,0));	/* use comma, to get around the mixed code and declarations thing */

    #pragma omp parallel private(color, d_dirac_p, y_dirac_p)
    {
          for (color=elements->minColor;color<=elements->maxColor;color++) {
             /*  open loop over all elements: */
             #pragma omp for private(e) schedule(static)
             for(e=0;e<elements->numElements;e++){
                if (elements->Color[e]==color) {
                   
		   d_dirac_p=getSampleDataRO(d_dirac, e);
                   y_dirac_p=getSampleDataRO(y_dirac, e);
		   
                   row_index=p.row_DOF[elements->Nodes[INDEX2(0,e,p.NN)]];
		   
		   if (NULL!=y_dirac_p)  Finley_Util_AddScatter(1,
                                                        &row_index,
                                                        p.numEqu,
                                                        y_dirac_p,
                                                        F_p, 
                                                        p.row_DOF_UpperBound);
		   
                   if (NULL!=d_dirac_p) Finley_Assemble_addToSystemMatrix(Mat,
                                                                   1,
                                                                   &row_index,
                                                                   p.numEqu,
                                                                   1,
                                                                   &row_index,
                                                                   p.numComp,
                                                                   d_dirac_p);
                } /* end color check */
             } /* end element loop */
         } /* end color loop */
   } /* end parallel region */
}