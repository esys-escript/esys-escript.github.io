
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

/* Finley: Converting an element list into a matrix shape     */

/************************************************************************************/

#include "IndexList.h"

/* Translate from distributed/local array indices to global indices */

/************************************************************************************/
/* inserts the contributions from the element matrices of elements
   into the row index col. If symmetric is set, only the upper
   triangle of the matrix is stored. */

void Finley_IndexList_insertElements(Finley_IndexList* index_list, Finley_ElementFile* elements,
                                       bool_t reduce_row_order, index_t* row_map,
                                       bool_t reduce_col_order, index_t* col_map) {
  /* index_list is an array of linked lists. Each entry is a row (DOF) and contains the indices to the non-zero columns */
  index_t color;
  Finley_ReferenceElement*refElement; 
  dim_t e, kr, kc, NN_row, NN_col, icol, irow, NN, *row_node=NULL, *col_node=NULL, isub, numSub;
  if (elements!=NULL) {
    NN=elements->numNodes;
    refElement= Finley_ReferenceElementSet_borrowReferenceElement(elements->referenceElementSet, FALSE);
	   
    if (reduce_col_order) {
		  numSub=1;
          col_node=refElement->Type->linearNodes;
          NN_col=(refElement->LinearBasisFunctions->Type->numShapes) * (refElement->Type->numSides) ;
    } else {
		  numSub=refElement->Type->numSubElements;
          col_node=refElement->Type->subElementNodes;
          NN_col=(refElement->BasisFunctions->Type->numShapes) * (refElement->Type->numSides) ;
    }

    if (reduce_row_order) {
		  numSub=1;
          row_node=refElement->Type->linearNodes;
          NN_row=(refElement->LinearBasisFunctions->Type->numShapes) * (refElement->Type->numSides) ;
    } else {
		  numSub=refElement->Type->numSubElements;
          row_node=refElement->Type->subElementNodes;
          NN_row=(refElement->BasisFunctions->Type->numShapes) * (refElement->Type->numSides) ;
	}

	for (color=elements->minColor;color<=elements->maxColor;color++) {
           #pragma omp for private(e,irow,kr,kc,icol,isub) schedule(static)
           for (e=0;e<elements->numElements;e++) {
               if (elements->Color[e]==color) {
				   for (isub=0;isub<numSub; isub++) {
					   for (kr=0;kr<NN_row;kr++) {
						   irow=row_map[elements->Nodes[INDEX2(row_node[INDEX2(kr,isub,NN_row)],e,NN)]];
						   for (kc=0;kc<NN_col;kc++) {
							   icol=col_map[elements->Nodes[INDEX2(col_node[INDEX2(kc,isub,NN_col)],e,NN)]];
							   Finley_IndexList_insertIndex(&(index_list[irow]),icol);
						   }
					   }
				   }
               }
           }
       }
  }
  return;
}


void Finley_IndexList_insertElementsWithRowRange(Finley_IndexList* index_list, index_t firstRow, index_t lastRow,
                                                 Finley_ElementFile* elements, index_t* row_map, index_t* col_map)
{
/* this does not resolve macro elements */
	index_t color;
  dim_t e,kr,kc,icol,irow, NN;
  if (elements!=NULL) {
    NN=elements->numNodes;
    for (color=elements->minColor;color<=elements->maxColor;color++) {
           #pragma omp for private(e,irow,kr,kc,icol) schedule(static)
           for (e=0;e<elements->numElements;e++) {
               if (elements->Color[e]==color) {
                   for (kr=0;kr<NN;kr++) {
                     irow=row_map[elements->Nodes[INDEX2(kr,e,NN)]];
                     if ((firstRow<=irow) && (irow < lastRow)) {
                          irow-=firstRow;
                          for (kc=0;kc<NN;kc++) {
                              icol=col_map[elements->Nodes[INDEX2(kc,e,NN)]];
                              Finley_IndexList_insertIndex(&(index_list[irow]),icol);
                          }
                      }
                  }
               }
           }
    }
  }
}
void Finley_IndexList_insertElementsWithRowRangeNoMainDiagonal(Finley_IndexList* index_list, index_t firstRow, index_t lastRow,
                                                              Finley_ElementFile* elements, index_t* row_map, index_t* col_map)
{
  /* this does not resolve macro elements */
  index_t color;
  dim_t e,kr,kc,icol,irow, NN,irow_loc;
  if (elements!=NULL) {
    NN=elements->numNodes;
    for (color=elements->minColor;color<=elements->maxColor;color++) {
           #pragma omp for private(e,irow,kr,kc,icol,irow_loc) schedule(static)
           for (e=0;e<elements->numElements;e++) {
               if (elements->Color[e]==color) {
                   for (kr=0;kr<NN;kr++) {
                     irow=row_map[elements->Nodes[INDEX2(kr,e,NN)]];
                     if ((firstRow<=irow) && (irow < lastRow)) {
                          irow_loc=irow-firstRow;
                          for (kc=0;kc<NN;kc++) {
                              icol=col_map[elements->Nodes[INDEX2(kc,e,NN)]];
                              if (icol != irow) Finley_IndexList_insertIndex(&(index_list[irow_loc]),icol);
                          }
                      }
                  }
               }
           }
    }
  }
}

