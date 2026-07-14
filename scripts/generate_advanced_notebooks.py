from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"


COMMON_IMPORTS = """
import math
import random
import sys
from pathlib import Path

import numpy as np

ROOT = Path.cwd()
if not (ROOT / "src").exists() and (ROOT.parent / "src").exists():
    ROOT = ROOT.parent
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

try:
    import matplotlib.pyplot as plt
    HAS_PLOT = True
except ModuleNotFoundError:
    plt = None
    HAS_PLOT = False

np.set_printoptions(precision=3, suppress=True)

def plot_unavailable():
    if not HAS_PLOT:
        print("Install matplotlib to see plots: pip install -r requirements.txt")
"""


def md(text: str):
    return nbf.v4.new_markdown_cell(dedent(text).strip())


def code(text: str):
    return nbf.v4.new_code_cell(dedent(text).strip())


NOTEBOOK_GUIDES = {
    "11_math_for_robotics.ipynb": (
        "Review the math tools that repeatedly appear in robotics: projections, least squares, covariance, and Gaussian uncertainty.",
        "Robotics papers and systems use these ideas constantly. Understanding them makes estimation, calibration, control, and learning much less mysterious.",
        "Work through small numeric examples, fit a noisy line, compute covariance, and interpret uncertainty as geometry."
    ),
    "12_spatial_math_se3.ipynb": (
        "Move from 2D frames into 3D rigid transforms, transform inverses, and quaternions.",
        "Real robots operate in 3D. Arms, cameras, grippers, maps, and simulators all depend on reliable SE(3) reasoning.",
        "Construct rotation matrices and homogeneous transforms, invert them, transform points, and combine simple quaternions."
    ),
    "13_robot_dynamics_energy.ipynb": (
        "Simulate pendulum dynamics, energy, damping, and torque feedback control.",
        "Dynamics explains why robots overshoot, oscillate, heat up, fall, or need torque-aware controllers.",
        "Integrate a pendulum forward in time, compare free and controlled motion, and inspect energy loss and control effort."
    ),
    "14_trajectory_generation.ipynb": (
        "Generate smooth robot motion profiles instead of jumping directly from start to goal.",
        "Robots need trajectories that respect velocity, acceleration, smoothness, and hardware limits.",
        "Compare cubic, quintic, and trapezoidal profiles, then inspect endpoint behavior and duration."
    ),
    "15_lqr_mpc_control.ipynb": (
        "Study optimal feedback with LQR and short-horizon optimization with a tiny MPC example.",
        "Advanced robots often need controllers that balance accuracy, effort, constraints, and future consequences.",
        "Compute an LQR gain for a double integrator, simulate feedback, then choose actions by evaluating short candidate futures."
    ),
    "16_mobile_robot_models.ipynb": (
        "Model common mobile robot motion using unicycle and bicycle dynamics plus pure pursuit tracking.",
        "Wheeled robots are everywhere, and their motion constraints determine which paths and controllers are realistic.",
        "Implement simple motion models, follow a sinusoidal reference path, and compare with a bicycle-style trajectory."
    ),
    "17_manipulator_jacobian_control.ipynb": (
        "Control an arm endpoint iteratively using the Jacobian and damped least squares.",
        "Closed-form inverse kinematics is not always available. Jacobian methods are the practical backbone of many arm controllers.",
        "Move a 2-link arm toward a target with resolved-rate IK, then inspect singular values to identify weak configurations."
    ),
    "18_computer_vision_geometry.ipynb": (
        "Understand pinhole camera projection, depth back-projection, and stereo depth.",
        "Robot perception depends on turning pixels into geometry. Calibration errors here become bad grasps, maps, and navigation.",
        "Project 3D points into image pixels, reconstruct them with depth, and recover depth from stereo disparity."
    ),
    "19_lidar_point_clouds_icp.ipynb": (
        "Register two 2D point clouds using a small iterative closest point loop.",
        "Lidar mapping, scan matching, and point cloud alignment are core tools for mobile robots and 3D perception.",
        "Create a transformed point cloud, repeatedly match nearest neighbors, estimate the best rigid transform, and measure alignment error."
    ),
    "20_grasping_manipulation.ipynb": (
        "Build first principles for grasping: friction cones, antipodal contacts, and pick-place state machines.",
        "Manipulation is not only arm motion. It also needs contact reasoning, perception, sequencing, and recovery behavior.",
        "Check whether forces fit a friction cone, score simple contact pairs, and step through a pick-place finite-state machine."
    ),
    "21_ros2_architecture.ipynb": (
        "Learn ROS 2 concepts without needing ROS 2 installed: nodes, topics, services, actions, and dropped messages.",
        "Modern robot projects are distributed systems. You need architecture instincts before adding hardware complexity.",
        "Simulate publish/subscribe callbacks, a service call, and an action-style feedback/result flow in plain Python."
    ),
    "22_simulation_domain_randomization.ipynb": (
        "Train and evaluate a controller across randomized simulated physics.",
        "Simulators are useful but imperfect. Robust policies must survive variation in mass, friction, sensors, and actuators.",
        "Randomize dynamics parameters, sweep controller gains, choose a robust setting, and compare nominal versus randomized performance."
    ),
    "23_robot_dataset_engineering.ipynb": (
        "Create a small robot episode dataset with observations, actions, instructions, statistics, and splits.",
        "Robot learning is often bottlenecked by data quality. Bad timestamps, normalization, or splits can ruin a policy.",
        "Generate toy episodes, compute normalization statistics, create train/validation splits, and draft a dataset card."
    ),
    "24_behavior_cloning_numpy_mlp.ipynb": (
        "Train a small neural behavior cloning policy from scratch using NumPy.",
        "Frameworks are useful, but implementing a tiny network once makes policy learning and gradients more concrete.",
        "Generate supervised reaching data, train a one-hidden-layer MLP by backpropagation, then evaluate it in closed-loop rollout."
    ),
    "25_diffusion_policy_intuition.ipynb": (
        "Develop intuition for diffusion-style action sampling on a multimodal action problem.",
        "Manipulation often has multiple valid futures. Predicting the average action can be physically wrong or unsafe.",
        "Create two action modes, train a tiny local denoiser, sample actions, and compare sampled modes against the bad mean."
    ),
    "26_continuous_control_rl_cem.ipynb": (
        "Optimize a continuous action sequence with the cross-entropy method.",
        "This bridges trajectory optimization, MPC, and reinforcement learning without requiring a deep RL framework.",
        "Sample candidate action sequences, keep elites, update the sampling distribution, and roll out the best sequence."
    ),
    "27_robot_safety_reliability.ipynb": (
        "Implement basic safety layers: action limits, a watchdog, barrier-like filtering, and hazard logging.",
        "Robots can damage hardware and hurt people. Safety must be independent of the learned policy or main controller.",
        "Filter unsafe proposed velocities, simulate command timeouts, log safety interventions, and visualize constrained motion."
    ),
    "28_multi_robot_coordination.ipynb": (
        "Coordinate several robots with formation control, collision repulsion, and simple task assignment.",
        "Multiple robots introduce communication, allocation, and interaction problems that single-robot intuition does not cover.",
        "Move a team into formation, add pairwise spacing behavior, and greedily assign robots to task locations."
    ),
    "29_research_paper_reading.ipynb": (
        "Learn how to read robotics papers for implementable details rather than vague inspiration.",
        "Research claims only matter if you can identify assumptions, data, embodiments, actions, baselines, and reproducibility gaps.",
        "Fill a structured paper template, inspect common claim types, and score how reproducible a result appears."
    ),
    "30_master_capstone_portfolio.ipynb": (
        "Turn the curriculum into a portfolio-level robotics capstone plan.",
        "Mastery needs a finished system with metrics, safety, documentation, and a connection to current research.",
        "Define a capstone scope, milestones, evaluation rubric, and final deliverables you can actually build."
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
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    }
    nb["cells"] = [md(f"# {title}"), guide_cell(filename)] + cells
    path = NOTEBOOK_DIR / filename
    nbf.write(nb, path)
    print(f"wrote {path.relative_to(ROOT)}")


def nb11_math():
    return [
        md(
            """
            ## Goal

            Robotics uses math as a working language. This notebook reviews the pieces that appear everywhere:

            - Vectors and projections
            - Least squares
            - Covariance and uncertainty ellipses
            - Gaussian probability intuition
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            a = np.array([3.0, 1.0])
            b = np.array([1.0, 2.0])
            projection_of_a_on_b = b * (a @ b) / (b @ b)
            residual = a - projection_of_a_on_b
            print("projection:", projection_of_a_on_b)
            print("residual is orthogonal:", round(float(residual @ b), 8))
            """
        ),
        code(
            """
            rng = np.random.default_rng(1)
            x = np.linspace(-2, 2, 30)
            y = 1.7 * x - 0.4 + rng.normal(0, 0.25, size=len(x))
            A = np.c_[x, np.ones_like(x)]
            slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
            print("estimated line: y =", round(float(slope), 3), "* x +", round(float(intercept), 3))
            """
        ),
        code(
            """
            samples = rng.multivariate_normal(mean=[1, 2], cov=[[0.5, 0.3], [0.3, 0.8]], size=500)
            mean = samples.mean(axis=0)
            covariance = np.cov(samples.T)
            eigenvalues, eigenvectors = np.linalg.eigh(covariance)
            print("mean:", mean)
            print("covariance:\\n", covariance)
            print("uncertainty axes:", np.sqrt(eigenvalues))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 5))
                plt.scatter(samples[:, 0], samples[:, 1], s=8, alpha=0.25)
                plt.scatter([mean[0]], [mean[1]], c="tab:red")
                plt.axis("equal")
                plt.grid(True, alpha=0.3)
                plt.title("Gaussian samples as uncertainty")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Replace least squares with a noisy quadratic fit.\n2. Change covariance off-diagonal terms and explain correlation.\n3. Explain why uncertainty is a matrix, not just one number."),
    ]


def nb12_spatial_math():
    return [
        md(
            """
            ## Goal

            Robotics in 3D uses rotations, rigid transforms, and quaternions.

            This notebook builds a practical SE(3) vocabulary:

            - Rotation matrices
            - Homogeneous transforms
            - Quaternions
            - Transform inversion and composition
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            from robotics_mastery.geometry import quaternion_from_axis_angle, quaternion_multiply

            def rotx(theta):
                c, s = np.cos(theta), np.sin(theta)
                return np.array([[1, 0, 0], [0, c, -s], [0, s, c]], dtype=float)

            def rotz(theta):
                c, s = np.cos(theta), np.sin(theta)
                return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]], dtype=float)

            def transform3(R, t):
                T = np.eye(4)
                T[:3, :3] = R
                T[:3, 3] = t
                return T

            def invert_transform(T):
                R = T[:3, :3]
                t = T[:3, 3]
                T_inv = np.eye(4)
                T_inv[:3, :3] = R.T
                T_inv[:3, 3] = -R.T @ t
                return T_inv

            T_world_camera = transform3(rotz(np.deg2rad(30)) @ rotx(np.deg2rad(10)), [1.0, 0.5, 1.2])
            T_camera_world = invert_transform(T_world_camera)
            print("T_world_camera:\\n", T_world_camera)
            print("inverse check:\\n", T_camera_world @ T_world_camera)
            """
        ),
        code(
            """
            qz = quaternion_from_axis_angle(np.array([0, 0, 1]), np.deg2rad(90))
            qx = quaternion_from_axis_angle(np.array([1, 0, 0]), np.deg2rad(30))
            q_combined = quaternion_multiply(qz, qx)
            print("qz:", qz)
            print("qx:", qx)
            print("combined:", q_combined)
            print("unit norm:", np.linalg.norm(q_combined))
            """
        ),
        code(
            """
            point_camera = np.array([0.2, -0.1, 1.5, 1.0])
            point_world = T_world_camera @ point_camera
            roundtrip = T_camera_world @ point_world
            print("world point:", point_world[:3])
            print("roundtrip error:", np.linalg.norm(roundtrip - point_camera))
            """
        ),
        md("## Exercises\n\n1. Compose three transforms: world to base, base to wrist, wrist to gripper.\n2. Verify every rotation matrix has determinant 1.\n3. Explain why quaternions are often preferred over Euler angles in robot software."),
    ]


def nb13_dynamics():
    return [
        md(
            """
            ## Goal

            Dynamics asks: how do forces and torques create motion?

            You will simulate:

            - A pendulum
            - Energy
            - Damping
            - A simple torque controller
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            def simulate_pendulum(kp=0.0, kd=0.0, target=0.0, damping=0.05, dt=0.01, steps=1200):
                g, length, mass = 9.81, 1.0, 1.0
                theta, omega = np.deg2rad(80), 0.0
                rows = []
                for step in range(steps):
                    error = target - theta
                    torque = kp * error - kd * omega
                    alpha = -(g / length) * np.sin(theta) - damping * omega + torque / (mass * length**2)
                    omega += alpha * dt
                    theta += omega * dt
                    kinetic = 0.5 * mass * (length * omega) ** 2
                    potential = mass * g * length * (1 - np.cos(theta))
                    rows.append((step * dt, theta, omega, torque, kinetic + potential))
                return np.array(rows)

            free = simulate_pendulum()
            controlled = simulate_pendulum(kp=20.0, kd=5.0)
            print("free final angle deg:", np.rad2deg(free[-1, 1]))
            print("controlled final angle deg:", np.rad2deg(controlled[-1, 1]))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(8, 3))
                plt.plot(free[:, 0], np.rad2deg(free[:, 1]), label="free")
                plt.plot(controlled[:, 0], np.rad2deg(controlled[:, 1]), label="controlled")
                plt.xlabel("time [s]")
                plt.ylabel("angle [deg]")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        code(
            """
            energy_drop = free[0, 4] - free[-1, 4]
            control_effort = np.mean(np.abs(controlled[:, 3]))
            print("energy lost to damping:", round(float(energy_drop), 3))
            print("mean control effort:", round(float(control_effort), 3))
            """
        ),
        md("## Exercises\n\n1. Set damping to zero and observe energy conservation.\n2. Increase `kp` until the system oscillates.\n3. Add torque saturation.\n4. Explain why dynamics matters more for fast arms and legged robots."),
    ]


