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
    "31_humanoid_systems_overview.ipynb": (
        "Decompose an Optimus-like humanoid into hardware, software, autonomy, data, safety, and manufacturing subsystems.",
        "Humanoids look like one robot, but they are really a stack of hard coupled systems. A serious builder learns the decomposition first.",
        "Use a subsystem map, dependency graph, and build-readiness scoring model to identify what must be mastered before full humanoids become realistic."
    ),
    "32_humanoid_mechatronics_actuators.ipynb": (
        "Study actuator sizing, torque-speed tradeoffs, power, thermal load, and series elasticity.",
        "Humanoid capability is limited by actuators and energy as much as by AI. Weak or hot actuators make impressive demos impossible.",
        "Estimate joint torque and power for simple motions, compare gear ratios, and simulate a compliant actuator response."
    ),
    "33_biped_balance_lipm.ipynb": (
        "Learn the linear inverted pendulum model, capture point, support polygon, and foot placement intuition.",
        "Biped robots fall unless their center of mass and foot contacts are managed continuously.",
        "Simulate COM dynamics, compute capture points, check support polygon margin, and test foot placement strategies."
    ),
    "34_humanoid_locomotion_rl.ipynb": (
        "Build a toy locomotion policy loop with rewards, domain randomization, and gait features.",
        "Modern humanoid walking is often trained in simulation with reinforcement learning and transferred to hardware.",
        "Optimize simple gait parameters under randomized dynamics and evaluate robustness instead of one perfect nominal run."
    ),
    "35_whole_body_control.ipynb": (
        "Understand whole-body control as prioritized objectives under constraints.",
        "Humanoids must balance, move hands, avoid joint limits, and respect contacts at the same time.",
        "Solve small least-squares control problems with task weights, joint limits, and secondary posture objectives."
    ),
    "36_humanoid_hands_tactile.ipynb": (
        "Model dexterous hands, tactile feedback, grasp force, slip detection, and manipulation state machines.",
        "Optimus-like usefulness depends heavily on hands. Walking matters, but value comes from manipulating the world.",
        "Simulate grip force, tactile slip signals, grasp adjustment, and a small manipulation controller."
    ),
    "37_humanoid_perception_stack.ipynb": (
        "Sketch the perception stack for a humanoid: cameras, depth, segmentation, tracking, pose, and scene memory.",
        "A general-purpose robot needs persistent understanding of objects, humans, free space, hands, and task state.",
        "Build a toy scene graph from detections, update tracks over time, and query the graph for task-relevant objects."
    ),
    "38_teleoperation_data_factory.ipynb": (
        "Design a teleoperation and data-collection loop for humanoid robot learning.",
        "Human demonstrations are the practical fuel for current humanoid manipulation systems.",
        "Simulate latency, action smoothing, episode metadata, data quality checks, and correction loops."
    ),
    "39_humanoid_vla_architecture.ipynb": (
        "Understand VLA-style humanoid autonomy: perception, language, planning, action chunks, and low-level controllers.",
        "Systems like GR00T, Gemini Robotics, OpenPI, SmolVLA, Xiaomi-Robotics-0, and Dexora point toward layered language-conditioned robot policies.",
        "Build a tiny hierarchical policy mockup that turns a language command into skill selection and action chunks."
    ),
    "40_sim_to_real_humanoids.ipynb": (
        "Study sim-to-real for humanoids: randomization, residual errors, hardware limits, and staged deployment.",
        "Humanoid policies that work in sim can fail quickly on hardware because contacts, delays, and actuators differ.",
        "Run randomized rollouts, quantify robustness, and build a staged deployment checklist."
    ),
    "41_humanoid_edge_compute.ipynb": (
        "Estimate compute budgets for humanoid perception, planning, control, and VLA inference.",
        "A useful humanoid must react in real time. Large models must coexist with high-frequency control loops.",
        "Create latency budgets, compare synchronous versus asynchronous inference, and simulate missed control deadlines."
    ),
    "42_humanoid_safety_standards.ipynb": (
        "Design safety layers for a human-scale autonomous robot.",
        "A full-size humanoid combines mobile robot, manipulator, and AI-agent risks in one machine.",
        "Implement toy risk scoring, speed-and-separation monitoring, fall zones, and safety case structure."
    ),
    "43_humanoid_manufacturing_cost.ipynb": (
        "Reason about manufacturability, reliability, cost, serviceability, and fleet learning.",
        "Optimus-like robots are not just lab prototypes; they require supply chains, calibration, testing, and maintenance.",
        "Build a simple bill-of-materials model, failure-rate estimate, and fleet data flywheel simulation."
    ),
    "44_open_source_humanoid_lab.ipynb": (
        "Map open-source and accessible platforms into a realistic humanoid learning lab.",
        "You cannot clone Tesla Optimus, but you can learn many ingredients through open platforms and smaller robots.",
        "Score candidate platforms by cost, openness, risk, software stack, and learning value, then design a staged lab."
    ),
    "45_optimus_style_capstone.ipynb": (
        "Plan a multi-stage capstone that approximates an Optimus-like robot stack with open tools.",
        "The right goal is not to build Optimus tomorrow; it is to build progressively harder subsystems that converge toward humanoid competence.",
        "Define milestones, metrics, datasets, safety gates, and a final public portfolio roadmap."
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
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    }
    nb["cells"] = [md(f"# {title}"), guide_cell(filename)] + cells
    path = NOTEBOOK_DIR / filename
    nbf.write(nb, path)
    print(f"wrote {path.relative_to(ROOT)}")


