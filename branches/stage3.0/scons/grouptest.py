########################################################
#
# Copyright (c) 2003-2009 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au/esscc
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

__copyright__="""Copyright (c) 2003-2009 by University of Queensland
Earth Systems Science Computational Center (ESSCC)
http://www.uq.edu.au/esscc
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"



class GroupTest:
    def __init__(self, exec_cmd, evars, python_dir, working_dir, test_list, single_processor_only=False):
	self.python_dir=python_dir
	self.working_dir=working_dir
	self.test_list=test_list
	self.exec_cmd=exec_cmd
	self.evars=evars
	self.mkdirs=[]
        self.single_processor_only=single_processor_only
	
    def makeDir(self,dirname):
    	self.mkdirs.append(dirname)

    def makeHeader(build_platform):
	res="#!/bin/bash\n"
	res=res+"\n#############################################\n"
	res=res+"# This file is autogenerated by scons.\n"
	res=res+"# It will be regenerated each time scons is run\n"
	res=res+"#############################################\n\n"
	res=res+"function failed()\n{\n  echo ""Execution failed for $@""\n  exit 1\n}\n"
	res=res+"if [ $# -ne 1 ]\nthen\n echo Usage: $0 wrapper_options\necho Runs all unit tests. Options must be a single string.\nexit 2\nfi\n"
	res=res+'CMDSTR="getopt -uq -o p:n: -- $1"\nSTR=`$CMDSTR`\nNUMPROCS=1\n'
	res=res+'NUMNODES=1\n#This little complication is required because set --\n'
	res=res+'#does not seem to like -n as the first positional parameter\n'
	res=res+'STATE=0\nfor name in $STR\ndo \n'
	res=res+'case $STATE in\n'
	res=res+'     0) case $name in\n'
	res=res+'	  -n) STATE=1;;\n'
	res=res+'	  -p) STATE=2;;\n'
	res=res+'	  --) break 2;;\n'
	res=res+'        esac;;\n'
	res=res+'     1) if [ $name == "--" ];then break; fi; NUMNODES=$name; STATE=0;;\n'
	res=res+'     2) if [ $name == "--" ];then break; fi; NUMPROCS=$name; STATE=0;;\n'
	res=res+'   esac\n'
	res=res+'done\n'
	res=res+'let MPIPROD="$NUMPROCS * $NUMNODES"\n'
	res=res+"\nexport LD_LIBRARY_PATH=`pwd`/lib:$LD_LIBRARY_PATH\n"
	if build_platform=='darwin':
		res=res+"export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH\n"
	res=res+"\nexport OLD_PYTHON=`pwd`:$PYTHONPATH\nBINRUNNER=\"`pwd`/bin/escript -b $1\"\nPYTHONRUNNER=\"`pwd`/bin/escript $1\"\nBATCH_ROOT=`pwd`\n"
	res=res+"BUILD_DIR=$BATCH_ROOT/build/"+build_platform
	res=res+"\nif [ ! -d $BUILD_DIR ]\nthen\n echo Can not find build directory $BUILD_DIR\n exit 2\nfi\n" 
	#res=res+"if [ $# -lt 2 ]\nthen\n echo Usage: $0 bin_run_cmd python_run_cmd\n exit 2\nfi\n"
	return res
    makeHeader=staticmethod(makeHeader)

    def makeString(self):
	res=""
        if self.single_processor_only:
            res+="if [ $MPIPROD -le 1 ]; then\n"
            tt="\t"
        else:
            tt=""
	for d in self.mkdirs:
	    res=res+tt+"if [ ! -d "+str(d)+" ]\n"+tt+"then\n"+tt+"\tmkdir "+d+"\n"+tt+"fi\n"
	for v in self.evars:
	    res=res+tt+"export "+str(v[0])+"="+str(v[1])+"\n"
        if len(self.python_dir)>0:
	    res=res+tt+"export PYTHONPATH="+self.python_dir+":$OLD_PYTHON"+"\n"+tt+"cd "+self.working_dir+"\n"
        else:
	    res=res+tt+"export PYTHONPATH=$OLD_PYTHON"+"\n"+tt+"cd "+self.working_dir+"\n"
	for t in self.test_list:
	    res=res+tt+"echo Starting "+t+"\n"
	    res=res+tt+self.exec_cmd+' '+t+' || failed '+t+'\n'
	    res=res+tt+"echo Completed "+t+"\n"
        if self.single_processor_only:
            res+="fi\n"
	res=res+"\n"
	return res
	
