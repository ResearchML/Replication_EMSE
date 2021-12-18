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

package mlssad.antipatterns.test;

import java.util.HashSet;
import java.util.Set;
import org.w3c.dom.Document;
import junit.framework.TestCase;
import mlssad.antipatterns.detection.repository.ExcessiveInterLanguageCommunicationDetection;
import mlssad.kernel.impl.MLSAntiPattern;
import mlssad.utils.CodeToXml;

public class TestCaseExcessiveInterLanguageCommunication
		extends AbstractAntiPatternTestCase {
	String expectedAntiPattern = "ExcessiveInterLanguageCommunication";
	String expectedPackage =
		"antiPatternsJava.excessiveInterLanguageCommunication";
	String expectedClass = "ExcessiveInterLanguageCommunication";

	protected void setUp() throws Exception {
		super.setUp();
		this.detector = new ExcessiveInterLanguageCommunicationDetection();
		this.aPathC =
			"../MLS SAD Tests/rsc/CodeSmellsC/src/antiPatternsC/excessiveInterLanguageCommunication.c";
		this.aPathJava =
			"../MLS SAD Tests/rsc/CodeSmellsJNI/src/antiPatternsJava/ExcessiveInterLanguageCommunication/ExcessiveInterLanguageCommunication.java";
		this.expectedSmells = new HashSet<MLSAntiPattern>();
		this.expectedSmells
			.add(
				new MLSAntiPattern(
					this.expectedAntiPattern,
					"",
					"square",
					this.expectedClass,
					this.expectedPackage,
					this.aPathJava));
	}

	public void testSameMethod() {
		final String aPathJava =
			"../MLS SAD Tests/rsc/CodeSmellsJNI/src/antiPatternsJava/ExcessiveInterLanguageCommunication/ExcessiveInterLanguageCommunication2.java";
		final Document javaXml = CodeToXml.parse(aPathJava);
		final Set<MLSAntiPattern> expectedSmells = new HashSet<>();
		expectedSmells
			.add(
				new MLSAntiPattern(
					this.expectedAntiPattern,
					"",
					"square",
					this.expectedClass + 2,
					this.expectedPackage,
					aPathJava));

		this.detector.detect(javaXml);

		TestCase
			.assertEquals(
				expectedSmells.size(),
				this.detector.getAntiPatterns().size());
		TestCase.assertEquals(this.detector.getAntiPatterns(), expectedSmells);
	}

	public void testSameVariable() {
		final String aPathJava =
			"../MLS SAD Tests/rsc/CodeSmellsJNI/src/antiPatternsJava/ExcessiveInterLanguageCommunication/ExcessiveInterLanguageCommunication3.java";
		final Document javaXml = CodeToXml.parse(aPathJava);
		final Set<MLSAntiPattern> expectedSmells = new HashSet<>();
		expectedSmells
			.add(
				new MLSAntiPattern(
					this.expectedAntiPattern,
					"",
					"square",
					this.expectedClass + 3,
					this.expectedPackage,
					aPathJava));
		expectedSmells
			.add(
				new MLSAntiPattern(
					this.expectedAntiPattern,
					"",
					"factorial",
					this.expectedClass + 3,
					this.expectedPackage,
					aPathJava));

		this.detector.detect(javaXml);

		TestCase
			.assertEquals(
				expectedSmells.size(),
				this.detector.getAntiPatterns().size());
		TestCase.assertEquals(expectedSmells, this.detector.getAntiPatterns());
	}

	public void testTooManyNativeCalls() {
		final String aPathJava =
			"../MLS SAD Tests/rsc/CodeSmellsJNI/src/antiPatternsJava/ExcessiveInterLanguageCommunication/ExcessiveInterLanguageCommunication4.java";
		final Document javaXml = CodeToXml.parse(aPathJava);
		final Set<MLSAntiPattern> expectedSmells = new HashSet<>();
		for (char letter = 'a'; letter <= 'z'; letter++) {
			expectedSmells
				.add(
					new MLSAntiPattern(
						this.expectedAntiPattern,
						"",
						String.valueOf(letter),
						this.expectedClass + 4,
						this.expectedPackage,
						aPathJava));
		}

		this.detector.detect(javaXml);

		TestCase
			.assertEquals(
				expectedSmells.size(),
				this.detector.getAntiPatterns().size());
		TestCase.assertEquals(expectedSmells, this.detector.getAntiPatterns());
	}

	public void testCallsInDifferentMethods() {
		final String aPathJava =
			"../MLS SAD Tests/rsc/CodeSmellsJNI/src/antiPatternsJava/ExcessiveInterLanguageCommunication/ExcessiveInterLanguageCommunication5.java";
		final Document javaXml = CodeToXml.parse(aPathJava);
		final Set<MLSAntiPattern> expectedSmells = new HashSet<>();

		this.detector.detect(javaXml);

		TestCase
			.assertEquals(
				expectedSmells.size(),
				this.detector.getAntiPatterns().size());
		TestCase.assertEquals(expectedSmells, this.detector.getAntiPatterns());
	}

}
