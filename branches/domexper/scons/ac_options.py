
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


mpi_path = '/opt/anupack/1.0/include'
mpi_lib_path = '/opt/anupack/1.0/lib'
mpi_libs = ['mpi']
mpi_flavour = "MPICH"

# locations of libs etc used by mkl
mkl_path = '/opt/intel-mkl/8.0/include'
mkl_lib_path ='/opt/intel-mkl/8.0/lib/64'
mkl_libs = ['mkl_solver', 'mkl_lapack', 'mkl_ipf']

# locations of libs etc used by SCSL
### scsl_path = '/opt/scsl-1.6.1.0/include/'
### scsl_lib_path = '/opt/scsl-1.6.1.0/lib'
### scsl_libs = ['scs_mp']

# locations of include files for python
python_path = '/home/escript/python-2.4.4/include/python2.4'
python_lib_path = '/home/escript/python-2.4.4/lib'
python_lib = 'python2.4'

# locations of libraries for boost (on ac use module load something/boost)
boost_path = '/home/escript/boost-1.33.1.ken/include/boost-1_33_1'
boost_lib_path = '/home/escript/boost-1.33.1.ken/lib'
boost_lib = ['boost_python-gcc-mt']

# locations of doc building executables
#doxygen_path = '/raid2/tools/doxygen/1.4.2/gcc-3.3.5/bin'
#epydoc_path = '/raid2/tools/epydoc/2.1/python-2.3.4/bin'

# locations of netcdf
useNetCDF = 'yes'
netCDF_path = "/opt/netcdf/3.6.2/gcc-4.1.2/include"
netCDF_lib_path = "/opt/netcdf/3.6.2/gcc-4.1.2/lib"
netCDF_libs = [ 'netcdf_c++', 'netcdf']

# locations of PAPI
# papi_path = '/data/raid2/toolspp4/papi/3.0.8.1/gcc-3.3.6/include'
# papi_lib_path = '/data/raid2/toolspp4/papi/3.0.8.1/gcc-3.3.6/lib'
# papi_libs = [ 'papi' ]

# c flags to use
cc_flags  = "-O3 -ftz -IPF_ftlacc- -IPF_fma -fno-alias -openmp -openmp_report0 -fno-alias -c99 -w1 -fpic"
cc_flags_debug  = '-g -O0 -openmp -openmp_report0 -c99 -ansi_alias -w1 -fpic'

# c++ flags to use
cxx_flags = '-ansi -ansi_alias'
cxx_flags_debug = '-ansi -UDOASSERT -DDOPROF'

# system specific libraries to link with
sys_libs = ['guide', 'irc']
