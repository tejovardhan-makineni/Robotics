from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"


COMMON_IMPORTS = """
import math
import random
from collections import defaultdict

import numpy as np

try:
    import matplotlib.pyplot as plt
    HAS_PLOT = True
except ModuleNotFoundError:
    plt = None
    HAS_PLOT = False

np.set_printoptions(precision=3, suppress=True)

def plot_unavailable():
    if not HAS_PLOT:
        print("Install matplotlib to see the plot: pip install -r requirements.txt")
"""


def md(text: str):
    return nbf.v4.new_markdown_cell(dedent(text).strip())


def code(text: str):
    return nbf.v4.new_code_cell(dedent(text).strip())


NOTEBOOK_GUIDES = {
    "01_basics_robot_loop.ipynb": (
        "Build the smallest complete robot loop: state, observation, action, dynamics, and feedback.",
        "Every robot, from a toy rover to a humanoid, repeatedly senses, decides, and acts. If this loop is unclear, advanced control and learning will feel like magic.",
        "Simulate a 1D robot moving to a target, inspect the feedback variables, then change gains and limits to see how behavior changes."
    ),
    "02_kinematics_frames.ipynb": (
        "Learn how robots describe where things are using coordinate frames, transforms, forward kinematics, inverse kinematics, and Jacobians.",
        "Robots fail when frames are confused. Cameras, arms, bases, grippers, and maps all need explicit frame relationships.",
        "Start with 2D transforms, compute a 2-link arm endpoint, solve for joint angles, and use the Jacobian to connect joint motion to endpoint motion."
    ),
    "03_dynamics_control.ipynb": (
        "Connect commands to motion using dynamics, PID control, actuator limits, and differential-drive movement.",
        "Real robots have inertia, delay, saturation, and wheel geometry. Controllers must handle those physical limits.",
        "Simulate a controlled mass, compare soft versus aggressive gains, then drive a differential robot through turns and toward a waypoint."
    ),
    "04_sensing_state_estimation.ipynb": (
        "Estimate hidden robot state by fusing noisy odometry-like predictions and noisy position measurements.",
        "A robot almost never knows the truth directly. State estimation is the bridge between imperfect sensors and reliable control.",
        "Generate noisy motion data, run a 1D Kalman filter, and compare raw measurement error against filtered estimate error."
    ),
    "05_mapping_slam_intro.ipynb": (
        "Build intuition for mapping and localization with occupancy grids, log odds, and a particle filter.",
        "Navigation requires knowing both where obstacles are and where the robot is. SLAM grows from these ideas.",
        "Update grid cells from simulated range hits, then use landmark distance measurements to localize a robot with particles."
    ),
    "06_motion_planning.ipynb": (
        "Plan collision-free motion with graph search and sampling-based planning.",
        "A controller can follow commands, but a planner decides which route is safe and feasible before motion begins.",
        "Implement A* on a grid, visualize the path, then grow an RRT through continuous 2D space with obstacle checks."
    ),
    "07_imitation_learning.ipynb": (
        "Train a policy from demonstrations using behavior cloning and action chunks.",
        "Most practical robot learning starts from examples because random real-world exploration is slow and unsafe.",
        "Generate expert trajectories, fit a supervised policy, roll it out closed-loop, and compare single actions with short action chunks."
    ),
    "08_reinforcement_learning.ipynb": (
        "Learn how reward-driven training works using Q-learning in a small navigation world.",
        "Reinforcement learning is powerful, but robotics makes exploration expensive and safety-critical. This notebook shows the core idea in a safe toy setting.",
        "Define states, actions, rewards, and updates, train a Q-table, then evaluate the learned greedy route."
    ),
    "09_modern_robot_learning_vla.ipynb": (
        "Connect fundamentals to modern robot learning: action chunks, diffusion/flow policies, action tokens, and vision-language-action models.",
        "Current frontier systems still depend on classical robotics concepts, but they use large datasets and distributional policies to handle messy real tasks.",
        "Use toy action distributions to see why mean regression fails, sample safe actions, tokenize actions, and inspect a minimal VLA-style episode record."
    ),
    "10_capstone_robot_stack.ipynb": (
        "Integrate planning, control, learning, evaluation, and safety thinking into one small robot stack.",
        "Robotics mastery comes from combining pieces. A good robot is a system, not just a controller or a model.",
        "Plan a grid route, follow it under biased dynamics, learn a residual correction from data, and compare metrics across runs."
    ),
}


def guide_cell(filename: str):
    what, why, how = NOTEBOOK_GUIDES[filename]
    return md(
        f"""
        ## What / Why / How

        **What we are trying to do:** {what}

        **Why this matters:** {why}

        **How we will do it:** {how}
        """
    )


def write_notebook(filename: str, title: str, cells):
    nb = nbf.v4.new_notebook()
    nb["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "name": "python",
            "pygments_lexer": "ipython3",
        },
    }
    nb["cells"] = [md(f"# {title}"), guide_cell(filename)] + cells
    path = NOTEBOOK_DIR / filename
    nbf.write(nb, path)
    print(f"wrote {path.relative_to(ROOT)}")