def nb31():
    return [
        md(
            """
            ## Public Reality Check

            Tesla Optimus is not open source, and public details are incomplete. Treat it as a target architecture to reason about, not as a blueprint to copy.

            A credible Optimus-like robot needs:

            - Human-scale mechatronics
            - Biped locomotion
            - Dexterous hands
            - Vision and proprioception
            - Whole-body control
            - Language-conditioned task policies
            - Teleoperation and data pipelines
            - Fleet learning and manufacturing
            - Layered safety
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            subsystems = {
                "mechanical": ["skeleton", "joints", "transmissions", "hands", "thermal design"],
                "electronics": ["motor drivers", "battery", "power distribution", "compute", "networking"],
                "sensing": ["cameras", "IMU", "joint encoders", "force/torque", "tactile"],
                "control": ["joint control", "whole-body control", "balance", "locomotion", "manipulation"],
                "learning": ["teleop data", "imitation", "RL locomotion", "VLA manipulation", "evaluation"],
                "systems": ["ROS 2-like middleware", "logging", "simulation", "deployment", "fleet updates"],
                "safety": ["limits", "collision checking", "watchdogs", "fall handling", "human safety"],
                "manufacturing": ["BOM", "calibration", "QA", "serviceability", "reliability"],
            }
            for area, pieces in subsystems.items():
                print(f"{area:>14}: {', '.join(pieces)}")
            """
        ),
        code(
            """
            prerequisites = {
                "biped locomotion": ["dynamics", "state estimation", "RL", "safety"],
                "dexterous manipulation": ["kinematics", "vision", "tactile", "imitation"],
                "language autonomy": ["VLA", "task planning", "safety policy", "dataset engineering"],
                "factory deployment": ["reliability", "telemetry", "maintenance", "manufacturing"],
            }

            completed = {"dynamics", "state estimation", "kinematics", "vision", "imitation", "dataset engineering"}
            for capability, needs in prerequisites.items():
                readiness = sum(n in completed for n in needs) / len(needs)
                missing = [n for n in needs if n not in completed]
                print(f"{capability:24} readiness={readiness:.0%} missing={missing}")
            """
        ),
        code(
            """
            # A tiny dependency graph as an adjacency list.
            graph = {
                "actuators": ["joint control", "whole-body control"],
                "sensors": ["state estimation", "perception"],
                "state estimation": ["balance", "locomotion"],
                "perception": ["manipulation", "VLA policy"],
                "teleoperation": ["datasets"],
                "datasets": ["VLA policy", "imitation policy"],
                "safety": ["deployment"],
                "whole-body control": ["deployment"],
            }
            for source, targets in graph.items():
                print(source, "->", targets)
            """
        ),
        md("## Exercises\n\n1. Add one missing subsystem that would matter in a factory.\n2. Mark which subsystems can be learned with open-source tools today.\n3. Write a one-page architecture for your own humanoid learning lab."),
    ]


def nb32():
    return [
        md("## Actuator Sizing\n\nHuman-scale robots live or die by torque, speed, mass, heat, and cost. This notebook keeps the math simple but forces the right engineering questions."),
        code(COMMON_IMPORTS),
        code(
            """
            gravity = 9.81
            segment_mass = 4.0
            segment_length = 0.45
            payload = 2.0
            lever_arm = 0.35
            safety_factor = 2.0

            shoulder_torque = safety_factor * gravity * (segment_mass * segment_length / 2 + payload * lever_arm)
            print("estimated shoulder hold torque [Nm]:", round(shoulder_torque, 2))
            """
        ),
        code(
            """
            motor_speed = np.linspace(0, 6000, 80)  # rpm
            stall_torque = 0.8  # Nm at motor
            no_load_speed = 6000
            motor_torque = stall_torque * np.maximum(0, 1 - motor_speed / no_load_speed)
            gear_ratios = [30, 60, 100]
            for ratio in gear_ratios:
                joint_speed = motor_speed / ratio
                joint_torque = motor_torque * ratio * 0.75
                print(f"ratio={ratio:3}: max joint torque={joint_torque.max():.1f} Nm, max joint speed={joint_speed.max():.1f} rpm")
            """
        ),
        code(
            """
            from robotics_mastery.humanoid import actuator_power

            torque = np.array([10, 20, 30, 20, 10], dtype=float)
            velocity = np.array([0.5, 1.0, 1.2, -0.8, -0.4])
            power = actuator_power(torque, velocity)
            print("instantaneous mechanical power [W]:", power)
            print("positive power mean [W]:", power[power > 0].mean())
            """
        ),
        code(
            """
            stiffness = 120.0
            damping = 2.5
            load_torque = 8.0
            motor_angle = 0.2
            joint_angle, joint_velocity = 0.0, 0.0
            rows = []
            for step in range(300):
                spring_torque = stiffness * (motor_angle - joint_angle)
                net_torque = spring_torque - damping * joint_velocity - load_torque
                joint_velocity += net_torque * 0.002
                joint_angle += joint_velocity * 0.002
                rows.append((step * 0.002, joint_angle, spring_torque))
            rows = np.array(rows)
            print("final joint angle:", rows[-1, 1])
            print("final spring torque:", rows[-1, 2])
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(7, 3))
                plt.plot(rows[:, 0], rows[:, 1], label="joint angle")
                plt.plot(rows[:, 0], rows[:, 2] / stiffness, label="spring deflection equivalent")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.title("Compliant actuator toy response")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Estimate knee torque for standing from a squat.\n2. Add motor temperature as a state.\n3. Explain the tradeoff between high gear ratio and backdrivability."),
    ]


def nb33():
    return [
        md("## Balance Models\n\nThis is a toy introduction to biped balance. Real humanoids use full rigid-body dynamics, contacts, state estimation, and whole-body control."),
        code(COMMON_IMPORTS),
        code(
            """
            from robotics_mastery.humanoid import capture_point, footstep_sequence, lipm_step, support_polygon_margin

            x, v = 0.05, 0.35
            zmp = 0.0
            rows = []
            for step in range(250):
                x, v = lipm_step(x, v, zmp, height=0.85, dt=0.01)
                rows.append((step * 0.01, x, v, capture_point(x, v, height=0.85)))
            rows = np.array(rows)
            print("final COM:", rows[-1, 1], "final capture point:", rows[-1, 3])
            """
        ),
        code(
            """
            feet = footstep_sequence(step_length=0.28, step_width=0.09, count=8)
            print(feet)
            """
        ),
        code(
            """
            foot_polygon = np.array([[-0.12, -0.05], [0.12, -0.05], [0.12, 0.05], [-0.12, 0.05]])
            test_points = [np.array([0.0, 0.0]), np.array([0.1, 0.04]), np.array([0.2, 0.0])]
            for p in test_points:
                print("point", p, "support margin", round(support_polygon_margin(p, foot_polygon), 3))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(7, 3))
                plt.plot(rows[:, 0], rows[:, 1], label="COM x")
                plt.plot(rows[:, 0], rows[:, 3], label="capture point")
                plt.axhline(0.12, color="black", linestyle="--", alpha=0.4, label="foot edge")
                plt.axhline(-0.12, color="black", linestyle="--", alpha=0.4)
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Change COM height and observe capture point behavior.\n2. Move the ZMP and stabilize the COM.\n3. Add alternating footsteps and keep capture point inside the next foot."),
    ]