def nb14_trajectory():
    return [
        md(
            """
            ## Goal

            Robots need trajectories, not just goals.

            You will implement:

            - Cubic time scaling
            - Quintic time scaling
            - Trapezoidal velocity profiles
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            def cubic_s(t):
                return 3*t**2 - 2*t**3

            def quintic_s(t):
                return 10*t**3 - 15*t**4 + 6*t**5

            time = np.linspace(0, 1, 101)
            q0, q1 = -1.0, 2.0
            cubic_q = q0 + (q1 - q0) * cubic_s(time)
            quintic_q = q0 + (q1 - q0) * quintic_s(time)
            cubic_v = np.gradient(cubic_q, time)
            quintic_v = np.gradient(quintic_q, time)
            print("cubic endpoint velocities:", cubic_v[0], cubic_v[-1])
            print("quintic endpoint velocities:", quintic_v[0], quintic_v[-1])
            """
        ),
        code(
            """
            def trapezoid_profile(distance, vmax, amax, dt=0.02):
                t_acc = vmax / amax
                d_acc = 0.5 * amax * t_acc**2
                if 2 * d_acc > distance:
                    t_acc = np.sqrt(distance / amax)
                    t_flat = 0.0
                    vmax = amax * t_acc
                else:
                    t_flat = (distance - 2*d_acc) / vmax
                total = 2*t_acc + t_flat
                ts = np.arange(0, total + dt, dt)
                xs, vs = [], []
                for t in ts:
                    if t < t_acc:
                        v = amax * t
                        x = 0.5 * amax * t**2
                    elif t < t_acc + t_flat:
                        v = vmax
                        x = 0.5 * amax * t_acc**2 + vmax * (t - t_acc)
                    else:
                        tau = t - t_acc - t_flat
                        v = vmax - amax * tau
                        x = distance - 0.5 * amax * max(total - t, 0)**2
                    xs.append(x)
                    vs.append(max(v, 0))
                return ts, np.array(xs), np.array(vs)

            ts, xs, vs = trapezoid_profile(distance=3.0, vmax=1.2, amax=1.5)
            print("duration:", round(float(ts[-1]), 3), "final distance:", round(float(xs[-1]), 3))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(8, 3))
                plt.plot(time, cubic_q, label="cubic q")
                plt.plot(time, quintic_q, label="quintic q")
                plt.plot(ts / ts[-1], xs / xs[-1] * (q1 - q0) + q0, label="trapezoid scaled")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add acceleration plots.\n2. Make a trajectory through three waypoints.\n3. Explain why smooth acceleration protects hardware."),
    ]


def nb15_lqr_mpc():
    return [
        md(
            """
            ## Goal

            Learn two control ideas that appear in serious robotics:

            - LQR: optimal feedback for linear systems.
            - MPC: repeatedly optimize a short-horizon action sequence.
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            from robotics_mastery.control import dlqr

            dt = 0.1
            A = np.array([[1, dt], [0, 1]])
            B = np.array([[0.5*dt*dt], [dt]])
            Q = np.diag([10.0, 1.0])
            R = np.array([[0.1]])
            K = dlqr(A, B, Q, R)
            print("LQR gain:", K)
            """
        ),
        code(
            """
            def rollout_lqr(x0, steps=80):
                x = np.array(x0, dtype=float)
                rows = []
                for step in range(steps):
                    u = float(np.clip(-(K @ x)[0], -3.0, 3.0))
                    x = A @ x + B[:, 0] * u
                    rows.append((step*dt, x[0], x[1], u))
                return np.array(rows)

            lqr_rows = rollout_lqr([3.0, 0.0])
            print("final state:", lqr_rows[-1, 1:3])
            """
        ),
        code(
            """
            def one_step_mpc_action(x, candidates=np.linspace(-3, 3, 31), horizon=12):
                best_cost, best_u = float("inf"), 0.0
                for u0 in candidates:
                    sim = x.copy()
                    cost = 0.0
                    for h in range(horizon):
                        u = u0 if h == 0 else float(np.clip(-(K @ sim)[0], -3, 3))
                        cost += sim @ Q @ sim + R[0, 0] * u * u
                        sim = A @ sim + B[:, 0] * u
                    if cost < best_cost:
                        best_cost, best_u = cost, u0
                return float(best_u)

            x = np.array([3.0, 0.0])
            mpc = []
            for step in range(80):
                u = one_step_mpc_action(x)
                x = A @ x + B[:, 0] * u
                mpc.append((step*dt, x[0], x[1], u))
            mpc = np.array(mpc)
            print("MPC final state:", mpc[-1, 1:3])
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(8, 3))
                plt.plot(lqr_rows[:, 0], lqr_rows[:, 1], label="LQR position")
                plt.plot(mpc[:, 0], mpc[:, 1], label="MPC position", linestyle="--")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Increase action limits and compare settling time.\n2. Change Q to punish velocity more.\n3. Add an obstacle penalty to the MPC cost."),
    ]


