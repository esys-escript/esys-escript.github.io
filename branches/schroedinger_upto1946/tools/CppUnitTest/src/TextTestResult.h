//
// Permission to reproduce and create derivative works from the Software ("Software Derivative Works") 
// is hereby granted to you under the copyright of Michael Feathers. Michael Feathers also grants you 
// the right to distribute the Software and Software Derivative Works. 
//
// Michael Feathers licenses the Software to you on an "AS IS" basis, without warranty of any kind.  
// Michael Feathers HEREBY EXPRESSLY DISCLAIMS ALL WARRANTIES OR CONDITIONS, EITHER EXPRESS OR IMPLIED, 
// INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OR CONDITIONS OF MERCHANTABILITY, NON INFRINGEMENT 
// AND FITNESS FOR A PARTICULAR PURPOSE.&nbsp; You are solely responsible for determining the appropriateness 
// of using the Software and assume all risks associated with the use and distribution of this Software, 
// including but not limited to the risks of program errors, damage to or loss of data, programs or 
// equipment, and unavailability or interruption of operations.&nbsp; MICHAEL FEATHERS WILL NOT BE 
// LIABLE FOR ANY DIRECT DAMAGES OR FOR ANY SPECIAL, INCIDENTAL, OR INDIRECT DAMAGES OR FOR ANY ECONOMIC 
// CONSEQUENTIAL DAMAGES (INCLUDING LOST PROFITS OR SAVINGS), EVEN IF MICHAEL FEATHERS HAD BEEN ADVISED 
// OF THE POSSIBILITY OF SUCH DAMAGE.&nbsp; Michael Feathers will not be liable for the loss of, or damage 
// to, your records or data, or any damages claimed by you based on a third party claim. 
//
// You agree to distribute the Software and any Software Derivatives under a license agreement that: 
//
//  1) is sufficient to notify all licensees of the Software and Software Derivatives that Michael 
//     Feathers assumes no liability for any claim that may arise regarding the Software or 
//     Software Derivatives, and 
//  2) that disclaims all warranties, both express and implied, from Michael Feathers regarding the 
//     Software and Software Derivatives.&nbsp; (If you include this Agreement with any distribution 
//     of the Software and Software Derivatives you will have meet this requirement) You agree that 
//     you will not delete any copyright notices in the Software. 
//
// This Agreement is the exclusive statement of your rights in the Software as provided by Michael 
// Feathers. Except for the licenses granted to you in the second paragraph above, no other licenses 
// are granted hereunder, by estoppel, implication or otherwise. 
//
#ifndef CPPUNIT_TEXTTESTRESULT_H
#define CPPUNIT_TEXTTESTRESULT_H

#include <iostream>

#include "TestResult.h"
#include "CppUnitTestNamespace.h"

BEGIN_NAMESPACE_CPPUNITTEST

class TextTestResult : public TestResult
{
public:
    virtual void        addError      (Test *test, CppUnitException *e);
    virtual void        addFailure    (Test *test, CppUnitException *e);
    virtual void        startTest     (Test *test);
    virtual void        print         (std::ostream& stream);
    virtual void        printErrors   (std::ostream& stream);
    virtual void        printFailures (std::ostream& stream);
    virtual void        printHeader   (std::ostream& stream);

};


/* insertion operator for easy output */
inline std::ostream& operator<< (std::ostream& stream, TextTestResult& result)
{ result.print (stream); return stream; }

END_NAMESPACE_CPPUNITTEST

#endif