def nb34():
    return [
        md("## Locomotion RL Toy\n\nHumanoid-Gym, Isaac Lab, and related systems train locomotion in high-throughput physics. Here we only practice the idea: optimize gait parameters under randomized conditions."),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(34)

            def evaluate_gait(params, randomized=True):
                step_length, cadence, lateral_gain = params
                friction = rng.uniform(0.55, 1.2) if randomized else 0.9
                actuator = rng.uniform(0.8, 1.2) if randomized else 1.0
                terrain = rng.normal(0, 0.03) if randomized else 0.0
                speed = actuator * step_length * cadence
                target_speed = 0.8
                stability_penalty = max(0, abs(lateral_gain + terrain) - friction * 0.35) ** 2
                energy = 0.3 * cadence**2 + 0.8 * step_length**2
                reward = 2.0 - abs(speed - target_speed) - 3.0 * stability_penalty - 0.15 * energy
                return reward

            population = rng.uniform([0.1, 1.0, -0.2], [0.55, 3.0, 0.2], size=(80, 3))
            for generation in range(30):
                scores = np.array([np.mean([evaluate_gait(p) for _ in range(8)]) for p in population])
                elites = population[np.argsort(scores)[-10:]]
                population = elites.mean(axis=0) + rng.normal(0, elites.std(axis=0) + 1e-3, size=(80, 3))
                population = np.clip(population, [0.05, 0.5, -0.4], [0.7, 4.0, 0.4])
            best = population[np.argmax([np.mean([evaluate_gait(p) for _ in range(20)]) for p in population])]
            print("best gait [step_length, cadence, lateral_gain]:", best)
            """
        ),
        code(
            """
            robust_scores = [evaluate_gait(best, randomized=True) for _ in range(300)]
            nominal_scores = [evaluate_gait(best, randomized=False) for _ in range(50)]
            print("nominal mean reward:", np.mean(nominal_scores))
            print("randomized mean reward:", np.mean(robust_scores))
            print("randomized 10th percentile:", np.percentile(robust_scores, 10))
            """
        ),
        code(
            """
            phase = np.linspace(0, 2*np.pi, 120)
            left_foot = best[0] * np.sin(phase)
            right_foot = best[0] * np.sin(phase + np.pi)
            if HAS_PLOT:
                plt.figure(figsize=(7, 3))
                plt.plot(phase, left_foot, label="left foot swing")
                plt.plot(phase, right_foot, label="right foot swing")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add a fall penalty when friction is low.\n2. Add terrain slope as a randomized variable.\n3. Explain why this toy optimizer is not enough for real walking."),
    ]