def nb16_mobile_models():
    return [
        md(
            """
            ## Goal

            Understand common mobile robot models:

            - Unicycle
            - Differential drive
            - Bicycle model
            - Pure pursuit tracking
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            from robotics_mastery.control import pure_pursuit_control
            from robotics_mastery.geometry import wrap_angle

            def unicycle_step(pose, v, omega, dt=0.05):
                x, y, theta = pose
                return np.array([
                    x + v*np.cos(theta)*dt,
                    y + v*np.sin(theta)*dt,
                    wrap_angle(theta + omega*dt),
                ])

            def bicycle_step(state, speed, steering, wheelbase=0.35, dt=0.05):
                x, y, theta = state
                beta = np.tan(steering) / wheelbase
                return np.array([
                    x + speed*np.cos(theta)*dt,
                    y + speed*np.sin(theta)*dt,
                    wrap_angle(theta + speed*beta*dt),
                ])
            """
        ),
        code(
            """
            path = np.array([[i * 0.25, np.sin(i * 0.25)] for i in range(45)])
            pose = np.array([0.0, -0.5, 0.0])
            traj = []
            waypoint_idx = 0
            for _ in range(300):
                while waypoint_idx < len(path)-1 and np.linalg.norm(path[waypoint_idx] - pose[:2]) < 0.5:
                    waypoint_idx += 1
                v, omega = pure_pursuit_control(pose, path[waypoint_idx], lookahead=0.8, speed=0.5)
                pose = unicycle_step(pose, v, omega)
                traj.append(pose.copy())
            traj = np.array(traj)
            print("final pose:", traj[-1])
            print("last waypoint:", path[-1])
            """
        ),
        code(
            """
            car = np.array([0.0, -0.5, 0.0])
            car_traj = []
            for _ in range(160):
                steering = 0.35 * np.sin(_ * 0.04)
                car = bicycle_step(car, speed=0.6, steering=steering)
                car_traj.append(car.copy())
            car_traj = np.array(car_traj)
            print("bicycle final:", car_traj[-1])
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(6, 4))
                plt.plot(path[:, 0], path[:, 1], "k--", label="reference")
                plt.plot(traj[:, 0], traj[:, 1], label="pure pursuit")
                plt.plot(car_traj[:, 0], car_traj[:, 1], label="bicycle sample")
                plt.axis("equal")
                plt.grid(True, alpha=0.3)
                plt.legend()
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add wheel speed limits.\n2. Increase lookahead and explain the tracking change.\n3. Implement Stanley control and compare with pure pursuit."),
    ]


def nb17_jacobian_control():
    return [
        md(
            """
            ## Goal

            Move from inverse kinematics formulas to iterative Jacobian control.

            You will implement:

            - Resolved-rate IK
            - Damped least squares
            - Singularity awareness
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            from robotics_mastery.control import resolved_rate_step

            lengths = (1.0, 0.7)

            def fk(q):
                q1, q2 = q
                l1, l2 = lengths
                elbow = np.array([l1*np.cos(q1), l1*np.sin(q1)])
                wrist = elbow + np.array([l2*np.cos(q1+q2), l2*np.sin(q1+q2)])
                return elbow, wrist

            def jacobian(q):
                q1, q2 = q
                l1, l2 = lengths
                return np.array([
                    [-l1*np.sin(q1)-l2*np.sin(q1+q2), -l2*np.sin(q1+q2)],
                    [ l1*np.cos(q1)+l2*np.cos(q1+q2),  l2*np.cos(q1+q2)],
                ])

            target = np.array([0.7, 1.0])
            q = np.deg2rad([5.0, 20.0])
            rows = []
            for _ in range(120):
                elbow, wrist = fk(q)
                rows.append(np.r_[q, wrist])
                q = resolved_rate_step(q, target, fk, jacobian, gain=1.5, max_step=0.05, damping=1e-2)
            rows = np.array(rows)
            print("final endpoint:", rows[-1, 2:])
            print("target error:", np.linalg.norm(rows[-1, 2:] - target))
            """
        ),
        code(
            """
            configs = [np.deg2rad([0, 0]), np.deg2rad([45, 90]), np.deg2rad([0, 180])]
            for cfg in configs:
                singular_values = np.linalg.svd(jacobian(cfg), compute_uv=False)
                print("q deg", np.rad2deg(cfg), "singular values", singular_values)
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 5))
                plt.plot(rows[:, 2], rows[:, 3], label="endpoint path")
                plt.scatter([target[0]], [target[1]], c="tab:red", label="target")
                plt.axis("equal")
                plt.grid(True, alpha=0.3)
                plt.legend()
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Try a target near the reach boundary.\n2. Set damping very small near a singularity.\n3. Add joint limits and reject steps outside them."),
    ]


