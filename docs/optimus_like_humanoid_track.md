# Optimus-Like Humanoid Track

Checked on 2026-06-11.

This document explains how to study an Optimus-like robot using public information and open alternatives.

## Public Facts Versus Inference

Tesla Optimus is not open source. Public information confirms the goal of a general-purpose, bipedal, autonomous humanoid robot for unsafe, repetitive, or boring tasks, but detailed hardware specifications, training data, controller implementation, fleet learning infrastructure, manufacturing process, and safety case are not public.

Source:
- [Tesla AI & Robotics](https://www.tesla.com/AI?redirect=no)

So this course separates:

- Public claims: what Tesla or other organizations publicly state.
- General robotics principles: what any full-size humanoid requires.
- Open-source approximations: tools and platforms you can actually use.
- Speculation: ideas that may be plausible but should not be treated as fact.

## What An Optimus-Like Robot Requires

### 1. Mechatronics

You need:
- Human-scale structure
- High torque-density actuators
- Hands
- Thermal design
- Battery and power distribution
- Serviceable joints and wiring

Study:
- Notebook 32
- Notebook 43

### 2. Biped Locomotion

You need:
- State estimation
- Foot contact sensing or inference
- Balance control
- Whole-body dynamics
- RL or optimization-based locomotion
- Fall detection and recovery

Study:
- Notebook 33
- Notebook 34
- Notebook 35
- Notebook 40

### 3. Dexterous Manipulation

You need:
- Arm kinematics
- Hand control
- Tactile feedback
- Visual servoing
- Grasp planning
- Force-aware manipulation

Study:
- Notebook 17
- Notebook 20
- Notebook 36

### 4. Perception

You need:
- Cameras and calibration
- Depth or 3D reconstruction
- Object detection and tracking
- Human awareness
- Scene memory
- Task-relevant world state

Study:
- Notebook 18
- Notebook 19
- Notebook 37

### 5. Robot Learning

You need:
- Teleoperation
- Demonstration collection
- Dataset formats
- Imitation learning
- Action chunks
- Diffusion or flow policies
- VLA-style language-conditioned policies
- Closed-loop evaluation

Study:
- Notebook 7
- Notebook 23
- Notebook 24
- Notebook 25
- Notebook 38
- Notebook 39

### 6. Compute And Deployment

You need:
- Fast real-time control loops
- Perception pipelines
- On-device inference
- Watchdogs
- Logging
- Fleet updates

Study:
- Notebook 21
- Notebook 27
- Notebook 41

### 7. Safety

You need:
- Independent safety layers
- Human distance monitoring
- Force and speed limits
- Emergency stop
- Fall zones
- Validation before deployment
- Incident logs

Study:
- Notebook 27
- Notebook 42

## Open And Public Systems To Study

### GR00T

NVIDIA describes Isaac GR00T as a platform for humanoid robot foundation models and data pipelines, and announced GR00T N1 as an open foundation model for humanoid robots.

Sources:
- [NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t)
- [GR00T N1 research page](https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots)
- [GR00T N1 arXiv](https://arxiv.org/abs/2503.14734)

### Gemini Robotics

Google DeepMind describes Gemini Robotics as adapting across robot forms, including bimanual platforms and humanoids such as Apptronik Apollo. Gemini Robotics-ER focuses on embodied reasoning.

Sources:
- [Gemini Robotics](https://deepmind.google/models/gemini-robotics/)
- [Gemini Robotics-ER 1.6](https://deepmind.google/blog/gemini-robotics-er-1-6/)

### LeRobot

LeRobot is an open-source robot learning library with datasets, policies, supported robots, and simulation integrations. The v0.5 release includes Unitree G1 support and expanded simulation/policy support.

Sources:
- [LeRobot docs](https://huggingface.co/docs/lerobot/main/index)
- [LeRobot v0.5.0 announcement](https://huggingface.co/blog/lerobot-release-v050)
- [LeRobot paper](https://arxiv.org/abs/2602.22818)
- [Unitree G1 in LeRobot](https://huggingface.co/docs/lerobot/unitree_g1)
- [Reachy 2 in LeRobot](https://huggingface.co/docs/lerobot/en/reachy2)

### Open VLA Systems

Use these to understand the open equivalents of humanoid policy learning, while remembering that real deployment depends on embodiment, action space, latency, and safety layers.

Sources:
- [OpenPI](https://github.com/Physical-Intelligence/openpi)
- [SmolVLA](https://huggingface.co/blog/smolvla)
- [Xiaomi-Robotics-0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-0)
- [Dexora](https://github.com/dexoravla/Dexora)
- [vla-evaluation-harness](https://github.com/allenai/vla-evaluation-harness)

### Humanoid-Gym And Isaac Lab

Humanoid-Gym is an RL framework for humanoid locomotion with zero-shot sim-to-real emphasis. Isaac Lab is an open-source GPU-accelerated framework for robot learning across embodiments, including humanoids.

Sources:
- [Humanoid-Gym GitHub](https://github.com/roboterax/humanoid-gym)
- [Humanoid-Gym arXiv](https://arxiv.org/abs/2404.05695)
- [NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab)

### Open Hardware Platforms

Study these to understand accessible humanoid or humanoid-adjacent hardware:

- [ROBOTIS OP3 ROS index](https://index.ros.org/r/robotis_op3/)
- [Berkeley Humanoid](https://arxiv.org/abs/2407.21781)
- [Berkeley Humanoid Lite](https://arxiv.org/abs/2504.17249)
- [ToddlerBot](https://arxiv.org/abs/2502.00893)
- [OpenArm](https://github.com/reazon-research/openarm)
- [Reachy](https://www.pollen-robotics.com/reachy/)
- [RUKA-v2](https://ruka-hand-v2.github.io/)

For the most current open-source stack, use notebooks 46-50 and [latest open-source advancements](latest_open_source_advancements_2026.md).

## A Realistic Build Path

1. Finish notebooks 1-30.
2. Work through notebooks 31-45 for humanoid foundations.
3. Work through notebooks 46-50 to choose open-source tools with a radar instead of hype.
4. Build a mobile manipulation simulation.
5. Add a bimanual manipulation dataset.
6. Train a behavior cloning or action-chunk policy.
7. Build a humanoid locomotion simulation.
8. Add whole-body control and safety gates.
9. Evaluate an open humanoid platform if budget and safety allow.
10. Only then attempt full-body hardware experiments.

## What Not To Do

Do not:
- Start with a full-size untethered humanoid.
- Put a learned policy directly in charge of powerful motors.
- Treat trade-show demos as complete autonomy proof.
- Assume public marketing contains enough detail to reproduce a robot.
- Ignore safety because the robot is "just a prototype."