def nb35():
    return [
        md("## Whole-Body Control\n\nA humanoid needs to satisfy many objectives at once: balance, hand pose, posture, joint limits, and contact constraints."),
        code(COMMON_IMPORTS),
        code(
            """
            # Toy robot with 6 joints and 3 tasks.
            rng = np.random.default_rng(35)
            J_hand = rng.normal(0, 1, size=(2, 6))
            J_com = rng.normal(0, 0.5, size=(2, 6))
            J_posture = np.eye(6)

            hand_error = np.array([0.12, -0.05])
            com_error = np.array([-0.03, 0.02])
            posture_error = np.array([0.0, 0.1, -0.1, 0.0, 0.05, -0.05])

            A = np.vstack([10 * J_hand, 20 * J_com, 0.5 * J_posture])
            b = np.r_[10 * hand_error, 20 * com_error, 0.5 * posture_error]
            dq, *_ = np.linalg.lstsq(A, b, rcond=None)
            print("joint velocity command:", dq)
            print("hand residual:", np.linalg.norm(J_hand @ dq - hand_error))
            print("COM residual:", np.linalg.norm(J_com @ dq - com_error))
            """
        ),
        code(
            """
            joint_limits = np.array([[-1.0, 1.0]] * 6)
            q = np.array([0.9, 0.0, -0.95, 0.2, 0.0, 0.0])
            q_next = q + dq
            q_safe = np.clip(q_next, joint_limits[:, 0], joint_limits[:, 1])
            print("raw next q:", q_next)
            print("safe next q:", q_safe)
            print("clipped joints:", np.where(np.abs(q_next - q_safe) > 1e-9)[0])
            """
        ),
        code(
            """
            weights = np.linspace(1, 50, 20)
            residuals = []
            for w in weights:
                A = np.vstack([10 * J_hand, w * J_com, 0.5 * J_posture])
                b = np.r_[10 * hand_error, w * com_error, 0.5 * posture_error]
                sol, *_ = np.linalg.lstsq(A, b, rcond=None)
                residuals.append((np.linalg.norm(J_hand @ sol - hand_error), np.linalg.norm(J_com @ sol - com_error)))
            residuals = np.array(residuals)
            print("first/last residuals:", residuals[0], residuals[-1])
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(7, 3))
                plt.plot(weights, residuals[:, 0], label="hand residual")
                plt.plot(weights, residuals[:, 1], label="COM residual")
                plt.xlabel("COM task weight")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add a foot contact task.\n2. Change task weights and explain tradeoffs.\n3. Replace clipping with a penalty before joint limits."),
    ]


def nb36():
    return [
        md("## Hands And Tactile Feedback\n\nHumanoid usefulness depends on picking up, holding, placing, and using objects. Tactile feedback helps detect slip and contact state."),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(36)
            object_weight = 1.2
            mu = 0.6
            fingers = 4
            required_normal_force = object_weight * 9.81 / (mu * fingers)
            print("minimum per-finger normal force [N]:", round(required_normal_force, 2))
            """
        ),
        code(
            """
            grip_force = 1.0
            log = []
            for t in range(60):
                tangential = object_weight * 9.81 / fingers + rng.normal(0, 0.15)
                max_static = mu * grip_force
                slip = tangential > max_static
                if slip:
                    grip_force += 0.25
                else:
                    grip_force *= 0.998
                log.append((t, grip_force, tangential, max_static, slip))
            log = np.array(log, dtype=float)
            print("final grip force:", log[-1, 1])
            print("slip events:", int(log[:, 4].sum()))
            """
        ),
        code(
            """
            states = ["approach", "contact", "load_test", "lift", "transport", "place", "release"]
            state = 0
            events = []
            for tick in range(20):
                tactile_contact = tick >= 3
                stable_grip = tick >= 7
                at_place = tick >= 15
                current = states[state]
                events.append((tick, current))
                if current == "approach" and tactile_contact:
                    state += 1
                elif current == "contact":
                    state += 1
                elif current == "load_test" and stable_grip:
                    state += 1
                elif current == "lift":
                    state += 1
                elif current == "transport" and at_place:
                    state += 1
                elif current == "place":
                    state += 1
            print(events)
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(7, 3))
                plt.plot(log[:, 0], log[:, 1], label="grip force")
                plt.plot(log[:, 0], log[:, 2], label="tangential load")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.title("Slip-reactive grip")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add fragile-object max force.\n2. Add two tactile sensors per finger.\n3. Explain why vision alone is not enough for dexterous manipulation."),
    ]


def nb37():
    return [
        md("## Perception Stack\n\nA humanoid needs an object-centric scene representation: what exists, where it is, whether it moved, and how it relates to the task."),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(37)
            detections_t0 = [
                {"label": "red cup", "xy": np.array([0.5, 0.2]), "confidence": 0.94},
                {"label": "blue bowl", "xy": np.array([0.9, 0.1]), "confidence": 0.91},
                {"label": "person", "xy": np.array([1.5, -0.4]), "confidence": 0.98},
            ]
            tracks = {}
            next_id = 0
            for det in detections_t0:
                tracks[next_id] = {**det, "age": 1}
                next_id += 1
            print(tracks)
            """
        ),
        code(
            """
            detections_t1 = [
                {"label": "red cup", "xy": np.array([0.54, 0.22]), "confidence": 0.92},
                {"label": "blue bowl", "xy": np.array([0.91, 0.12]), "confidence": 0.88},
                {"label": "person", "xy": np.array([1.45, -0.38]), "confidence": 0.97},
                {"label": "spoon", "xy": np.array([0.75, 0.3]), "confidence": 0.78},
            ]

            def update_tracks(tracks, detections, max_dist=0.2):
                global next_id
                assigned = set()
                for det in detections:
                    best = None
                    best_dist = float("inf")
                    for tid, track in tracks.items():
                        if tid in assigned or track["label"] != det["label"]:
                            continue
                        dist = np.linalg.norm(track["xy"] - det["xy"])
                        if dist < best_dist:
                            best, best_dist = tid, dist
                    if best is not None and best_dist < max_dist:
                        tracks[best].update(det)
                        tracks[best]["age"] += 1
                        assigned.add(best)
                    else:
                        tracks[next_id] = {**det, "age": 1}
                        next_id += 1
                return tracks

            tracks = update_tracks(tracks, detections_t1)
            for tid, track in tracks.items():
                print(tid, track)
            """
        ),
        code(
            """
            scene_graph = []
            labels = list(tracks.items())
            for i, a in labels:
                for j, b in labels:
                    if i >= j:
                        continue
                    dist = np.linalg.norm(a["xy"] - b["xy"])
                    if dist < 0.45:
                        scene_graph.append((a["label"], "near", b["label"], round(float(dist), 2)))
            print(scene_graph)
            """
        ),
        code(
            """
            instruction = "put the red cup in the blue bowl"
            relevant = [track for track in tracks.values() if any(word in track["label"] for word in ["cup", "bowl"])]
            print("instruction:", instruction)
            print("relevant objects:", relevant)
            """
        ),
        md("## Exercises\n\n1. Add object disappearance and memory timeout.\n2. Add a table surface and support relations.\n3. Explain how bad tracking could cause unsafe manipulation."),
    ]


