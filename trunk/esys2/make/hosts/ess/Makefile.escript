# $Id$

# escript

PKG_CC_INC_DIRS  += $(ESYS_ROOT)/escript/inc
PKG_CPP_INC_DIRS += $(ESYS_ROOT)/escript/inc

PKG_LD_LIB_DIRS += $(ESYS_ROOT)/escript/lib

PKG_LD_LIBS += escript

# $Log$
# Revision 1.1  2004/10/26 06:53:58  jgs
# Initial revision
#
# Revision 1.1.1.1.2.2  2004/09/28 07:03:14  jgs
# *** empty log message ***
#
# Revision 1.1.1.1.2.1  2004/09/27 06:37:54  jgs
# restructured make files
#
# Revision 1.1.1.1  2004/06/24 04:00:39  johng
# Initial version of eys using boost-python.
#
# Revision 1.1  2003/09/11 02:03:52  davies
# Added makefile configurations for several platforms.
#
