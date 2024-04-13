// Copyright 2012- Bill Campbell, Swami Iyer and Bahar Akbal-Delibas

package jminusminus;

import static jminusminus.CLConstants.*;

/**
 * The AST node for a double literal.
 */
class JLiteralDouble extends JExpression {
    // String representation of the literal.
    private String text;

    /**
     * Constructs an AST node for a double literal given its line number and string representation.
     *
     * @param line line in which the literal occurs in the source file.
     * @param text string representation of the literal.
     */
    public JLiteralDouble(int line, String text) {
        super(line);
        this.text = text;
    }

    /**
     * Returns the literal as a double.
     *
     * @return the literal as a double.
     */
    public double toDouble() {
        return Double.parseDouble(text);
    }

    /**
     * {@inheritDoc}
     */
    public JExpression analyze(Context context) {
        // Added Proj5, same as JLiteralLong
        type = Type.DOUBLE;
        return this;
    }

    /**
     * {@inheritDoc}
     */
    public void codegen(CLEmitter output) {
        // Added Proj5, same as JLiteralLong
        double myDouble = toDouble();
        if(myDouble == 0d){
            output.addNoArgInstruction(DCONST_0);
        }
        else if (myDouble == 1d)
        {
            output.addNoArgInstruction(DCONST_1);
        }
        else {
        output.addLDCInstruction(myDouble);
        }
    }

    /**
     * {@inheritDoc}
     */
    public void toJSON(JSONElement json) {
        JSONElement e = new JSONElement();
        json.addChild("JLiteralDouble:" + line, e);
        e.addAttribute("type", type == null ? "" : type.toString());
        e.addAttribute("value", text);
    }
}
