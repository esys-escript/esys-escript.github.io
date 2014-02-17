
/*****************************************************************************
*
* Copyright (c) 2003-2013 by University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development since 2012 by School of Earth Sciences
*
*****************************************************************************/


#include <escript/Data.h>

#include <weipa/EscriptDataset.h>
#include <weipa/VisItControl.h>

#include <boost/python.hpp>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/object.hpp>
#include <boost/version.hpp>

using namespace boost::python;

BOOST_PYTHON_MODULE(weipacpp)
{
#if BOOST_VERSION >= 103500
// params are: bool show_user_defined, bool show_py_signatures, bool show_cpp_signatures
  docstring_options docopt(true,true,false);
#endif

    class_<weipa::EscriptDataset>("EscriptDataset","Represents an escript dataset including a domain and data variables for one timestep. It is used for exporting", init<>())
        .def("setDomain", &weipa::EscriptDataset::setDomain)
        .def("addData", &weipa::EscriptDataset::addData, (arg("data"), arg("name"), arg("units")=""))
        .def("setCycleAndTime", &weipa::EscriptDataset::setCycleAndTime, args("cycle","time"))
        .def("setMeshLabels", &weipa::EscriptDataset::setMeshLabels, (arg("x"),arg("y"),arg("z")=""))
        .def("setMeshUnits", &weipa::EscriptDataset::setMeshUnits, (arg("x"),arg("y"),arg("z")=""))
        .def("setMetadataSchemaString", &weipa::EscriptDataset::setMetadataSchemaString, (arg("schema")="", arg("metadata")=""))
        .def("setSaveMeshData", &weipa::EscriptDataset::setSaveMeshData)
        .def("saveSilo", &weipa::EscriptDataset::saveSilo, (arg("filename"), arg("useMultimesh")=true))
        .def("saveVTK", &weipa::EscriptDataset::saveVTK, args("filename"));

    // VisIt Control
    def("visitInitialize", weipa::VisItControl::initialize, (arg("simFile"), arg("comment")=""));
    def("visitPublishData", weipa::VisItControl::publishData, args("dataset"));
}
