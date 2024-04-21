using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using BehaviorTree;
public class Patrol : Node
{
    private Transform _transforms;
    private Transform[] _waypoints;
    public Patrol(Transform transform, Transform[] waypoints)
    {
        _transforms = transform;
        _waypoints = waypoints;
    }

    // public override NodeState Evaluate()
    // {
    //     return base.Evaluate();
    // }
}
