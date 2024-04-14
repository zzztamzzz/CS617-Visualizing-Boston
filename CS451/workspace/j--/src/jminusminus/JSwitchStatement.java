// Copyright 2012- Bill Campbell, Swami Iyer and Bahar Akbal-Delibas

package jminusminus;

import java.util.ArrayList;

import static jminusminus.CLConstants.*;

// Added Proj 5
import java.util.Comparator;
import java.util.TreeMap;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * The AST node for a switch-statement.
 */
public class JSwitchStatement extends JStatement {
    // Test expression.
    private JExpression condition;

    // List of switch-statement groups.
    private ArrayList<SwitchStatementGroup> stmtGroup;
    /*
    Added Proj 5
    For interget literal verification for case expression. 2nd bullet on instructions
    */
    private int lo, hi, nLabels;
    private ArrayList<Integer> ascendingArrL;
    boolean sawBreakWord;
    String breakLabelStr;
    boolean hasDefault = false; // default label

    /**
     * Constructs an AST node for a switch-statement.
     *
     * @param line      line in which the switch-statement occurs in the source file.
     * @param condition test expression.
     * @param stmtGroup list of statement groups.
     */
    public JSwitchStatement(int line, JExpression condition,
                            ArrayList<SwitchStatementGroup> stmtGroup) {
        super(line);
        this.condition = condition;
        this.stmtGroup = stmtGroup;
    }

    /**
     * {@inheritDoc}
     */
    public JStatement analyze(Context context) {
        // Added Proj 5
        condition = condition.analyze(context);
        condition.type().mustMatchExpected(line(), Type.INT);

        AtomicInteger nLabels = new AtomicInteger();
        ArrayList<Integer> ascendingArrL = new ArrayList<>();
        LocalContext statement;

        for (SwitchStatementGroup switchStatement : stmtGroup) {
            statement = new LocalContext(context);
            LocalContext finalStatement1 = statement;
            switchStatement.getSwitchLabels().forEach(caseInSwitch -> {
                if(caseInSwitch != null){
                    caseInSwitch.analyze(finalStatement1);
                    caseInSwitch.type().mustMatchExpected(line(), Type.INT);
                    ascendingArrL.add(((JLiteralInt) caseInSwitch).toInt());
                    nLabels.getAndIncrement();
                }
            });

            LocalContext finalStatement = statement;
            switchStatement.getBlock().forEach(block -> {
                if (block instanceof JBreakStatement) {
                    JMember.enclosingStatement.push(this);
                }
                block.analyze(finalStatement);
            });
        }

        ascendingArrL.sort(Comparator.naturalOrder());
        int lo = ascendingArrL.get(0);
        int hi = ascendingArrL.get(ascendingArrL.size() - 1);

        return this;
    }

