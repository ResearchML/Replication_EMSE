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
import mlssad.codesmells.detection.repository.UnusedParametersDetection;
import mlssad.kernel.impl.MLSCodeSmell;
import mlssad.utils.CodeToXml;

public class TestCaseUnusedParameters extends AbstractCodeSmellTestCase {

	@Override
	protected void setUp() throws Exception {
		super.setUp();
		this.aPathC =
			"../MLS SAD Tests/rsc/CodeSmellsC/src/codeSmellsC/UnusedParameters.c";
		final String cs = "UnusedParameters";
		final String fct = "Java_codeSmellsJava_UnusedParameters_distance";
		this.expectedSmells = new HashSet<>(
			Arrays
				.asList(
					new MLSCodeSmell(
						cs,
						"acceleration",
						fct,
						"",
						"",
						this.aPathC),
					new MLSCodeSmell(
						cs,
						"fuelVolume",
						fct,
						"",
						"",
						this.aPathC)));
		this.detector = new UnusedParametersDetection();
	}

	public void testUnusedParametersDetector() {
		final String aPathJava =
			"../MLS SAD/src/mlssad/codesmells/detection/repository/UnusedParametersDetection.java";
		final Set<MLSCodeSmell> expectedSmells = new HashSet<>();

		this.detector.detect(CodeToXml.parse(aPathJava));

		TestCase
			.assertEquals(
				expectedSmells.size(),
				this.detector.getCodeSmells().size());
		TestCase.assertEquals(expectedSmells, this.detector.getCodeSmells());
	}
}