def notebook_01():
    return [
        md(
            """
            ## Goal

            Build the basic mental model of a robot:

            - A robot has state: where it is, how fast it moves, what it senses.
            - A robot receives observations from sensors.
            - A controller or policy chooses actions.
            - Actuators apply actions to the physical world.
            - Feedback closes the loop.

            In learning-based robotics, a policy is often trained from data. In classical robotics, a controller is usually designed from equations. You will use both.
            """
        ),
        code(COMMON_IMPORTS),
        md(
            """
            ## The Robot Loop

            At each time step:

            1. Sense the world.
            2. Estimate the state.
            3. Decide an action.
            4. Apply the action.
            5. Repeat.

            We will start with the smallest possible robot: a 1D point that moves toward a target.
            """
        ),
        code(
            """
            dt = 0.05
            target = 1.0
            x = -1.0
            velocity_limit = 1.2
            k_p = 1.8

            history = []
            for step in range(120):
                t = step * dt
                observation = x
                error = target - observation
                action_velocity = np.clip(k_p * error, -velocity_limit, velocity_limit)
                x = x + action_velocity * dt
                history.append((t, observation, error, action_velocity))

            history = np.array(history)
            print("final position:", round(float(x), 4))
            print("final error:", round(float(target - x), 4))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(8, 3))
                plt.plot(history[:, 0], history[:, 1], label="position")
                plt.axhline(target, color="black", linestyle="--", label="target")
                plt.xlabel("time [s]")
                plt.ylabel("x")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
                print("first rows: time, x, error, action")
                print(history[:5])
            """
        ),
        md(
            """
            ## State, Observation, Action, Policy

            A useful vocabulary:

            - State: the real variables needed to describe the robot and world.
            - Observation: what sensors report. It may be noisy or incomplete.
            - Action: the command sent to actuators.
            - Policy: a function that maps observations to actions.
            - Dynamics: how the world changes after an action.

            A classical controller may be hand-designed. A learned policy is trained from examples or rewards.
            """
        ),
        code(
            """
            def proportional_policy(observation, target, gain=1.0, limit=1.0):
                error = target - observation
                return np.clip(gain * error, -limit, limit)

            for gain in [0.5, 1.0, 2.0, 5.0]:
                x = -1.0
                for _ in range(80):
                    u = proportional_policy(x, target=1.0, gain=gain, limit=1.0)
                    x += u * dt
                print(f"gain={gain:>3}: final x={x:.3f}, error={1.0 - x:.3f}")
            """
        ),
        md(
            """
            ## Exercises

            1. Change `velocity_limit`. What happens when the robot is too weak?
            2. Change `k_p`. What happens when gain is low or high?
            3. Add sensor noise: `observation = x + np.random.normal(0, 0.02)`.
            4. Explain why feedback is more robust than sending one fixed command.
            """
        ),
    ]