def nb38():
    return [
        md("## Teleoperation Data Factory\n\nHumanoid data is expensive. A practical builder needs teleop, metadata, quality checks, and correction loops."),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(38)
            dt = 0.05
            latency_steps = 3
            human_commands = [np.array([0.04, 0.02]) * np.sin(i * 0.1) + np.array([0.03, 0.0]) for i in range(120)]
            command_buffer = [np.zeros(2) for _ in range(latency_steps)]
            robot_pos = np.zeros(2)
            episode = []
            for t, cmd in enumerate(human_commands):
                command_buffer.append(cmd)
                delayed = command_buffer.pop(0)
                smooth = 0.8 * delayed
                robot_pos = robot_pos + smooth + rng.normal(0, 0.002, 2)
                episode.append({"t": t * dt, "obs": robot_pos.copy(), "action": smooth.copy(), "latency_steps": latency_steps})
            print("episode length:", len(episode))
            print("last record:", episode[-1])
            """
        ),
        code(
            """
            actions = np.array([step["action"] for step in episode])
            speeds = np.linalg.norm(actions, axis=1) / dt
            quality = {
                "max_speed": float(speeds.max()),
                "mean_speed": float(speeds.mean()),
                "saturation_rate": float(np.mean(np.linalg.norm(actions, axis=1) > 0.045)),
                "missing_frames": 0,
            }
            print(quality)
            """
        ),
        code(
            """
            episode_card = {
                "task": "toy reach under teleoperation",
                "operator": "simulated",
                "robot": "2D end-effector proxy",
                "control_rate_hz": int(1 / dt),
                "latency_ms": latency_steps * dt * 1000,
                "quality": quality,
            }
            for k, v in episode_card.items():
                print(f"{k}: {v}")
            """
        ),
        code(
            """
            corrections = []
            for i, step in enumerate(episode):
                if np.linalg.norm(step["action"]) > 0.045:
                    corrections.append({"index": i, "reason": "too fast", "new_action": step["action"] * 0.7})
            print("corrections needed:", len(corrections))
            print(corrections[:3])
            """
        ),
        md("## Exercises\n\n1. Add camera timestamps and detect action-observation misalignment.\n2. Add success/failure labels.\n3. Design a teleop setup for bimanual humanoid manipulation."),
    ]


def nb39():
    return [
        md("## Humanoid VLA Architecture\n\nThis notebook is a mock architecture, not a real foundation model. It teaches the interfaces between language, perception, skill selection, and low-level action."),
        code(COMMON_IMPORTS),
        code(
            """
            skills = {
                "pick": {"preconditions": ["object_visible", "hand_free"], "action_dim": 7},
                "place": {"preconditions": ["holding_object", "target_visible"], "action_dim": 7},
                "walk": {"preconditions": ["path_clear"], "action_dim": 3},
                "look": {"preconditions": [], "action_dim": 2},
            }

            def parse_instruction(text):
                text = text.lower()
                if "pick" in text or "grab" in text:
                    return "pick"
                if "place" in text or "put" in text:
                    return "place"
                if "walk" in text or "go" in text:
                    return "walk"
                return "look"

            instruction = "pick up the red cup"
            selected = parse_instruction(instruction)
            print("selected skill:", selected, skills[selected])
            """
        ),
        code(
            """
            world_state = {"object_visible", "hand_free", "target_visible", "path_clear"}

            def preconditions_ok(skill, state):
                missing = [p for p in skills[skill]["preconditions"] if p not in state]
                return missing

            missing = preconditions_ok(selected, world_state)
            print("missing preconditions:", missing)
            """
        ),
        code(
            """
            rng = np.random.default_rng(39)

            def action_chunk_for_skill(skill, horizon=6):
                dim = skills[skill]["action_dim"]
                base = rng.normal(0, 0.02, size=(horizon, dim))
                if skill == "pick":
                    base[:, 2] -= np.linspace(0, 0.08, horizon)
                    base[:, -1] = np.linspace(0.08, 0.0, horizon)  # gripper close
                elif skill == "place":
                    base[:, 2] += np.linspace(0, 0.08, horizon)
                    base[:, -1] = np.linspace(0.0, 0.08, horizon)
                elif skill == "walk":
                    base[:, 0] = 0.2
                return base

            chunk = action_chunk_for_skill(selected)
            print(chunk)
            """
        ),
        code(
            """
            safety_limits = np.array([0.05] * chunk.shape[1])
            safe_chunk = np.clip(chunk, -safety_limits, safety_limits)
            print("clipped elements:", int(np.sum(np.abs(chunk - safe_chunk) > 1e-9)))
            """
        ),
        md("## Exercises\n\n1. Add a recovery skill when preconditions are missing.\n2. Add a high-level planner that sequences pick then place.\n3. Explain why action chunks still need low-level safety filters."),
    ]


def nb40():
    return [
        md("## Humanoid Sim-To-Real\n\nThe question is not whether simulation is useful. It is where simulation lies, and how you protect the robot when reality disagrees."),
        code(COMMON_IMPORTS),
        code(
            """
            rng = np.random.default_rng(40)

            def run_policy(randomized=True):
                mass_scale = rng.uniform(0.8, 1.25) if randomized else 1.0
                motor_delay = rng.integers(0, 5) if randomized else 1
                foot_friction = rng.uniform(0.45, 1.1) if randomized else 0.8
                command = 0.0
                buffer = [0.0] * motor_delay
                speed = 0.0
                distance = 0.0
                fall = False
                for step in range(160):
                    desired = 0.8
                    command = np.clip(2.0 * (desired - speed), -1.0, 1.0)
                    buffer.append(command)
                    delayed = buffer.pop(0)
                    speed += (delayed / mass_scale - 0.05 * speed) * 0.02
                    distance += speed * 0.02
                    if abs(command) > foot_friction * 1.3:
                        fall = True
                        break
                return distance, speed, fall, {"mass_scale": mass_scale, "delay": motor_delay, "friction": foot_friction}

            trials = [run_policy(True) for _ in range(300)]
            fall_rate = np.mean([t[2] for t in trials])
            distances = np.array([t[0] for t in trials])
            print("fall rate:", fall_rate)
            print("distance mean/p10:", distances.mean(), np.percentile(distances, 10))
            """
        ),
        code(
            """
            failures = [meta for _, _, fall, meta in trials if fall]
            print("num failures:", len(failures))
            print("first failures:", failures[:5])
            """
        ),
        code(
            """
            deployment_stages = [
                ("sim", "10k randomized episodes", "no regression in fall rate"),
                ("sim-to-sim", "different physics backend", "similar metrics"),
                ("bench", "legs suspended or low power", "commands bounded"),
                ("tethered", "overhead support", "no hard falls"),
                ("free walk", "clear test area", "human outside fall zone"),
            ]
            for stage in deployment_stages:
                print(stage)
            """
        ),
        md("## Exercises\n\n1. Add sensor noise and estimate state.\n2. Add a safety filter that reduces command when friction is low.\n3. Write a deployment stop condition for each stage."),
    ]


def nb41():
    return [
        md("## Edge Compute\n\nA humanoid has fast loops and slow loops. Joint control might run at 500-2000 Hz, locomotion at 50-200 Hz, perception at 10-60 Hz, and high-level VLA reasoning slower."),
        code(COMMON_IMPORTS),
        code(
            """
            loops = {
                "joint_current": {"hz": 1000, "budget_ms": 1.0},
                "whole_body_control": {"hz": 200, "budget_ms": 5.0},
                "locomotion_policy": {"hz": 50, "budget_ms": 20.0},
                "vision_tracking": {"hz": 30, "budget_ms": 33.3},
                "vla_action_chunk": {"hz": 5, "budget_ms": 200.0},
                "task_planner": {"hz": 1, "budget_ms": 1000.0},
            }
            for name, cfg in loops.items():
                print(f"{name:20} {cfg['hz']:4} Hz budget={cfg['budget_ms']:6.1f} ms")
            """
        ),
        code(
            """
            rng = np.random.default_rng(41)
            measured_latency = {
                "whole_body_control": rng.normal(3.2, 0.8, 200),
                "vision_tracking": rng.normal(24, 8, 200),
                "vla_action_chunk": rng.normal(130, 45, 200),
            }
            for name, values in measured_latency.items():
                budget = loops[name]["budget_ms"]
                miss_rate = np.mean(values > budget)
                print(name, "p95", np.percentile(values, 95), "miss_rate", miss_rate)
            """
        ),
        code(
            """
            # Async inference: fast controller reuses the last action chunk while slow VLA computes the next one.
            control_steps = 120
            chunk_period = 10
            current_chunk_id = 0
            used_chunks = []
            for step in range(control_steps):
                if step % chunk_period == 0:
                    current_chunk_id += 1
                used_chunks.append(current_chunk_id)
            print("chunks used:", used_chunks[:25], "...", used_chunks[-5:])
            """
        ),
        md("## Exercises\n\n1. Add camera preprocessing latency.\n2. Add a watchdog if VLA outputs stop arriving.\n3. Explain which loops must never depend directly on cloud inference."),
    ]


def nb42():
    return [
        md("## Human-Scale Safety\n\nThis is educational, not legal advice. Full-size humanoids require professional safety engineering, standards review, and controlled test environments."),
        code(COMMON_IMPORTS),
        code(
            """
            hazards = [
                {"name": "fall near human", "severity": 5, "likelihood": 2, "detectability": 2},
                {"name": "pinch point in hand", "severity": 3, "likelihood": 3, "detectability": 3},
                {"name": "unexpected arm swing", "severity": 4, "likelihood": 2, "detectability": 3},
                {"name": "battery thermal event", "severity": 5, "likelihood": 1, "detectability": 2},
                {"name": "bad VLA command", "severity": 4, "likelihood": 3, "detectability": 2},
            ]
            for h in hazards:
                h["risk_priority"] = h["severity"] * h["likelihood"] * h["detectability"]
            for h in sorted(hazards, key=lambda x: -x["risk_priority"]):
                print(h)
            """
        ),
        code(
            """
            def speed_limit(distance_to_human):
                if distance_to_human < 0.5:
                    return 0.0
                if distance_to_human < 1.5:
                    return 0.2 * (distance_to_human - 0.5)
                return 0.5

            for d in [0.2, 0.6, 1.0, 1.5, 2.0]:
                print("distance", d, "speed_limit", speed_limit(d))
            """
        ),
        code(
            """
            safety_case = {
                "claim": "Robot can perform low-speed tabletop pick-place in a marked lab cell.",
                "assumptions": ["single trained operator", "clear floor", "speed limited", "emergency stop tested"],
                "evidence": ["unit tests", "simulation tests", "dry runs", "risk assessment", "incident logs"],
                "monitors": ["human distance", "joint torque", "command timeout", "workspace boundary"],
            }
            for k, v in safety_case.items():
                print(k, ":", v)
            """
        ),
        md("## Exercises\n\n1. Add a fall-zone calculation for a 1.7 m robot.\n2. Add a safety case for teleoperation.\n3. Explain why demos at trade shows are not proof of autonomous safety."),
    ]


def nb43():
    return [
        md("## Manufacturing And Fleet Learning\n\nTesla's advantage, if Optimus succeeds, would likely be manufacturing plus AI data loops. This notebook models those pressures at toy scale."),
        code(COMMON_IMPORTS),
        code(
            """
            bom = {
                "actuators": 40 * 180,
                "sensors": 900,
                "compute": 1200,
                "battery_power": 800,
                "structure": 1500,
                "hands": 2200,
                "assembly_test": 2500,
            }
            total = sum(bom.values())
            for k, v in bom.items():
                print(f"{k:14}: ${v:,.0f}")
            print("toy BOM total:", f"${total:,.0f}")
            """
        ),
        code(
            """
            units = np.array([10, 100, 1000, 10000], dtype=float)
            learning_rate = 0.85  # cost falls to 85% each doubling, toy assumption
            cost = total * learning_rate ** (np.log2(units / units[0]))
            for u, c in zip(units, cost):
                print(f"units={int(u):5} estimated unit cost=${c:,.0f}")
            """
        ),
        code(
            """
            fleet_size = 100
            tasks_per_robot_per_day = 80
            failure_rate = 0.08
            days = 30
            failures = []
            for day in range(days):
                attempts = fleet_size * tasks_per_robot_per_day
                failures.append(attempts * failure_rate)
                failure_rate *= 0.97  # learning from failures
            print("first day failures:", round(failures[0]))
            print("day 30 failures:", round(failures[-1]))
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(7, 3))
                plt.plot(np.arange(days) + 1, failures)
                plt.xlabel("day")
                plt.ylabel("failures/day")
                plt.grid(True, alpha=0.3)
                plt.title("Toy fleet learning curve")
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add service labor cost.\n2. Add actuator replacement rate.\n3. Explain why fleet data can be more valuable than a single impressive demo."),
    ]


