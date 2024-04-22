using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using BehaviorTree;
using UnityEngine.UIElements;
public class Patrol : Node 
{
    private Transform _transform;
    private Transform[] _waypoints;
    private int _currentWayPointIndex = 0;
    private float _waitTime = 1f;
    private float _waitCounter = 0f;
    private bool _isWaiting = false;
    public Patrol(Transform transform, Transform[] waypoints)
    {
        _transform = transform;
        _waypoints = waypoints;
    }
    public override NodeState Evaluate()
    {
        if(_isWaiting)
        {
            _waitCounter += Time.deltaTime;
            if(_waitCounter >= _waitTime)
            {
                _isWaiting = false;
            }
        }
        else 
        {
            Transform wp = _waypoints[_currentWayPointIndex];
            if(Vector3.Distance(_transform.position, wp.position) < 0.01f)
            {
                _transform.position = wp.position;
                _waitCounter = 0f;
                _isWaiting = true;

                _currentWayPointIndex = (_currentWayPointIndex + 1) % _waypoints.Length;
            }
            else 
            {
                _transform.position =  Vector3.MoveTowards(_transform.position, wp.position, ZombieBT.speed * Time.deltaTime);
                _transform.LookAt(wp.position);
            }
        }
        state = NodeState.RUNNING;
        return state;
    }
}
