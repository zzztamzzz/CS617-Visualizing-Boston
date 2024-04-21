using System.Collections;
using System.Collections.Generic;
using UnityEngine;
namespace BehaviorTree
{
    /*
    Derived Node class file that contains a reference
    to a root that is a node that itself recursively contains 
    the entire tree
    */
    public abstract class Tree : MonoBehaviour
    {
        private Node _root = null;
        // On launch
        protected void Start()
        {
            _root = SetupTree();
        }
        // Continuously evaluate if tree exists
        private void Update()
        {
            if(_root != null)
            {
                _root.Evaluate();
            }
        }
        // Base class for sequence and selector classes
        protected abstract Node SetupTree();
    }
}
