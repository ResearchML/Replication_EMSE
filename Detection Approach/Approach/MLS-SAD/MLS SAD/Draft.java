package mlssad.codesmells.detection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

public class MemoryManagementMismatchDetection {

	public String getName() {
		return "MemoryManagementMismatchDetection";
	}

	public List<String> unusedDeclList = new ArrayList<String>();

	public void detect(final Document cXml, final Document javaXml) {
		XPath xPath = XPathFactory.newInstance().newXPath();

		List<String> getFunctions = Arrays.asList("GetStringChars", "GetStringUTFChars", "GetBooleanArrayElements",
				"GetByteArrayElements", "GetCharArrayElements", "GetShortArrayElements", "GetIntArrayElements",
				"GetLongArrayElements", "GetFloatArrayElements", "GetDoubleArrayElements", "GetPrimitiveArrayCritical",
				"GetStringCritical");
		List<String> releaseFunctions = Arrays.asList("ReleaseStringChars", "ReleaseStringUTFChars",
				"ReleaseBooleanArrayElements", "ReleaseByteArrayElements", "ReleaseCharArrayElements",
				"ReleaseShortArrayElements", "ReleaseIntArrayElements", "ReleaseLongArrayElements",
				"ReleaseFloatArrayElements", "ReleaseDoubleArrayElements", "ReleasePrimitiveArrayCritical",
				"ReleaseStringCritical");

		/*
		 * const jchar * GetStringChars(JNIEnv *env, jstring string, jboolean *isCopy);
		 * void ReleaseStringChars(JNIEnv *env, jstring string, const jchar *chars);
		 */

		/*
		 * const char *name = (*env)->GetStringUTFChars(env, fieldName, NULL);
		 * (*env)->ReleaseStringUTFChars(env, fieldName, name);
		 */

		/*
		 * const char *inCStr = (*env)->GetStringUTFChars(env, inJNIStr, NULL);
		 * <decl_stmt><decl><type><specifier>const</specifier> <name>char</name>
		 * <modifier>*</modifier></type><name>inCStr</name> <init>=
		 * <expr><call><name><operator>(</operator><operator>*</operator><name>env</name
		 * ><operator>)</operator><operator>-&gt;</operator><name>GetStringUTFChars</
		 * name></name><argument_list>(<argument><expr><name>env</name></expr></argument
		 * >, <argument><expr><name>inJNIStr</name></expr></argument>,
		 * <argument><expr><name>NULL</name></expr></argument>)</argument_list></call></
		 * expr></init></decl>;</decl_stmt>
		 * 
		 * 
		 * inCStr = (*env)->GetStringUTFChars(env, inJNIStr, NULL);
		 * <expr_stmt><expr><name>inCStr</name> <operator>=</operator>
		 * <call><name><operator>(</operator><operator>*</operator><name>env</name><
		 * operator>)</operator><operator>-&gt;</operator><name>GetStringUTFChars</name>
		 * </name><argument_list>(<argument><expr><name>env</name></expr></argument>,
		 * <argument><expr><name>inJNIStr</name></expr></argument>,
		 * <argument><expr><name>NULL</name></expr></argument>)</argument_list></call></
		 * expr>;</expr_stmt>
		 */

		String genericCallQuery = "//call[name/name='%s']";
		String argsQuery = "argument_list/argument/expr/name";
		// TODO: get number of calls, variables and converted variables
		try {
			int c = 0;
			String getCallQuery;
			String releaseCallQuery;
			NodeList getList;
			NodeList releaseList;
			XPathExpression argsExpr = xPath.compile(argsQuery);
			Iterator<String> getIt = getFunctions.iterator();
			Iterator<String> releaseIt = releaseFunctions.iterator();
			while (getIt.hasNext() && releaseIt.hasNext()) {
				getCallQuery = String.format(genericCallQuery, getIt.next());
				releaseCallQuery = String.format(genericCallQuery, releaseIt.next());
				getList = (NodeList) xPath.compile(getCallQuery).evaluate(cXml, XPathConstants.NODESET);
				releaseList = (NodeList) xPath.compile(releaseCallQuery).evaluate(cXml, XPathConstants.NODESET);
				for (int i = 0; i < getList.getLength(); i++) {
					c++;
					NodeList argsList = (NodeList) argsExpr.evaluate(getList.item(i), XPathConstants.NODESET);
					System.out.println(getList.item(i).getTextContent());
					for (int j = 0; j < argsList.getLength(); j++) {
						System.out.println("\t" + argsList.item(j).getTextContent());
					}
				}
				for (int i = 0; i < releaseList.getLength(); i++) {
					c--;
					NodeList argsList = (NodeList) argsExpr.evaluate(releaseList.item(i), XPathConstants.NODESET);
					System.out.println(releaseList.item(i).getTextContent());
					for (int j = 0; j < argsList.getLength(); j++) {
						System.out.println("\t" + argsList.item(j).getTextContent());
					}
				}
			}
			System.out.println(c);

		} catch (XPathExpressionException e) {
			e.printStackTrace();
		}
	}

}