def nb18_vision_geometry():
    return [
        md(
            """
            ## Goal

            Robotics vision starts with geometry.

            You will implement:

            - Pinhole camera projection
            - Depth back-projection
            - Stereo triangulation
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            fx, fy = 500.0, 500.0
            cx, cy = 320.0, 240.0
            K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

            points_3d = np.array([
                [0.0, 0.0, 2.0],
                [0.2, 0.1, 2.5],
                [-0.3, 0.2, 3.0],
                [0.1, -0.2, 1.5],
            ])

            def project(points):
                uvw = (K @ points.T).T
                return uvw[:, :2] / uvw[:, 2:3]

            pixels = project(points_3d)
            print("pixels:\\n", pixels)
            """
        ),
        code(
            """
            def backproject(pixel, depth):
                u, v = pixel
                x = (u - cx) * depth / fx
                y = (v - cy) * depth / fy
                return np.array([x, y, depth])

            reconstructed = np.array([backproject(p, d) for p, d in zip(pixels, points_3d[:, 2])])
            print("reconstruction error:", np.linalg.norm(reconstructed - points_3d, axis=1))
            """
        ),
        code(
            """
            baseline = 0.12
            left_u = pixels[:, 0]
            right_u = left_u - fx * baseline / points_3d[:, 2]
            disparity = left_u - right_u
            stereo_depth = fx * baseline / disparity
            print("true depth:", points_3d[:, 2])
            print("stereo depth:", stereo_depth)
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 4))
                plt.scatter(pixels[:, 0], pixels[:, 1])
                plt.xlim(0, 640)
                plt.ylim(480, 0)
                plt.grid(True, alpha=0.3)
                plt.title("Projected image points")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add pixel noise and measure depth error.\n2. Increase baseline and compare depth accuracy.\n3. Explain why calibration is essential before robot vision is useful."),
    ]


def nb19_lidar_icp():
    return [
        md(
            """
            ## Goal

            Learn the shape of lidar and point cloud registration.

            You will implement a small 2D ICP loop:

            - Generate a point cloud.
            - Transform it.
            - Estimate the rigid transform back.
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(5)
            angles = np.linspace(0, 2*np.pi, 80, endpoint=False)
            base = np.c_[np.cos(angles), 0.6*np.sin(angles)]
            base += rng.normal(0, 0.01, base.shape)

            true_theta = np.deg2rad(18)
            R_true = np.array([[np.cos(true_theta), -np.sin(true_theta)], [np.sin(true_theta), np.cos(true_theta)]])
            t_true = np.array([0.4, -0.2])
            moved = base @ R_true.T + t_true
            print("created two point clouds")
            """
        ),
        code(
            """
            def nearest_neighbors(src, dst):
                indexes = []
                for p in src:
                    indexes.append(int(np.argmin(np.linalg.norm(dst - p, axis=1))))
                return np.array(indexes)

            def best_fit_transform(src, dst):
                src_mean = src.mean(axis=0)
                dst_mean = dst.mean(axis=0)
                X = src - src_mean
                Y = dst - dst_mean
                U, _, Vt = np.linalg.svd(X.T @ Y)
                R = Vt.T @ U.T
                if np.linalg.det(R) < 0:
                    Vt[-1] *= -1
                    R = Vt.T @ U.T
                t = dst_mean - R @ src_mean
                return R, t

            aligned = moved.copy()
            total_R = np.eye(2)
            total_t = np.zeros(2)
            for _ in range(20):
                idx = nearest_neighbors(aligned, base)
                R, t = best_fit_transform(aligned, base[idx])
                aligned = aligned @ R.T + t
                total_R = R @ total_R
                total_t = R @ total_t + t
            mean_error = np.mean(np.linalg.norm(aligned - base[nearest_neighbors(aligned, base)], axis=1))
            print("mean registration error:", round(float(mean_error), 4))
            print("estimated inverse translation:", total_t)
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 5))
                plt.scatter(base[:, 0], base[:, 1], s=12, label="target")
                plt.scatter(moved[:, 0], moved[:, 1], s=12, alpha=0.3, label="before")
                plt.scatter(aligned[:, 0], aligned[:, 1], s=12, alpha=0.7, label="after ICP")
                plt.axis("equal")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Try a less symmetric point cloud.\n2. Add outliers and reject bad matches.\n3. Explain why ICP needs a reasonable initial guess."),
    ]


