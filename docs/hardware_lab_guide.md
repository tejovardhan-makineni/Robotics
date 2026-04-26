# Hardware Lab Guide

You can learn a lot from simulation, but hardware teaches latency, friction, backlash, calibration, wiring, power, noise, and failure.

## Beginner Hardware Path

### Stage 1: No hardware

Use the notebooks. Build intuition first.

Required:
- Python
- NumPy
- Jupyter

### Stage 2: Small mobile base

Good for learning:
- Differential drive
- Encoders
- IMU
- Lidar or depth camera
- ROS 2
- Nav2

Skills:
- Wheel calibration
- Odometry
- Mapping
- Localization
- Path following

### Stage 3: Low-cost arm

Good for learning:
- Joint control
- Kinematics
- Teleoperation
- Demonstration collection
- Imitation learning

Skills:
- Calibration
- Workspace limits
- Grasp attempts
- Camera alignment
- Dataset collection

### Stage 4: Mobile manipulation

Good for mastery:
- Whole-system integration
- Navigation plus manipulation
- Long-horizon tasks
- Safety architecture
- Learning from demonstrations

## Parts To Understand

### Actuators

Learn:
- DC motors
- Servos
- Steppers
- Brushless motors
- Gearboxes
- Backlash
- Torque-speed curves

### Sensors

Learn:
- Encoders
- IMUs
- Cameras
- Depth cameras
- Lidars
- Force/torque sensors
- Tactile sensors

### Compute

Learn:
- Microcontrollers for timing-sensitive control
- Single-board computers for ROS 2
- GPUs for perception and learning
- Edge deployment limits

### Power

Learn:
- Battery voltage and current
- Motor current spikes
- Fuses
- Power distribution
- Grounding
- Heat

## What To Buy First

If your goal is mastery, do not buy an expensive humanoid first.

Better sequence:

1. A small wheeled robot or build kit.
2. A depth camera or lidar.
3. A low-cost arm with safe torque and speed.
4. A teleoperation device or leader-follower arm setup.
5. Only then consider expensive platforms.

## Hardware Notebook Pairings

- Mobile base: notebooks 3, 4, 5, 6, 16, 21, 27.
- Arm: notebooks 2, 12, 14, 17, 18, 20, 21, 27.
- Learning from demos: notebooks 7, 23, 24, 25.
- Sim-to-real: notebooks 22, 27, 30.