def notebook_02():
    return [
        md(
            """
            ## Goal

            Learn how robots represent geometry:

            - Coordinate frames
            - Rotation matrices
            - Homogeneous transforms
            - Forward and inverse kinematics
            - Jacobians

            This is the language used by arms, mobile robots, cameras, grippers, and simulation engines.
            """
        ),
        code(COMMON_IMPORTS),
        md("## 2D Rotation And Transform Matrices"),
        code(
            """
            def rot2(theta):
                c, s = np.cos(theta), np.sin(theta)
                return np.array([[c, -s], [s, c]])

            def transform2(theta, tx, ty):
                T = np.eye(3)
                T[:2, :2] = rot2(theta)
                T[:2, 2] = [tx, ty]
                return T

            def apply_transform(T, point_xy):
                p = np.array([point_xy[0], point_xy[1], 1.0])
                return (T @ p)[:2]

            T_world_robot = transform2(theta=np.deg2rad(30), tx=1.0, ty=0.5)
            point_robot = np.array([0.4, 0.0])
            point_world = apply_transform(T_world_robot, point_robot)
            print("T_world_robot:")
            print(T_world_robot)
            print("point in world:", point_world)
            """
        ),
        md("## Forward Kinematics: 2-Link Arm"),
        code(
            """
            def fk_2link(q, lengths=(1.0, 0.7)):
                q1, q2 = q
                l1, l2 = lengths
                elbow = np.array([l1 * np.cos(q1), l1 * np.sin(q1)])
                wrist = elbow + np.array([l2 * np.cos(q1 + q2), l2 * np.sin(q1 + q2)])
                return elbow, wrist

            q = np.deg2rad([35, 55])
            elbow, wrist = fk_2link(q)
            print("elbow:", elbow)
            print("end effector:", wrist)
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(4, 4))
                xs = [0, elbow[0], wrist[0]]
                ys = [0, elbow[1], wrist[1]]
                plt.plot(xs, ys, marker="o", linewidth=3)
                plt.axis("equal")
                plt.xlim(-1.8, 1.8)
                plt.ylim(-1.8, 1.8)
                plt.grid(True, alpha=0.3)
                plt.title("2-link arm")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Inverse Kinematics"),
        code(
            """
            def ik_2link(target_xy, lengths=(1.0, 0.7), elbow_up=True):
                x, y = target_xy
                l1, l2 = lengths
                r2 = x * x + y * y
                c2 = (r2 - l1 * l1 - l2 * l2) / (2 * l1 * l2)
                c2 = np.clip(c2, -1.0, 1.0)
                s2 = np.sqrt(max(0.0, 1 - c2 * c2))
                if not elbow_up:
                    s2 = -s2
                q2 = np.arctan2(s2, c2)
                q1 = np.arctan2(y, x) - np.arctan2(l2 * s2, l1 + l2 * c2)
                return np.array([q1, q2])

            target_xy = np.array([1.0, 0.8])
            q_sol = ik_2link(target_xy, elbow_up=True)
            _, reached = fk_2link(q_sol)
            print("q degrees:", np.rad2deg(q_sol))
            print("target:", target_xy, "reached:", reached, "error:", np.linalg.norm(target_xy - reached))
            """
        ),
        md("## Jacobian: Joint Velocity To End-Effector Velocity"),
        code(
            """
            def jacobian_2link(q, lengths=(1.0, 0.7)):
                q1, q2 = q
                l1, l2 = lengths
                return np.array([
                    [-l1*np.sin(q1) - l2*np.sin(q1+q2), -l2*np.sin(q1+q2)],
                    [ l1*np.cos(q1) + l2*np.cos(q1+q2),  l2*np.cos(q1+q2)],
                ])

            J = jacobian_2link(q_sol)
            qdot = np.array([0.2, -0.1])
            ee_velocity = J @ qdot
            print("Jacobian:")
            print(J)
            print("end-effector velocity:", ee_velocity)
            """
        ),
        md(
            """
            ## Exercises

            1. Try targets outside the arm reach. What does clipping do?
            2. Compare elbow-up and elbow-down inverse kinematics.
            3. Use the Jacobian pseudo-inverse to move the endpoint toward a target.
            """
        ),
    ]


def notebook_03():
    return [
        md(
            """
            ## Goal

            Learn how actions change motion:

            - Dynamics: forces and torques cause acceleration.
            - Control: feedback chooses actions based on error.
            - Saturation: real motors have limits.
            - Differential drive: many mobile robots move by left and right wheel speeds.
            """
        ),
        code(COMMON_IMPORTS),
        md("## PID Control On A Simple Mass"),
        code(
            """
            def simulate_mass_pid(kp=8.0, kd=3.0, ki=0.0, force_limit=8.0, dt=0.02, steps=250):
                x, v = -1.0, 0.0
                target = 1.0
                integral = 0.0
                rows = []
                for step in range(steps):
                    error = target - x
                    integral += error * dt
                    force = kp * error - kd * v + ki * integral
                    force = np.clip(force, -force_limit, force_limit)
                    acceleration = force  # mass = 1 kg
                    v += acceleration * dt
                    x += v * dt
                    rows.append((step * dt, x, v, error, force))
                return np.array(rows)

            runs = {
                "soft": simulate_mass_pid(kp=3, kd=1.5),
                "balanced": simulate_mass_pid(kp=8, kd=3),
                "aggressive": simulate_mass_pid(kp=18, kd=1),
            }
            for name, rows in runs.items():
                print(name, "final x", round(float(rows[-1, 1]), 3), "max force", round(float(np.max(np.abs(rows[:, 4]))), 3))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(8, 3))
                for name, rows in runs.items():
                    plt.plot(rows[:, 0], rows[:, 1], label=name)
                plt.axhline(1.0, color="black", linestyle="--")
                plt.xlabel("time [s]")
                plt.ylabel("position")
                plt.grid(True, alpha=0.3)
                plt.legend()
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Differential Drive Robot"),
        code(
            """
            def diff_drive_step(pose, left_speed, right_speed, wheel_base=0.4, dt=0.05):
                x, y, theta = pose
                v = 0.5 * (left_speed + right_speed)
                omega = (right_speed - left_speed) / wheel_base
                x += v * np.cos(theta) * dt
                y += v * np.sin(theta) * dt
                theta += omega * dt
                theta = np.arctan2(np.sin(theta), np.cos(theta))
                return np.array([x, y, theta])

            pose = np.array([0.0, 0.0, 0.0])
            path = []
            for _ in range(120):
                pose = diff_drive_step(pose, left_speed=0.7, right_speed=1.0)
                path.append(pose.copy())
            path = np.array(path)
            print("final pose [x, y, heading]:", path[-1])
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(4, 4))
                plt.plot(path[:, 0], path[:, 1])
                plt.axis("equal")
                plt.grid(True, alpha=0.3)
                plt.title("Differential-drive arc")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Waypoint Controller"),
        code(
            """
            def drive_to_waypoint(start_pose, goal, steps=300):
                pose = np.array(start_pose, dtype=float)
                rows = []
                for step in range(steps):
                    dx, dy = goal[0] - pose[0], goal[1] - pose[1]
                    distance = np.hypot(dx, dy)
                    desired_heading = np.arctan2(dy, dx)
                    heading_error = np.arctan2(np.sin(desired_heading - pose[2]), np.cos(desired_heading - pose[2]))
                    v = np.clip(1.0 * distance, 0.0, 0.8)
                    omega = np.clip(3.0 * heading_error, -2.0, 2.0)
                    left = v - 0.2 * omega
                    right = v + 0.2 * omega
                    pose = diff_drive_step(pose, left, right)
                    rows.append(pose.copy())
                    if distance < 0.03:
                        break
                return np.array(rows)

            wp_path = drive_to_waypoint([0, 0, 0], goal=np.array([2.0, 1.2]))
            print("steps:", len(wp_path), "final:", wp_path[-1])
            """
        ),
        md(
            """
            ## Exercises

            1. Make the PID aggressive enough to overshoot.
            2. Add actuator saturation and compare trajectories.
            3. Change the wheel base. How does turning change?
            4. Add a second waypoint and drive a small route.
            """
        ),
    ]


def notebook_04():
    return [
        md(
            """
            ## Goal

            Robots rarely know their true state. They estimate it from noisy sensors.

            You will implement a 1D Kalman filter that fuses:

            - Odometry-like velocity commands
            - Noisy position measurements
            - A simple motion model
            """
        ),
        code(COMMON_IMPORTS),
        md("## Simulate Noisy Motion"),
        code(
            """
            rng = np.random.default_rng(7)
            dt = 0.1
            steps = 80
            true_x = 0.0
            true_v = 0.7
            process_sigma = 0.03
            measurement_sigma = 0.25

            true_positions = []
            odom_velocities = []
            measurements = []
            for _ in range(steps):
                true_v = 0.7 + rng.normal(0, 0.02)
                true_x += true_v * dt + rng.normal(0, process_sigma)
                odom_v = true_v + rng.normal(0, 0.08)
                z = true_x + rng.normal(0, measurement_sigma)
                true_positions.append(true_x)
                odom_velocities.append(odom_v)
                measurements.append(z)

            true_positions = np.array(true_positions)
            odom_velocities = np.array(odom_velocities)
            measurements = np.array(measurements)
            print("first measurements:", measurements[:5])
            """
        ),
        md("## Kalman Filter"),
        code(
            """
            x_hat = 0.0
            P = 1.0
            Q = process_sigma ** 2
            R = measurement_sigma ** 2
            estimates = []
            uncertainties = []

            for u, z in zip(odom_velocities, measurements):
                # Predict
                x_hat = x_hat + u * dt
                P = P + Q

                # Update
                K = P / (P + R)
                x_hat = x_hat + K * (z - x_hat)
                P = (1 - K) * P

                estimates.append(x_hat)
                uncertainties.append(P)

            estimates = np.array(estimates)
            rmse_measurement = np.sqrt(np.mean((measurements - true_positions) ** 2))
            rmse_filter = np.sqrt(np.mean((estimates - true_positions) ** 2))
            print("measurement RMSE:", round(float(rmse_measurement), 3))
            print("filter RMSE:", round(float(rmse_filter), 3))
            """
        ),
        code(
            """
            if HAS_PLOT:
                t = np.arange(steps) * dt
                plt.figure(figsize=(9, 3))
                plt.plot(t, true_positions, label="true")
                plt.scatter(t, measurements, s=15, alpha=0.5, label="measurements")
                plt.plot(t, estimates, label="Kalman estimate")
                plt.xlabel("time [s]")
                plt.ylabel("x")
                plt.grid(True, alpha=0.3)
                plt.legend()
                plt.show()
            else:
                plot_unavailable()
                print("last estimate:", estimates[-1], "true:", true_positions[-1])
            """
        ),
        md(
            """
            ## What To Notice

            The filter is not magic. It is a disciplined compromise between prediction and measurement:

            - If measurements are noisy, trust the model more.
            - If the model is uncertain, trust measurements more.
            - Real robots use higher-dimensional versions: EKF, UKF, factor graphs, visual-inertial odometry, and SLAM backends.
            """
        ),
        md(
            """
            ## Exercises

            1. Increase `measurement_sigma`. Does the Kalman gain become more cautious?
            2. Increase `process_sigma`. Does the filter trust measurements more?
            3. Extend the state to include velocity.
            """
        ),
    ]


def notebook_05():
    return [
        md(
            """
            ## Goal

            Mapping and SLAM connect robot motion with world structure.

            This notebook introduces:

            - Occupancy grids
            - Log-odds updates
            - Particle-filter localization

            Full SLAM is more complex, but these pieces are the foundation.
            """
        ),
        code(COMMON_IMPORTS),
        md("## Occupancy Grid With Log Odds"),
        code(
            """
            grid_size = 40
            resolution = 0.1
            log_odds = np.zeros((grid_size, grid_size))
            robot_cell = np.array([20, 20])

            # Simulated obstacle points in grid cells.
            obstacles = np.array([
                [28, 24], [30, 25], [31, 26], [12, 28], [10, 29], [25, 10]
            ])

            def update_ray(log_odds, robot_cell, hit_cell, free_delta=-0.4, occ_delta=0.9):
                steps = int(np.linalg.norm(hit_cell - robot_cell)) + 1
                for alpha in np.linspace(0.0, 1.0, steps):
                    cell = np.round(robot_cell + alpha * (hit_cell - robot_cell)).astype(int)
                    r, c = cell
                    if 0 <= r < log_odds.shape[0] and 0 <= c < log_odds.shape[1]:
                        log_odds[r, c] += free_delta
                r, c = hit_cell
                if 0 <= r < log_odds.shape[0] and 0 <= c < log_odds.shape[1]:
                    log_odds[r, c] += occ_delta

            for hit in obstacles:
                update_ray(log_odds, robot_cell, hit)

            occupancy_prob = 1 - 1 / (1 + np.exp(log_odds))
            print("occupied-ish cells:", np.argwhere(occupancy_prob > 0.6)[:10])
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 5))
                plt.imshow(occupancy_prob, origin="lower", cmap="gray_r", vmin=0, vmax=1)
                plt.scatter(robot_cell[1], robot_cell[0], c="tab:blue", label="robot")
                plt.colorbar(label="P(occupied)")
                plt.legend()
                plt.title("Occupancy grid")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Particle Filter Localization In A 1D Hallway"),
        code(
            """
            rng = np.random.default_rng(42)
            landmarks = np.array([1.5, 5.5, 8.5])
            true_x = 3.2
            sigma = 0.18
            measurements = np.abs(landmarks - true_x) + rng.normal(0, sigma, size=len(landmarks))

            num_particles = 2000
            particles = rng.uniform(0, 10, size=num_particles)
            weights = np.ones(num_particles) / num_particles

            for iteration in range(6):
                expected = np.abs(particles[:, None] - landmarks[None, :])
                residual = expected - measurements[None, :]
                weights = np.exp(-0.5 * np.sum((residual / sigma) ** 2, axis=1))
                weights += 1e-12
                weights /= weights.sum()
                particles = rng.choice(particles, size=num_particles, p=weights)
                particles += rng.normal(0, 0.04, size=num_particles)
                particles = np.clip(particles, 0, 10)

            estimate = particles.mean()
            print("true x:", true_x)
            print("estimated x:", round(float(estimate), 3))
            print("particle std:", round(float(particles.std()), 3))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(8, 2.5))
                plt.hist(particles, bins=50, density=True, alpha=0.7)
                for lm in landmarks:
                    plt.axvline(lm, color="black", linestyle=":", alpha=0.4)
                plt.axvline(true_x, color="tab:green", label="true")
                plt.axvline(estimate, color="tab:red", label="estimate")
                plt.xlabel("x position")
                plt.yticks([])
                plt.legend()
                plt.title("Particle belief")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md(
            """
            ## Exercises

            1. Add more obstacle hits to the occupancy grid.
            2. Increase sensor noise in the particle filter.
            3. Move the true position close to a symmetric landmark layout and observe ambiguity.
            """
        ),
    ]


def notebook_06():
    return [
        md(
            """
            ## Goal

            Motion planning answers: how can a robot move from start to goal without collisions?

            You will implement:

            - A* on a grid
            - Collision checking
            - A small RRT planner in continuous 2D
            """
        ),
        code(COMMON_IMPORTS),
        md("## A* Grid Planner"),
        code(
            """
            import heapq

            H, W = 20, 24
            grid = np.zeros((H, W), dtype=int)
            grid[5:16, 10] = 1
            grid[4, 4:14] = 1
            grid[13, 10:21] = 1
            start = (2, 2)
            goal = (17, 21)

            def heuristic(a, b):
                return abs(a[0] - b[0]) + abs(a[1] - b[1])

            def neighbors(cell):
                r, c = cell
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W and grid[nr, nc] == 0:
                        yield (nr, nc)

            def astar(start, goal):
                frontier = [(0, start)]
                came_from = {start: None}
                cost_so_far = {start: 0}
                while frontier:
                    _, current = heapq.heappop(frontier)
                    if current == goal:
                        break
                    for nxt in neighbors(current):
                        new_cost = cost_so_far[current] + 1
                        if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                            cost_so_far[nxt] = new_cost
                            priority = new_cost + heuristic(nxt, goal)
                            heapq.heappush(frontier, (priority, nxt))
                            came_from[nxt] = current
                if goal not in came_from:
                    return []
                path = []
                cur = goal
                while cur is not None:
                    path.append(cur)
                    cur = came_from[cur]
                return path[::-1]

            path = astar(start, goal)
            print("path length:", len(path))
            print("first five cells:", path[:5])
            """
        ),
        code(
            """
            if HAS_PLOT:
                img = grid.astype(float)
                for r, c in path:
                    img[r, c] = 0.5
                plt.figure(figsize=(7, 4))
                plt.imshow(img, origin="lower", cmap="gray_r")
                plt.scatter([start[1], goal[1]], [start[0], goal[0]], c=["tab:green", "tab:red"], s=80)
                plt.title("A* path")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## RRT In Continuous Space"),
        code(
            """
            rng = np.random.default_rng(4)
            rects = [(3, 3, 2, 5), (6, 0, 1.5, 5), (7, 6, 2, 2)]

            def in_collision(point):
                x, y = point
                if x < 0 or x > 10 or y < 0 or y > 10:
                    return True
                for rx, ry, rw, rh in rects:
                    if rx <= x <= rx + rw and ry <= y <= ry + rh:
                        return True
                return False

            def segment_free(a, b, checks=20):
                for alpha in np.linspace(0, 1, checks):
                    p = (1 - alpha) * a + alpha * b
                    if in_collision(p):
                        return False
                return True

            def rrt(start, goal, step_size=0.45, iterations=2500):
                nodes = [np.array(start, dtype=float)]
                parents = [-1]
                for _ in range(iterations):
                    sample = np.array(goal) if rng.random() < 0.1 else rng.uniform(0, 10, size=2)
                    dists = [np.linalg.norm(n - sample) for n in nodes]
                    nearest_idx = int(np.argmin(dists))
                    direction = sample - nodes[nearest_idx]
                    norm = np.linalg.norm(direction)
                    if norm < 1e-9:
                        continue
                    new = nodes[nearest_idx] + step_size * direction / norm
                    if segment_free(nodes[nearest_idx], new):
                        nodes.append(new)
                        parents.append(nearest_idx)
                        if np.linalg.norm(new - goal) < 0.6 and segment_free(new, np.array(goal)):
                            nodes.append(np.array(goal, dtype=float))
                            parents.append(len(nodes) - 2)
                            break
                idx = len(nodes) - 1
                if np.linalg.norm(nodes[idx] - goal) > 1e-6:
                    return nodes, parents, []
                route = []
                while idx != -1:
                    route.append(nodes[idx])
                    idx = parents[idx]
                return nodes, parents, route[::-1]

            nodes, parents, route = rrt([0.8, 0.8], [9.2, 9.0])
            print("nodes:", len(nodes), "route points:", len(route))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 5))
                for rx, ry, rw, rh in rects:
                    plt.gca().add_patch(plt.Rectangle((rx, ry), rw, rh, color="black", alpha=0.25))
                for i, parent in enumerate(parents):
                    if parent >= 0:
                        a, b = nodes[i], nodes[parent]
                        plt.plot([a[0], b[0]], [a[1], b[1]], color="gray", alpha=0.15)
                if route:
                    route_arr = np.array(route)
                    plt.plot(route_arr[:, 0], route_arr[:, 1], color="tab:red", linewidth=3)
                plt.xlim(0, 10)
                plt.ylim(0, 10)
                plt.grid(True, alpha=0.2)
                plt.title("RRT")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md(
            """
            ## Exercises

            1. Change the A* heuristic and observe path length.
            2. Add diagonal neighbors and compare.
            3. Add a narrow passage to the RRT world.
            4. Add path smoothing after RRT.
            """
        ),
    ]


def notebook_07():
    return [
        md(
            """
            ## Goal

            Learn the most practical first training method in robotics: imitation learning.

            You will:

            - Generate expert demonstrations.
            - Train a behavior cloning policy.
            - See why closed-loop evaluation matters.
            - Build a tiny action-chunking policy.

            This connects to ACT, ALOHA, Mobile ALOHA, Diffusion Policy, OpenVLA, SmolVLA, and pi0-style robot policies.
            """
        ),
        code(COMMON_IMPORTS),
        md("## Generate Demonstrations"),
        code(
            """
            rng = np.random.default_rng(0)
            target = np.array([1.0, 1.0])

            def expert_action(pos):
                return np.clip(0.7 * (target - pos), -0.35, 0.35)

            demos = []
            for _ in range(60):
                pos = rng.uniform(-1.2, 1.2, size=2)
                states, actions = [], []
                for _ in range(35):
                    action = expert_action(pos)
                    states.append(pos.copy())
                    actions.append(action.copy())
                    pos = pos + action + rng.normal(0, 0.01, size=2)
                demos.append({"states": np.array(states), "actions": np.array(actions)})

            print("num demonstrations:", len(demos))
            print("one state/action:", demos[0]["states"][0], demos[0]["actions"][0])
            """
        ),
        md("## Behavior Cloning With Linear Regression"),
        code(
            """
            def features(pos):
                x, y = pos
                return np.array([x, y, target[0], target[1], 1.0])

            X = []
            Y = []
            for demo in demos:
                for s, a in zip(demo["states"], demo["actions"]):
                    X.append(features(s))
                    Y.append(a)
            X = np.array(X)
            Y = np.array(Y)

            W, *_ = np.linalg.lstsq(X, Y, rcond=None)

            def cloned_policy(pos):
                return np.clip(features(pos) @ W, -0.35, 0.35)

            print("weights shape:", W.shape)
            for test in [np.array([-1, -1]), np.array([0.2, 1.4]), np.array([1.2, -0.8])]:
                print("pos", test, "expert", expert_action(test), "clone", cloned_policy(test))
            """
        ),
        md("## Closed-Loop Evaluation"),
        code(
            """
            def rollout(policy, start, steps=35):
                pos = np.array(start, dtype=float)
                route = [pos.copy()]
                for _ in range(steps):
                    action = policy(pos)
                    pos = pos + action
                    route.append(pos.copy())
                return np.array(route)

            starts = [np.array([-1.0, -0.8]), np.array([1.4, -1.0]), np.array([-1.2, 1.3])]
            for start in starts:
                route = rollout(cloned_policy, start)
                print("start", start, "final error", round(float(np.linalg.norm(route[-1] - target)), 3))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 5))
                for start in starts:
                    route = rollout(cloned_policy, start)
                    plt.plot(route[:, 0], route[:, 1], marker="o", markersize=2)
                plt.scatter([target[0]], [target[1]], c="tab:red", s=80, label="target")
                plt.axis("equal")
                plt.grid(True, alpha=0.3)
                plt.legend()
                plt.title("Behavior cloning rollouts")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Action Chunking"),
        code(
            """
            horizon = 4
            Xc, Yc = [], []
            for demo in demos:
                states = demo["states"]
                actions = demo["actions"]
                for i in range(len(states) - horizon):
                    Xc.append(features(states[i]))
                    Yc.append(actions[i:i+horizon].reshape(-1))
            Xc = np.array(Xc)
            Yc = np.array(Yc)
            W_chunk, *_ = np.linalg.lstsq(Xc, Yc, rcond=None)

            def chunk_policy(pos):
                chunk = (features(pos) @ W_chunk).reshape(horizon, 2)
                return np.clip(chunk[0], -0.35, 0.35)

            route = rollout(chunk_policy, [-1.1, -0.9])
            print("chunk policy final error:", round(float(np.linalg.norm(route[-1] - target)), 3))
            print("first predicted action chunk:")
            print((features(np.array([-1.1, -0.9])) @ W_chunk).reshape(horizon, 2))
            """
        ),
        md(
            """
            ## What To Notice

            Behavior cloning can work very well when demonstrations cover the states the robot will visit. It fails when the robot drifts into states not present in the data.

            Modern systems reduce this problem using:

            - More diverse demos.
            - Better sensors and proprioception.
            - Action chunks.
            - Diffusion or flow policies that model multiple valid futures.
            - Human correction loops such as DAgger-style data collection.
            """
        ),
        md(
            """
            ## Exercises

            1. Reduce the number of demos to 5. What fails?
            2. Add noisy actions to the demonstrations.
            3. Change `target` and retrain.
            4. Make a validation set and report mean final error.
            """
        ),
    ]


