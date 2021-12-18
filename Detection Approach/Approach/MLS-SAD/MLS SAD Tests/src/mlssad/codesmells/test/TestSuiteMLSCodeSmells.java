/* (c) Copyright 2019 and following years, PalmyreB.
 *
 * Use and copying of this software and preparation of derivative works
 * based upon this software are permitted. Any copy of this software or
 * of any derivative work must include the above copyright notice of
 * the author, this paragraph and the one after it.
 *
 * This software is made available AS IS, and THE AUTHOR DISCLAIMS
 * ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE, AND NOT WITHSTANDING ANY OTHER PROVISION CONTAINED HEREIN,
 * ANY LIABILITY FOR DAMAGES RESULTING FROM THE SOFTWARE OR ITS USE IS
 * EXPRESSLY DISCLAIMED, WHETHER ARISING IN CONTRACT, TORT (INCLUDING
 * NEGLIGENCE) OR STRICT LIABILITY, EVEN IF THE AUTHOR IS ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGES.
 *
 * All Rights Reserved.
 */

package mlssad.codesmells.test;

import junit.framework.Test;

public final class TestSuiteMLSCodeSmells extends junit.framework.TestSuite {
	public static Test suite() {

		final TestSuiteMLSCodeSmells suite = new TestSuiteMLSCodeSmells();

		suite.addTestSuite(TestCaseAssumingSelfMultiLanguageReturnValues.class);
		suite.addTestSuite(TestCaseHardCodingLibraries.class);
		suite.addTestSuite(TestCaseLocalReferencesAbuse.class);
		suite.addTestSuite(TestCaseMemoryManagementMismatch.class);
		suite.addTestSuite(TestCaseNotCachingObjectsElements.class);
		suite.addTestSuite(TestCaseNotHandlingExceptions.class);
		suite.addTestSuite(TestCaseNotSecuringLibraries.class);
		suite.addTestSuite(TestCaseNotUsingRelativePath.class);
		suite.addTestSuite(TestCasePassingExcessiveObjects.class);
		suite.addTestSuite(TestCaseUnusedDeclaration.class);
		suite.addTestSuite(TestCaseUnusedImplementation.class);
		suite.addTestSuite(TestCaseUnusedParameters.class);

		return suite;
	}
}
