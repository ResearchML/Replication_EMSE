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
import mlssad.antipatterns.detection.repository.TooMuchClusteringDetection;
import mlssad.kernel.impl.MLSAntiPattern;

public class TestCaseTooMuchClustering extends AbstractAntiPatternTestCase {
	String expectedAntiPattern = "TooMuchClustering";
	String expectedPackage = "antiPatternsJava.tooMuchClustering";
	String expectedClass = "TooMuchClustering";

	protected void setUp() throws Exception {
		super.setUp();
		this.detector = new TooMuchClusteringDetection();
		this.aPathJava =
			"../MLS SAD Tests/rsc/CodeSmellsJNI/src/antiPatternsJava/TooMuchClustering/";
		this.expectedSmells = new HashSet<MLSAntiPattern>();
		this.expectedSmells
			.add(
				new MLSAntiPattern(
					this.expectedAntiPattern,
					"",
					"",
					this.expectedClass,
					this.expectedPackage,
					this.aPathJava));
	}
}