def notebook_08():
    return [
        md(
            """
            ## Goal

            Reinforcement learning trains from reward, not demonstrations.

            RL can discover strategies, but robotics RL is expensive because robots are slow, fragile, and safety constrained. This is why RL is usually done in simulation first.

            You will implement Q-learning in a small gridworld.
            """
        ),
        code(COMMON_IMPORTS),
        md("## Gridworld Environment"),
        code(
            """
            H, W = 7, 9
            start = (0, 0)
            goal = (6, 8)
            obstacles = {(2, 2), (2, 3), (2, 4), (4, 5), (5, 5), (1, 7)}
            actions = [(1,0), (-1,0), (0,1), (0,-1)]

            def step_env(state, action_idx):
                r, c = state
                dr, dc = actions[action_idx]
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= H or nc < 0 or nc >= W or (nr, nc) in obstacles:
                    nr, nc = r, c
                    reward = -1.0
                else:
                    reward = -0.05
                done = (nr, nc) == goal
                if done:
                    reward = 5.0
                return (nr, nc), reward, done

            print("states:", H * W, "actions:", len(actions))
            """
        ),
        md("## Q-Learning"),
        code(
            """
            rng = np.random.default_rng(9)
            Q = np.zeros((H, W, len(actions)))
            alpha = 0.3
            gamma = 0.95
            epsilon = 0.25
            episode_returns = []

            for episode in range(600):
                state = start
                total = 0.0
                for _ in range(100):
                    if rng.random() < epsilon:
                        action_idx = rng.integers(len(actions))
                    else:
                        action_idx = int(np.argmax(Q[state[0], state[1]]))
                    next_state, reward, done = step_env(state, action_idx)
                    total += reward
                    best_next = np.max(Q[next_state[0], next_state[1]])
                    td_target = reward + gamma * best_next * (not done)
                    td_error = td_target - Q[state[0], state[1], action_idx]
                    Q[state[0], state[1], action_idx] += alpha * td_error
                    state = next_state
                    if done:
                        break
                episode_returns.append(total)
                epsilon = max(0.03, epsilon * 0.995)

            print("last 20 episode return mean:", round(float(np.mean(episode_returns[-20:])), 3))
            """
        ),
        md("## Evaluate Learned Policy"),
        code(
            """
            def greedy_route(max_steps=50):
                state = start
                route = [state]
                total = 0.0
                for _ in range(max_steps):
                    a = int(np.argmax(Q[state[0], state[1]]))
                    state, reward, done = step_env(state, a)
                    route.append(state)
                    total += reward
                    if done:
                        break
                return route, total

            route, total = greedy_route()
            print("route length:", len(route), "return:", round(total, 3), "success:", route[-1] == goal)
            print(route)
            """
        ),
        code(
            """
            if HAS_PLOT:
                canvas = np.zeros((H, W))
                for r, c in obstacles:
                    canvas[r, c] = -1
                for r, c in route:
                    canvas[r, c] = 0.5
                canvas[goal] = 1
                plt.figure(figsize=(6, 4))
                plt.imshow(canvas, origin="upper", cmap="viridis")
                plt.title("Q-learning route")
                plt.xticks(range(W))
                plt.yticks(range(H))
                plt.grid(color="white", alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md(
            """
            ## Robotics Reality Check

            RL is powerful, but physical robots make it hard:

            - Real-world exploration can break hardware.
            - Rewards are hard to design.
            - Training needs many trials.
            - Simulators do not perfectly match reality.

            This is why many practical systems use imitation first, then RL for refinement in simulation, then careful real-world adaptation.
            """
        ),
        md(
            """
            ## Exercises

            1. Make the reward sparse: only reward the goal.
            2. Add random action slip.
            3. Compare Q-learning with the A* planner from notebook 6.
            4. Describe what would make this unsafe on a real robot.
            """
        ),
    ]


def notebook_09():
    return [
        md(
            """
            ## Goal

            Connect the fundamentals to current robot-learning research.

            You will learn the ideas behind:

            - Action chunks
            - Diffusion and flow policies
            - Action tokenization
            - Vision-language-action models
            - Embodied reasoning systems

            This notebook is conceptual and lightweight. Training a real VLA requires GPUs, robot datasets, careful evaluation, and safety infrastructure.
            """
        ),
        code(COMMON_IMPORTS),
        md(
            """
            ## Research Snapshot

            Important systems and papers:

            - Open X-Embodiment and RT-X: pooled robot data across embodiments.
            - Diffusion Policy: action-sequence generation by denoising.
            - Octo: open generalist robot policy.
            - OpenVLA: open-source VLA trained on Open X-Embodiment episodes.
            - pi0: VLA flow model for general robot control.
            - SmolVLA and LeRobot: accessible open robot-learning stack.
            - GR00T and Gemini Robotics: industry-scale foundation models, embodied reasoning, and humanoid control.

            Read the project research brief after this notebook:
            `research/latest_research_brief.md`
            """
        ),
        md("## Why Mean Regression Can Fail"),
        code(
            """
            rng = np.random.default_rng(123)

            # A robot can go around an obstacle above or below.
            # Both actions are valid. Averaging them points into the obstacle.
            upper_actions = np.column_stack([
                np.ones(100) * 0.8,
                rng.normal(0.55, 0.05, size=100),
            ])
            lower_actions = np.column_stack([
                np.ones(100) * 0.8,
                rng.normal(-0.55, 0.05, size=100),
            ])
            demo_actions = np.vstack([upper_actions, lower_actions])

            mean_action = demo_actions.mean(axis=0)
            sampled_actions = demo_actions[rng.choice(len(demo_actions), size=8, replace=False)]

            def hits_obstacle(action):
                # Toy obstacle centered at y=0. The averaged action goes through it.
                return abs(action[1]) < 0.2 and action[0] > 0.4

            print("mean action:", mean_action, "hits obstacle?", hits_obstacle(mean_action))
            print("sampled actions hit obstacle?", [hits_obstacle(a) for a in sampled_actions[:5]])
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 4))
                plt.scatter(demo_actions[:, 0], demo_actions[:, 1], s=10, alpha=0.4, label="demo actions")
                plt.scatter([mean_action[0]], [mean_action[1]], c="tab:red", s=100, label="MSE mean")
                circle = plt.Circle((0.8, 0.0), 0.2, color="black", alpha=0.2, label="obstacle zone")
                plt.gca().add_patch(circle)
                plt.xlabel("forward")
                plt.ylabel("sideways")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.title("Multimodal actions")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md(
            """
            ## Diffusion And Flow Intuition

            Diffusion and flow policies try to model a distribution over action sequences, not just one average action.

            In real manipulation, this matters because there may be many valid grasps, paths, and recovery motions.
            """
        ),
        code(
            """
            def toy_action_sampler(num_samples=10, noise=0.03):
                choices = demo_actions[rng.choice(len(demo_actions), size=num_samples)]
                return choices + rng.normal(0, noise, size=choices.shape)

            samples = toy_action_sampler(6)
            print("sampled candidate actions:")
            print(samples)
            print("choose one with a safety filter:")
            safe = [a for a in samples if not hits_obstacle(a)]
            print(safe[0] if safe else "no safe sample")
            """
        ),
        md("## Action Tokenization"),
        code(
            """
            def tokenize_actions(actions, low=-1.0, high=1.0, bins=256):
                actions = np.clip(actions, low, high)
                scaled = (actions - low) / (high - low)
                tokens = np.round(scaled * (bins - 1)).astype(int)
                return tokens

            def detokenize_actions(tokens, low=-1.0, high=1.0, bins=256):
                scaled = tokens / (bins - 1)
                return low + scaled * (high - low)

            action_chunk = np.array([[0.2, -0.1, 0.0], [0.3, -0.1, 1.0], [0.25, 0.0, 1.0]])
            tokens = tokenize_actions(action_chunk)
            reconstructed = detokenize_actions(tokens)
            print("action chunk:")
            print(action_chunk)
            print("tokens:")
            print(tokens)
            print("reconstructed:")
            print(reconstructed)
            """
        ),
        md("## A Minimal VLA Data Record"),
        code(
            """
            robot_episode = {
                "instruction": "pick up the red block and place it in the bowl",
                "image_embedding_shape": (16, 16, 768),
                "proprioception": {
                    "joint_positions": np.zeros(7),
                    "gripper_width": 0.04,
                },
                "action_chunk": action_chunk,
            }

            for key, value in robot_episode.items():
                print(key, "=>", value)
            """
        ),
        md(
            """
            ## Exercises

            1. Add a third action mode to the multimodal example.
            2. Change token bins from 256 to 16. How much precision is lost?
            3. Write down what data you would need to train a robot to open a drawer.
            4. Read one source from each section of `research/latest_research_brief.md`.
            """
        ),
    ]


