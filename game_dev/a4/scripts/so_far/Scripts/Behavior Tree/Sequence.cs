using System.Collections;
using System.Collections.Generic;

namespace BehaviorTree
{
    /*
    Derived composite node class. An AND logic gate
    Only if all child nodes succeeds will it succeed itself
    */
    public class Sequence : Node
    {
        public Sequence() : base(){}
        public Sequence(List<Node> children) : base(children) {}
        public override NodeState Evaluate()
        {
            bool anyChildIsRunning = false;
            // Iteratively evaluate children nodes
            // If any child fails, we stop and return fail state
            // Otherwise keep processing the children nodes
            foreach (Node node in children)
            {
                switch (node.Evaluate())
                {
                    case NodeState.FAILURE:
                        state = NodeState.FAILURE;
                        return state;
                    case NodeState.SUCCESS:
                        continue;
                    case NodeState.RUNNING:
                        anyChildIsRunning = true;
                        continue;
                    default: 
                        state = NodeState.SUCCESS;
                        return state;
                }
            }
            state = anyChildIsRunning ? NodeState.RUNNING : NodeState.SUCCESS;
            return state;
        }
    }
}
