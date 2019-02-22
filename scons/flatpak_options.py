
##############################################################################
#
# Copyright (c) 2003-2018 by The University of Queensland
# http://www.uq.edu.au
#
# Primary Business: Queensland, Australia
# Licensed under the Apache License, version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
#
# Development until 2012 by Earth Systems Science Computational Center (ESSCC)
# Development 2012-2013 by School of Earth Sciences
# Development from 2014 by Centre for Geoscience Computing (GeoComp)
#
##############################################################################

# This is a template configuration file for escript on Debian/GNU Linux.
# Refer to README_FIRST for usage instructions.

escript_opts_version = 203
#cxx_extra = '-Wno-literal-suffix'
openmp = True
umfpack=True
silo=True
trilinos=True

import os

cxx_extra='-w'

prefix='/app'

boost_prefix=['/app/include','/app/lib']
netcdf = 4
netcdf_prefix=['/app/include','/app/lib']
umfpack_prefix = ['/app/include','/app/lib']
umfpack_libs = ['umfpack', 'openblas', 'amd']
lapack_prefix = ['/app/include/', '/app/lib']
silo_prefix = ['/app/include/', '/app/lib']
silo_libs = ['silo','hdf5']
trilinos_prefix = ['/app/include/', '/app/lib']

p3name = ''
for x in os.listdir("/app/lib"):
  if x.startswith('libboost_python3') and x.endswith('.so'):
    p3name=x
    break

# boost-python library/libraries to link against
boost_libs = [p3name[3:-3]]

# this can be used by options files importing us
boost_py3_libs = [p3name[3:-3]]