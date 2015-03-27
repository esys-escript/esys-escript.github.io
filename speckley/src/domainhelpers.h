
/*****************************************************************************
*
* Copyright (c) 2003-2014 by University of Queensland
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
#ifndef _SPECKLEY_DOMAINHELPERS_H_
#define _SPECKLEY_DOMAINHELPERS_H_

#include <speckley/Speckley.h>
#include <escript/Data.h>

namespace speckley {

typedef std::map<std::string, escript::Data> DataMap;

/// returns the data associated with the string key or an empty data object
/// if the map does not contain the given key
inline const escript::Data unpackData(const std::string target,
                                      const DataMap& mapping)
{
    DataMap::const_iterator i = mapping.find(target);
    return (i == mapping.end() ? escript::Data() : i->second);
}

/**
    returns true if the given string is in the mapping AND the resulting
    coefficient is not empty
*/
inline bool isNotEmpty(const std::string target, const DataMap& mapping)
{
    DataMap::const_iterator i = mapping.find(target);
    return i != mapping.end() && !i->second.isEmpty();
}

/**
    factorises 'product' and inserts the factors into the vector 'factors'
    in order of smallest to largest
*/
void factorise(std::vector<int>& factors, int product);


#ifdef USE_BOOSTIO
/**
    converts the given gzip compressed char vector into an uncompressed form 
*/
std::vector<char> unzip(const std::vector<char>& compressed);
#endif // USE_BOOSTIO

} //namespace speckley

#endif // _SPECKLEY_DOMAINHELPERS_H_