/* inserts row index row into the Finley_IndexList in if it does not exist */

void Finley_IndexList_insertIndex(Finley_IndexList* in, index_t index) {
  dim_t i;
  /* is index in in? */
  for (i=0;i<in->n;i++) {
    if (in->index[i]==index)  return;
  }
  /* index could not be found */
  if (in->n==INDEXLIST_LENGTH) {
     /* if in->index is full check the extension */
     if (in->extension==NULL) {
        in->extension=new Finley_IndexList;
        if (Finley_checkPtr(in->extension)) return;
        in->extension->n=0;
        in->extension->extension=NULL;
     }
     Finley_IndexList_insertIndex(in->extension,index);
  } else {
     /* insert index into in->index*/
     in->index[in->n]=index;
     in->n++;
  }
}

/* counts the number of row indices in the Finley_IndexList in */

dim_t Finley_IndexList_count(Finley_IndexList* in, index_t range_min,index_t range_max) {
  dim_t i;
  dim_t out=0;
  register index_t itmp;
  if (in==NULL) {
     return 0;
  } else {
    for (i=0;i<in->n;i++) {
          itmp=in->index[i];
          if ((itmp>=range_min) && (range_max>itmp)) ++out;
    }
     return out+Finley_IndexList_count(in->extension, range_min,range_max);
  }
}

/* count the number of row indices in the Finley_IndexList in */

void Finley_IndexList_toArray(Finley_IndexList* in, index_t* array, index_t range_min,index_t range_max, index_t index_offset) {
  dim_t i, ptr;
  register index_t itmp;
  if (in!=NULL) {
    ptr=0;
    for (i=0;i<in->n;i++) {
          itmp=in->index[i];
          if ((itmp>=range_min) && (range_max>itmp)) {
             array[ptr]=itmp+index_offset;
             ptr++;
          }

    }
    Finley_IndexList_toArray(in->extension,&(array[ptr]), range_min, range_max, index_offset);
  }
}

/* deallocates the Finley_IndexList in by recursive calls */

void Finley_IndexList_free(Finley_IndexList* in) {
  if (in!=NULL) {
    Finley_IndexList_free(in->extension);
    delete in;
  }
}

/* creates a Paso_pattern from a range of indices */
Paso_Pattern* Finley_IndexList_createPattern(dim_t n0, dim_t n,Finley_IndexList* index_list,index_t range_min,index_t range_max,index_t index_offset)
{
   dim_t *ptr=NULL;
   register dim_t s,i,itmp;
   index_t *index=NULL;
   Paso_Pattern* out=NULL;

   ptr=new index_t[n+1-n0];
   if (! Finley_checkPtr(ptr) ) {
       /* get the number of connections per row */
       #pragma omp parallel for schedule(static) private(i)
       for(i=n0;i<n;++i) {
              ptr[i-n0]=Finley_IndexList_count(&index_list[i],range_min,range_max);
       }
       /* accumulate ptr */
       s=0;
       for(i=n0;i<n;++i) {
               itmp=ptr[i-n0];
               ptr[i-n0]=s;
               s+=itmp;
       }
       ptr[n-n0]=s;
       /* fill index */
       index=new index_t[ptr[n-n0]];
       if (! Finley_checkPtr(index)) {
              #pragma omp parallel for schedule(static)
              for(i=n0;i<n;++i) {
                  Finley_IndexList_toArray(&index_list[i],&index[ptr[i-n0]],range_min,range_max,index_offset);
              }
              out=Paso_Pattern_alloc(MATRIX_FORMAT_DEFAULT,n-n0,range_max+index_offset,ptr,index);
       }
  }
  if (! Finley_noError()) {
        delete[] ptr;
        delete[] index;
        Paso_Pattern_free(out);
  }
  return out;
}