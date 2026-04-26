# Robotics Mastery Map

This project is built as a path from first principles to modern robot learning. The goal is not to memorize algorithms. The goal is to become the kind of person who can look at a robot system, understand its moving parts, debug it, improve it, and eventually train useful behavior.

## The Five Layers

### 1. Math and physical intuition

Master:
- Vectors, matrices, least squares, covariance
- Coordinate frames and transforms
- Rotations in 2D and 3D
- Dynamics, energy, constraints, friction
- Probability and uncertainty

Evidence of mastery:
- You can draw frames before writing code.
- You can predict units and signs.
- You can explain what each matrix maps from and to.

Primary notebooks: 1, 2, 3, 11, 12, 13, 14.

### 2. Classical robotics

Master:
- Kinematics
- Feedback control
- State estimation
- Mapping
- Motion planning
- Trajectory generation
- Manipulation primitives

Evidence of mastery:
- You can make a robot reach, drive, localize, and plan in simulation.
- You can explain the failure modes of PID, A*, RRT, Kalman filters, ICP, and Jacobian IK.
- You can evaluate a robot behavior with measurable metrics.

Primary notebooks: 2, 4, 5, 6, 10, 15, 16, 17, 18, 19, 20.

### 3. Robot software systems

Master:
- Nodes, topics, services, actions
- Message schemas and timestamps
- Transforms and robot descriptions
- Logging, replay, debugging
- Simulation integration
- Safety interlocks

Evidence of mastery:
- You can split a robot into planner, estimator, controller, perception, and logger.
- You can identify whether a bug belongs to sensing, estimation, planning, control, timing, or hardware.
- You can write a minimal ROS 2 architecture diagram before implementing.

Primary notebooks: 21, 22, 27, 30.

### 4. Robot learning

Master:
- Demonstration collection
- Behavior cloning
- Action chunking
- Dataset normalization and splits
- Reinforcement learning in simulation
- Domain randomization
- Diffusion and flow-policy intuition
- Evaluation under distribution shift

Evidence of mastery:
- You can collect or simulate a dataset and write a dataset card.
- You can train a simple policy and evaluate closed-loop success.
- You understand why offline validation error is not the same as robot success.

Primary notebooks: 7, 8, 9, 22, 23, 24, 25, 26.

### 5. Modern foundation robotics

Master:
- Vision-language-action models
- Embodied reasoning
- Cross-embodiment datasets
- Generalist policies
- Fine-tuning versus training from scratch
- Safety and deployment constraints

Evidence of mastery:
- You can read a VLA paper and extract observation/action spaces, data sources, baselines, metrics, and limits.
- You can explain why modern systems still need classical robotics.
- You can propose a realistic fine-tuning and evaluation plan for one robot skill.

Primary notebooks: 9, 23, 25, 29, 30.

## The Mastery Loop

For every topic:

1. Read the short explanation.
2. Run the notebook.
3. Change one assumption.
4. Break the system intentionally.
5. Fix it.
6. Write what failed and why.
7. Connect it to a real robot system or research paper.

You master robotics by debugging the gap between the model in your head and the behavior in the world.

## Suggested Outcome

By the end, you should have:

- 30 completed notebooks.
- A glossary of concepts in your own words.
- At least 3 portfolio projects.
- One paper reproduction or partial reproduction.
- One ROS 2 simulation project.
- One robot-learning dataset and trained policy.
- A written safety and evaluation plan.
