# $Id$

# This makefile automatically finds, calculates dependencies, compiles
# and makes a static library from all C++ files found in the directories
# under ${L_SRC_DIR} (see below). Files and even whole directory trees
# under ${L_SRC_DIR} can be skipped by postfixing the name with a "-".

# Matt Davies 04/08/03

DEFAULT_TARGET := libescript.so pyc

PACKAGES := esysUtils python23 boostStatic

L_DEFS := DOASSERT

L_SRC_DIR:= ./src ./py_src 

include $(ESYS_ROOT)/make/Makefile.default