def nb44():
    return [
        md("## Open-Source Humanoid Lab\n\nThis is a practical bridge: learn Optimus-like ingredients using available tools, smaller robots, and public research stacks."),
        code(COMMON_IMPORTS),
        code(
            """
            platforms = [
                {"name": "ROBOTIS OP3", "cost": 12000, "openness": 0.8, "risk": 0.3, "humanoid": 0.6, "learning": 0.6},
                {"name": "Berkeley Humanoid Lite", "cost": 5000, "openness": 0.9, "risk": 0.6, "humanoid": 0.8, "learning": 0.8},
                {"name": "ToddlerBot-style platform", "cost": 6000, "openness": 0.8, "risk": 0.6, "humanoid": 0.7, "learning": 0.8},
                {"name": "Unitree G1 + LeRobot", "cost": 16000, "openness": 0.5, "risk": 0.8, "humanoid": 0.9, "learning": 0.9},
                {"name": "OpenArm bimanual", "cost": 6500, "openness": 0.8, "risk": 0.4, "humanoid": 0.5, "learning": 0.9},
                {"name": "Reachy 2/Mini", "cost": 70000, "openness": 0.85, "risk": 0.55, "humanoid": 0.75, "learning": 0.85},
                {"name": "RUKA-v2 hand", "cost": 1800, "openness": 0.9, "risk": 0.55, "humanoid": 0.55, "learning": 0.85},
                {"name": "Simulation-only Isaac/MuJoCo", "cost": 0, "openness": 0.9, "risk": 0.05, "humanoid": 0.7, "learning": 0.7},
            ]
            for p in platforms:
                affordability = 1 / (1 + p["cost"] / 10000)
                p["score"] = 0.25*p["openness"] + 0.25*p["learning"] + 0.2*p["humanoid"] + 0.2*affordability - 0.1*p["risk"]
            for p in sorted(platforms, key=lambda x: -x["score"]):
                print(f"{p['name']:30} score={p['score']:.3f} cost=${p['cost']:,}")
            """
        ),
        code(
            """
            lab_stages = [
                "NumPy simulation and notebooks",
                "ROS 2 mobile base or small arm",
                "LeRobot dataset and behavior cloning",
                "MuJoCo/Isaac humanoid simulation",
                "Low-cost bimanual or small humanoid platform",
                "Tethered full-body humanoid experiments",
            ]
            for i, stage in enumerate(lab_stages, start=1):
                print(i, stage)
            """
        ),
        code(
            """
            open_tools = {
                "middleware": ["ROS 2", "ros2_control"],
                "navigation": ["Nav2"],
                "manipulation": ["MoveIt 2", "Drake"],
                "simulation": ["MuJoCo", "Gazebo Sim", "Isaac Lab", "ManiSkill", "RoboCasa365", "RoboTwin 2.0", "Genesis"],
                "learning": ["LeRobot", "Humanoid-Gym", "Booster Gym", "OpenPI", "vla-evaluation-harness"],
                "models": ["OpenVLA", "SmolVLA", "pi0/pi0.5", "Xiaomi-Robotics-0", "Dexora", "GR00T-family resources where available"],
                "hardware": ["OpenArm", "Reachy 2/Mini", "RUKA-v2", "Berkeley Humanoid Lite", "Unitree G1 when safety/budget allow"],
            }
            for k, v in open_tools.items():
                print(k, ":", ", ".join(v))
            """
        ),
        md("## Exercises\n\n1. Pick a lab budget and choose platforms.\n2. Design a safe first humanoid experiment.\n3. Explain what cannot be learned without real hardware."),
    ]


