#ifndef _DOMAINHELPERS_H_
#define _DOMAINHELPERS_H_

#include <vector>
#include <ripley/Ripley.h>

/**
    factorises 'product' and inserts the factors into the vector 'factors'
    in order of smallest to largest
*/
void factorise(std::vector<int>& factors, int product);

/**
    sets va[a] = b and vb[b] = a, used in constructing CSC and CSR matrix
    formats simultaneously
*/
void doublyLink(std::vector<ripley::IndexVector>& va,
        std::vector<ripley::IndexVector>& vb, int a, int b);

#ifdef USE_BOOSTIO
/**
    converts the given gzip compressed char vector unto an uncompressed form 
*/
std::vector<char> unzip(const std::vector<char> compressed);
#endif
#endif
