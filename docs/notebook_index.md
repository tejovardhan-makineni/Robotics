# Notebook Index

## Foundations

| # | Notebook | Focus |
|---:|---|---|
| 1 | `01_basics_robot_loop.ipynb` | State, observation, action, feedback |
| 2 | `02_kinematics_frames.ipynb` | Frames, transforms, 2-link arm IK |
| 3 | `03_dynamics_control.ipynb` | PID, dynamics, differential drive |
| 4 | `04_sensing_state_estimation.ipynb` | Sensor noise, Kalman filtering |
| 5 | `05_mapping_slam_intro.ipynb` | Occupancy grids, particles |
| 6 | `06_motion_planning.ipynb` | A*, collision checking, RRT |
| 7 | `07_imitation_learning.ipynb` | Behavior cloning, action chunking |
| 8 | `08_reinforcement_learning.ipynb` | Q-learning and rewards |
| 9 | `09_modern_robot_learning_vla.ipynb` | VLA and diffusion/flow intuition |
| 10 | `10_capstone_robot_stack.ipynb` | Integrated plan-estimate-control-learn stack |

## Mastery Expansion

| # | Notebook | Focus |
|---:|---|---|
| 11 | `11_math_for_robotics.ipynb` | Linear algebra, covariance, least squares |
| 12 | `12_spatial_math_se3.ipynb` | SE(3), quaternions, transform inverse |
| 13 | `13_robot_dynamics_energy.ipynb` | Pendulum dynamics, energy, torque control |
| 14 | `14_trajectory_generation.ipynb` | Cubic, quintic, trapezoidal trajectories |
| 15 | `15_lqr_mpc_control.ipynb` | LQR and small MPC |
| 16 | `16_mobile_robot_models.ipynb` | Unicycle, bicycle, pure pursuit |
| 17 | `17_manipulator_jacobian_control.ipynb` | Resolved-rate IK, singularities |
| 18 | `18_computer_vision_geometry.ipynb` | Pinhole projection, depth, stereo |
| 19 | `19_lidar_point_clouds_icp.ipynb` | Point cloud alignment, ICP |
| 20 | `20_grasping_manipulation.ipynb` | Friction cones, grasp quality, state machines |
| 21 | `21_ros2_architecture.ipynb` | Nodes, topics, services, actions |
| 22 | `22_simulation_domain_randomization.ipynb` | Domain randomization, sim-to-real |
| 23 | `23_robot_dataset_engineering.ipynb` | Episodes, normalization, dataset cards |
| 24 | `24_behavior_cloning_numpy_mlp.ipynb` | NumPy neural policy training |
| 25 | `25_diffusion_policy_intuition.ipynb` | Denoising and multimodal action sampling |
| 26 | `26_continuous_control_rl_cem.ipynb` | Cross-entropy method for continuous control |
| 27 | `27_robot_safety_reliability.ipynb` | Safety filters, watchdogs, hazards |
| 28 | `28_multi_robot_coordination.ipynb` | Formation control and task assignment |
| 29 | `29_research_paper_reading.ipynb` | Reading and reproducing robotics papers |
| 30 | `30_master_capstone_portfolio.ipynb` | Portfolio-level capstone planning |

## Humanoid And Optimus-Style Track

| # | Notebook | Focus |
|---:|---|---|
| 31 | `31_humanoid_systems_overview.ipynb` | Humanoid subsystem decomposition |
| 32 | `32_humanoid_mechatronics_actuators.ipynb` | Actuators, torque, power, compliance |
| 33 | `33_biped_balance_lipm.ipynb` | LIPM, capture point, support polygon |
| 34 | `34_humanoid_locomotion_rl.ipynb` | RL locomotion intuition and gait robustness |
| 35 | `35_whole_body_control.ipynb` | Task prioritization and whole-body objectives |
| 36 | `36_humanoid_hands_tactile.ipynb` | Dexterous hands, tactile feedback, slip |
| 37 | `37_humanoid_perception_stack.ipynb` | Scene graphs, tracking, task-relevant perception |
| 38 | `38_teleoperation_data_factory.ipynb` | Teleoperation, latency, data quality |
| 39 | `39_humanoid_vla_architecture.ipynb` | Language-conditioned skill and action chunk architecture |
| 40 | `40_sim_to_real_humanoids.ipynb` | Sim-to-real robustness and deployment stages |
| 41 | `41_humanoid_edge_compute.ipynb` | Real-time loops, latency budgets, async inference |
| 42 | `42_humanoid_safety_standards.ipynb` | Human-scale safety mindset and risk scoring |
| 43 | `43_humanoid_manufacturing_cost.ipynb` | BOM, reliability, fleet learning |
| 44 | `44_open_source_humanoid_lab.ipynb` | Open-source lab design and platform selection |
| 45 | `45_optimus_style_capstone.ipynb` | Optimus-style staged capstone roadmap |

## Latest Open-Source Robotics Frontier

| # | Notebook | Focus |
|---:|---|---|
| 46 | `46_open_source_robotics_frontier_radar.ipynb` | Current open-source robotics ecosystem radar |
| 47 | `47_open_vla_models_action_heads.ipynb` | Open VLA models and action-head tradeoffs |
| 48 | `48_open_benchmarks_evaluation_harnesses.ipynb` | Open benchmarks, confidence intervals, VLA evaluation |
| 49 | `49_open_simulators_synthetic_data.ipynb` | Open simulators, synthetic data, domain randomization |
| 50 | `50_open_hardware_humanoids_dexterity.ipynb` | Open humanoid hardware and dexterity ladder |

## How To Use The Notebooks

Do not only run them. For every notebook, do three things:

1. Change a parameter and predict the result before running.
2. Add one failure case.
3. Write a short note on what would change on real hardware.

If you cannot explain why something failed, you have found the next thing to learn.
