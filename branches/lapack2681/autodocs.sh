#!/bin/bash

# Build all escript documentation on shake71 and put it on the web server
# in the proper place so the ESSCC twiki can find it. The build command is
#	scons docs

# If this fails make sure you have logged in to the repository and can
# do password-less svn to shake200.  Verify that you can do it by hand
# with the exact same svn checkout command (full host name) as used below.

# Run this nightly on shake71 via cron using:
# 0 1 * * 0-6 /home/Work/EscriptDev/Documentation/autodocs.sh > /home/Work/EscriptDev/Documentation/log 2>&1

# Requires:
#	svn checkout from shake200
#	scp to shake200 to upload new documentation to web site
#	epydoc
#	doxygen
#	latex
#	latex2html

export PATH="/home/Work/InstallArea/python-2.4.4/bin:$PATH"
export LD_LIBRARY_PATH="$DIR/sandbox/trunk/lib:/home/Work/InstallArea/python-2.4.4/lib"
export PYTHONPATH="$DIR/sandbox/trunk:/home/Work/InstallArea/numarray-1.5.2/lib"

DIR="/home/Work/EscriptDev/Documentation"

START=`date '+%Y/%m/%d %H:%M'`
RunDate=`date '+%Y_%m_%d'`

prependpath    () { test -d "$1" && export PATH="$1:$PATH"; }
prependldpath  () { test -d "$1" && export LD_LIBRARY_PATH="$1:$LD_LIBRARY_PATH"; }
prependpypath  () { test -d "$1" && export PYTHONPATH="$1:$PYTHONPATH"; }

# For compiling and running Escript
unset          PYTHONSTARTUP
export         PYTHONHOME=/home/Work/InstallArea/python-2.4.4
prependpath    /home/Work/InstallArea/python-2.4.4/bin
prependldpath  /home/Work/InstallArea/python-2.4.4/lib
prependpath    /home/Work/InstallArea/scons-0.98.5/bin
prependpypath  /home/Work/InstallArea/numarray-1.5.2/lib
prependldpath  /home/Work/InstallArea/mesa-7.0.3/usr/local/lib
prependldpath  /home/Work/InstallArea/vtk-5.0.4/lib
prependpypath  /home/Work/InstallArea/vtk-5.0.4/lib/python2.4/site-packages
prependpath    /home/Work/InstallArea/mpich2-1.0.7/bin
prependpath    /home/Work/InstallArea/mayavi-1.5/bin
prependpath    /home/Work/InstallArea/visit1.10.0/bin
prependpypath  /home/Work/InstallArea/epydoc-3.0.1/lib/python2.4/site-packages
prependpath    /home/Work/InstallArea/epydoc-3.0.1/bin


finish () {
  # state will be 'FAILURE' or 'SUCCESS'
  state="$1"
  date
  # Clean up the sandbox
  cd $DIR
  /bin/rm -rf sandbox
  END=`date '+%Y/%m/%d %H:%M'`
  # cat << END_MSG | mail -s "ESYS_TESTS docs $RunDate $state" k.steube@uq.edu.au j.fenwick1@uq.edu.au
  cat << END_MSG | mail -s "ESYS_TESTS docs $RunDate $state" k.steube@uq.edu.au kensteube@gmail.com
$2.
The tests ran from $START to $END
See the log file $DIR/log for info
This mail was sent by $0
running via cron as $LOGNAME on `hostname`.
END_MSG
  if [ "x$state" = "xFAILURE" ]; then
    exit 1
  fi
  exit 0
}

umask 022

cd $DIR			|| finish FAILURE "Could not cd to $DIR"

/bin/rm -rf sandbox
mkdir sandbox		|| finish FAILURE "Could not mkdir sandbox"
cd sandbox		|| finish FAILURE "Could not cd to sandbox"

echo "Checking out esys13/trunk from Subversion"
svn checkout https://shake200.esscc.uq.edu.au/svn/esys13/trunk || finish FAILURE "Could not checkout esys13/trunk"

# Generate documentation
echo "Generating documentation"

cd trunk							|| finish FAILURE "Could not cd to trunk"
mkdir release release/doc					|| finish FAILURE "Could not create release directory"
scons usedebug=yes usempi=no usewarnings=no docs		|| finish FAILURE "Could not run scons docs"
scp -r release/doc/* shake200:/home/www/esys/esys13/nightly	|| finish FAILURE "Could not copy documentation to nightly area"

echo "Cleaning up"

finish SUCCESS "Successfully ran 'scons docs' on `hostname`"
