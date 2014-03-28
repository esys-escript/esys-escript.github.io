
/*****************************************************************************
*
* Copyright (c) 2003-2014 by University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development 2012-2013 by School of Earth Sciences
* Development from 2014 by Centre for Geoscience Computing (GeoComp)
*
*****************************************************************************/


/****************************************************************************

  Finley: Mesh

*****************************************************************************/

#include "Mesh.h"
#include "IndexList.h"

namespace finley {

/// returns a reference to the matrix pattern
paso::SystemMatrixPattern* Mesh::getPattern(bool reduce_row_order, bool reduce_col_order)
{
    paso::SystemMatrixPattern *out=NULL;
    resetError();
    /* make sure that the requested pattern is available */
    if (reduce_row_order) {
        if (reduce_col_order) {
            if (ReducedReducedPattern==NULL)
                ReducedReducedPattern=makePattern(reduce_row_order,reduce_col_order);
        } else {
            if (ReducedFullPattern==NULL)
                ReducedFullPattern=makePattern(reduce_row_order,reduce_col_order);
        }
    } else {
        if (reduce_col_order) {
            if (FullReducedPattern==NULL)
                FullReducedPattern=makePattern(reduce_row_order,reduce_col_order);
        } else {
            if (FullFullPattern==NULL)
                FullFullPattern=makePattern(reduce_row_order,reduce_col_order);
        }
    }
    if (noError()) {
        if (reduce_row_order) {
            if (reduce_col_order) {
                out=paso::SystemMatrixPattern_getReference(ReducedReducedPattern);
            } else {
                out=paso::SystemMatrixPattern_getReference(ReducedFullPattern);
            }
        } else {
            if (reduce_col_order) {
                out=paso::SystemMatrixPattern_getReference(FullReducedPattern);
            } else {
                out=paso::SystemMatrixPattern_getReference(FullFullPattern);
            }
        }
    }  
    return out;
}

paso::SystemMatrixPattern* Mesh::makePattern(bool reduce_row_order, bool reduce_col_order)
{
    paso::SystemMatrixPattern* out=NULL;
    paso::Pattern *main_pattern = NULL, *col_couple_pattern=NULL, *row_couple_pattern=NULL;
    paso::Connector *col_connector, *row_connector;
    paso::Distribution_ptr colDistribution, rowDistribution;
  
    resetError();

    int myNumColTargets, myNumRowTargets;
    int numColTargets, numRowTargets;
    const int *colTarget, *rowTarget;

    if (reduce_col_order) {
        myNumColTargets=Nodes->getNumReducedDegreesOfFreedom();
        numColTargets=Nodes->reducedDegreesOfFreedomMapping.getNumTargets();
        colTarget=Nodes->borrowTargetReducedDegreesOfFreedom();
        colDistribution=Nodes->reducedDegreesOfFreedomDistribution;
        col_connector=Nodes->reducedDegreesOfFreedomConnector;
    } else {
        myNumColTargets=Nodes->getNumDegreesOfFreedom();
        numColTargets=Nodes->degreesOfFreedomMapping.getNumTargets();
        colTarget=Nodes->borrowTargetDegreesOfFreedom();
        colDistribution=Nodes->degreesOfFreedomDistribution;
        col_connector=Nodes->degreesOfFreedomConnector;
    }

    if (reduce_row_order) {
        myNumRowTargets=Nodes->getNumReducedDegreesOfFreedom();
        numRowTargets=Nodes->reducedDegreesOfFreedomMapping.getNumTargets();
        rowTarget=Nodes->borrowTargetReducedDegreesOfFreedom();
        rowDistribution=Nodes->reducedDegreesOfFreedomDistribution;
        row_connector=Nodes->reducedDegreesOfFreedomConnector;
    } else {
        myNumRowTargets=Nodes->getNumDegreesOfFreedom();
        numRowTargets=Nodes->degreesOfFreedomMapping.getNumTargets();
        rowTarget=Nodes->borrowTargetDegreesOfFreedom();
        rowDistribution=Nodes->degreesOfFreedomDistribution;
        row_connector=Nodes->degreesOfFreedomConnector;
    }
    IndexListArray index_list(numRowTargets);
  
#pragma omp parallel
    {
        // insert contributions from element matrices into columns in indexlist:
        IndexList_insertElements(index_list, Elements, reduce_row_order,
                                 rowTarget, reduce_col_order, colTarget);
        IndexList_insertElements(index_list, FaceElements,
                                 reduce_row_order, rowTarget, reduce_col_order,
                                 colTarget);
        IndexList_insertElements(index_list, ContactElements,
                                 reduce_row_order, rowTarget, reduce_col_order,
                                 colTarget);
        IndexList_insertElements(index_list, Points, reduce_row_order,
                                 rowTarget, reduce_col_order, colTarget);
    }
 
    /* create pattern */
    main_pattern=paso::Pattern_fromIndexListArray(
            0, myNumRowTargets, index_list, 0, myNumColTargets, 0);
    col_couple_pattern=paso::Pattern_fromIndexListArray(
            0, myNumRowTargets, index_list, myNumColTargets,
            numColTargets, -myNumColTargets);
    row_couple_pattern=paso::Pattern_fromIndexListArray(
            myNumRowTargets, numRowTargets, index_list, 0, myNumColTargets, 0);

    // if everything is in order we can create the return value
    if (noError()) {
        out = new paso::SystemMatrixPattern(MATRIX_FORMAT_DEFAULT,
                rowDistribution, colDistribution, main_pattern,
                col_couple_pattern, row_couple_pattern,
                col_connector, row_connector);
    }
    paso::Pattern_free(main_pattern);
    paso::Pattern_free(col_couple_pattern);
    paso::Pattern_free(row_couple_pattern);
    Esys_MPIInfo_noError(MPIInfo);
    return out;
}

} // namespace finley

