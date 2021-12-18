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
import mlssad.antipatterns.detection.IAntiPatternDetection;
import mlssad.kernel.impl.MLSAntiPattern;
import mlssad.utils.CodeToXml;

public abstract class AbstractAntiPatternTestCase extends TestCase {

	protected final static String PATH_C_NO_CODE_SMELL =
		"../MLS SAD Tests/rsc/CodeSmellsC/src/noCodeSmell/NoCodeSmell.c";
	protected final static String PATH_JAVA_NO_CODE_SMELL =
		"../MLS SAD Tests/rsc/CodeSmellsJNI/src/noCodeSmell/NoCodeSmell.java";
	protected IAntiPatternDetection detector;
	protected Set<MLSAntiPattern> expectedSmells;
	protected String aPathC;
	protected String aPathJava;
	protected final Document noCodeSmellXml = CodeToXml
		.parse(
			AbstractAntiPatternTestCase.PATH_C_NO_CODE_SMELL,
			AbstractAntiPatternTestCase.PATH_JAVA_NO_CODE_SMELL);

	/**
	 * Runs a test to check the presence of the expected anti-patterns in the
	 * minimal example.
	 */
	public void testCodeSmells() {
		this.detector.detect(CodeToXml.parse(this.aPathC, this.aPathJava));

		TestCase
			.assertEquals(
				this.expectedSmells.size(),
				this.detector.getAntiPatterns().size());
		TestCase
			.assertEquals(this.expectedSmells, this.detector.getAntiPatterns());
	}

	/**
	 * Runs a test to check the absence of anti-patterns in the correct
	 * example.
	 */
	public void testNoCodeSmell() {
		this.detector.detect(this.noCodeSmellXml);

		TestCase.assertEquals(0, this.detector.getAntiPatterns().size());
		TestCase
			.assertEquals(
				new HashSet<String>(),
				this.detector.getAntiPatterns());
	}
}
