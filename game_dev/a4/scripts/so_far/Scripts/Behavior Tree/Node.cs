using System.Collections;
using System.Collections.Generic;

namespace BehaviorTree
{
    /*
    Class to represent a single element in the behaviro tree
    and can:
    1. Access both its children and parents
    2. Can store, retrieve and clear
    */
    public enum NodeState
    {
        RUNNING,
        SUCCESS,
        FAILURE
    }
    public class Node 
    {
        // protected so that other derivable classes can access and modify this variable
        protected NodeState state;
        public Node parent;
        // store shared data in a dictionary. Using Object Type to make agnostic data storage
        private Dictionary<string, object> _dataContext = new Dictionary<string, object>();
        protected List<Node> children = new List<Node>();
        /*
        Having a link between children and parent in both directions 
        on the tree becasue it will streamline creating composite nodes
        by looking at the children and to have shared data by looking at the parent
        and backtracking in the branch
        */
        public Node()
        {
            parent = null;
        }
        public Node(List<Node> children)
        {
            foreach (Node child in children)
            {
                _Attach(child);
            }
        }
        // Create edges between parent and new child
        private void _Attach(Node node)
        {
            node.parent = this;
            children.Add(node);
        }

        /*
        Prototype evaluate function.
        Each derived node class can implement it's own 'evaluate'
        fucntion for a unique role in the behavior tree.
        */
        public virtual NodeState Evaluate() => NodeState.FAILURE;
        // Setter. Add key and store to dictionary
        public void SetData(string key, object value)
        {
            _dataContext[key] = value;
        }
        // Getter needs to verify whether data is defined somewhere in our branch.
        // Recursively work up the branch either until the key is found or have reached tree root
        public object GetData(string key)
        {
            object value = null;
            if (_dataContext.TryGetValue(key, out value))
            {
                return value;
            }
            Node node = parent;
            while (node != null)
            {
                value = node.GetData(key);
                if (value != null)
                    return value;
                node = node.parent;
            }
            return null;
        }
        // Clear data. Similar to GetData. We have to recursively search for key and remove
        // it upon discorvery in the branch then stop at the root
        public bool ClearData(string key)
        {
            if (_dataContext.ContainsKey(key))
            {
                _dataContext.Remove(key);
                return true;
            }

            Node node = parent;
            while (node != null)
            {
                bool cleared = node.ClearData(key);
                if (cleared)
                    return true;
                node = node.parent;
            }
            return false;
        }
    }
}
