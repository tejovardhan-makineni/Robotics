# Robotics Glossary

## Action

The command sent to a robot or simulator. Examples: wheel velocity, joint target, torque, gripper command, end-effector delta.

## Actuator

A device that turns commands into motion or force, such as a motor or servo.

## Behavior Cloning

Supervised learning from demonstrations. The policy learns to map observations to expert actions.

## Coordinate Frame

A reference origin and axes used to describe positions and orientations.

## Covariate Shift

The problem where a learned policy visits states not present in its training demonstrations.

## Dynamics

The relationship between forces, torques, mass, inertia, acceleration, and motion.

## Embodiment

The physical form of a robot: arms, grippers, wheels, sensors, degrees of freedom, and action space.

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
