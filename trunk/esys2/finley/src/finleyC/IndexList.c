/* $Id$ */

/**************************************************************/

/* Finley: Converting an element list into a matrix shape     */

/**************************************************************/

/* Copyrights by ACcESS Australia 2003,2004 */
/* Author: gross@access.edu.au */

/**************************************************************/

#include "Finley.h"
#include "ElementFile.h"
#include "System.h"
#include "IndexList.h"

/**************************************************************/
/* inserts the contributions from the element matrices of elements
   into the row index col. If symmetric is set, only the upper
   triangle of the matrix is stored. */

void Finley_IndexList_insertElements(Finley_IndexList* index_list, Finley_ElementFile* elements,
                                       int reduce_row_order, int packed_row_block_size, maybelong* row_Label,
                                       int reduce_col_order, int packed_col_block_size, maybelong* col_Label,
                                       int symmetric, Finley_SystemMatrixType matType) {
  maybelong e,kr,ir,kc,ic,NN_row,NN_col,i;
  Finley_IndexList * tmp_list;
  maybelong jr,jc,icol,irow,color;


  if (elements!=NULL) {
    maybelong NN=elements->ReferenceElement->Type->numNodes;
    maybelong id[NN],*row_node,*col_node;
    for (i=0;i<NN;i++) id[i]=i;
    if (reduce_col_order) {
       col_node=elements->ReferenceElement->Type->linearNodes;
       NN_col=elements->LinearReferenceElement->Type->numNodes;
    } else {
       col_node=id;
       NN_col=elements->ReferenceElement->Type->numNodes;
    }
    if (reduce_row_order) {
       row_node=elements->ReferenceElement->Type->linearNodes;
       NN_row=elements->LinearReferenceElement->Type->numNodes;
    } else {
       row_node=id;
       NN_row=elements->ReferenceElement->Type->numNodes;
    }

    #pragma omp parallel private(color)
    {
       switch(matType) {
       case CSR:
         if (symmetric) {
            for (color=0;color<elements->numColors;color++) {
               #pragma omp for private(e,kr,jr,kc,jc,ir,irow,ic,icol,tmp_list) schedule(static)
               for (e=0;e<elements->numElements;e++) {
                  if (elements->Color[e]==color) {
                     for (kr=0;kr<NN_row;kr++) {
                        jr=row_Label[elements->Nodes[INDEX2(row_node[kr],e,NN)]];
                        for (ir=0;ir<packed_row_block_size;ir++) {
                           irow=ir+packed_row_block_size*jr;
                           tmp_list=&(index_list[irow]);
                           for (kc=0;kc<NN_col;kc++) {
                              jc=col_Label[elements->Nodes[INDEX2(col_node[kc],e,NN)]];
                              for (ic=0;ic<packed_col_block_size;ic++) {
                                 icol=ic+packed_col_block_size*jc;
                                 if (irow<=icol) Finley_IndexList_insertIndex(tmp_list,icol);
                              }
                           }
                        }
                     }
                  }
               }
            }
         } else {
            for (color=0;color<elements->numColors;color++) {
               #pragma omp for private(e,kr,jr,kc,jc,ir,irow,ic,icol,tmp_list) schedule(static)
               for (e=0;e<elements->numElements;e++) {
                  if (elements->Color[e]==color) {
                     for (kr=0;kr<NN_row;kr++) {
                        jr=row_Label[elements->Nodes[INDEX2(row_node[kr],e,NN)]];
                        for (ir=0;ir<packed_row_block_size;ir++) {
                           irow=ir+packed_row_block_size*jr;
                           tmp_list=&(index_list[irow]);
                           for (kc=0;kc<NN_col;kc++) {
                              jc=col_Label[elements->Nodes[INDEX2(col_node[kc],e,NN)]];
                              for (ic=0;ic<packed_col_block_size;ic++) {                                  icol=ic+packed_col_block_size*jc;
                                 Finley_IndexList_insertIndex(tmp_list,icol);
                              }
                           }
                        }
                     }
                  }
               }
            }
         } /* if else */
         break;
       case CSC:
         if (symmetric) {
            for (color=0;color<elements->numColors;color++) {
               #pragma omp for private (e,kr,jr,kc,jc,ir,irow,ic,icol,tmp_list) schedule(static)
               for (e=0;e<elements->numElements;e++) {
                  if (elements->Color[e]==color) {
                     for (kc=0;kc<NN_col;kc++) {
                        jc=col_Label[elements->Nodes[INDEX2(col_node[kc],e,NN)]];
                        for (ic=0;ic<packed_col_block_size;ic++) {
                           icol=ic+packed_col_block_size*jc;
                           tmp_list=&(index_list[icol]);
                           for (kr=0;kr<NN_row;kr++) {
                              jr=row_Label[elements->Nodes[INDEX2(row_node[kr],e,NN)]];
                              for (ir=0;ir<packed_row_block_size;ir++) {
                                 irow=ir+packed_row_block_size*jr;
                                 if (irow<=icol) Finley_IndexList_insertIndex(tmp_list,irow);
                              }
                           }
                        }
                     }
                  }
               }
            }
         } else {
           for (color=0;color<elements->numColors;color++) {
               #pragma omp for private (e,kr,jr,kc,jc,ir,irow,ic,icol,tmp_list) schedule(static)
               for (e=0;e<elements->numElements;e++) {
                  if (elements->Color[e]==color) {
                     for (kc=0;kc<NN_col;kc++) {
                        jc=col_Label[elements->Nodes[INDEX2(col_node[kc],e,NN)]];
                        for (ic=0;ic<packed_col_block_size;ic++) {
                           icol=ic+packed_col_block_size*jc;
                           tmp_list=&(index_list[icol]);
                           for (kr=0;kr<NN_row;kr++) {
                              jr=row_Label[elements->Nodes[INDEX2(row_node[kr],e,NN)]];
                              for (ir=0;ir<packed_row_block_size;ir++) {
                                 irow=ir+packed_row_block_size*jr;
                                 Finley_IndexList_insertIndex(tmp_list,irow);
                              }
                           }
                        }
                     }
                  }
               }
            }
         } /* if else */
       } /* switch matType */
    }
  }
  return;
}

