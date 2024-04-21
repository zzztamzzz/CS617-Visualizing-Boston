using UnityEngine;
using UnityEngine.AI;


[RequireComponent(typeof(Animator))]
public class AnimationHandler : MonoBehaviour {
	[SerializeField] float m_MovingTurnSpeed = 360;
	[SerializeField] float m_StationaryTurnSpeed = 180;						
	[SerializeField] float m_AnimSpeedMultiplier = 1f;
		

	Animator m_Animator;
		
	float m_TurnAmount;
	float m_ForwardAmount;
	Vector3 m_GroundNormal;
		


	void Start() {
		m_Animator = GetComponent<Animator>();
		m_Animator.applyRootMotion = true;

	}


    public void Update() {
		Move(GetComponent<NavMeshAgent>().velocity);
    }
    public void Idle() {
		m_Animator.SetFloat("Forward", 0);
		m_Animator.SetFloat("Turn", 0);

	}
	public void Move(Vector3 move) {

		// convert the world relative moveInput vector into a local-relative
		// turn amount and forward amount required to head in the desired
		// direction.
		if(move.magnitude > 1f) move.Normalize();
		move = transform.InverseTransformDirection(move);
		move = Vector3.ProjectOnPlane(move, m_GroundNormal);
		m_TurnAmount = Mathf.Atan2(move.x, move.z);
		m_ForwardAmount = move.z;

		ApplyExtraTurnRotation();

		// send input and other state parameters to the animator
		// update the animator parameters
		m_Animator.SetFloat("Forward", m_ForwardAmount, 0.1f, Time.deltaTime);
		m_Animator.SetFloat("Turn", m_TurnAmount, 0.1f, Time.deltaTime);
		m_Animator.speed = 1;

	}





	void ApplyExtraTurnRotation() {
		// help the character turn faster (this is in addition to root rotation in the animation)
		float turnSpeed = Mathf.Lerp(m_StationaryTurnSpeed, m_MovingTurnSpeed, m_ForwardAmount);
		transform.Rotate(0, m_TurnAmount * turnSpeed * Time.deltaTime, 0);
	}


		

}

