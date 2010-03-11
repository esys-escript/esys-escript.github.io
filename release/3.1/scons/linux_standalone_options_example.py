
########################################################
#
# Copyright (c) 2003-2010 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au/esscc
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

PKG_ROOT=""

# Example configuration for linux running gcc

# If you cannot use the default compiler flags set in SConstruct, then change them here
# C/C++ Compiler flags (always use cc_flags and either cc_optim or cc_debug)
# cc_flags		= '-ansi'
# cc_optim		= '-O2'
# cc_debug		= '-g'
omp_optim		= '-fopenmp'
omp_debug		= '-fopenmp'
#omp_libs		= ['gomp']
omp_libs		= []
#Do not link gomp unless you are sure you need to

# Use the default C/C++ flags but add something only for this host:
#cc_extra		= '-Wall -pedantic -isystem /usr/include/boost/ -isystem /usr/include/python2.5/ -Wno-sign-compare -Wno-long-long'
#cc_extra		= '-fopenmp'
# ld_extra		= ''
#cc_extra = '--std=c99'
#cxx_extra = ''

# Be picky about errors
# usepedantic		= 'no'

# Extra libraries
# sys_libs		= ['guide', 'pthread', 'stdc++']

# Python libraries
python_path		= PKG_ROOT+"/python/include/python2.6"
python_lib_path		= PKG_ROOT+"/python/lib"
python_libs		= 'python2.6'
# python_cmd		= 'python'

# Boost libraries
boost_path		= PKG_ROOT+"/boost/include/boost-1_39"
boost_lib_path		= PKG_ROOT+"/boost/lib"
boost_libs		= ['boost_python']

# Specify whether or not to use VTK
# usevtk		= 'yes'

# NetCDF
# usenetcdf		= 'yes'
netCDF_path		= PKG_ROOT+'/netcdf/include'
netCDF_lib_path		= PKG_ROOT+'/netcdf/lib'
# netCDF_libs		= ['netcdf_c++', 'netcdf']

# MKL
# usemkl		= 'yes'
# mkl_path		= '/sw/sdev/cmkl/10.0.2.18/include'
# mkl_lib_path		= '/sw/sdev/cmkl/10.0.2.18/lib/em64t'
# mkl_libs		= ['mkl_solver', 'mkl_em64t', 'mkl_core', 'guide', 'pthread']

# UMFPACK (requires AMD and BLAS)
# useumfpack		= 'yes'
# ufc_path		= '/sw/libs/umfpack/x86_64/gcc-4.1.2/umfpack-5.2/include'
# umf_path		= '/sw/libs/umfpack/x86_64/gcc-4.1.2/umfpack-5.2/include'
# umf_lib_path		= '/sw/libs/umfpack/x86_64/gcc-4.1.2/umfpack-5.2/lib'
# umf_libs		= ['umfpack']
# amd_path		= '/sw/libs/umfpack/x86_64/gcc-4.1.2/umfpack-5.2/include'
# amd_lib_path		= '/sw/libs/umfpack/x86_64/gcc-4.1.2/umfpack-5.2/lib'
# amd_libs		= ['amd']
# blas_path		= '/sw/libs/umfpack/x86_64/gcc-4.1.2/umfpack-5.2/include'
# blas_lib_path		= '/sw/libs/umfpack/x86_64/gcc-4.1.2/umfpack-5.2/lib'
# blas_libs		= ['blas']

# OpenMP
#useopenmp		= 'yes'

# MPICH2 (to run Escript use: module load mpich2/gcc-4.1.2/mpich2-1.0.7)
# usempi		= 'no'
# mpi_path		= '/home/Work/InstallArea/mpich2-1.0.7/include'
# mpi_lib_path		= '/home/Work/InstallArea/mpich2-1.0.7/lib'
# mpi_libs		= ['mpich', 'rt']
# mpi_flavour		= 'MPICH'

# MPICH2 for jumpshot (to run Escript use: module load mpich2/gcc-4.1.2/mpich2-1.0.7)
# mpi_path		= '/home/Work/InstallArea/mpich2-1.0.7/include'
# mpi_lib_path		= '/home/Work/InstallArea/mpich2-1.0.7/lib'
# mpi_libs		= ['lmpe', 'mpe', 'mpich', 'rt']
# mpi_flavour		= 'MPICH'

# ParMETIS (for use with MPI)
# useparmetis		= 'yes'
# parmetis_path		= '/home/Work/InstallArea/parmetis-3.1/include'
# parmetis_lib_path	= '/home/Work/InstallArea/parmetis-3.1/lib'
# parmetis_libs		= ['parmetis', 'metis']

# PAPI
# usepapi		= 'no'
# papi_path		= '/usr/include'
# papi_lib_path		= '/usr/lib'
# papi_libs		= ['papi']
# papi_instrument_solver	= 'no'

