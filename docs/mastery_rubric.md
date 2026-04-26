# Mastery Rubric

Use this to honestly assess progress.

## Level 1: Familiar

You can:
- Run the notebooks.
- Recognize major terms.
- Explain state, action, observation, and feedback.

Not enough yet:
- You cannot debug failures without looking at the solution.

## Level 2: Functional

You can:
- Modify notebook parameters and predict outcomes.
- Implement simple controllers and planners.
- Explain common failure modes.

Evidence:
- You complete notebooks 1-10 and one small project.

## Level 3: Builder

You can:
- Build a small robot stack from components.
- Add logging and evaluation.
- Write safety checks.
- Train a behavior cloning policy and evaluate closed-loop success.

Evidence:
- You complete notebooks 1-24.
- You build a simulated robot project with metrics.

## Level 4: Research-Ready

You can:
- Read papers critically.
- Reproduce a simplified result.
- Compare baselines.
- Explain data, action representation, and evaluation design.

Evidence:
- You complete notebooks 25-30.
- You write a paper-style report on one reproduction.

## Level 5: Real-World Capable

You can:
- Bring up hardware safely.
- Debug timing, calibration, sensing, and control.
- Move from simulation to real tests gradually.
- Collect data and improve a policy through failure analysis.

Evidence:
- You have one physical or high-fidelity simulated robot project with safety notes, logs, metrics, and a demo.

## The Honest Test

For any robot behavior, you should be able to answer:

1. What does the robot observe?
2. What action does it command?
3. What state is hidden?
4. What assumptions does the controller or policy make?
5. What can fail?
6. How would you detect failure?
7. How would you stop safely?
8. How would you improve it with data?
