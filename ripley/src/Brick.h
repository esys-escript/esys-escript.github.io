
/*****************************************************************************
*
* Copyright (c) 2003-2016 by The University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development 2012-2013 by School of Earth Sciences
* Development from 2014 by Centre for Geoscience Computing (GeoComp)
*
*****************************************************************************/

#ifndef __RIPLEY_BRICK_H__
#define __RIPLEY_BRICK_H__

#include <ripley/RipleyDomain.h>

#include <paso/Coupler.h>

namespace ripley {

/**
   \brief
   Brick is the 3-dimensional implementation of a RipleyDomain.
*/
class RIPLEY_DLL_API Brick: public RipleyDomain
{
    friend class DefaultAssembler3D;
    friend class WaveAssembler3D;
    friend class LameAssembler3D;
public:

    /**
       \brief creates a hexagonal mesh with n0 x n1 x n2 elements over the
              brick [x0,x1] x [y0,y1] x [z0,z1].
       \param n0,n1,n2 number of elements in each dimension
       \param x0,y0,z0,x1,y1,z1 coordinates of corner nodes of the brick
       \param d0,d1,d2 number of subdivisions in each dimension
    */
    Brick(dim_t n0, dim_t n1, dim_t n2, double x0, double y0, double z0,
          double x1, double y1, double z1, int d0=-1, int d1=-1, int d2=-1,
          const std::vector<double>& points = std::vector<double>(),
          const std::vector<int>& tags = std::vector<int>(),
          const TagMap& tagnamestonums = TagMap(),
          escript::SubWorld_ptr w=escript::SubWorld_ptr());

    /**
       \brief
       Destructor.
    */
    ~Brick();

    /**
       \brief
       returns a description for this domain
    */
    virtual std::string getDescription() const;

    /**
       \brief equality operator
    */
    virtual bool operator==(const escript::AbstractDomain& other) const;

    /**
       \brief
       writes the current mesh to a file with the given name
       \param filename The name of the file to write to
    */
    virtual void write(const std::string& filename) const;

    /**
       \brief
       dumps the mesh to a file with the given name
       \param filename The name of the output file
    */
    void dump(const std::string& filename) const;

    /**
    */
    virtual void readNcGrid(escript::Data& out, std::string filename,
            std::string varname, const ReaderParameters& params) const;

    /**
    */
    virtual void readBinaryGrid(escript::Data& out, std::string filename,
                                const ReaderParameters& params) const;

#ifdef USE_BOOSTIO
    virtual void readBinaryGridFromZipped(escript::Data& out, std::string filename,
                                const ReaderParameters& params) const;
#endif

    /**
    */
    virtual void writeBinaryGrid(const escript::Data& in,
                                 std::string filename,
                                 int byteOrder, int dataType) const;

    /**
       \brief
       returns the array of reference numbers for a function space type
       \param fsType The function space type
    */
    const dim_t* borrowSampleReferenceIDs(int fsType) const;

    /**
       \brief
       returns true if this rank owns the sample id.
    */
    virtual bool ownSample(int fsType, index_t id) const;

    /**
       \brief
       copies the surface normals at data points into out. The actual function
       space to be considered is defined by out. out has to be defined on this
       domain.
    */
    virtual void setToNormal(escript::Data& out) const;

    /**
       \brief
       copies the size of samples into out. The actual function space to be
       considered is defined by out. out has to be defined on this domain.
    */
    virtual void setToSize(escript::Data& out) const;

    /**
       \brief
       returns the number of data points summed across all MPI processes
    */
    virtual dim_t getNumDataPointsGlobal() const;

    /**
       \brief
       writes information about the mesh to standard output
       \param full whether to print additional data
    */
    virtual void Print_Mesh_Info(const bool full=false) const;

    /**
       \brief
       returns the number of nodes per MPI rank in each dimension
    */
    virtual const dim_t* getNumNodesPerDim() const { return m_NN; }

    /**
       \brief
       returns the number of elements per MPI rank in each dimension
    */
    virtual const dim_t* getNumElementsPerDim() const { return m_NE; }

    /**
       \brief
       returns the number of face elements in the order
       (left,right,bottom,top,front,back) on current MPI rank
    */
    virtual const dim_t* getNumFacesPerBoundary() const { return m_faceCount; }

    /**
       \brief
       returns the node distribution vector
    */
    virtual IndexVector getNodeDistribution() const { return m_nodeDistribution; }

    /**
       \brief
       returns the number of spatial subdivisions in each dimension
    */
    virtual const int* getNumSubdivisionsPerDim() const { return m_NX; }

    /**
       \brief
       returns the index'th coordinate value in given dimension for this rank
    */
    virtual double getLocalCoordinate(index_t index, int dim) const;

    /**
       \brief
       returns the tuple (origin, spacing, number_of_elements)
    */
    virtual boost::python::tuple getGridParameters() const;

    /**
     * \brief
       Returns a Data object filled with random data passed through filter.
    */
    virtual escript::Data randomFill(const escript::DataTypes::ShapeType& shape,
                                     const escript::FunctionSpace& what,
                                     long seed,
                                     const boost::python::tuple& filter) const;

    /**
       \brief
       returns the lengths of the domain
    */
    const double *getLength() const { return m_length; }

    /**
       \brief
       returns the lengths of an element
    */
    const double *getElementLength() const { return m_dx; }

