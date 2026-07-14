# Zero To Hero Robotics Course

This is the complete learning path for the repository. The goal is to move from first principles to a realistic understanding of how Optimus-like humanoid robots can be approached with public knowledge and open tools.

## Course Promise

If you work through this course seriously, you should be able to:

- Explain the full robotics stack from math to deployment.
- Build simulated mobile robots and manipulators.
- Implement estimation, planning, and control from scratch.
- Train simple policies from demonstrations and rewards.
- Understand modern VLA, diffusion, and humanoid robot learning systems.
- Design an open-source humanoid learning lab.
- Plan an Optimus-style capstone without confusing public facts, research prototypes, and speculation.

This course will not magically make a full Tesla Optimus clone possible. Tesla Optimus is not open source, and its detailed hardware, software, data, and manufacturing systems are not public. The course teaches the principles and open equivalents you can study.

## Phase 0: Setup

Read:
- `README.md`
- `docs/00_mastery_map.md`
- `docs/safety_first.md`

Run:
- `python3 tests/test_core.py`
- `MPLBACKEND=Agg python3 scripts/smoke_check_notebooks.py`

## Phase 1: Robot Fundamentals

Notebooks:
- 01 Robot loop
- 02 Kinematics and frames
- 03 Dynamics and control
- 11 Math for robotics
- 12 Spatial math
- 13 Dynamics and energy
- 14 Trajectory generation

Outcome:
- You can model state, action, frames, transforms, simple dynamics, and smooth motion.

## Phase 2: Classical Robot Stack

Notebooks:
- 04 State estimation
- 05 Mapping and SLAM intro
- 06 Motion planning
- 10 Capstone robot stack
- 15 LQR and MPC
- 16 Mobile robot models

Outcome:
- You can build a simulated robot that estimates, plans, controls, and evaluates behavior.

## Phase 3: Manipulation And Perception

Notebooks:
- 17 Manipulator Jacobian control
- 18 Computer vision geometry
- 19 Lidar and ICP
- 20 Grasping and manipulation

Outcome:
- You can reason about arms, cameras, point clouds, grasps, and manipulation sequences.

## Phase 4: Robot Software And Safety

Notebooks:
- 21 ROS 2 architecture
- 22 Simulation and domain randomization
- 27 Robot safety and reliability
- 28 Multi-robot coordination

Outcome:
- You can design a robot as a distributed, logged, safety-aware software system.

## Phase 5: Robot Learning

Notebooks:
- 07 Imitation learning
- 08 Reinforcement learning
- 23 Robot dataset engineering
- 24 Behavior cloning with a NumPy MLP
- 25 Diffusion policy intuition
- 26 Continuous-control RL with CEM

Outcome:
- You can create datasets, train toy policies, evaluate them closed-loop, and explain why robot learning is difficult.

## Phase 6: Research Literacy

Notebooks:
- 09 Modern robot learning and VLAs
- 29 Reading robotics research
- 30 Master capstone portfolio

Outcome:
- You can read modern robotics papers and extract what is implementable.

## Phase 7: Humanoid And Optimus-Style Track

Notebooks:
- 31 Humanoid systems overview
- 32 Humanoid mechatronics and actuators
- 33 Biped balance with LIPM
- 34 Humanoid locomotion RL intuition
- 35 Whole-body control
- 36 Humanoid hands and tactile manipulation
- 37 Humanoid perception stack
- 38 Teleoperation and data factory
- 39 Humanoid VLA architecture
- 40 Sim-to-real for humanoids
- 41 Humanoid edge compute
- 42 Humanoid safety and standards mindset
- 43 Humanoid manufacturing and cost
- 44 Open-source humanoid lab
- 45 Optimus-style capstone

Outcome:
- You can explain the major ingredients of an Optimus-like humanoid and design an achievable open-source learning roadmap.

## Phase 8: Latest Open-Source Frontier

Notebooks:
- 46 Open-source robotics frontier radar
- 47 Open VLA models and action heads
- 48 Open benchmarks and evaluation harnesses
- 49 Open simulators and synthetic data
- 50 Open hardware, humanoids, and dexterity

Outcome:
- You can keep your own robotics radar current, choose open-source tools responsibly, and avoid chasing demos that are not reproducible.

## Mastery Projects

Complete at least three:

1. Differential-drive navigation stack.
2. 2D or 3D arm manipulation stack.
3. Robot learning dataset and policy.
4. ROS 2 simulation with safety checks.
5. Humanoid locomotion simulation.
6. Humanoid VLA-style manipulation mockup.
7. Optimus-style capstone plan with metrics and safety gates.

## Graduation Standard

You are ready to call yourself serious about robotics when you can:

- Build and debug a working simulated robot.
- Explain why it fails.
- Improve it using either better models, better controllers, better data, or better safety layers.
- Read a current paper and reproduce a simplified result.
- Design a safe path from simulation to hardware.
