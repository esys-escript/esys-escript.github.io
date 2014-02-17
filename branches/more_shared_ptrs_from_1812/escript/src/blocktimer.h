
/*******************************************************
*
* Copyright (c) 2003-2008 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


#ifndef blocktimer_h
#define blocktimer_h

#include <stdio.h>
#include <search.h>
#include "system_dep.h"

/* Enable the block timer (or remove this and use -DBLOCKTIMER) */
/* # define BLOCKTIMER */

# define NUM_TIMERS 1024

ESCRIPT_DLL_API
void blocktimer_initialize();
ESCRIPT_DLL_API
void blocktimer_increment(__const char *name, double start_time);
ESCRIPT_DLL_API
int blocktimer_getOrCreateTimerId(__const char *name);
ESCRIPT_DLL_API
void blocktimer_reportSortByName();
ESCRIPT_DLL_API
void blocktimer_reportSortByTime();
ESCRIPT_DLL_API
double blocktimer_time();


#endif