    /**
       \brief
       returns a vector of rank numbers where vec[i]=n means that rank n
       'owns' element/face element i.
    */
    virtual RankVector getOwnerVector(int fsType) const;

protected:
    virtual dim_t getNumNodes() const;
    virtual dim_t getNumElements() const;
    virtual dim_t getNumFaceElements() const;
    virtual dim_t getNumDOF() const;
    virtual IndexVector getDiagonalIndices(bool upperOnly) const;
    virtual void assembleCoordinates(escript::Data& arg) const;
    virtual void assembleGradient(escript::Data& out, const escript::Data& in) const;
    virtual void assembleIntegrate(DoubleVector& integrals, const escript::Data& arg) const;
    virtual paso::SystemMatrixPattern_ptr getPasoMatrixPattern(
                             bool reducedRowOrder, bool reducedColOrder) const;
    virtual void interpolateNodesOnElements(escript::Data& out,
                                  const escript::Data& in, bool reduced) const;
    virtual void interpolateNodesOnFaces(escript::Data& out,
                                         const escript::Data& in,
                                         bool reduced) const;
    virtual void nodesToDOF(escript::Data& out, const escript::Data& in) const;
    virtual void dofToNodes(escript::Data& out, const escript::Data& in) const;
    virtual dim_t getDofOfNode(dim_t node) const;
    Assembler_ptr createAssembler(std::string type, const DataMap& constants) const;

    void populateSampleIds();
    void populateDofMap();
    std::vector<IndexVector> getConnections() const;
    void addToMatrixAndRHS(escript::AbstractSystemMatrix* S, escript::Data& F,
           const DoubleVector& EM_S, const DoubleVector& EM_F,
           bool addS, bool addF, index_t firstNode, int nEq=1, int nComp=1) const;

    template<typename ValueType>
    void readBinaryGridImpl(escript::Data& out, const std::string& filename,
                            const ReaderParameters& params) const;
    template<typename ValueType>
    void readBinaryGridZippedImpl(escript::Data& out, const std::string& filename,
                            const ReaderParameters& params) const;
    template<typename ValueType>
    void writeBinaryGridImpl(const escript::Data& in,
                             const std::string& filename, int byteOrder) const;

    dim_t findNode(const double *coords) const;

    virtual escript::Data randomFillWorker(
            const escript::DataTypes::ShapeType& shape, long seed,
            const boost::python::tuple& filter) const;

    /// total number of elements in each dimension
    dim_t m_gNE[3];

    /// origin of domain
    double m_origin[3];

    /// side lengths of domain
    double m_length[3];

    /// grid spacings / cell sizes of domain
    double m_dx[3];

    /// number of spatial subdivisions
    int m_NX[3];

    /// number of elements for this rank in each dimension including shared
    dim_t m_NE[3];

    /// number of own elements for this rank in each dimension
    dim_t m_ownNE[3];

    /// number of nodes for this rank in each dimension
    dim_t m_NN[3];

    /// first node on this rank is at (offset0,offset1,offset2) in global mesh
    dim_t m_offset[3];

    /// number of face elements per edge (left, right, bottom, top, front, back)
    dim_t m_faceCount[6];

    /// faceOffset[i]=-1 if face i is not an external face, otherwise it is
    /// the index of that face (where i: 0=left, 1=right, 2=bottom, 3=top,
    /// 4=front, 5=back)
    IndexVector m_faceOffset;

    /// vector of sample reference identifiers
    IndexVector m_dofId;
    IndexVector m_nodeId;
    IndexVector m_elementId;
    IndexVector m_faceId;

    // vector with first node id on each rank
    IndexVector m_nodeDistribution;

    // vector that maps each node to a DOF index (used for the coupler)
    IndexVector m_dofMap;

    // Paso connector used by the system matrix and to interpolate DOF to
    // nodes
    paso::Connector_ptr m_connector;

    // the Paso System Matrix pattern
    mutable paso::SystemMatrixPattern_ptr m_pattern;
};

////////////////////////////// inline methods ////////////////////////////////
inline dim_t Brick::getDofOfNode(dim_t node) const
{
    return m_dofMap[node];
}

inline dim_t Brick::getNumDataPointsGlobal() const
{
    return (m_gNE[0]+1)*(m_gNE[1]+1)*(m_gNE[2]+1);
}

inline double Brick::getLocalCoordinate(index_t index, int dim) const
{
    ESYS_ASSERT_MPI(dim>=0 && dim<3, "'dim' out of bounds", m_mpiInfo);
    ESYS_ASSERT_MPI(index>=0 && index<m_NN[dim], "'index' out of bounds", m_mpiInfo);
    return m_origin[dim]+m_dx[dim]*(m_offset[dim]+index);
}

inline boost::python::tuple Brick::getGridParameters() const
{
    return boost::python::make_tuple(
            boost::python::make_tuple(m_origin[0], m_origin[1], m_origin[2]),
            boost::python::make_tuple(m_dx[0], m_dx[1], m_dx[2]),
            boost::python::make_tuple(m_gNE[0], m_gNE[1], m_gNE[2]));
}

//protected
inline dim_t Brick::getNumDOF() const
{
    return (m_gNE[0]+1)/m_NX[0]*(m_gNE[1]+1)/m_NX[1]*(m_gNE[2]+1)/m_NX[2];
}

//protected
inline dim_t Brick::getNumNodes() const
{
    return m_NN[0]*m_NN[1]*m_NN[2];
}

//protected
inline dim_t Brick::getNumElements() const
{
    return m_NE[0]*m_NE[1]*m_NE[2];
}

//protected
inline dim_t Brick::getNumFaceElements() const
{
    return m_faceCount[0] + m_faceCount[1] + m_faceCount[2]
            + m_faceCount[3] + m_faceCount[4] + m_faceCount[5];
}

} // end of namespace ripley

#endif // __RIPLEY_BRICK_H__

