// Copyright 2012- Bill Campbell, Swami Iyer and Bahar Akbal-Delibas

package jminusminus;

import static jminusminus.CLConstants.*;

/**
 * An AST node for a break-statement.
 */
public class JBreakStatement extends JStatement {
    private JStatement enclosingStatement; // Added Proj 5
    /**
     * Constructs an AST node for a break-statement.
     *
     * @param line line in which the break-statement occurs in the source file.
     */
    public JBreakStatement(int line) {
        super(line);
    }

    /**
     * {@inheritDoc}
     */
    public JStatement analyze(Context context) {
        // Added Proj 5
        enclosingStatement = JMember.enclosingStatement.peek();
        if (enclosingStatement instanceof JDoStatement) {
            ((JDoStatement) enclosingStatement).hasBreak = true;

        } else if (enclosingStatement instanceof JForStatement) {
            ((JForStatement) enclosingStatement).hasBreak = true;

        } else if (enclosingStatement instanceof JSwitchStatement) {
            ((JSwitchStatement) enclosingStatement).sawBreakWord = true;

        } else if (enclosingStatement instanceof JWhileStatement) {
            ((JWhileStatement) enclosingStatement).hasBreak = true;
        }
        return this;
    }

    /**
     * {@inheritDoc}
     */
    public void codegen(CLEmitter output) {
        // Added Proj 5
        if (enclosingStatement instanceof JDoStatement) {
            output.addBranchInstruction(GOTO, ((JDoStatement) enclosingStatement).breakLabel);

        } else if (enclosingStatement instanceof JSwitchStatement) {
            output.addBranchInstruction(GOTO, ((JSwitchStatement) enclosingStatement).breakLabelStr);

        } else if (enclosingStatement instanceof JWhileStatement) {
            output.addBranchInstruction(GOTO, ((JWhileStatement) enclosingStatement).breakLabel);

        } else if (enclosingStatement instanceof JForStatement) {
            output.addBranchInstruction(GOTO, ((JForStatement) enclosingStatement).breakLabelStr);
        }
    }

    /**
     * {@inheritDoc}
     */
    public void toJSON(JSONElement json) {
        JSONElement e = new JSONElement();
        json.addChild("JBreakStatement:" + line, e);
    }
}