def nb20_grasping():
    return [
        md(
            """
            ## Goal

            Grasping is where geometry, contact, planning, and perception meet.

            You will model:

            - A friction cone
            - Antipodal grasp intuition
            - A pick-place state machine
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            def within_friction_cone(contact_normal, force, mu):
                n = contact_normal / np.linalg.norm(contact_normal)
                f = force / np.linalg.norm(force)
                normal_component = max(0.0, f @ n)
                tangential = np.linalg.norm(f - normal_component * n)
                return tangential <= mu * normal_component

            normal = np.array([1.0, 0.0])
            test_forces = [np.array([1.0, 0.1]), np.array([1.0, 0.8]), np.array([-1.0, 0.0])]
            for force in test_forces:
                print(force, "stable?", within_friction_cone(normal, force, mu=0.5))
            """
        ),
        code(
            """
            object_points = np.array([[np.cos(a), np.sin(a)] for a in np.linspace(0, 2*np.pi, 64, endpoint=False)])

            def grasp_quality(i, j):
                p1, p2 = object_points[i], object_points[j]
                distance = np.linalg.norm(p1 - p2)
                center_alignment = abs((p1 + p2).sum())
                return distance - 0.2 * center_alignment

            candidates = []
            for i in range(len(object_points)):
                for j in range(i + 1, len(object_points)):
                    candidates.append((grasp_quality(i, j), i, j))
            best = max(candidates)
            print("best quality, contacts:", best)
            print("contact points:", object_points[best[1]], object_points[best[2]])
            """
        ),
        code(
            """
            states = ["approach", "pregrasp", "close_gripper", "lift", "move_to_place", "open_gripper", "retreat"]
            state_index = 0
            log = []
            for tick in range(14):
                state = states[state_index]
                log.append((tick, state))
                if tick % 2 == 1 and state_index < len(states) - 1:
                    state_index += 1
            print(log)
            """
        ),
        md("## Exercises\n\n1. Add a failure state for missed grasp.\n2. Add a force threshold to decide when the gripper has closed.\n3. Explain what perception must estimate before grasp planning can start."),
    ]


def nb21_ros2_architecture():
    return [
        md(
            """
            ## Goal

            Understand ROS 2 architecture without requiring ROS 2 installed.

            You will model:

            - Nodes
            - Topics
            - Services
            - Actions
            - QoS-like message dropping

            In a new real system, use ROS 2 Lyrical LTS unless a specific robot, driver, or vendor stack still requires Jazzy, Kilted, or Humble.
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            class Topic:
                def __init__(self, drop_probability=0.0):
                    self.subscribers = []
                    self.drop_probability = drop_probability

                def subscribe(self, callback):
                    self.subscribers.append(callback)

                def publish(self, message):
                    for callback in self.subscribers:
                        if random.random() >= self.drop_probability:
                            callback(message)

            odom = Topic(drop_probability=0.05)
            cmd_vel = Topic()
            logs = []

            def controller_callback(msg):
                error = np.array(msg["goal"]) - np.array(msg["pose"])
                command = 0.5 * error
                cmd_vel.publish({"vx": command[0], "vy": command[1]})

            def motor_callback(msg):
                logs.append(msg)

            odom.subscribe(controller_callback)
            cmd_vel.subscribe(motor_callback)

            for i in range(20):
                odom.publish({"pose": [i*0.05, 0.0], "goal": [1.0, 0.5]})

            print("commands received:", len(logs))
            print("last command:", logs[-1])
            """
        ),
        code(
            """
            def inverse_kinematics_service(request):
                x, y = request["target"]
                return {"joint_guess": [np.arctan2(y, x), 0.0], "success": True}

            response = inverse_kinematics_service({"target": [1.0, 1.0]})
            print(response)
            """
        ),
        code(
            """
            def navigate_action(goal, max_feedback=5):
                for step in range(max_feedback):
                    yield {"type": "feedback", "progress": (step + 1) / max_feedback}
                yield {"type": "result", "success": True, "goal": goal}

            for event in navigate_action([2.0, 3.0]):
                print(event)
            """
        ),
        md("## Exercises\n\n1. Add a watchdog that stops motors when no command arrives.\n2. Model a latched topic for robot description.\n3. Explain when you would use a service versus an action."),
    ]


