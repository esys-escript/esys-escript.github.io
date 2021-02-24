
##############################################################################
#
# Copyright (c) 2003-2020 by The University of Queensland
# http://www.uq.edu.au
#
# Primary Business: Queensland, Australia
# Licensed under the Apache License, version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
#
# Development until 2012 by Earth Systems Science Computational Center (ESSCC)
# Development 2012-2013 by School of Earth Sciences
# Development from 2014 by Centre for Geoscience Computing (GeoComp)
# Development from 2019 by School of Earth and Environmental Sciences
#
##############################################################################

# This is a template configuration file for escript on Debian/GNU Linux.
# Refer to README_FIRST for usage instructions.

escript_opts_version = 203

openmp = True

umfpack = True
umfpack_prefix = ['/usr/include/suitesparse', '/usr/lib']
umfpack_libs = ['umfpack', 'blas', 'amd']

pythoncmd="/usr/bin/python3"
pythonlibname = 'python3.9'
pythonlibpath = '/usr/lib/x86_64-linux-gnu/'
pythonincpath = '/usr/include/python3.9'

boost_python='boost_python39'
boost_prefix=['/usr/include','/usr/lib/x86_64-linux-gnu/']
