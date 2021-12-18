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
import mlssad.codesmells.detection.repository.UnusedDeclarationDetection;
import mlssad.kernel.impl.MLSCodeSmell;

public class TestCaseUnusedDeclaration extends AbstractCodeSmellTestCase {

	@Override
	protected void setUp() throws Exception {
		super.setUp();
		this.aPathC =
			"../MLS SAD Tests/rsc/CodeSmellsC/src/codeSmellsC/UnusedDeclaration.c";
		this.aPathJava =
			"../MLS SAD Tests/rsc/CodeSmellsJNI/src/codeSmellsJava/UnusedDeclaration.java";
		final String cs = "UnusedDeclaration";
		final String cls = "UnusedDeclaration";
		final String pkg = "codeSmellsJava";
		this.expectedSmells = new HashSet<>(
			Arrays
				.asList(
					new MLSCodeSmell(
						cs,
						"",
						"sayHelloMonday",
						cls,
						pkg,
						this.aPathJava),
					new MLSCodeSmell(
						cs,
						"",
						"sayHelloTuesday",
						cls,
						pkg,
						this.aPathJava),
					new MLSCodeSmell(
						cs,
						"",
						"sayHelloWednesday",
						cls,
						pkg,
						this.aPathJava),
					new MLSCodeSmell(
						cs,
						"",
						"sayHelloThursday",
						cls,
						pkg,
						this.aPathJava),
					new MLSCodeSmell(
						cs,
						"",
						"sayHelloFriday",
						cls,
						pkg,
						this.aPathJava),
					new MLSCodeSmell(
						cs,
						"",
						"sayHelloSaturday",
						cls,
						pkg,
						this.aPathJava),
					new MLSCodeSmell(
						cs,
						"",
						"sayHelloSunday",
						cls,
						pkg,
						this.aPathJava)));
		this.detector = new UnusedDeclarationDetection();
	}

}