def nb45():
    return [
        md("## Optimus-Style Capstone\n\nThis is the north-star project plan. It deliberately starts small and adds capability in gates."),
        code(COMMON_IMPORTS),
        code(
            """
            roadmap = [
                {"stage": "S1", "name": "2D mobile-manipulation sim", "risk": "low", "metric": "task success > 90%"},
                {"stage": "S2", "name": "ROS 2 sim with logs and safety", "risk": "low", "metric": "zero unsafe commands in replay"},
                {"stage": "S3", "name": "bimanual tabletop teleop dataset", "risk": "medium", "metric": "100 quality episodes"},
                {"stage": "S4", "name": "BC/VLA-style action chunk policy", "risk": "medium", "metric": "closed-loop success > 70%"},
                {"stage": "S5", "name": "humanoid locomotion sim", "risk": "medium", "metric": "fall rate < 5% randomized"},
                {"stage": "S6", "name": "integrated humanoid sim demo", "risk": "high", "metric": "complete long-horizon task"},
                {"stage": "S7", "name": "tethered hardware transfer", "risk": "very high", "metric": "safety case approved"},
            ]
            for item in roadmap:
                print(item)
            """
        ),
        code(
            """
            portfolio_artifacts = [
                "system architecture diagram",
                "simulation video",
                "dataset card",
                "policy card",
                "safety case",
                "failure analysis",
                "paper reading notes",
                "reproducible code",
            ]
            for artifact in portfolio_artifacts:
                print("-", artifact)
            """
        ),
        code(
            """
            metrics = {
                "locomotion": ["distance", "fall rate", "energy", "disturbance recovery"],
                "manipulation": ["success rate", "grasp retries", "object damage", "time"],
                "autonomy": ["instruction success", "recovery success", "human interventions"],
                "safety": ["near misses", "watchdog trips", "limit violations", "E-stop count"],
                "systems": ["latency p95", "dropped frames", "log completeness", "uptime"],
            }
            for area, ms in metrics.items():
                print(area, ":", ", ".join(ms))
            """
        ),
        code(
            """
            readiness_scores = {
                "classical robotics": 0.75,
                "robot learning": 0.55,
                "humanoid locomotion": 0.35,
                "dexterous manipulation": 0.40,
                "systems safety": 0.60,
                "hardware manufacturing": 0.20,
            }
            weighted = np.mean(list(readiness_scores.values()))
            print("example readiness:", round(float(weighted), 3))
            for k, v in readiness_scores.items():
                print(f"{k:24}: {v:.0%}")
            """
        ),
        md("## Exercises\n\n1. Replace the example readiness scores with your own.\n2. Choose one stage to build first and define exact acceptance tests.\n3. Write what you will not attempt until you have a safety mentor or lab."),
    ]


