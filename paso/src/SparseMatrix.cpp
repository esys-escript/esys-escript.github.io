
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


/****************************************************************************/

/* Paso: SparseMatrix */

/****************************************************************************/

/* Author: Lutz Gross, l.gross@uq.edu.au */

/****************************************************************************/

#include "Paso.h"
#include "SparseMatrix.h"
#include "MKL.h"
#include "Preconditioner.h"
#include "UMFPACK.h"
#include "TRILINOS.h"
#include "mmio.h"

/****************************************************************************/

namespace paso {

static void swap( index_t*, index_t*, double*, int, int );
static void q_sort( index_t*, index_t*, double*, int, int );
/*static void print_entries( index_t*, index_t*, double* );*/

static int M, N, nz;

/* debug: print the entries */
/*
void print_entries(index_t *r, index_t *c, double *v)
{
    for(int i=0; i<nz; i++)
        printf("(%ld, %ld) == %e\n", (long)r[i], (long)c[i], v[i]);
}
*/

/* swap function */
void swap( index_t *r, index_t *c, double *v, int left, int right )
{
    double v_temp;
    index_t temp;

    temp = r[left];
    r[left] = r[right];
    r[right] = temp;

    temp = c[left];
    c[left] = c[right];
    c[right] = temp;

    v_temp = v[left];
    v[left] = v[right];
    v[right] = v_temp;
}

void q_sort( index_t *row, index_t *col, double *val, int begin, int end )
{
    int l, r;
    index_t pivot, lval;

    if( end > begin )
    {
        pivot = N * row[begin] + col[begin];
        l = begin + 1;
        r = end;

        while( l < r )
        {
            lval = N * row[l] + col[l];
            if( lval < pivot )
                l++;
            else
            {
                r--;
                swap( row, col, val, l, r );
            }
        }
        l--;
        swap( row, col, val, begin, l );
        q_sort( row, col, val, begin, l );
        q_sort( row, col, val, r, end );
    }
}


/* Allocates a SparseMatrix of given type using the given matrix pattern.
   Values are initialized with zero.
   If patternIsUnrolled and type & MATRIX_FORMAT_BLK1, it is assumed that the
   pattern is already unrolled to match the requested block size
   and offsets. Otherwise unrolling and offset adjustment will be performed.
*/
SparseMatrix* SparseMatrix_alloc(SparseMatrixType type, Pattern_ptr pattern,
                                 int row_block_size, int col_block_size,
                                 bool patternIsUnrolled)
{
    SparseMatrix* out=NULL;
    SparseMatrixType pattern_format_out;
    bool unroll=FALSE;

    if (patternIsUnrolled) {
        if (! XNOR(type & MATRIX_FORMAT_OFFSET1, pattern->type & MATRIX_FORMAT_OFFSET1) ) {
            Esys_setError(TYPE_ERROR,"SparseMatrix_alloc: requested offset and pattern offset do not match.");
            return NULL;
        }
    }
    /* do we need to apply unrolling? */
    unroll
            /* we don't like non-square blocks */
        =   (row_block_size!=col_block_size)
#ifndef USE_LAPACK
            /* or any block size bigger than 3 */
            ||  (col_block_size>3)
# endif
            /* or if block size one requested and the block size is not 1 */
            ||  ((type & MATRIX_FORMAT_BLK1) &&  (col_block_size>1) )
            /* offsets don't match */
            || ( (type & MATRIX_FORMAT_OFFSET1) != ( pattern->type & MATRIX_FORMAT_OFFSET1) );

    pattern_format_out= (type & MATRIX_FORMAT_OFFSET1)? MATRIX_FORMAT_OFFSET1:  MATRIX_FORMAT_DEFAULT;

    Esys_resetError();
    out=new SparseMatrix;
    out->val=NULL;
    out->reference_counter=1;
    out->type=type;
    out->solver_package=PASO_PASO;
    out->solver_p=NULL;

    /* ====== compressed sparse columns === */
    if (type & MATRIX_FORMAT_CSC) {
        if (unroll) {
            if (patternIsUnrolled) {
                out->pattern=pattern;
            } else {
                out->pattern=pattern->unrollBlocks(pattern_format_out, col_block_size, row_block_size);
            }
            out->row_block_size=1;
            out->col_block_size=1;
        } else {
            out->pattern=pattern->unrollBlocks(pattern_format_out, 1, 1);
            out->row_block_size=row_block_size;
            out->col_block_size=col_block_size;
        }
        if (Esys_noError()) {
            out->numRows = out->pattern->numInput;
            out->numCols = out->pattern->numOutput;
        }

    } else {
    /* ====== compressed sparse row === */
        if (unroll) {
            if (patternIsUnrolled) {
                out->pattern=pattern;
            } else {
                out->pattern=pattern->unrollBlocks(pattern_format_out, row_block_size, col_block_size);
            }
            out->row_block_size=1;
            out->col_block_size=1;
        } else {
            out->pattern=pattern->unrollBlocks(pattern_format_out, 1, 1);
            out->row_block_size=row_block_size;
            out->col_block_size=col_block_size;
        }
        if (Esys_noError()) {
            out->numRows = out->pattern->numOutput;
            out->numCols = out->pattern->numInput;
        }
    }
    if (Esys_noError()) {
        if (type & MATRIX_FORMAT_DIAGONAL_BLOCK) {
            out->block_size=MIN(out->row_block_size,out->col_block_size);
        } else {
            out->block_size=out->row_block_size*out->col_block_size;
        }
        out->len=(size_t)(out->pattern->len)*(size_t)(out->block_size);

        out->val=new double[out->len];
        SparseMatrix_setValues(out, DBLE(0));
    }
    /* all done: */
    if (Esys_noError()) {
        return out;
    } else {
        SparseMatrix_free(out);
        return NULL;
    }
}

/* returns a reference to SparseMatrix in */

SparseMatrix* SparseMatrix_getReference(SparseMatrix* in)
{
   if (in!=NULL) ++(in->reference_counter);
   return in;
}

/* deallocates a SparseMatrix: */

void SparseMatrix_free(SparseMatrix* in)
{
  if (in!=NULL) {
     in->reference_counter--;
     if (in->reference_counter<=0) {
        switch(in->solver_package) {

            case PASO_SMOOTHER:
               Paso_Preconditioner_LocalSmoother_free((Paso_Preconditioner_LocalSmoother*) in->solver_p);
               break;

            case PASO_MKL:
               Paso_MKL_free(in); /* releases solver_p */
               break;

            case PASO_UMFPACK:
               Paso_UMFPACK_free(in); /* releases solver_p */
               break;
        }
        delete[] in->val;
        delete in;
     }
   }
}

SparseMatrix* SparseMatrix_loadMM_toCSR( char *fileName_p )
{
    index_t *col_ind = NULL;
    index_t *row_ind = NULL;
    index_t *row_ptr = NULL;
    double *val = NULL;
    FILE *fileHandle_p = NULL;
    SparseMatrix *out = NULL;
    int i, curr_row, scan_ret;
    MM_typecode matrixCode;
    Esys_resetError();

    /* open the file */
    fileHandle_p = fopen( fileName_p, "r" );
    if( fileHandle_p == NULL )
    {
        Esys_setError(IO_ERROR, "SparseMatrix_loadMM_toCSR: Cannot open file for reading.");
        return NULL;
    }

    /* process banner */
    if( mm_read_banner(fileHandle_p, &matrixCode) != 0 )
    {
        Esys_setError(IO_ERROR, "SparseMatrix_loadMM_toCSR: Error processing MM banner.");
        fclose( fileHandle_p );
        return NULL;
    }
    if( !(mm_is_real(matrixCode) && mm_is_sparse(matrixCode) && mm_is_general(matrixCode)) )
    {
        Esys_setError(TYPE_ERROR,"SparseMatrix_loadMM_toCSR: found Matrix Market type is not supported.");
        fclose( fileHandle_p );
        return NULL;
    }

    /* get matrix size */
    if( mm_read_mtx_crd_size(fileHandle_p, &M, &N, &nz) != 0 )
    {
        Esys_setError(IO_ERROR, "SparseMatrix_loadMM_toCSR: Could not parse matrix size.");
        fclose( fileHandle_p );
        return NULL;
    }

    /* prepare storage */
    col_ind = new index_t[nz];
    row_ind = new index_t[nz];
    val = new  double [nz];
    row_ptr = new index_t[(M+1)];

    /* perform actual read of elements */
    for( i=0; i<nz; i++ )
    {
        scan_ret = fscanf( fileHandle_p, "%d %d %le\n", &row_ind[i], &col_ind[i], &val[i] );
        if (scan_ret!=3)
        {
            delete[] val;
            delete[] row_ind;
            delete[] col_ind;
            delete[]row_ptr;
            fclose(fileHandle_p);
            return NULL;
        }
        row_ind[i]--;
        col_ind[i]--;
    }
    fclose( fileHandle_p );

    /* sort the entries */
    q_sort( row_ind, col_ind, val, 0, nz );

    /* setup row_ptr */
    curr_row = 0;
    for( i=0; (i<nz && curr_row<M); curr_row++ )
    {
        while( row_ind[i] != curr_row )
            i++;
        row_ptr[curr_row] = i;
    }
    row_ptr[M] = nz;

    Pattern_ptr mainPattern(new Pattern(MATRIX_FORMAT_DEFAULT, M, N,
                                        row_ptr, col_ind));
    out  = SparseMatrix_alloc(MATRIX_FORMAT_DEFAULT, mainPattern, 1, 1, TRUE);
    /* copy values and cleanup temps */
    for( i=0; i<nz; i++ ) out->val[i] = val[i];

    delete[] val;
    delete[] row_ind;
    return out;
}


void SparseMatrix_saveMM(const SparseMatrix* A_p, const char* fileName_p)
{
   FILE * fileHandle_p = NULL;
   dim_t N,M,i,j, irow, icol, ib, irb, icb, iptr;
   MM_typecode matcode;
   const dim_t col_block_size = A_p->col_block_size;
   const dim_t row_block_size = A_p->row_block_size;
   const dim_t block_size = A_p->block_size;
   const index_t offset=(A_p->type & MATRIX_FORMAT_OFFSET1 ? 1:0);

   if (col_block_size !=row_block_size) {
      Esys_setError(TYPE_ERROR, "SparseMatrix_saveMM: currently only square blocks are supported.");
      return;
   }

   /* open the file */
   fileHandle_p = fopen(fileName_p, "w");
   if (fileHandle_p==NULL) {
      Esys_setError(IO_ERROR,"SparseMatrix_saveMM: File could not be opened for writing");
      return;
   }
   if (A_p->type & MATRIX_FORMAT_CSC) {
      Esys_setError(TYPE_ERROR,"SparseMatrix_saveMM does not support CSC yet.");
   } else {
      mm_initialize_typecode(&matcode);
      mm_set_matrix(&matcode);
      mm_set_coordinate(&matcode);
      mm_set_real(&matcode);

      N=SparseMatrix_getNumRows(A_p);
      M=SparseMatrix_getNumCols(A_p);
      mm_write_banner(fileHandle_p, matcode);
      mm_write_mtx_crd_size(fileHandle_p, N*row_block_size, M*col_block_size, A_p->pattern->ptr[N]*block_size);

      if (A_p->type & MATRIX_FORMAT_DIAGONAL_BLOCK) {
         for (i=0; i<N; i++) {
            for (iptr = A_p->pattern->ptr[i]-offset;iptr<A_p->pattern->ptr[i+1]-offset; ++iptr) {
               j=A_p->pattern->index[iptr]-offset;
               for (ib=0;ib<block_size;ib++) {
                  irow=ib+row_block_size*i;
                  icol=ib+col_block_size*j;
                  fprintf(fileHandle_p, "%d %d %25.15e\n", irow+1, icol+1, A_p->val[iptr*block_size+ib]);
               }
            }
         }
      } else {
         for (i=0; i<N; i++) {
            for (iptr = A_p->pattern->ptr[i]-offset;iptr<A_p->pattern->ptr[i+1]-offset; ++iptr) {
               j=A_p->pattern->index[iptr]-offset;
               for (irb=0;irb<row_block_size;irb++) {
                  irow=irb+row_block_size*i;
                  for (icb=0;icb<col_block_size;icb++) {
                     icol=icb+col_block_size*j;
                     fprintf(fileHandle_p, "%d %d %25.15e\n", irow+1, icol+1, A_p->val[iptr*block_size+irb+row_block_size*icb]);
                  }
               }
            }
         }
      }
   }
   /* close the file */
   fclose(fileHandle_p);
   return;
}

index_t* SparseMatrix_borrowMainDiagonalPointer(const SparseMatrix* A_p)
{
    return A_p->pattern->borrowMainDiagonalPointer();
}

dim_t SparseMatrix_getNumColors(const SparseMatrix* A_p)
{
   return A_p->pattern->getNumColors();
}

index_t* SparseMatrix_borrowColoringPointer(const SparseMatrix* A_p)
{
   return A_p->pattern->borrowColoringPointer();
}

dim_t SparseMatrix_maxDeg(const SparseMatrix* A_p)
{
   return A_p->pattern->maxDeg();
}

dim_t SparseMatrix_getTotalNumRows(const SparseMatrix* A)
{
   return A->numRows * A->row_block_size;
}

dim_t SparseMatrix_getTotalNumCols(const SparseMatrix* A)
{
   return A->numCols * A->col_block_size;
}

dim_t SparseMatrix_getNumRows(const SparseMatrix* A)
{
   return A->numRows;
}

dim_t SparseMatrix_getNumCols(const SparseMatrix* A)
{
   return A->numCols;
}

double SparseMatrix_getSize(const SparseMatrix* A)
{
   if (A!=NULL) {
      return DBLE(A->len);
   } else {
      return DBLE(0.);
   }
}

double SparseMatrix_getSparsity(const SparseMatrix* A)
{
    return SparseMatrix_getSize(A)/(DBLE(SparseMatrix_getTotalNumRows(A))*DBLE(SparseMatrix_getTotalNumCols(A)));
}

} // namespace paso