def nb22_sim_randomization():
    return [
        md(
            """
            ## Goal

            Simulation is essential, but simulators are wrong in small ways.

            You will use domain randomization to train a controller that survives variation in:

            - Mass
            - Friction
            - Actuator scale
            - Sensor noise
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(22)

            def run_episode(gain, randomized=True):
                mass = rng.uniform(0.6, 1.8) if randomized else 1.0
                actuator = rng.uniform(0.75, 1.25) if randomized else 1.0
                friction = rng.uniform(0.02, 0.2) if randomized else 0.08
                x, v = -1.0, 0.0
                target = 1.0
                total_error = 0.0
                for _ in range(150):
                    observed_x = x + rng.normal(0, 0.02 if randomized else 0.0)
                    force = actuator * np.clip(gain * (target - observed_x) - 1.5*v, -4, 4)
                    a = force / mass - friction * v
                    v += a * 0.02
                    x += v * 0.02
                    total_error += abs(target - x)
                return total_error / 150, abs(target - x)

            gains = np.linspace(0.5, 12.0, 30)
            scores = []
            for gain in gains:
                errors = [run_episode(gain, randomized=True)[1] for _ in range(60)]
                scores.append(np.mean(errors))
            best_gain = float(gains[int(np.argmin(scores))])
            print("best randomized gain:", best_gain)
            """
        ),
        code(
            """
            nominal_errors = [run_episode(best_gain, randomized=False)[1] for _ in range(20)]
            randomized_errors = [run_episode(best_gain, randomized=True)[1] for _ in range(100)]
            print("nominal final error mean:", np.mean(nominal_errors))
            print("randomized final error mean:", np.mean(randomized_errors))
            print("randomized 90th percentile:", np.percentile(randomized_errors, 90))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(7, 3))
                plt.plot(gains, scores)
                plt.axvline(best_gain, color="tab:red", linestyle="--")
                plt.xlabel("gain")
                plt.ylabel("mean final error")
                plt.grid(True, alpha=0.3)
                plt.title("Domain randomization sweep")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add latency to the simulator.\n2. Train on nominal physics and test on randomized physics.\n3. Explain why domain randomization is not a substitute for real tests."),
    ]


def nb23_datasets():
    return [
        md(
            """
            ## Goal

            Robot learning quality often depends more on data than model architecture.

            You will build a tiny episode dataset with:

            - Observations
            - Actions
            - Language instructions
            - Normalization statistics
            - Train/validation split
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(23)
            episodes = []
            for ep in range(12):
                instruction = "move to target"
                target = rng.uniform(-1, 1, size=2)
                state = rng.uniform(-1, 1, size=2)
                observations, actions = [], []
                for _ in range(30):
                    action = np.clip(0.25 * (target - state), -0.12, 0.12)
                    observations.append(np.r_[state, target])
                    actions.append(action)
                    state = state + action + rng.normal(0, 0.005, size=2)
                episodes.append({
                    "instruction": instruction,
                    "observations": np.array(observations),
                    "actions": np.array(actions),
                })

            all_obs = np.vstack([ep["observations"] for ep in episodes])
            all_actions = np.vstack([ep["actions"] for ep in episodes])
            stats = {
                "obs_mean": all_obs.mean(axis=0),
                "obs_std": all_obs.std(axis=0) + 1e-6,
                "action_mean": all_actions.mean(axis=0),
                "action_std": all_actions.std(axis=0) + 1e-6,
            }
            print("episodes:", len(episodes))
            print("obs shape:", all_obs.shape, "action shape:", all_actions.shape)
            print(stats)
            """
        ),
        code(
            """
            rng.shuffle(episodes)
            train = episodes[:9]
            val = episodes[9:]

            def normalize_obs(obs):
                return (obs - stats["obs_mean"]) / stats["obs_std"]

            train_obs = normalize_obs(np.vstack([ep["observations"] for ep in train]))
            val_obs = normalize_obs(np.vstack([ep["observations"] for ep in val]))
            print("train normalized mean:", train_obs.mean(axis=0))
            print("val normalized mean:", val_obs.mean(axis=0))
            """
        ),
        code(
            """
            dataset_card = {
                "task": "2D target reaching",
                "num_episodes": len(episodes),
                "control_rate_hz": 20,
                "observation_keys": ["state_xy", "target_xy"],
                "action_keys": ["delta_xy"],
                "known_biases": ["scripted expert", "toy simulator", "no camera input"],
            }
            for key, value in dataset_card.items():
                print(f"{key}: {value}")
            """
        ),
        md("## Exercises\n\n1. Save this dataset as `.npz` under `data/generated`.\n2. Add success labels.\n3. Add a data quality check for action saturation.\n4. Write a dataset card for a real robot skill."),
    ]


def nb24_bc_mlp():
    return [
        md(
            """
            ## Goal

            Train a small behavior cloning policy from scratch using NumPy.

            This avoids deep-learning framework setup while teaching:

            - Mini-batch training
            - Nonlinear policies
            - Train/validation error
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(24)
            N = 1200
            state = rng.uniform(-1.5, 1.5, size=(N, 2))
            target = rng.uniform(-1.0, 1.0, size=(N, 2))
            obs = np.c_[state, target]
            action = np.tanh(1.3 * (target - state)) * 0.25
            action += rng.normal(0, 0.01, size=action.shape)

            idx = rng.permutation(N)
            train_idx, val_idx = idx[:900], idx[900:]
            X_train, Y_train = obs[train_idx], action[train_idx]
            X_val, Y_val = obs[val_idx], action[val_idx]
            print(X_train.shape, Y_train.shape)
            """
        ),
        code(
            """
            hidden = 32
            W1 = rng.normal(0, 0.2, size=(4, hidden))
            b1 = np.zeros(hidden)
            W2 = rng.normal(0, 0.2, size=(hidden, 2))
            b2 = np.zeros(2)

            def forward(X):
                Z1 = X @ W1 + b1
                H = np.tanh(Z1)
                Y = H @ W2 + b2
                return Z1, H, Y

            lr = 0.03
            batch = 64
            for epoch in range(250):
                batch_idx = rng.choice(len(X_train), size=batch, replace=False)
                Xb, Yb = X_train[batch_idx], Y_train[batch_idx]
                Z1, H, pred = forward(Xb)
                grad_pred = 2 * (pred - Yb) / len(Xb)
                grad_W2 = H.T @ grad_pred
                grad_b2 = grad_pred.sum(axis=0)
                grad_H = grad_pred @ W2.T
                grad_Z1 = grad_H * (1 - np.tanh(Z1) ** 2)
                grad_W1 = Xb.T @ grad_Z1
                grad_b1 = grad_Z1.sum(axis=0)
                W2 -= lr * grad_W2
                b2 -= lr * grad_b2
                W1 -= lr * grad_W1
                b1 -= lr * grad_b1

            _, _, train_pred = forward(X_train)
            _, _, val_pred = forward(X_val)
            print("train MSE:", np.mean((train_pred - Y_train)**2))
            print("val MSE:", np.mean((val_pred - Y_val)**2))
            """
        ),
        code(
            """
            def policy(pos, goal):
                _, _, out = forward(np.array([[pos[0], pos[1], goal[0], goal[1]]]))
                return np.clip(out[0], -0.25, 0.25)

            pos = np.array([-1.2, 0.8])
            goal = np.array([0.8, -0.7])
            route = [pos.copy()]
            for _ in range(35):
                pos = pos + policy(pos, goal)
                route.append(pos.copy())
            route = np.array(route)
            print("final error:", np.linalg.norm(route[-1] - goal))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 5))
                plt.plot(route[:, 0], route[:, 1], marker="o", markersize=2)
                plt.scatter([goal[0]], [goal[1]], c="tab:red")
                plt.axis("equal")
                plt.grid(True, alpha=0.3)
                plt.title("NumPy behavior cloning rollout")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add a second hidden layer.\n2. Train with fewer samples and observe overfitting.\n3. Add action delay to closed-loop evaluation."),
    ]


def nb25_diffusion():
    return [
        md(
            """
            ## Goal

            Build intuition for diffusion policies.

            This is not a production diffusion model. It is a tiny denoising toy that shows why sampling can preserve multiple action modes where mean regression fails.
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(25)
            n = 600
            modes = rng.choice([-1.0, 1.0], size=n)
            clean_actions = np.c_[0.8 + rng.normal(0, 0.04, n), modes * 0.55 + rng.normal(0, 0.05, n)]
            sigma = 0.35
            noisy = clean_actions + rng.normal(0, sigma, size=clean_actions.shape)
            print("clean mean:", clean_actions.mean(axis=0))
            print("mean action would hit obstacle:", abs(clean_actions.mean(axis=0)[1]) < 0.2)
            """
        ),
        code(
            """
            # Train a local denoiser: predict clean action as weighted average of nearest noisy examples.
            def denoise(x, bandwidth=0.35):
                distances = np.linalg.norm(noisy - x[None, :], axis=1)
                weights = np.exp(-0.5 * (distances / bandwidth) ** 2)
                weights = weights / (weights.sum() + 1e-9)
                return weights @ clean_actions

            samples = rng.normal(0, 1.0, size=(60, 2))
            for step in range(12):
                for i in range(len(samples)):
                    target = denoise(samples[i])
                    samples[i] = 0.75 * samples[i] + 0.25 * target + rng.normal(0, 0.02, 2)

            print("sample mean:", samples.mean(axis=0))
            print("sample y modes approx:", np.percentile(samples[:, 1], [10, 50, 90]))
            """
        ),
        code(
            """
            safe_samples = samples[np.abs(samples[:, 1]) > 0.2]
            chosen = safe_samples[0]
            print("chosen sampled action:", chosen)
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 4))
                plt.scatter(clean_actions[:, 0], clean_actions[:, 1], s=8, alpha=0.2, label="data")
                plt.scatter(samples[:, 0], samples[:, 1], s=20, label="samples")
                plt.axhspan(-0.2, 0.2, color="black", alpha=0.1, label="bad mean zone")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add a third action mode.\n2. Reduce the number of demonstrations.\n3. Explain how action chunks differ from single-step actions."),
    ]


def nb26_continuous_rl():
    return [
        md(
            """
            ## Goal

            Learn a simple continuous-control optimizer: the cross-entropy method.

            This is a useful bridge between planning, model predictive control, and reinforcement learning.
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(26)
            horizon = 35
            dt = 0.08
            target = np.array([1.0, 0.0])

            def evaluate_sequence(actions):
                x = np.array([-1.0, 0.0])
                v = np.array([0.0, 0.0])
                cost = 0.0
                for a in actions.reshape(horizon, 2):
                    a = np.clip(a, -2, 2)
                    v = 0.95 * v + a * dt
                    x = x + v * dt
                    cost += np.linalg.norm(x - target) ** 2 + 0.02 * np.linalg.norm(a) ** 2
                cost += 20 * np.linalg.norm(x - target) ** 2
                return cost

            dim = horizon * 2
            mean = np.zeros(dim)
            std = np.ones(dim) * 0.8
            history = []
            for iteration in range(18):
                candidates = rng.normal(mean, std, size=(300, dim))
                costs = np.array([evaluate_sequence(c) for c in candidates])
                elite = candidates[np.argsort(costs)[:30]]
                mean = elite.mean(axis=0)
                std = elite.std(axis=0) + 1e-3
                history.append(costs.min())
            print("best cost:", history[-1])
            """
        ),
        code(
            """
            actions = mean.reshape(horizon, 2)
            x = np.array([-1.0, 0.0])
            v = np.array([0.0, 0.0])
            route = [x.copy()]
            for a in actions:
                v = 0.95 * v + np.clip(a, -2, 2) * dt
                x = x + v * dt
                route.append(x.copy())
            route = np.array(route)
            print("final position:", route[-1], "error:", np.linalg.norm(route[-1] - target))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 4))
                plt.plot(route[:, 0], route[:, 1], marker="o", markersize=2)
                plt.scatter([target[0]], [target[1]], c="tab:red")
                plt.axis("equal")
                plt.grid(True, alpha=0.3)
                plt.title("CEM optimized action sequence")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add an obstacle cost.\n2. Replan every 5 steps like MPC.\n3. Compare this with Q-learning from notebook 8."),
    ]


