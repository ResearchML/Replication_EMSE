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

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import junit.framework.TestCase;
import mlssad.codesmells.detection.repository.NotHandlingExceptionsDetection;
import mlssad.kernel.impl.MLSCodeSmell;

public class TestCaseNotHandlingExceptions extends AbstractCodeSmellTestCase {

	@Override
	protected void setUp() throws Exception {
		super.setUp();
		this.aPathC =
			"../MLS SAD Tests/rsc/CodeSmellsC/src/codeSmellsC/NotHandlingExceptions.c";
		this.aPathJava =
			"../MLS SAD Tests/rsc/CodeSmellsJNI/src/codeSmellsJava/NotHandlingExceptions.java";
		this.expectedSmells = new HashSet<>(
			Arrays
				.asList(
					new MLSCodeSmell(
						"NotHandlingExceptions",
						"name",
						"Java_codeSmellsJava_NotHandlingExceptions_getCharField",
						"",
						"",
						this.aPathC))); //
		this.detector = new NotHandlingExceptionsDetection();
	}

	@Override
	public void testNoCodeSmell() {

		// Although there are expected code smells, they are not really code smells,
		// since they are checked in a condition (they pass the test
		// AssumingSelfMultiLanguageValues)
		final Set<MLSCodeSmell> expectedSmells = new HashSet<>(
			Arrays
				.asList(
					new MLSCodeSmell(
						"NotHandlingExceptions",
						"\"message\"",
						"Java_noCodeSmell_NoCodeSmell_modifyInstanceVariable",
						"",
						"",
						AbstractCodeSmellTestCase.PATH_C_NO_CODE_SMELL),
					new MLSCodeSmell(
						"NotHandlingExceptions",
						"\"number\"",
						"Java_noCodeSmell_NoCodeSmell_modifyInstanceVariable",
						"",
						"",
						AbstractCodeSmellTestCase.PATH_C_NO_CODE_SMELL)));

		this.detector.detect(this.noCodeSmellXml);

		TestCase
			.assertEquals(
				expectedSmells.size(),
				this.detector.getCodeSmells().size());
		TestCase.assertEquals(expectedSmells, this.detector.getCodeSmells());
	}

}
