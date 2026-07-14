# Robotics Glossary

## Action

The command sent to a robot or simulator. Examples: wheel velocity, joint target, torque, gripper command, end-effector delta.

## Actuator

A device that turns commands into motion or force, such as a motor or servo.

## Behavior Cloning

Supervised learning from demonstrations. The policy learns to map observations to expert actions.

## Action Chunk

A short sequence of future robot actions predicted at once. Action chunks reduce inference pressure but require low-level controllers and safety checks between model calls.

## Coordinate Frame

A reference origin and axes used to describe positions and orientations.

## Covariate Shift

The problem where a learned policy visits states not present in its training demonstrations.

## Dynamics

The relationship between forces, torques, mass, inertia, acceleration, and motion.

## Embodiment

The physical form of a robot: arms, grippers, wheels, sensors, degrees of freedom, and action space.

## Evaluation Harness

A repeatable framework for running models on shared tasks, metrics, and environments. In robot learning, a harness helps separate real progress from one-off demos.

## End Effector

The tool or hand at the end of a robot arm.

## Forward Kinematics

Computing end-effector pose from joint positions.

## Inverse Kinematics

Computing joint positions that achieve a desired end-effector pose.

## Jacobian

A matrix that maps joint velocities to end-effector velocities, locally.

## Kalman Filter

A recursive estimator that combines a motion model and noisy measurements.

## Motion Planning

Finding a collision-free path or trajectory from start to goal.

## Observation

What the robot senses. It may be incomplete or noisy.

## Occupancy Grid

A grid map where each cell stores the probability of being occupied.

## Policy

A function that maps observations to actions.

## Real-Time Chunking

A deployment strategy where a slower learned policy predicts short action chunks while faster robot control loops consume, smooth, monitor, and interrupt those actions.

## Proprioception

The robot's internal sensing, such as joint angles, velocities, currents, and gripper state.

## Reinforcement Learning

Learning behavior from rewards through trial and error.

## SLAM

Simultaneous localization and mapping: estimating robot pose and a map at the same time.

## State

The variables needed to describe the robot and relevant world.

## Transform

A mathematical object that maps points or poses from one coordinate frame to another.

## VLA

Vision-language-action model. A model that maps visual observations and language instructions to robot actions.

## VLA Evaluation

Testing a vision-language-action model across defined tasks, embodiments, action spaces, and metrics. Strong VLA evaluation reports uncertainty, failure cases, and benchmark mismatch.

## Capture Point

For simplified biped balance, the ground point where the robot should step or shift support to stop falling under the linear inverted pendulum model.

## LIPM

Linear inverted pendulum model. A simplified model of biped balance where the center of mass moves at roughly constant height.

## Support Polygon

The ground area enclosed by active contacts, such as a foot or both feet. A robot is more stable when its balance point remains inside this region.

## Whole-Body Control

Control that coordinates many joints and contacts to satisfy multiple tasks at once, such as balancing while moving a hand.

## Teleoperation

Human control of a robot, often used to collect demonstrations for imitation learning.
