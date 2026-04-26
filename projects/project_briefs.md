# Robotics Portfolio Project Briefs

Pick at least three. One should be classical robotics, one should be robot learning, and one should be a systems project.

## Project 1: Differential-Drive Navigation

Build:
- Differential-drive simulator
- Noisy odometry
- Kalman filter
- Occupancy grid
- A* planner
- Pure pursuit controller

Metrics:
- Path length
- Final pose error
- Collision rate
- Localization RMSE

Related notebooks:
- 3, 4, 5, 6, 10, 16, 27

## Project 2: 2D Arm Manipulation

Build:
- 2-link or 3-link arm
- Forward kinematics
- Jacobian controller
- Trajectory generator
- Grasp state machine

Metrics:
- Endpoint error
- Joint-limit violations
- Time to reach
- Grasp success rate

Related notebooks:
- 2, 12, 14, 17, 20, 27

## Project 3: Imitation Learning Reacher

Build:
- Expert controller
- Demonstration dataset
- Dataset card
- Behavior cloning policy
- Closed-loop evaluator

Metrics:
- Validation MSE
- Final task success
- Intervention rate
- Generalization to new starts/goals

Related notebooks:
- 7, 23, 24, 25

## Project 4: Sim-To-Real Robust Controller

Build:
- Randomized simulator
- Controller parameter sweep
- Evaluation across randomized physics
- Report on sensitivity

Metrics:
- Mean final error
- 90th percentile error
- Collision or failure rate
- Robustness to latency/noise

Related notebooks:
- 15, 22, 26, 27

## Project 5: ROS 2 Architecture Design

Build:
- Node graph
- Message definitions
- Topic/service/action split
- Watchdog design
- Logging and replay plan

Optional implementation:
- ROS 2 Jazzy package with simulated nodes.

Related notebooks:
- 21, 27, 30

## Project 6: Research Reproduction

Build:
- Paper review
- Minimal reproduction
- Baseline
- One ablation
- Short report

Suggested papers:
- Diffusion Policy
- OpenVLA
- Octo
- SmolVLA
- LeRobot

Related notebooks:
- 9, 23, 25, 29, 30