/* inserts row index row into the Finley_IndexList in if it does not exist */

void Finley_IndexList_insertIndex(Finley_IndexList* in, maybelong index) {
  int i;
  /* is index in in? */
  for (i=0;i<in->n;i++) {
    if (in->index[i]==index) return;
  }
  /* index could not be found */
  if (in->n==INDEXLIST_LENGTH) {
     /* if in->index is full check the extension */
     if (in->extension==NULL) {
        in->extension=(Finley_IndexList*) TMPMEMALLOC(sizeof(Finley_IndexList));
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

int Finley_IndexList_count(Finley_IndexList* in) {
  if (in==NULL) {
     return 0;
  } else {
     return (in->n)+Finley_IndexList_count(in->extension);
  }
}

/* count the number of row indices in the Finley_IndexList in */

void Finley_IndexList_toArray(Finley_IndexList* in, maybelong* array) {
  int i;
  if (in!=NULL) {
    for (i=0;i<in->n;i++) array[i]=in->index[i]+INDEX_OFFSET;
    Finley_IndexList_toArray(in->extension,&(array[in->n]));
  }
}

/* deallocates the Finley_IndexList in by recursive calls */

void Finley_IndexList_free(Finley_IndexList* in) {
  if (in!=NULL) {
    Finley_IndexList_free(in->extension);
    TMPMEMFREE(in);
  }
}

/*
 * $Log$
 * Revision 1.3  2004/12/15 03:48:45  jgs
 * *** empty log message ***
 *
 * Revision 1.1.1.1  2004/10/26 06:53:57  jgs
 * initial import of project esys2
 *
 * Revision 1.1.2.2  2004/10/26 06:36:39  jgs
 * committing Lutz's changes to branch jgs
 *
 * Revision 1.2  2004/10/13 01:53:42  gross
 * bug in CSC assembling fixed
 *
 * Revision 1.1  2004/07/02 04:21:13  gross
 * Finley C code has been included
 *
 *
 */
