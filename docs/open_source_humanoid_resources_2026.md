# Open-Source Humanoid Resources 2026

Checked on 2026-06-11.

This is a practical resource map for learning humanoid robotics with public and open tools.

## Simulation And Learning

### Isaac Lab

Open-source, GPU-accelerated robot learning framework built for scalable policy training across embodiments including humanoids.

Source:
- [NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab)

Use for:
- RL locomotion
- Sim-to-real workflows
- Large-scale randomized environments

### MuJoCo

Open physics simulator widely used for control, locomotion, and robot learning.

Source:
- [MuJoCo](https://mujoco.org/)

Use for:
- Fast local dynamics experiments
- Control and RL prototyping
- Contact-rich simulation

### Humanoid-Gym

Humanoid locomotion RL framework based on Isaac Gym with sim-to-real transfer emphasis.

Sources:
- [Humanoid-Gym GitHub](https://github.com/roboterax/humanoid-gym)
- [Humanoid-Gym arXiv](https://arxiv.org/abs/2404.05695)

Use for:
- Learning humanoid locomotion training recipes
- Domain randomization
- Sim-to-sim validation

### Booster Gym

End-to-end RL framework for humanoid locomotion from Booster Robotics.

Source:
- [Booster Gym](https://booster-gym.github.io/)

Use for:
- Comparing locomotion training stacks
- Studying modern humanoid RL workflows

## Robot Learning And VLA

### LeRobot

Open-source library for robot learning with policies, datasets, robot integrations, and simulation support.

Sources:
- [LeRobot docs](https://huggingface.co/docs/lerobot/main/index)
- [LeRobot v0.5.0](https://huggingface.co/blog/lerobot-release-v050)
- [LeRobot arXiv](https://arxiv.org/abs/2602.22818)
- [Unitree G1 in LeRobot](https://huggingface.co/docs/lerobot/unitree_g1)
- [Reachy 2 in LeRobot](https://huggingface.co/docs/lerobot/en/reachy2)

Use for:
- Dataset collection
- Imitation learning
- Policy training
- Open robot integrations
- Humanoid and bimanual learning workflows

### SmolVLA

Compact VLA model for affordable and efficient robotics.

Sources:
- [SmolVLA arXiv](https://arxiv.org/abs/2506.01844)
- [Hugging Face SmolVLA announcement](https://huggingface.co/blog/smolvla)
- [SmolVLA docs in LeRobot](https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx)

Use for:
- Understanding efficient VLA policies
- Learning action chunks and asynchronous inference ideas

### OpenPI / pi0 / pi0.5

OpenPI provides open code and checkpoints for pi0-family VLA policies, including pi0, pi0-FAST, and pi0.5-style workflows.

Sources:
- [OpenPI GitHub](https://github.com/Physical-Intelligence/openpi)
- [Open-sourcing pi0](https://www.pi.website/blog/openpi)
- [LeRobot pi0.5 docs](https://huggingface.co/docs/lerobot/en/pi05)

Use for:
- Understanding flow-matching VLA policies
- Fine-tuning public robot foundation models
- Studying action-token and chunked-action deployment constraints

### Xiaomi-Robotics-0

Open real-time VLA model direction with emphasis on smooth, asynchronous execution and public code/model links.

Sources:
- [Xiaomi-Robotics-0 project](https://xiaomi-robotics-0.github.io/)
- [Xiaomi-Robotics-0 GitHub](https://github.com/XiaomiRobotics/Xiaomi-Robotics-0)
- [Xiaomi-Robotics-0 arXiv](https://arxiv.org/html/2602.12684v1)

Use for:
- Real-time VLA architecture study
- Benchmark comparison against LIBERO, SimplerEnv, CALVIN, and bimanual tasks
- Advanced reading after you understand action chunking

### Dexora

Open-source VLA system for high-DoF dual-arm dual-hand dexterous manipulation.

Sources:
- [Dexora GitHub](https://github.com/dexoravla/Dexora)
- [Dexora arXiv](https://arxiv.org/abs/2605.18722)

Use for:
- Bimanual dexterity research
- Teleoperation and high-DoF action-space design
- Understanding data quality requirements for humanoid manipulation

### GR00T

Humanoid robot foundation model ecosystem from NVIDIA.

Sources:
- [NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t)
- [GR00T N1 arXiv](https://arxiv.org/abs/2503.14734)

Use for:
- Understanding humanoid VLA architecture
- Synthetic data and post-training concepts

## Hardware Platforms

### ROBOTIS OP3

Miniature humanoid platform with ROS support.

Source:
- [ROBOTIS OP3 ROS index](https://index.ros.org/r/robotis_op3/)

Use for:
- Humanoid basics
- Walking modules
- ROS-based humanoid software

### Reachy 2 And Reachy Mini

Open-source humanoid and desktop humanoid-adjacent robots in the Pollen Robotics / Hugging Face ecosystem.

Sources:
- [Pollen Robotics Reachy](https://www.pollen-robotics.com/reachy/)
- [Reachy 2 in LeRobot docs](https://huggingface.co/docs/lerobot/en/reachy2)
- [Pollen Robotics on Hugging Face](https://huggingface.co/pollen-robotics)

Use for:
- Accessible embodied AI experiments
- Bimanual manipulation and teleoperation practice
- A safer stepping stone before full-size humanoids

### Berkeley Humanoid And Berkeley Humanoid Lite

Research humanoid platforms focused on learning-based control and accessible customization.

Sources:
- [Berkeley Humanoid arXiv](https://arxiv.org/abs/2407.21781)
- [Berkeley Humanoid Lite arXiv](https://arxiv.org/abs/2504.17249)

Use for:
- Studying accessible humanoid design
- Learning locomotion platform constraints

### ToddlerBot

Low-cost open-source humanoid platform for loco-manipulation research.

Source:
- [ToddlerBot arXiv](https://arxiv.org/abs/2502.00893)

Use for:
- Understanding low-cost humanoid design
- Learning reproducible hardware documentation practices

### OpenArm

Open-source 7-DOF humanoid arm aimed at physical AI research and contact-rich manipulation.

Source:
- [OpenArm GitHub](https://github.com/reazon-research/openarm)

Use for:
- Bimanual manipulation
- Teleoperation
- Imitation learning
- ROS 2 and MuJoCo practice

### RUKA-v2

Fully open-source tendon-driven humanoid hand with a wrist and finger abduction/adduction.

Sources:
- [RUKA-v2 project page](https://ruka-hand-v2.github.io/)
- [RUKA-v2 arXiv](https://arxiv.org/abs/2603.26660)

Use for:
- Dexterous-hand mechanics
- Tendon routing and calibration
- Manipulation safety and maintenance planning

## Benchmarks And Evaluation

### vla-evaluation-harness

Open evaluation harness for comparing VLA models across simulation benchmarks and model servers.

Sources:
- [vla-evaluation-harness GitHub](https://github.com/allenai/vla-evaluation-harness)
- [VLA leaderboard](https://allenai.github.io/vla-evaluation-harness/leaderboard/)
- [vla-eval OpenReview](https://openreview.net/forum?id=IpKQsHWaYS)

Use for:
- Reproducible VLA evaluation
- Benchmark mismatch analysis
- Confidence intervals and model comparison discipline

## Suggested Learning Lab

### Laptop-only

Use:
- Notebooks
- MuJoCo
- LeRobot datasets
- simple NumPy simulations

Goal:
- Understand concepts without hardware risk.

### Simulation workstation

Use:
- Isaac Lab
- Humanoid-Gym
- LeRobot
- ROS 2

Goal:
- Train and evaluate policies in randomized simulation.

### Low-cost hardware

Use:
- OpenArm or a small arm
- mobile base
- cameras
- ROS 2
- LeRobot

Goal:
- Learn calibration, teleoperation, real data, and safety.

### Humanoid hardware

Use only with:
- Tethers or support rig
- emergency stop
- safety mentor
- clear test cell
- slow-speed bringup
- logs and incident review

Goal:
- Transfer a small, well-tested subsystem from simulation to hardware.
