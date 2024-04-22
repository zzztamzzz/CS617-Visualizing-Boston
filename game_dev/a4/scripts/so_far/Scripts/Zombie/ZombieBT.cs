using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using BehaviorTree;
public class ZombieBT : BehaviorTree.Tree
{
    public UnityEngine.Transform[] waypoints;
    public static float speed = 2f;
    protected override Node SetupTree()
    {
        Node root = new Patrol(transform, waypoints);
        return root;
    }
}
