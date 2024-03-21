import java.util.ArrayList;

import jminusminus.CLEmitter;

import static jminusminus.CLConstants.*;

/**
 * This class programmatically generates the class file for the following Java application:
 * 
 * <pre>
 * public class IsPrime {
 *     // Entry point.
 *     public static void main(String[] args) {
 *         int n = Integer.parseInt(args[0]);
 *         boolean result = isPrime(n);
 *         if (result) {
 *             System.out.println(n + " is a prime number");
 *         } else {
 *             System.out.println(n + " is not a prime number");
 *         }
 *     }
 *
 *     // Returns true if n is prime, and false otherwise.
 *     private static boolean isPrime(int n) {
 *         if (n < 2) {
 *             return false;
 *         }
 *         for (int i = 2; i <= n / i; i++) {
 *             if (n % i == 0) {
 *                 return false;
 *             }
 *         }
 *         return true;
 *     }
 * }
 * </pre>
 */
public class GenIsPrime {
    public static void main(String[] args) {
        CLEmitter e = new CLEmitter(true);
        
        // ArrayList instance to store modifiers
        ArrayList<String> modifiers = new ArrayList<String>();

        // public class IsPrime {
        modifiers.add("public");
        e.addClass(modifiers, "IsPrime", "java/lang/Object", null, true);

        // public static void main ( String [] args ) {
        modifiers.clear();
        modifiers.add("public");
        modifiers.add("static");
        e.addMethod(modifiers, "main", "([Ljava/lang/String;)V", null, true);

        // int n = Integer.parseInt(args[0]);
        // loading onto stack starts from here. use ALOAD and ICONST for stack slot creation and storage
        e.addNoArgInstruction(ALOAD_0);
        e.addNoArgInstruction(ICONST_0);
        e.addNoArgInstruction(AALOAD);
        e.addMemberAccessInstruction(INVOKESTATIC, "java/lang/Integer", "parseInt", "(Ljava/lang/String;)I");
        e.addNoArgInstruction(ISTORE_1);

        // boolean result = isPrime(n);
        // Boolean True -> 1, Boolean False -> 0. Use two slots for boolean and one for int n
        e.addNoArgInstruction(ILOAD_1);
        e.addMemberAccessInstruction(INVOKESTATIC, "IsPrime", "isPrime", "(I)Z");
        e.addNoArgInstruction(ISTORE_2);

        // Stack insertion for System.Out
        e.addMemberAccessInstruction(GETSTATIC, "java/lang/System", "out", "Ljava/io/PrintStream;");

        // Create StringBuffer instance on stack for string concatenation
        // sb = new StringBuffer();
        e.addReferenceInstruction(NEW, "java/lang/StringBuffer");
//        e.addNoArgInstruction(ALOAD_1); // not sure why it wont work. check appendix
        e.addNoArgInstruction(DUP);
        e.addMemberAccessInstruction(INVOKESPECIAL, "java/lang/StringBuffer", "<init>", "()V");

        // if (result) {
        e.addNoArgInstruction(ILOAD_2);
        e.addBranchInstruction(IFEQ, "notEqual");

        // System.out.println(n + " is a prime number ");
        // This part is for when a prime number is detected
        // Append n and ' is a prime number" to buffer
        e.addNoArgInstruction(ILOAD_1);
        e.addMemberAccessInstruction(INVOKEVIRTUAL, "java/lang/StringBuffer", "append",
                "(I)Ljava/lang/StringBuffer;");
        e.addLDCInstruction(" is a prime number");
        e.addMemberAccessInstruction(INVOKEVIRTUAL, "java/lang/StringBuffer", "append",
                "(Ljava/lang/String;)Ljava/lang/StringBuffer;");
        // System.out.println(sb.toString());
        e.addMemberAccessInstruction(INVOKEVIRTUAL, "java/lang/StringBuffer",
                "toString", "()Ljava/lang/String;");
        e.addMemberAccessInstruction(INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V");
        e.addBranchInstruction(GOTO, "prime");

        // System.out.println(n + " is not a prime number ");
        // Same as for when it is prime, only string output is different.
        e.addLabel("notEqual");
        e.addNoArgInstruction(ILOAD_1);
        e.addMemberAccessInstruction(INVOKEVIRTUAL, "java/lang/StringBuffer", "append",
                "(I)Ljava/lang/StringBuffer;");
        e.addLDCInstruction(" is not a prime number");
        e.addMemberAccessInstruction(INVOKEVIRTUAL, "java/lang/StringBuffer", "append",
                "(Ljava/lang/String;)Ljava/lang/StringBuffer;");
        // System.out.println(sb.toString());
        e.addMemberAccessInstruction(INVOKEVIRTUAL, "java/lang/StringBuffer",
                "toString", "()Ljava/lang/String;");
        e.addMemberAccessInstruction(INVOKEVIRTUAL, "java/io/PrintStream", "println", "(Ljava/lang/String;)V");

        // return
        e.addLabel("prime");
        e.addNoArgInstruction(RETURN);
        modifiers.clear();

        // isPrime
        modifiers.add("private");
        modifiers.add("static");
        e.addMethod(modifiers, "isPrime", "(I)Z", null, true);

        // if (n < 2) {
        e.addNoArgInstruction(ILOAD_0);
        e.addNoArgInstruction(ICONST_2);
        e.addBranchInstruction(IF_ICMPLT, "isNotPrime");

        // Below this comment line is 'for(int i = 2; i <= n/i; i++);'

        // for(int i = 2)
        e.addNoArgInstruction(ICONST_2);
        e.addNoArgInstruction(ISTORE_1);
        e.addLabel("forLoop");

        // i <= n/i;
        e.addNoArgInstruction(ILOAD_1); // i
        e.addNoArgInstruction(ILOAD_0); // n/i
        e.addNoArgInstruction(ILOAD_1);
        e.addNoArgInstruction(IDIV);

        // <=
        e.addBranchInstruction(IF_ICMPLE, "isLessThan");
        e.addNoArgInstruction(ICONST_1);
        e.addNoArgInstruction(IRETURN);
        e.addLabel("isLessThan");

        // if (n % i == 0) {
        e.addNoArgInstruction(ILOAD_0);
        e.addNoArgInstruction(ILOAD_1);
        e.addNoArgInstruction(IREM);
        e.addBranchInstruction(IFEQ, "isNotPrime");

        // if not 0 then increment by 1 until remainder is 0
        e.addIINCInstruction(1, 1);
        e.addBranchInstruction(GOTO, "forLoop");
        e.addLabel("isNotPrime");
        e.addNoArgInstruction(ICONST_0);
        e.addNoArgInstruction(IRETURN);

        // clear out before exit
        modifiers.clear();

        // exit to success. :)
        e.write();
    }
}