    /**
     * {@inheritDoc}
     */
    public void codegen(CLEmitter output) {
        // Added Proj 5
        breakLabelStr = output.createLabel();
        condition.codegen(output);
        String defaultLabel = output.createLabel();
        switch (TableLookS()) {
            case TABLESWITCH:
                ArrayList<String> labelsTable = new ArrayList<>();
                boolean hasDefaultTable = false;

                for (SwitchStatementGroup switchStatement : stmtGroup) {
                    for (JExpression caseInSwitch : switchStatement.getSwitchLabels()) {
                        if (caseInSwitch != null) {
                            labelsTable.add(output.createLabel());
                        } else {
                            output.addLabel(defaultLabel);
                            hasDefaultTable = true;
                        }
                    }
                }

                output.addTABLESWITCHInstruction(defaultLabel, lo, hi, labelsTable);

                int labelsIndexTable = 0;
                for (SwitchStatementGroup tempGroup : stmtGroup) {
                    for (JExpression switchLabel : tempGroup.getSwitchLabels()) {
                        if (switchLabel != null) {
                            output.addLabel(labelsTable.get(labelsIndexTable));
                        }
                        labelsIndexTable++;
                    }

                    tempGroup.getBlock().forEach(statement -> statement.codegen(output));
                }

                if (!hasDefaultTable) {
                    output.addLabel(defaultLabel);
                }
                break;

            case LOOKUPSWITCH:
                TreeMap<Integer, String> matchLabelPairs = new TreeMap<>();
                boolean hasDefaultLookup = false;

                for (SwitchStatementGroup switchStatement : stmtGroup) {
                    for (JExpression caseInSwitch : switchStatement.getSwitchLabels()) {
                        if (caseInSwitch != null) {
                            int key = ((JLiteralInt) caseInSwitch).toInt();
                            matchLabelPairs.put(key, output.createLabel());
                        } else {
                            output.addLabel(defaultLabel);
                            hasDefaultLookup = true;
                        }
                    }
                }
                output.addLOOKUPSWITCHInstruction(defaultLabel, matchLabelPairs.size(), matchLabelPairs);

                for (SwitchStatementGroup tempGroup : stmtGroup) {
                    for (JExpression switchLabel : tempGroup.getSwitchLabels()) {
                        if (switchLabel == null) {
                            output.addLabel(defaultLabel);
                        } else {
                            int key = ((JLiteralInt) switchLabel).toInt();
                            output.addLabel(matchLabelPairs.get(key));
                        }
                    }

                    tempGroup.getBlock().forEach(statement -> statement.codegen(output));
                }

                if (!hasDefaultLookup) {
                    output.addLabel(defaultLabel);
                }
                break;
        }
        if (sawBreakWord) {
            output.addLabel(breakLabelStr);
        }
    }


    /**
     * The algorithm for codegen to decide which instruction
     *  (TABLESWITCH or LOOKUPSWITCH) to emit using the above heuristic.
     */

    private int TableLookS() {
        long tableSpaceCost = 5 + hi - lo;
        long tableTimeCost = 3;
        long lookupSpaceCost = 3 + 2 * nLabels;
        long lookupTimeCost = nLabels;
        return nLabels > 0 && (tableSpaceCost + 3 * tableTimeCost <= lookupSpaceCost + 3 * lookupTimeCost) ?
                TABLESWITCH : LOOKUPSWITCH;
    }

    /**
     * {@inheritDoc}
     */
    public void toJSON(JSONElement json) {
        JSONElement e = new JSONElement();
        json.addChild("JSwitchStatement:" + line, e);
        JSONElement e1 = new JSONElement();
        e.addChild("Condition", e1);
        condition.toJSON(e1);
        for (SwitchStatementGroup group : stmtGroup) {
            group.toJSON(e);
        }
    }
}

/**
 * A switch statement group consists of case labels and a block of statements.
 */
class SwitchStatementGroup {
    // Case labels.
    private ArrayList<JExpression> switchLabels;

    // Block of statements.
    private ArrayList<JStatement> block;

    /**
     * Constructs a switch-statement group.
     *
     * @param switchLabels case labels.
     * @param block        block of statements.
     */
    public SwitchStatementGroup(ArrayList<JExpression> switchLabels, ArrayList<JStatement> block) {
        this.switchLabels = switchLabels;
        this.block = block;
    }

    public ArrayList<JStatement> getBlock() {
        return block;
    }

    public ArrayList<JExpression> getSwitchLabels() {
        return switchLabels;
    }

    /**
     * Stores information about this switch statement group in JSON format.
     *
     * @param json the JSON emitter.
     */
    public void toJSON(JSONElement json) {
        JSONElement e = new JSONElement();
        json.addChild("SwitchStatementGroup", e);
        for (JExpression label : switchLabels) {
            JSONElement e1 = new JSONElement();
            if (label != null) {
                e.addChild("Case", e1);
                label.toJSON(e1);
            } else {
                e.addChild("Default", e1);
            }
        }
        if (block != null) {
            for (JStatement stmt : block) {
                stmt.toJSON(e);
            }
        }
    }
}
