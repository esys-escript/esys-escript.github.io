#!/usr/bin/env python

import os
import inspect
import sys

if len(sys.argv)!=4:
  sys.stderr.write('Usage: startdir startpackage outputdirectory\n')
  sys.exit(1)

#startdir='./esys'
#startpackage='esys'
#outdir='doctest'

pathdir=sys.argv[1]
startpackage=sys.argv[2]
startdir=os.path.join(pathdir, startpackage)
outdir=sys.argv[3]

def dumpPackage(mname, ignorelist, modset):
  modset.add(mname)
  print "Starting dump on "+mname+' with ignore at '+str(ignorelist)
  pack=open(os.path.join(outdir,mname+'.rst'),'w')
  pack.write(mname+' Package\n')
  pack.write('='*len(mname)+'========\n\n')
  pack.write('.. py:module:: '+mname+'\n\n')
  #Automodule does not seem to do what we want so we need to drill down
  exec('import '+mname+' as PP')
  clist=[]
  flist=[]
  vlist=[]
  for (name, mem) in inspect.getmembers(PP):
      if inspect.ismodule(mem):
        if not name in ignorelist:
           try:
             ppfile=inspect.getfile(PP)
             memfile=inspect.getfile(mem)
           except:
             continue    #It will be a builtin module
           ppdir=ppfile[:ppfile.rfind(os.path.sep)]
           memdir=memfile[:memfile.rfind(os.path.sep)]
           if ppdir==memdir:
              print "About to dump "+name
              dumpPackage(mem.__name__, [], modset)
              print "Dump of "+mname+" complete"
	#pack.write('Module '+name+'\n')
      elif inspect.isclass(mem):
	clist+=[(name, mem)]
      elif inspect.isfunction(mem):
	flist+=[(name, mem)]
      else:
	if type(mem).__module__+'.'+type(mem).__name__=='Boost.Python.function':
	  flist+=[(name, mem)]
	else:
	  vlist+=[(name, mem)]
  pack.write('Classes\n')
  pack.write('-------\n')
  for (name, mem) in clist:
      pack.write('* `'+name+'`\n')
  pack.write('\n')
  for (name, mem) in clist:
    pack.write('.. autoclass:: '+name+'\n')
    pack.write('   :members:\n   :undoc-members:\n\n')
  pack.write('\n')
    
  pack.write('Functions\n')
  pack.write('---------\n')
  for (name, mem) in flist:
    pack.write('.. autofunction:: '+name+'\n')
  pack.write('\n')
    
  pack.write('Others\n')
  pack.write('------\n')
  for (name, mem) in vlist:
    pack.write('* '+name+'\n')
  pack.write('\n')
  pack.close()

def listmods():
  W=os.walk(startdir,topdown=True)
  sys.path.append(pathdir)
  main=open(os.path.join(outdir,'index.rst'),'w')
  main.write('.. Generated by Joel\'s script\n\n')
  main.write('Documentation for esys.escript\n')
  main.write('==============================\n')
  main.write('\n')
  main.write('Contents:\n\n')
  main.write('.. toctree::\n')
  main.write('   :maxdepth: 4\n')
  main.write('\n')
  modset=set()
  for z in W:
    if z[0].endswith('__pycache__'): continue
    print "Beginning ",z[0]
    # Now make the package name
    n=startpackage+'.'.join(z[0][len(startdir):].split(os.path.sep))
    dumpPackage(n, z[1], modset)
    print "-------------"+n
    
    for m in z[2]:	#This will list the files
      if m.split('.')[1]=='pyc' and m!='__init__.pyc':
	print ".."+n+"."+m
  l=list(modset)
  l.sort()
  for n in l:
      main.write("   "+n+"\n")
  main.write('\n')
  main.write('Indices and Tables\n')
  main.write('==================\n')
  main.write('\n')
  main.write('* :ref:`genindex`\n')
  main.write('* :ref:`modindex`\n')
  main.write('\n')
  main.close()	
    
    
listmods()    
