
/* $Id$ */

/*******************************************************
 *
 *           Copyright 2003-2007 by ACceSS MNRF
 *       Copyright 2007 by University of Queensland
 *
 *                http://esscc.uq.edu.au
 *        Primary Business: Queensland, Australia
 *  Licensed under the Open Software License version 3.0
 *     http://www.opensource.org/licenses/osl-3.0.php
 *
 *******************************************************/

/**
\file esys_malloc.h
\ingroup Other
 */
//
// @(#) esys_malloc.h
//

#ifndef esys_malloc_h
#define esys_malloc_h

#ifdef _WIN32

#   include <python.h>

#   define ESYS_MALLOC PyMem_Malloc
#   define ESYS_FREE PyMem_Free
#   define ESYS_REALLOC PyMem_Realloc

#else

#   include <malloc.h>

#   define ESYS_MALLOC ::malloc
#   define ESYS_FREE ::free
#   define ESYS_REALLOC ::realloc

#endif

namespace esysUtils
{

   inline
   void *malloc(size_t len)
   {
      return ESYS_MALLOC(len);
   }

   inline
   void free(void *ptr)
   {
      ESYS_FREE(ptr);
      return;
   }

   inline
   void *realloc(void *ptr, size_t len)
   {
      return ESYS_REALLOC(ptr,len);
   }
}

#undef ESYS_MALLOC
#undef ESYS_FREE
#undef ESYS_REALLOC

#endif
