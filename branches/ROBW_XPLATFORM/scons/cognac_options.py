# locations of libs etc used by mkl
mkl_path = '/opt/intel_mkl/8.0.19/include'
mkl_lib_path = '/opt/intel_mkl/8.0.19/lib/64'
mkl_libs = ['mkl_solver', 'mkl_lapack', 'mkl_ipf']

# locations of libs etc used by SCSL
scsl_path = '/opt/scsl/1.6.1.0/include'
scsl_lib_path = '/opt/scsl/1.6.1.0/lib'
scsl_libs = ['scs_mp']
# locations of libs etc used by UMFPACK

# locations of include files for python
python_path = '/usr/include/python2.3'
python_lib = 'python2.3'

# locations of libraries for boost
boost_path = '/home/woo409/dev/boost_1_33_1'
boost_lib_path = '/home/woo409/dev/boost_1_33_1/altix_binary/lib'
boost_lib = 'boost_python-il-mt-1_33_1'

# c flags to use
cc_flags  = '-O3 -fpic -IPF_fma -ftz -openmp -openmp_report0 -mp1 -tpp2 -c99 -ansi_alias -w1'
cc_flags_debug  = '-g -O0 -fpic -openmp -openmp_report0 -tpp2 -c99 -ansi_alias -w1'

# c++ flags to use - only need to list the additional ones compared with cc_flags
cxx_flags = '-ansi'
cxx_flags_debug = '-ansi -DDOASSERT -DDOPROF'

# system specific libraries to link with
sys_libs = ['guide', 'irc']

# FIXME: OLD STUFF TO BE REMOVED
cc = 'icc'
cxx = 'icpc'
