# Robotics Software Toolchain 2026

Checked on 2026-04-26.

This guide is a practical map of tools worth learning after you finish the core notebooks.

## ROS 2

Use ROS 2 for real robot software architecture: nodes, topics, services, actions, parameters, transforms, launch files, logging, replay, and distributed systems.

Current orientation:
- Kilted Kaiju is the latest released ROS 2 distribution.
- Jazzy Jalisco is the latest long-term support distribution.
- Lyrical Luth is planned for May 2026.

Sources:
- [ROS 2 distributions](https://docs.ros.org/en/ros2_documentation/kilted/Releases.html)
- [ROS getting started](https://ros.org/blog/getting-started/)

Learn after notebooks: 1, 2, 3, 4, 6, 21, 27.

## Nav2

Use Nav2 for mobile robot navigation. It provides perception, planning, control, localization, behavior trees, waypoint following, recovery behavior, and lifecycle management.

Source:
- [Nav2 docs](https://docs.nav2.org/)

Learn after notebooks: 5, 6, 16, 21, 27.

## MoveIt 2

Use MoveIt 2 for manipulation: robot model loading, motion planning, collision checking, grasp/manipulation pipelines, and integration with ROS 2.

Sources:
- [MoveIt 2 package docs](https://docs.ros.org/en/ros2_packages/rolling/api/moveit/)
- [MoveIt 2 repository](https://github.com/moveit/moveit2)

Learn after notebooks: 2, 14, 17, 18, 20, 21.

## ros2_control

Use ros2_control to connect controllers to hardware and simulation. It is the layer that helps separate high-level behavior from actuator-specific details.

Source:
- [ros2_control docs](https://control.ros.org/)

Learn after notebooks: 3, 15, 16, 21, 27.

## Gazebo Sim

Use Gazebo Sim for ROS-integrated simulation, sensors, physics, plugins, and robot worlds. Gazebo Classic is not the path to start new work; use current Gazebo Sim.

Sources:
- [Gazebo Sim docs](https://gazebosim.org/libs/sim/)
- [ROS 2 Gazebo setup tutorial](https://docs.ros.org/en/rolling/Tutorials/Advanced/Simulators/Gazebo/Gazebo.html)

Learn after notebooks: 5, 6, 16, 21, 22, 27.

## MuJoCo

Use MuJoCo for fast physics simulation, control research, contact-rich tasks, reinforcement learning, and model-based control experiments.

Source:
- [MuJoCo official site](https://mujoco.org/)

Learn after notebooks: 13, 15, 20, 22, 26.

## Drake

Use Drake for model-based design, dynamics, optimization, verification, manipulation, and underactuated robotics.

Source:
- [Drake official site](https://drake.mit.edu/)

Learn after notebooks: 12, 13, 15, 17, 20.

## Isaac Sim And Isaac Lab

Use Isaac Sim and Isaac Lab when you need GPU-accelerated robotics simulation, robot learning workflows, synthetic data, humanoids, and large-scale reinforcement/imitation learning.

Sources:
- [NVIDIA Isaac platform](https://developer.nvidia.com/isaac/)
- [Isaac Lab tutorial](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-lab/latest/an-introduction-to-robot-learning-and-isaac-lab/index.html)
- [Isaac Lab documentation in Isaac Sim docs](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/isaac_lab_tutorials/index.html)

Learn after notebooks: 8, 22, 23, 24, 25, 26, 30.

## LeRobot

Use LeRobot for modern open-source robot learning: datasets, policies, training, inference, hardware integrations, and community recipes.

Sources:
- [LeRobot docs](https://huggingface.co/docs/lerobot/main/en/index)
- [LeRobot paper](https://arxiv.org/abs/2602.22818)
- [LeRobot v0.5.0 announcement](https://huggingface.co/blog/lerobot-release-v050)

Learn after notebooks: 7, 9, 22, 23, 24, 25, 29.

## Recommended Order

1. Finish notebooks 1-10.
2. Learn ROS 2 basics and transforms.
3. Build a Gazebo mobile robot with Nav2.
4. Learn MoveIt 2 with a simulated arm.
5. Use MuJoCo or Isaac Lab for learning-heavy experiments.
6. Use LeRobot once you understand demonstrations, datasets, and policies.

Do not start with every tool at once. Learn the concepts first, then adopt tools when the concept has a job to do.
