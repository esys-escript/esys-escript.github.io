
/*******************************************************
*
* Copyright (c) 2003-2010 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


#ifdef ESYS_MPI
extern "C"
{
#include "esysUtils/Esys_MPI.h"
}
#endif

#include "BuckleyDomain.h"

#include "BuckleyException.h"
#include "esysUtils/esysExceptionTranslator.h"

#include "escript/AbstractContinuousDomain.h"

#include <boost/python.hpp>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/detail/defaults_gen.hpp>
#include <boost/version.hpp>

using namespace boost::python;

/**
   \page buckley

   \version 1.0.0 

   \section class_desc Class Description:
   None

   \section class_limits Class Limitations:
   None

   \section class_conds Class Conditions of Use:
   None

   \section throws Throws:
   depends what you try to do

*/

namespace buckley
{
  
escript::Domain_ptr buckley(double x, double y, double z)
{
    BuckleyDomain* temp=new BuckleyDomain(x, y, z);  
    return temp->getPtr();
}
  
  
  
}


BOOST_PYTHON_MODULE(buckleycpp)
{
// This feature was added in boost v1.34
#if ((BOOST_VERSION/100)%1000 > 34) || (BOOST_VERSION/100000 >1)
  // params are: bool show_user_defined, bool show_py_signatures, bool show_cpp_signatures
  docstring_options docopt(true, true, false);
#endif

  //
  // NOTE: The return_value_policy is necessary for functions that
  // return pointers.
  //
  register_exception_translator<buckley::BuckleyException>(&(esysUtils::esysExceptionTranslator));

//   def("LoadMesh",buckley::loadMesh,
//       (arg("fileName")="file.nc"),":rtype: `Domain`"
//       );
// 
//   def("ReadMesh",buckley::readMesh,
//       (arg("fileName")="file.fly",arg("integrationOrder")=-1,  arg("reducedIntegrationOrder")=-1,  arg("optimize")=true)
// 	,"Read a mesh from a file. For MPI parallel runs fan out the mesh to multiple processes.\n\n"
// ":rtype: `Domain`\n:param fileName:\n:type fileName: ``string``\n"
// ":param integrationOrder: order of the quadrature scheme. If *integrationOrder<0* the integration order is selected independently.\n"
// ":type integrationOrder: ``int``\n"
// ":param reducedIntegrationOrder: order of the quadrature scheme. If *reducedIntegrationOrder<0* the integration order is selected independently.\n"
// ":param optimize: Enable optimisation of node labels\n:type optimize: ``bool``");


     def("Buckley", buckley::buckley, (arg("n0")=1, arg("n1")=1, arg("n2")=1), "Creates an OctTree mesh for a box with the specified dimensions");
//   def ("Brick",buckley::brick,
//       (arg("n0")=1,arg("n1")=1,arg("n2")=1,
//       arg("order")=1,
//       arg("l0")=1.0,arg("l1")=1.0,arg("l2")=1.0,
//       arg("periodic0")=false,arg("periodic1")=false,arg("periodic2")=false,
//       arg("integrationOrder")=-1,  arg("reducedIntegrationOrder")=-1,
//       arg("useElementsOnFace")=false,
//       arg("useFullElementOrder")=false,
//       arg("optimize")=false)
// ,"Creates a tetrahedral mesh by subdividing n0 x n1 x n2 rectangular elements over the brick [0,l0] x [0,l1] x [0,l2]."
// "\n\n:param n0:\n:type n0:\n:param n1:\n:type n1:\n:param n2:\n:type n2:\n"
// ":param order: =1, =-1 or =2 gives the order of shape function. If -1 macro elements of order 1 are used.\n"
// ":param l0: length of side 0\n:param l1:\n:param l2:\n"
// ":param integrationOrder: order of the quadrature scheme. If integrationOrder<0 the integration order is selected independently.\n"
// ":param reducedIntegrationOrder: order of the quadrature scheme. If reducedIntegrationOrder<0 the integration order is selected independently.\n"
// ":param useElementsOnFace:  whether or not to use elements on face\n"
// ":type useElementsOnFace: ``int``"
// ":param periodic0:  whether or not boundary conditions are periodic\n"
// ":param periodic1:\n:param periodic2:\n"
// ":param useFullElementOrder:\n:param optimize:\n"
// ":param optimize: Enable optimisation of node labels\n:type optimize: ``bool``"
// );


  class_<buckley::BuckleyDomain, bases<escript::AbstractContinuousDomain> >
      ("BuckleyDomain","A concrete class representing a domain. For more details, please consult the c++ documentation.",no_init)
      .def("refineAll",&buckley::BuckleyDomain::refineAll, args("min_depth"),"Ensure all leaves are at depth >= min_depth")
      .def("refine",&buckley::BuckleyDomain::refinePoint, args("x", "y", "z" ,"min_depth"),"ensure leaf containing (x, y, z) is at depth >= min_depth")
      .def("collapseAll", &buckley::BuckleyDomain::collapseAll,args("max_depth"),"Ensure all leaves are at depth <= min_depth")
      .def("collapse",&buckley::BuckleyDomain::collapsePoint, args("x", "y", "z" ,"max_depth"),"ensure leaf containing (x, y, z) is at depth <= min_depth")
      
      .def("write",&buckley::BuckleyDomain::write,args("filename"),
"Write the current mesh to a file with the given name.")
      .def("print_mesh_info",&buckley::BuckleyDomain::Print_Mesh_Info,(arg("full")=false),
":param full:\n:type full: ``bool``")
      .def("dump",&buckley::BuckleyDomain::dump,args("fileName")
,"dumps the mesh to a file with the given name.")
      .def("getDescription",&buckley::BuckleyDomain::getDescription,
":return: a description for this domain\n:rtype: ``string``")
      .def("getDim",&buckley::BuckleyDomain::getDim,":rtype: ``int``")
      .def("getDataShape",&buckley::BuckleyDomain::getDataShape, args("functionSpaceCode"),
":return: a pair (dps, ns) where dps=the number of data points per sample, and ns=the number of samples\n:rtype: ``tuple``")
      .def("getNumDataPointsGlobal",&buckley::BuckleyDomain::getNumDataPointsGlobal,
":return: the number of data points summed across all MPI processes\n"
":rtype: ``int``")
      .def("addPDEToSystem",&buckley::BuckleyDomain::addPDEToSystem,
args("mat", "rhs","A", "B", "C", "D", "X", "Y", "d", "y", "d_contact", "y_contact"),
"adds a PDE onto the stiffness matrix mat and a rhs\n\n"
":param mat:\n:type mat: `OperatorAdapter`\n:param rhs:\n:type rhs: `Data`\n"
":param A:\n:type A: `Data`\n"
":param B:\n:type B: `Data`\n"
":param C:\n:type C: `Data`\n"
":param D:\n:type D: `Data`\n"
":param X:\n:type X: `Data`\n"
":param Y:\n:type Y: `Data`\n"
":param d:\n:type d: `Data`\n"
":param d_contact:\n:type d_contact: `Data`\n"
":param y_contact:\n:type y_contact: `Data`\n"
)

      .def("addPDEToRHS",&buckley::BuckleyDomain::addPDEToRHS, 
args("rhs", "X", "Y", "y", "y_contact"),
"adds a PDE onto the stiffness matrix mat and a rhs\n\n"
":param rhs:\n:type rhs: `Data`\n"
":param X:\n:type X: `Data`\n"
":param Y:\n:type Y: `Data`\n"
":param y:\n:type y: `Data`\n"
":param y_contact:\n:type y_contact: `Data`"
)
      .def("addPDEToTransportProblem",&buckley::BuckleyDomain::addPDEToTransportProblem,
args( "tp", "source", "M", "A", "B", "C", "D", "X", "Y", "d", "y", "d_contact", "y_contact"),
":param tp:\n:type tp: `TransportProblemAdapter`\n"
":param source:\n:type source: `Data`\n"
":param M:\n:type M: `Data`\n"
":param A:\n:type A: `Data`\n"
":param B:\n:type B: `Data`\n"
":param C:\n:type C: `Data`\n"
":param D:\n:type D: `Data`\n"
":param X:\n:type X: `Data`\n"
":param Y:\n:type Y: `Data`\n"
":param d:\n:type d: `Data`\n"
":param y:\n:type y: `Data`\n"
":param d_contact:\n:type d_contact: `Data`\n"
":param y_contact:\n:type y_contact: `Data`\n"
)
      .def("newOperator",&buckley::BuckleyDomain::newSystemMatrix,
args("row_blocksize", "row_functionspace", "column_blocksize", "column_functionspace", "type"),
"creates a SystemMatrixAdapter stiffness matrix and initializes it with zeros\n\n"
":param row_blocksize:\n:type row_blocksize: ``int``\n"
":param row_functionspace:\n:type row_functionspace: `FunctionSpace`\n"
":param column_blocksize:\n:type column_blocksize: ``int``\n"
":param column_functionspace:\n:type column_functionspace: `FunctionSpace`\n"
":param type:\n:type type: ``int``\n"
)
      .def("newTransportProblem",&buckley::BuckleyDomain::newTransportProblem,
args("theta", "blocksize", "functionspace", "type"),
"creates a TransportProblemAdapter\n\n"
":param theta:\n:type theta: ``float``\n"
":param blocksize:\n:type blocksize: ``int``\n"
":param functionspace:\n:type functionspace: `FunctionSpace`\n"
":param type:\n:type type: ``int``\n"
)
      .def("getSystemMatrixTypeId",&buckley::BuckleyDomain::getSystemMatrixTypeId,
args("solver", "preconditioner", "package", "symmetry"),
":return: the identifier of the matrix type to be used for the global stiffness matrix when a particular solver, package, perconditioner, and symmetric matrix is used.\n"
":rtype: ``int``\n"
":param solver:\n:type solver: ``int``\n"
":param preconditioner:\n:type preconditioner: ``int``\n"
":param package:\n:type package: ``int``\n"
":param symmetry:\n:type symmetry: ``int``\n"
)
      .def("getTransportTypeId",&buckley::BuckleyDomain::getTransportTypeId,
args("solver", "preconditioner", "package", "symmetry"),
":return: the identifier of the transport problem type to be used when a particular solver, perconditioner, package and symmetric matrix is used.\n"
":rtype: ``int``\n"
":param solver:\n:type solver: ``int``\n"
":param preconditioner:\n:type preconditioner: ``int``\n"
":param package:\n:type package: ``int``\n"
":param symmetry:\n:type symmetry: ``int``\n"
)
      .def("setX",&buckley::BuckleyDomain::setNewX,
args("arg"), "assigns new location to the domain\n\n:param arg:\n:type arg: `Data`")
      .def("getX",&buckley::BuckleyDomain::getX, ":return: locations in the FEM nodes\n\n"
":rtype: `Data`")
      .def("getNormal",&buckley::BuckleyDomain::getNormal,
":return: boundary normals at the quadrature point on the face elements\n"
":rtype: `Data`")
      .def("getSize",&buckley::BuckleyDomain::getSize,":return: the element size\n"
":rtype: `Data`")
      .def("saveDX",&buckley::BuckleyDomain::saveDX,args("filename" ,"arg"),
"Saves a dictonary of Data objects to an OpenDX input file. The keywords are used as identifier"
"\n\n:param filename: \n:type filename: ``string``\n"
"\n:param arg: \n:type arg: ``dict``\n")
      .def("saveVTK",&buckley::BuckleyDomain::saveVTK,
args("filename" ,"arg",  "metadata", "metadata_schema"),
"Saves a dictonary of Data objects to an VTK XML input file. The keywords are used as identifier"
"\n\n:param filename:\n:type filename: ``string``\n"
":param arg:\n:type arg: ``dict``\n"
":param metadata:\n:type metadata: ``string``\n"
":param metadata_schema:\n:type metadata_schema: ``string``\n"
)
      .def("setTagMap",&buckley::BuckleyDomain::setTagMap,args("name","tag"),
"Give a tag number a name.\n\n:param name: Name for the tag\n:type name: ``string``\n"
":param tag: numeric id\n:type tag: ``int``\n:note: Tag names must be unique within a domain")
      .def("getTag",&buckley::BuckleyDomain::getTag,args("name"),":return: tag id for "
"``name``\n:rtype: ``string``")
      .def("isValidTagName",&buckley::BuckleyDomain::isValidTagName,args("name"),
":return: True is ``name`` corresponds to a tag\n:rtype: ``bool``")
      .def("showTagNames",&buckley::BuckleyDomain::showTagNames,":return: A space separated list of tag names\n:rtype: ``string``")
      .def("getMPISize",&buckley::BuckleyDomain::getMPISize,":return: the number of processes used for this `Domain`\n:rtype: ``int``")
      .def("getMPIRank",&buckley::BuckleyDomain::getMPIRank,":return: the rank of this process\n:rtype: ``int``")
      .def("MPIBarrier",&buckley::BuckleyDomain::MPIBarrier,"Wait until all processes have reached this point")
      .def("onMasterProcessor",&buckley::BuckleyDomain::onMasterProcessor,":return: True if this code is executing on the master process\n:rtype: `bool`");

}
