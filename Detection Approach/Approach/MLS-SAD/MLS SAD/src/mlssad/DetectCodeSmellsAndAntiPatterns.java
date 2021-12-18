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

package mlssad;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Set;
import org.w3c.dom.Document;
import mlssad.antipatterns.detection.IAntiPatternDetection;
import mlssad.antipatterns.detection.repository.ExcessiveInterLanguageCommunicationDetection;
import mlssad.antipatterns.detection.repository.TooMuchClusteringDetection;
import mlssad.antipatterns.detection.repository.TooMuchScatteringDetection;
import mlssad.codesmells.detection.ICodeSmellDetection;
import mlssad.codesmells.detection.repository.AssumingSafeMultiLanguageReturnValuesDetection;
import mlssad.codesmells.detection.repository.HardCodingLibrariesDetection;
import mlssad.codesmells.detection.repository.LocalReferencesAbuseDetection;
import mlssad.codesmells.detection.repository.MemoryManagementMismatchDetection;
import mlssad.codesmells.detection.repository.NotHandlingExceptionsDetection;
import mlssad.codesmells.detection.repository.NotSecuringLibrariesDetection;
import mlssad.codesmells.detection.repository.NotUsingRelativePathDetection;
import mlssad.codesmells.detection.repository.PassingExcessiveObjectsDetection;
import mlssad.codesmells.detection.repository.UnusedParametersDetection;
// Detectors that need to analyse both languages
// Uncomment when giving both Java and native code as an argument
//import mlssad.codesmells.detection.repository.NotCachingObjectsElementsDetection;
//import mlssad.codesmells.detection.repository.UnusedDeclarationDetection;
//import mlssad.codesmells.detection.repository.UnusedImplementationDetection;
import mlssad.utils.CodeToXml;

public class DetectCodeSmellsAndAntiPatterns {

	/**
	 * Outputs a CSV listing the code smells and anti-patterns detected
	 * in the input project.
	 *
	 * @param args	Path to the input project (can be a file or a directory)
	 */
	public static void main(final String[] args) {
		final long start = System.currentTimeMillis();
		final Set<ICodeSmellDetection> codeSmellDetectors = new HashSet<>();
		final Set<IAntiPatternDetection> antiPatternDetectors = new HashSet<>();

		codeSmellDetectors
			.add(new AssumingSafeMultiLanguageReturnValuesDetection());
		codeSmellDetectors.add(new HardCodingLibrariesDetection());
		codeSmellDetectors.add(new LocalReferencesAbuseDetection());
		codeSmellDetectors.add(new MemoryManagementMismatchDetection());
		codeSmellDetectors.add(new NotHandlingExceptionsDetection());
		codeSmellDetectors.add(new NotSecuringLibrariesDetection());
		codeSmellDetectors.add(new NotUsingRelativePathDetection());
		codeSmellDetectors.add(new PassingExcessiveObjectsDetection());
		codeSmellDetectors.add(new UnusedParametersDetection());

		// Detectors that need to analyse both languages
		// Uncomment when giving both Java and native code as an argument
		//		codeSmellDetectors.add(new NotCachingObjectsElementsDetection());
		//		codeSmellDetectors.add(new UnusedDeclarationDetection());
		//		codeSmellDetectors.add(new UnusedImplementationDetection());

		antiPatternDetectors
			.add(new ExcessiveInterLanguageCommunicationDetection());
		antiPatternDetectors.add(new TooMuchClusteringDetection());
		antiPatternDetectors.add(new TooMuchScatteringDetection());

		final Document xml = CodeToXml.parse(args);
		System.out
			.println(
				"The creation of the XML took "
						+ (System.currentTimeMillis() - start) + " ms.\n");

		try {
			int id = 0;
			String bareName = "";
			if (bareName.equals("")) {
				final String[] parts = args[0].split("[\\/\\\\]");
				bareName = parts[parts.length - 1];
			}
			final String dir = "results";
			final String fullPath = dir + "/" + bareName + ".csv";

			if (new File(dir).mkdirs()) {
				System.out.println("Directory " + dir + " created");
			}

			System.out.println(bareName);
			System.out.println(args[0]);
			System.out.println();

			// FileWriter(..., false): no auto-append, write at the beginning of the file
			// PrintWriter(..., false): no autoflush for performance reason
			final PrintWriter outputWriter = new PrintWriter(
				new BufferedWriter(new FileWriter(fullPath, false)),
				false);
			outputWriter.println("ID,Name,Variable,Method,Class,Package,File,File Name");

			for (final ICodeSmellDetection detector : codeSmellDetectors) {
				detector.detect(xml);
				detector.output(outputWriter, id);
				final int nbCodeSmells = detector.getCodeSmells().size();
				id += nbCodeSmells;
				System.out
					.println(detector.getCodeSmellName() + ": " + nbCodeSmells);
			}

			for (final IAntiPatternDetection detector : antiPatternDetectors) {
				detector.detect(xml);
				detector.output(outputWriter, id);
				final int nbAntiPatterns = detector.getAntiPatterns().size();
				id += nbAntiPatterns;
				System.out
					.println(
						detector.getAntiPatternName() + ": " + nbAntiPatterns);
			}
			outputWriter.flush();
			outputWriter.close();
			System.out
				.println(
					"\nThe detection took "
							+ (System.currentTimeMillis() - start) + " ms.");
		}
		catch (final IOException e) {
			System.out.println("Cannot create output file");
			e.printStackTrace();
		}
	}
}