def main():
    NOTEBOOK_DIR.mkdir(exist_ok=True)
    notebooks = [
        ("31_humanoid_systems_overview.ipynb", "31 - Humanoid Systems Overview", nb31()),
        ("32_humanoid_mechatronics_actuators.ipynb", "32 - Humanoid Mechatronics And Actuators", nb32()),
        ("33_biped_balance_lipm.ipynb", "33 - Biped Balance With LIPM", nb33()),
        ("34_humanoid_locomotion_rl.ipynb", "34 - Humanoid Locomotion RL Intuition", nb34()),
        ("35_whole_body_control.ipynb", "35 - Whole-Body Control", nb35()),
        ("36_humanoid_hands_tactile.ipynb", "36 - Humanoid Hands And Tactile Manipulation", nb36()),
        ("37_humanoid_perception_stack.ipynb", "37 - Humanoid Perception Stack", nb37()),
        ("38_teleoperation_data_factory.ipynb", "38 - Teleoperation And Data Factory", nb38()),
        ("39_humanoid_vla_architecture.ipynb", "39 - Humanoid VLA Architecture", nb39()),
        ("40_sim_to_real_humanoids.ipynb", "40 - Sim-To-Real For Humanoids", nb40()),
        ("41_humanoid_edge_compute.ipynb", "41 - Humanoid Edge Compute", nb41()),
        ("42_humanoid_safety_standards.ipynb", "42 - Humanoid Safety And Standards Mindset", nb42()),
        ("43_humanoid_manufacturing_cost.ipynb", "43 - Humanoid Manufacturing And Cost", nb43()),
        ("44_open_source_humanoid_lab.ipynb", "44 - Open-Source Humanoid Lab", nb44()),
        ("45_optimus_style_capstone.ipynb", "45 - Optimus-Style Capstone", nb45()),
    ]
    for filename, title, cells in notebooks:
        write_notebook(filename, title, cells)


if __name__ == "__main__":
    main()