def nb27_safety():
    return [
        md(
            """
            ## Goal

            Safety is not a final checkbox. It is part of the architecture.

            You will implement:

            - Action limits
            - A watchdog
            - A simple control barrier function
            - Hazard logging
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            from robotics_mastery.safety import limit_norm

            def safety_filter(position, proposed_velocity, obstacle, min_distance=0.5):
                p = np.asarray(position)
                v = limit_norm(proposed_velocity, 0.4)
                vector_from_obstacle = p - obstacle
                distance = np.linalg.norm(vector_from_obstacle)
                if distance < min_distance:
                    outward = vector_from_obstacle / (distance + 1e-9)
                    if v @ outward < 0:
                        v = v - (v @ outward) * outward
                return v

            obstacle = np.array([0.0, 0.0])
            position = np.array([0.3, 0.0])
            proposed = np.array([-0.3, 0.0])
            print("proposed:", proposed, "filtered:", safety_filter(position, proposed, obstacle))
            """
        ),
        code(
            """
            class Watchdog:
                def __init__(self, timeout_steps):
                    self.timeout_steps = timeout_steps
                    self.last_command_step = -1

                def command_received(self, step):
                    self.last_command_step = step

                def ok(self, step):
                    return step - self.last_command_step <= self.timeout_steps

            watchdog = Watchdog(timeout_steps=3)
            for step in range(8):
                if step in [0, 1, 2]:
                    watchdog.command_received(step)
                print(step, "motors enabled?", watchdog.ok(step))
            """
        ),
        code(
            """
            hazards = []
            pos = np.array([-1.0, 0.0])
            goal = np.array([1.0, 0.0])
            route = [pos.copy()]
            for step in range(80):
                proposed = 0.6 * (goal - pos)
                filtered = safety_filter(pos, proposed, obstacle)
                if np.linalg.norm(filtered - proposed) > 1e-6:
                    hazards.append((step, "action_filtered", pos.copy()))
                pos = pos + 0.05 * filtered
                route.append(pos.copy())
            route = np.array(route)
            print("hazard events:", len(hazards))
            print("final pos:", route[-1])
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 4))
                plt.plot(route[:, 0], route[:, 1])
                plt.scatter([obstacle[0]], [obstacle[1]], c="tab:red", label="obstacle")
                plt.gca().add_patch(plt.Circle(obstacle, 0.5, color="tab:red", alpha=0.15))
                plt.axis("equal")
                plt.grid(True, alpha=0.3)
                plt.legend()
                plt.title("Safety-filtered motion")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add speed zones near people.\n2. Add current/torque limits.\n3. Write an emergency-stop test plan.\n4. Explain why a learned policy should not be the only safety layer."),
    ]


def nb28_multi_robot():
    return [
        md(
            """
            ## Goal

            Multi-robot systems add coordination problems:

            - Formation control
            - Collision avoidance
            - Communication limits
            - Task allocation
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            from robotics_mastery.safety import velocity_obstacle_safe, limit_norm

            rng = np.random.default_rng(28)
            positions = rng.uniform(-1.5, 1.5, size=(5, 2))
            desired_offsets = np.array([[-1,0], [-0.5,0.5], [0,0], [0.5,0.5], [1,0]], dtype=float)
            center_goal = np.array([2.0, 1.0])
            routes = [positions.copy()]

            for _ in range(120):
                center = positions.mean(axis=0)
                velocities = []
                for i, p in enumerate(positions):
                    desired = center_goal + desired_offsets[i]
                    v = 0.8 * (desired - p)
                    for j, other in enumerate(positions):
                        if i == j:
                            continue
                        diff = p - other
                        d = np.linalg.norm(diff)
                        if d < 0.45:
                            v += 0.2 * diff / (d + 1e-6)
                    velocities.append(limit_norm(v, 0.08))
                positions = positions + np.array(velocities)
                routes.append(positions.copy())
            routes = np.array(routes)
            print("final positions:\\n", positions)
            print("formation error:", np.linalg.norm((positions - positions.mean(axis=0)) - (desired_offsets - desired_offsets.mean(axis=0))))
            """
        ),
        code(
            """
            tasks = np.array([[2, 0], [2, 2], [3, 1], [1.5, 1.2], [2.5, -0.5]], dtype=float)
            costs = np.linalg.norm(positions[:, None, :] - tasks[None, :, :], axis=2)
            assignment = []
            remaining = set(range(len(tasks)))
            for robot in range(len(positions)):
                best_task = min(remaining, key=lambda t: costs[robot, t])
                assignment.append((robot, best_task, costs[robot, best_task]))
                remaining.remove(best_task)
            print("greedy assignment:", assignment)
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(6, 4))
                for i in range(routes.shape[1]):
                    plt.plot(routes[:, i, 0], routes[:, i, 1], label=f"robot {i}")
                plt.scatter(tasks[:, 0], tasks[:, 1], marker="x", c="black", label="tasks")
                plt.axis("equal")
                plt.grid(True, alpha=0.3)
                plt.legend(ncol=2, fontsize=8)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add communication dropout.\n2. Replace greedy assignment with Hungarian matching after installing SciPy.\n3. Add velocity obstacle checks between robot pairs."),
    ]


