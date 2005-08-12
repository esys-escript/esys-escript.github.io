#!/usr/bin/env python

# $Id$

"""
Make an mpeg movie from the pnm files in the current directory
"""

import os, sys, re
import getopt

(opts, args) = getopt.getopt(sys.argv[1:], 
	"s:o:f:p:h", 
	["framestem=", "output=", "format=", "pad=", "help"],
	)

def usage():
    print "Usage:"
    print "  make_movie -s <framestem> -o <output filename> -f <format> -p <pad>\n"
    print "  Arguments:"
    print "    -s/--framestem: The frame filename stem (the stuff before .pnm) (required)"
    print "    -o/--output: Output mpeg filename (optional)"
    print "    -f/--format: Input frame image format (optional)"
    print "    -p/--pad: How many frames to pad the movie (optional)"

mpegName = None
fnameStem = None
format = "pnm"  # if format not specified assume pnm
pad = 1

for option, arg in opts:
    if option in ('-s', '--stem'):
	fnameStem = arg
    elif option in ('-o', '--output'):
	mpegName = arg
    elif option in ('-f', '--format'):
	format = arg
    elif option in ('-p', '--pad'):
	pad = int(arg)
    elif option in ('-h', '--help'):
	usage()
	sys.exit(0)

if fnameStem is None:
    print "You must supply the stem of the frame filenames\n"
    usage()
    sys.exit(0)
if mpegName is None:
    mpegName = fnameStem + ".mpg"

# determine the number of files to convert
dirList = os.listdir('./')
r = re.compile( "%s\\d+\\.%s"%(fnameStem,format) )
count = 0  # counter for the number of files found
fnames = []
for fname in dirList:
    if r.match(fname):
	fnames.append(fname)
	count += 1

if count == 0:
    raise ValueError, "No matching files found"

# do a conversion if necessary
if format != "pnm":
    print "Converting frames to pnm"
    r = re.compile("%s\\d+\\." % (fnameStem))
    for fname in fnames:
	# strip off the bit after the last dot
	front = r.findall(fname)
	front = front[0]
	# make the conversion string to pass to 'convert'
	convString = "convert %s%s %spnm" % (front, format, front)
	retVal = os.system(convString)
	if retVal != 0:
	    raise SystemError, "Conversion of %s%s failed" % (front, format)

# use ppmtompeg to convert the pnms to a movie
print "Making movie"

# now automatically generate the ppmtompeg params file
print "Generating params file..."

# old pattern
# PATTERN IBBBPBBBPBBBPBBBPBBB

paramsFileString = """REFERENCE_FRAME DECODED
FRAME_RATE 24
OUTPUT %s
PATTERN IBBPBBPBB
FORCE_ENCODE_LAST_FRAME
GOP_SIZE 20
BSEARCH_ALG CROSS2
PSEARCH_ALG TWOLEVEL
IQSCALE 10
PQSCALE 11
BQSCALE 16
RANGE 8
SLICES_PER_FRAME 1
BASE_FILE_FORMAT PNM
INPUT_DIR .
INPUT_CONVERT *
INPUT
""" % (mpegName)

# need to determine the first number and last number of the list of files
# sort the files first just in case
fnames.sort()
firstFile = fnames[0]
lastFile = fnames[-1]

r = re.compile("([a-zA-Z-_\.\d])(\\d+)(\\.\\w+)$")
firstNum = r.findall(firstFile)
firstNum = firstNum[0][1]
lastNum = r.findall(lastFile)
lastNum = lastNum[0][1]


# finish off the params file string
if pad == 1:
    paramsFileString += "%s*.pnm [%s-%s]\n" % (fnameStem, firstNum, lastNum)
elif pad > 1:
    # positive padding: add duplicate frames (slow the movie down)
    for i in range(int(firstNum), int(lastNum)+1):
	for j in range(pad):
	    paramsFileString += "%s%04d.pnm\n" % (fnameStem, i)
elif pad < 1:
    # negative padding: i.e. remove frames (speed the movie up)
    for i in range(int(firstNum), int(lastNum)+1, abs(pad)):
	paramsFileString += "%s%04d.pnm\n" % (fnameStem, i)

paramsFileString += """END_INPUT
PIXEL HALF
ASPECT_RATIO 1
"""

# write the string to file
fp = open( "%s.params" % (fnameStem,), "w" )
fp.write(paramsFileString + '\n')
fp.close()
print "Done params file generation"

# now do the conversion to mpeg
print "Performing conversion to mpeg"
convertString = "ppmtompeg %s.params" % (fnameStem,)
result = os.system(convertString)
if result != 0:
    print "An error occurred in mpeg conversion"

# now clean up a bit
#for i in range(count):
#    rmFname = "%s_%04d.ppm" % (fnameStem,i)
#    os.unlink(rmFname)

print "\nDone!"
 
