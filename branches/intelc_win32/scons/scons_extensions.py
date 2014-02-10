
#          Copyright 2006 by ACcESS MNRF                   
#                                                          
#              http://www.access.edu.au                    
#       Primary Business: Queensland, Australia            
#  Licensed under the Open Software License version 3.0    
#     http://www.opensource.org/licenses/osl-3.0.php       
#                                                          


# Extensions to Scons

import py_compile
import sys
import os

# Code to build .pyc from .py
def build_py(target, source, env):
  py_compile.compile(str(source[0]), str(target[0]))
  return None

# Code to run unit_test executables
def runUnitTest(target, source, env):
  app = str(source[0].abspath)
  if not env.Execute(app):
    open(str(target[0]),'w').write("PASSED\n")
  else:
    return 1
  return None

def runPyUnitTest(target, source, env): 
   app = 'python '+str(source[0].abspath)
   if not env.Execute(app):
      open(str(target[0]),'w').write("PASSED\n")
   else:
     return 1
   return None