def nb29_paper_reading():
    return [
        md(
            """
            ## Goal

            Learn to read robotics research like an engineer.

            A paper is not just a story. You need to extract:

            - The task and assumptions
            - The data
            - The robot embodiment
            - The action representation
            - The baselines
            - The evaluation protocol
            - The failure modes
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            paper_template = {
                "title": "OpenVLA / Diffusion Policy / pi0 / your chosen paper",
                "core_claim": "",
                "robot_embodiments": [],
                "observations": [],
                "actions": [],
                "training_data": "",
                "baselines": [],
                "metrics": ["success rate", "generalization", "latency", "safety"],
                "what_would_break_it": [],
                "what_to_reproduce_first": "",
            }
            for key in paper_template:
                print(f"{key}: {paper_template[key]}")
            """
        ),
        code(
            """
            claims = [
                {"claim": "outperforms baseline", "needs": ["same tasks", "same robot", "same budget", "confidence intervals"]},
                {"claim": "generalizes", "needs": ["held-out objects", "held-out scenes", "held-out instructions"]},
                {"claim": "real-time", "needs": ["latency", "hardware", "control frequency", "failure recovery"]},
                {"claim": "open-source", "needs": ["weights", "code", "data license", "training recipe"]},
            ]
            for item in claims:
                print(item["claim"], "=> check", ", ".join(item["needs"]))
            """
        ),
        code(
            """
            def score_reproducibility(has_code, has_weights, has_data, has_eval_scripts, hardware_clear):
                return sum([has_code, has_weights, has_data, has_eval_scripts, hardware_clear]) / 5

            print("example reproducibility score:", score_reproducibility(True, True, False, True, True))
            """
        ),
        md("## Exercises\n\n1. Fill the template for Diffusion Policy.\n2. Fill the template for OpenVLA.\n3. Fill the template for a 2026 VLA paper.\n4. Write one experiment you could reproduce on a laptop."),
    ]


def nb30_master_capstone():
    return [
        md(
            """
            ## Goal

            Convert learning into a portfolio-level robotics project.

            Your capstone should include:

            - A robot task
            - A simulator
            - A controller
            - A planner or policy
            - A dataset
            - Evaluation
            - Safety notes
            - A final report
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            capstone = {
                "project_name": "Simulated mobile manipulator for pick-and-place",
                "robot": "differential base plus 2D arm",
                "simulator": "NumPy first, then ROS 2 + Gazebo or MuJoCo",
                "task": "navigate to table, reach object, move to bin",
                "classical_stack": ["A*", "pure pursuit", "resolved-rate IK", "Kalman filter"],
                "learning_stack": ["behavior cloning", "dataset cards", "optional diffusion policy"],
                "metrics": ["success rate", "collision rate", "final error", "latency", "interventions"],
                "safety": ["speed limits", "workspace limits", "watchdog", "emergency stop"],
            }
            for key, value in capstone.items():
                print(f"{key}: {value}")
            """
        ),
        code(
            """
            milestones = [
                ("M1", "robot model and simulator", 1),
                ("M2", "manual controller and logging", 1),
                ("M3", "state estimation and planner", 2),
                ("M4", "imitation dataset and BC policy", 2),
                ("M5", "safety and evaluation harness", 1),
                ("M6", "final report and demo video", 1),
            ]
            total_weeks = sum(item[2] for item in milestones)
            print("total planned weeks:", total_weeks)
            for item in milestones:
                print(item)
            """
        ),
        code(
            """
            rubric = {
                "correctness": 0.30,
                "safety": 0.20,
                "evaluation": 0.20,
                "code_quality": 0.15,
                "research_connection": 0.15,
            }
            scores = {
                "correctness": 0.8,
                "safety": 0.7,
                "evaluation": 0.75,
                "code_quality": 0.85,
                "research_connection": 0.7,
            }
            final_score = sum(rubric[k] * scores[k] for k in rubric)
            print("example weighted score:", round(final_score, 3))
            """
        ),
        md(
            """
            ## Final Deliverables

            1. A reproducible repo.
            2. A runnable simulation.
            3. A dataset card.
            4. A policy or controller card.
            5. A safety checklist.
            6. A short paper-style report.
            7. A demo video or screen recording.
            """
        ),
        md("## Exercises\n\n1. Replace the sample capstone with your own.\n2. Define three failure modes before you implement.\n3. Choose one paper from the research brief and connect it to your design."),
    ]


def main():
    NOTEBOOK_DIR.mkdir(exist_ok=True)
    notebooks = [
        ("11_math_for_robotics.ipynb", "11 - Math For Robotics", nb11_math()),
        ("12_spatial_math_se3.ipynb", "12 - Spatial Math: SE(3) And Quaternions", nb12_spatial_math()),
        ("13_robot_dynamics_energy.ipynb", "13 - Robot Dynamics And Energy", nb13_dynamics()),
        ("14_trajectory_generation.ipynb", "14 - Trajectory Generation", nb14_trajectory()),
        ("15_lqr_mpc_control.ipynb", "15 - LQR And MPC Control", nb15_lqr_mpc()),
        ("16_mobile_robot_models.ipynb", "16 - Mobile Robot Models", nb16_mobile_models()),
        ("17_manipulator_jacobian_control.ipynb", "17 - Manipulator Jacobian Control", nb17_jacobian_control()),
        ("18_computer_vision_geometry.ipynb", "18 - Computer Vision Geometry", nb18_vision_geometry()),
        ("19_lidar_point_clouds_icp.ipynb", "19 - Lidar, Point Clouds, And ICP", nb19_lidar_icp()),
        ("20_grasping_manipulation.ipynb", "20 - Grasping And Manipulation", nb20_grasping()),
        ("21_ros2_architecture.ipynb", "21 - ROS 2 Architecture", nb21_ros2_architecture()),
        ("22_simulation_domain_randomization.ipynb", "22 - Simulation And Domain Randomization", nb22_sim_randomization()),
        ("23_robot_dataset_engineering.ipynb", "23 - Robot Dataset Engineering", nb23_datasets()),
        ("24_behavior_cloning_numpy_mlp.ipynb", "24 - Behavior Cloning With A NumPy MLP", nb24_bc_mlp()),
        ("25_diffusion_policy_intuition.ipynb", "25 - Diffusion Policy Intuition", nb25_diffusion()),
        ("26_continuous_control_rl_cem.ipynb", "26 - Continuous-Control RL With CEM", nb26_continuous_rl()),
        ("27_robot_safety_reliability.ipynb", "27 - Robot Safety And Reliability", nb27_safety()),
        ("28_multi_robot_coordination.ipynb", "28 - Multi-Robot Coordination", nb28_multi_robot()),
        ("29_research_paper_reading.ipynb", "29 - Reading Robotics Research", nb29_paper_reading()),
        ("30_master_capstone_portfolio.ipynb", "30 - Master Capstone Portfolio", nb30_master_capstone()),
    ]
    for filename, title, cells in notebooks:
        write_notebook(filename, title, cells)


if __name__ == "__main__":
    main()