def notebook_10():
    return [
        md(
            """
            ## Goal

            Build a small integrated robot stack:

            - Plan a route with A*.
            - Follow waypoints with feedback control.
            - Add noisy motion.
            - Learn a residual correction from demonstrations.
            - Evaluate success and failure.

            This is the shape of real robotics work: not one clever model, but a system with planning, control, estimation, learning, and safety checks.
            """
        ),
        code(COMMON_IMPORTS),
        md("## Planning Layer"),
        code(
            """
            import heapq

            H, W = 22, 22
            grid = np.zeros((H, W), dtype=int)
            grid[6:17, 8] = 1
            grid[4, 8:18] = 1
            grid[14, 3:14] = 1
            grid[10:20, 17] = 1
            start = (2, 2)
            goal = (19, 20)

            def astar_grid(grid, start, goal):
                H, W = grid.shape
                def h(a, b):
                    return abs(a[0]-b[0]) + abs(a[1]-b[1])
                def nbrs(s):
                    r, c = s
                    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr, nc] == 0:
                            yield (nr, nc)
                frontier = [(0, start)]
                came = {start: None}
                cost = {start: 0}
                while frontier:
                    _, cur = heapq.heappop(frontier)
                    if cur == goal:
                        break
                    for nxt in nbrs(cur):
                        new = cost[cur] + 1
                        if nxt not in cost or new < cost[nxt]:
                            cost[nxt] = new
                            heapq.heappush(frontier, (new + h(nxt, goal), nxt))
                            came[nxt] = cur
                path = []
                cur = goal
                while cur in came and cur is not None:
                    path.append(cur)
                    cur = came[cur]
                return path[::-1]

            path = astar_grid(grid, start, goal)
            waypoints = np.array(path, dtype=float)
            print("planned cells:", len(path))
            """
        ),
        md("## Controller And Learned Residual"),
        code(
            """
            rng = np.random.default_rng(11)
            hidden_bias = np.array([0.06, -0.04])  # unmodeled drift in row/col coordinates

            def limit_norm(vec, max_norm=0.45):
                n = np.linalg.norm(vec)
                if n > max_norm:
                    return vec * (max_norm / n)
                return vec

            def residual_features(error):
                return np.array([error[0], error[1], 1.0])

            # Demonstrations tell us the correction needed to cancel the hidden bias.
            X_demo = []
            Y_demo = []
            for _ in range(200):
                error = rng.normal(0, 2.0, size=2)
                X_demo.append(residual_features(error))
                Y_demo.append(-hidden_bias + rng.normal(0, 0.01, size=2))
            X_demo = np.array(X_demo)
            Y_demo = np.array(Y_demo)
            W_residual, *_ = np.linalg.lstsq(X_demo, Y_demo, rcond=None)

            def learned_residual(error):
                return residual_features(error) @ W_residual

            print("learned residual for zero error:", learned_residual(np.array([0.0, 0.0])))
            print("true correction:", -hidden_bias)
            """
        ),
        md("## Closed-Loop Simulation"),
        code(
            """
            def is_collision(pos):
                cell = tuple(np.round(pos).astype(int))
                r, c = cell
                if r < 0 or r >= H or c < 0 or c >= W:
                    return True
                return grid[r, c] == 1

            def follow_path(use_residual=False, seed=0, max_steps=450):
                local_rng = np.random.default_rng(seed)
                pos = np.array(start, dtype=float)
                traj = [pos.copy()]
                waypoint_idx = 0
                collided = False

                for _ in range(max_steps):
                    target = waypoints[min(waypoint_idx, len(waypoints)-1)]
                    error = target - pos
                    if np.linalg.norm(error) < 0.35 and waypoint_idx < len(waypoints) - 1:
                        waypoint_idx += 1
                        target = waypoints[waypoint_idx]
                        error = target - pos
                    u = limit_norm(0.8 * error)
                    if use_residual:
                        u = u + learned_residual(error)
                    noise = local_rng.normal(0, 0.015, size=2)
                    pos = pos + u + hidden_bias + noise
                    traj.append(pos.copy())
                    if is_collision(pos):
                        collided = True
                        break
                    if np.linalg.norm(pos - np.array(goal, dtype=float)) < 0.6:
                        break
                return np.array(traj), collided

            nominal_traj, nominal_collision = follow_path(use_residual=False, seed=1)
            learned_traj, learned_collision = follow_path(use_residual=True, seed=1)

            def report(name, traj, collided):
                final_error = np.linalg.norm(traj[-1] - np.array(goal, dtype=float))
                print(name, "steps", len(traj), "final_error", round(float(final_error), 3), "collided", collided)

            report("nominal", nominal_traj, nominal_collision)
            report("learned residual", learned_traj, learned_collision)
            """
        ),
        code(
            """
            if HAS_PLOT:
                canvas = grid.astype(float)
                for r, c in path:
                    canvas[r, c] = 0.35
                plt.figure(figsize=(6, 6))
                plt.imshow(canvas, origin="lower", cmap="gray_r")
                plt.plot(nominal_traj[:, 1], nominal_traj[:, 0], label="nominal", color="tab:orange")
                plt.plot(learned_traj[:, 1], learned_traj[:, 0], label="learned residual", color="tab:blue")
                plt.scatter([start[1], goal[1]], [start[0], goal[0]], c=["tab:green", "tab:red"], s=80)
                plt.legend()
                plt.title("Capstone robot stack")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Evaluation Over Multiple Seeds"),
        code(
            """
            def evaluate(use_residual, n=40):
                successes = 0
                collisions = 0
                errors = []
                for seed in range(n):
                    traj, collided = follow_path(use_residual=use_residual, seed=seed)
                    err = np.linalg.norm(traj[-1] - np.array(goal, dtype=float))
                    successes += (err < 0.8 and not collided)
                    collisions += collided
                    errors.append(err)
                return {
                    "success_rate": successes / n,
                    "collision_rate": collisions / n,
                    "mean_final_error": float(np.mean(errors)),
                }

            print("nominal:", evaluate(False))
            print("learned residual:", evaluate(True))
            """
        ),
        md(
            """
            ## Capstone Extensions

            Choose one:

            1. Add a Kalman filter from notebook 4 so the controller uses an estimate instead of true position.
            2. Replace A* with RRT from notebook 6.
            3. Train the residual on biased trajectories instead of directly revealing the correction.
            4. Add a safety layer that rejects actions leading into occupied cells.
            5. Port the idea to ROS 2 with nodes for planner, controller, estimator, and logger.
            6. Replace the residual with a small neural policy once you install the advanced requirements.
            """
        ),
        md(
            """
            ## Mastery Checklist

            You are ready to move into real robot projects when you can explain and implement:

            - Coordinate frames and transformations.
            - Forward and inverse kinematics.
            - Feedback control with actuator limits.
            - State estimation under sensor noise.
            - Occupancy grids and localization.
            - Graph search and sampling-based planning.
            - Behavior cloning and action chunking.
            - Basic RL and why sim-to-real is hard.
            - Why modern robot policies use large datasets, multimodal inputs, and distributional action models.
            - How to evaluate robot behavior safely.
            """
        ),
    ]


def main():
    NOTEBOOK_DIR.mkdir(exist_ok=True)
    notebooks = [
        ("01_basics_robot_loop.ipynb", "01 - Basics: The Robot Loop", notebook_01()),
        ("02_kinematics_frames.ipynb", "02 - Kinematics And Coordinate Frames", notebook_02()),
        ("03_dynamics_control.ipynb", "03 - Dynamics And Control", notebook_03()),
        ("04_sensing_state_estimation.ipynb", "04 - Sensing And State Estimation", notebook_04()),
        ("05_mapping_slam_intro.ipynb", "05 - Mapping And SLAM Intro", notebook_05()),
        ("06_motion_planning.ipynb", "06 - Motion Planning", notebook_06()),
        ("07_imitation_learning.ipynb", "07 - Imitation Learning", notebook_07()),
        ("08_reinforcement_learning.ipynb", "08 - Reinforcement Learning", notebook_08()),
        ("09_modern_robot_learning_vla.ipynb", "09 - Modern Robot Learning And VLAs", notebook_09()),
        ("10_capstone_robot_stack.ipynb", "10 - Capstone Robot Stack", notebook_10()),
    ]
    for filename, title, cells in notebooks:
        write_notebook(filename, title, cells)


if __name__ == "__main__":
    main()
