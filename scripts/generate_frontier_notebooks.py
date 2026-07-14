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
    "46_open_source_robotics_frontier_radar.ipynb": (
        "Build a practical map of the latest open-source robotics ecosystem: middleware, simulation, datasets, VLA models, humanoid hardware, and evaluation.",
        "The field moves too fast for a static course. A radar helps you decide what to learn now, what to watch, and what to avoid until it matures.",
        "Score projects by openness, maturity, hardware cost, learning value, and risk, then produce a staged learning plan."
    ),
    "47_open_vla_models_action_heads.ipynb": (
        "Compare open VLA policy families such as OpenVLA, SmolVLA, pi0/pi0.5, GR00T-style models, Xiaomi-Robotics-0, and Dexora.",
        "Modern robotics is increasingly about action representation: regression, action chunks, flow matching, autoregression, discrete diffusion, and real-time chunking.",
        "Use toy action-head simulations to understand latency, multimodality, and action smoothing before touching large models."
    ),
    "48_open_benchmarks_evaluation_harnesses.ipynb": (
        "Learn how open benchmarks and evaluation harnesses make robotics results more reproducible.",
        "Training a policy is easier than proving it works. Open evaluation is becoming a major part of trustworthy robotics.",
        "Create a benchmark matrix, compute confidence intervals, and rank models while accounting for task mismatch and uncertainty."
    ),
    "49_open_simulators_synthetic_data.ipynb": (
        "Compare open simulators and synthetic-data engines: Isaac Lab, MuJoCo, ManiSkill, RoboCasa365, RoboTwin, Genesis, LIBERO, and CALVIN.",
        "Simulation is where most robot learning scales, but every simulator has a bias. Choosing the wrong one can waste months.",
        "Score simulators by task fit, speed, photorealism, contact quality, data generation, and sim-to-real risk."
    ),
    "50_open_hardware_humanoids_dexterity.ipynb": (
        "Map open and accessible hardware for humanoid and dexterous robotics: Reachy, Unitree G1 via LeRobot, Berkeley Humanoid Lite, RUKA-v2, OpenArm, Dexora-style platforms, and desktop robots.",
        "Optimus-like robots require hardware experience, but full-size humanoids are risky and expensive. Open hardware lets you climb the ladder safely.",
        "Build a hardware decision matrix and a staged lab plan from desktop robot to hands, arms, bimanual systems, and humanoid experiments."
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


def nb46():
    return [
        md(
            """
            ## Frontier Radar

            The open-source robotics ecosystem now spans middleware, simulation, robot-learning libraries, VLA models, open hardware, and evaluation harnesses.

            This notebook teaches a habit: do not ask "what is best?" in the abstract. Ask "best for which stage, task, budget, hardware risk, and reproducibility requirement?"
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            projects = [
                {"name": "ROS 2 Lyrical", "category": "middleware", "openness": 1.0, "maturity": 0.9, "cost": 0, "risk": 0.2, "learning": 0.9},
                {"name": "LeRobot v0.5", "category": "robot learning", "openness": 0.95, "maturity": 0.75, "cost": 0, "risk": 0.35, "learning": 1.0},
                {"name": "OpenPI pi0/pi0.5", "category": "VLA", "openness": 0.8, "maturity": 0.65, "cost": 1, "risk": 0.6, "learning": 0.95},
                {"name": "SmolVLA", "category": "VLA", "openness": 0.9, "maturity": 0.65, "cost": 0.4, "risk": 0.45, "learning": 0.9},
                {"name": "Xiaomi-Robotics-0", "category": "VLA", "openness": 0.75, "maturity": 0.55, "cost": 1, "risk": 0.6, "learning": 0.8},
                {"name": "Dexora", "category": "dexterous VLA", "openness": 0.8, "maturity": 0.45, "cost": 1.0, "risk": 0.75, "learning": 0.9},
                {"name": "vla-evaluation-harness", "category": "evaluation", "openness": 0.95, "maturity": 0.65, "cost": 0.2, "risk": 0.25, "learning": 0.85},
                {"name": "ManiSkill", "category": "simulation", "openness": 0.95, "maturity": 0.8, "cost": 0, "risk": 0.25, "learning": 0.85},
                {"name": "RoboCasa365", "category": "benchmark", "openness": 0.9, "maturity": 0.6, "cost": 0.2, "risk": 0.35, "learning": 0.8},
                {"name": "RUKA-v2", "category": "hardware", "openness": 0.9, "maturity": 0.45, "cost": 0.5, "risk": 0.65, "learning": 0.9},
                {"name": "Reachy 2/Mini", "category": "hardware", "openness": 0.85, "maturity": 0.7, "cost": 0.9, "risk": 0.55, "learning": 0.85},
            ]

            def radar_score(p):
                affordability = 1.0 / (1.0 + p["cost"])
                return 0.25*p["openness"] + 0.20*p["maturity"] + 0.25*p["learning"] + 0.15*affordability - 0.15*p["risk"]

            ranked = sorted([(radar_score(p), p) for p in projects], reverse=True)
            for score, project in ranked:
                print(f"{score:.3f}  {project['name']:24} {project['category']}")
            """
        ),
        code(
            """
            stages = {
                "beginner": ["ROS 2 Lyrical", "ManiSkill", "LeRobot v0.5", "SmolVLA"],
                "intermediate": ["vla-evaluation-harness", "RoboCasa365", "OpenPI pi0/pi0.5"],
                "advanced": ["Xiaomi-Robotics-0", "Dexora", "RUKA-v2", "Reachy 2/Mini"],
            }
            for stage, names in stages.items():
                print(stage.upper())
                for name in names:
                    print(" -", name)
            """
        ),
        code(
            """
            category_counts = {}
            for project in projects:
                category_counts[project["category"]] = category_counts.get(project["category"], 0) + 1
            print(category_counts)
            """
        ),
        md("## Exercises\n\n1. Add one new project you find this month.\n2. Change the score weights for a hardware-only learner.\n3. Explain why a high benchmark score can still be a bad first project."),
    ]


def nb47():
    return [
        md(
            """
            ## Open VLA Model Families

            Current open VLA systems differ most in action representation and deployment strategy:

            - OpenVLA: large open VLA with fine-tuning path.
            - SmolVLA: compact, accessible VLA.
            - OpenPI pi0/pi0.5: flow matching and pi0-FAST autoregressive variants.
            - GR00T-style models: humanoid-oriented foundation policies integrated with LeRobot.
            - Xiaomi-Robotics-0: real-time asynchronous deployment emphasis.
            - Dexora: high-DoF bimanual and dexterous manipulation.
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            action_heads = {
                "mean_regression": {"multimodal": 0.2, "latency": 0.95, "smoothness": 0.65, "difficulty": 0.2},
                "action_chunking": {"multimodal": 0.45, "latency": 0.85, "smoothness": 0.85, "difficulty": 0.35},
                "diffusion": {"multimodal": 0.9, "latency": 0.35, "smoothness": 0.8, "difficulty": 0.75},
                "flow_matching": {"multimodal": 0.85, "latency": 0.55, "smoothness": 0.85, "difficulty": 0.75},
                "autoregressive_tokens": {"multimodal": 0.7, "latency": 0.6, "smoothness": 0.65, "difficulty": 0.65},
                "real_time_chunking": {"multimodal": 0.65, "latency": 0.85, "smoothness": 0.9, "difficulty": 0.65},
            }
            for name, attrs in action_heads.items():
                print(name, attrs)
            """
        ),
        code(
            """
            # Toy latency budget: a slow VLA predicts chunks, a fast controller consumes them.
            control_hz = 50
            chunk_horizon = 10
            inference_ms = {
                "SmolVLA-ish": 45,
                "pi0.5-ish": 120,
                "large VLA-ish": 260,
            }
            for model, ms in inference_ms.items():
                chunk_duration_ms = 1000 * chunk_horizon / control_hz
                margin = chunk_duration_ms - ms
                print(model, "chunk_duration_ms", chunk_duration_ms, "inference_margin_ms", margin)
            """
        ),
        code(
            """
            # Multimodal action example: go above or below an obstacle.
            rng = np.random.default_rng(47)
            modes = rng.choice([-1, 1], size=400)
            actions = np.c_[rng.normal(0.8, 0.04, 400), modes * rng.normal(0.55, 0.04, 400)]
            mean_action = actions.mean(axis=0)
            sampled = actions[rng.choice(len(actions), 6, replace=False)]
            print("mean action:", mean_action)
            print("mean crosses obstacle band?", abs(mean_action[1]) < 0.2)
            print("sampled safe actions:")
            print(sampled)
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(5, 4))
                plt.scatter(actions[:, 0], actions[:, 1], s=8, alpha=0.25)
                plt.scatter([mean_action[0]], [mean_action[1]], c="tab:red", s=80, label="mean")
                plt.axhspan(-0.2, 0.2, color="black", alpha=0.1, label="unsafe band")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Add a discrete diffusion action head to the table.\n2. Change control frequency to 200 Hz and inspect latency pressure.\n3. Write which VLA family you would try first on a small arm and why."),
    ]


def nb48():
    return [
        md(
            """
            ## Evaluation Harnesses

            Open evaluation is now as important as open training. A model that wins one benchmark may fail another because sensors, action spaces, objects, instructions, or time horizons differ.
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            benchmarks = [
                {"name": "LIBERO", "focus": "lifelong manipulation", "horizon": "short/medium", "visual": True},
                {"name": "CALVIN", "focus": "long-horizon language tasks", "horizon": "long", "visual": True},
                {"name": "ManiSkill", "focus": "GPU manipulation sim/data", "horizon": "short/medium", "visual": True},
                {"name": "RoboCasa365", "focus": "household mobile manipulation", "horizon": "medium/long", "visual": True},
                {"name": "RoboTwin 2.0", "focus": "bimanual data generation", "horizon": "medium", "visual": True},
                {"name": "SimplerEnv", "focus": "real-to-sim policy eval", "horizon": "short", "visual": True},
            ]
            for b in benchmarks:
                print(f"{b['name']:12} {b['focus']:34} horizon={b['horizon']}")
            """
        ),
        code(
            """
            rng = np.random.default_rng(48)
            models = ["SmolVLA", "OpenVLA", "pi0.5", "Xiaomi-Robotics-0"]
            true_success = {"SmolVLA": 0.62, "OpenVLA": 0.66, "pi0.5": 0.72, "Xiaomi-Robotics-0": 0.75}
            episodes = 120
            results = {}
            for model in models:
                successes = rng.binomial(episodes, true_success[model])
                p = successes / episodes
                se = math.sqrt(p * (1 - p) / episodes)
                results[model] = (p, 1.96 * se)
            for model, (p, ci) in sorted(results.items(), key=lambda x: -x[1][0]):
                print(f"{model:18} success={p:.3f}  95% CI +/- {ci:.3f}")
            """
        ),
        code(
            """
            # Penalize models evaluated on mismatched benchmarks.
            task_match = {"SmolVLA": 0.8, "OpenVLA": 0.75, "pi0.5": 0.7, "Xiaomi-Robotics-0": 0.65}
            reproducibility = {"SmolVLA": 0.85, "OpenVLA": 0.8, "pi0.5": 0.75, "Xiaomi-Robotics-0": 0.65}
            for model in models:
                p, ci = results[model]
                adjusted = p * task_match[model] * reproducibility[model]
                print(f"{model:18} raw={p:.3f} adjusted_for_your_lab={adjusted:.3f}")
            """
        ),
        md("## Exercises\n\n1. Increase episodes from 120 to 1000 and inspect confidence intervals.\n2. Add a real-robot evaluation column.\n3. Explain why leaderboard rankings should not directly choose your capstone model."),
    ]


def nb49():
    return [
        md(
            """
            ## Simulator Selection

            Simulation is not one thing. Locomotion, dexterous contact, photorealistic perception, mobile manipulation, and benchmark reproducibility all favor different tools.
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            simulators = [
                {"name": "Isaac Lab", "speed": 0.9, "photo": 0.8, "contact": 0.75, "robot_learning": 0.95, "ease": 0.45},
                {"name": "MuJoCo", "speed": 0.85, "photo": 0.35, "contact": 0.85, "robot_learning": 0.8, "ease": 0.75},
                {"name": "ManiSkill", "speed": 0.9, "photo": 0.65, "contact": 0.8, "robot_learning": 0.9, "ease": 0.7},
                {"name": "RoboCasa365", "speed": 0.65, "photo": 0.8, "contact": 0.65, "robot_learning": 0.85, "ease": 0.55},
                {"name": "RoboTwin 2.0", "speed": 0.75, "photo": 0.65, "contact": 0.75, "robot_learning": 0.8, "ease": 0.6},
                {"name": "Genesis", "speed": 0.95, "photo": 0.65, "contact": 0.7, "robot_learning": 0.8, "ease": 0.75},
                {"name": "Gazebo Sim", "speed": 0.45, "photo": 0.55, "contact": 0.55, "robot_learning": 0.45, "ease": 0.65},
            ]

            task_weights = {"speed": 0.25, "photo": 0.15, "contact": 0.25, "robot_learning": 0.25, "ease": 0.10}
            for sim in sorted(simulators, key=lambda s: sum(s[k]*w for k, w in task_weights.items()), reverse=True):
                score = sum(sim[k] * w for k, w in task_weights.items())
                print(f"{score:.3f} {sim['name']}")
            """
        ),
        code(
            """
            # Domain randomization coverage toy model.
            rng = np.random.default_rng(49)
            train_friction = rng.uniform(0.4, 1.2, 1000)
            real_friction = rng.normal(0.75, 0.18, 500)
            real_friction = np.clip(real_friction, 0.1, 1.5)
            covered = np.mean((real_friction >= train_friction.min()) & (real_friction <= train_friction.max()))
            print("real friction covered by train range:", covered)
            """
        ),
        code(
            """
            if HAS_PLOT:
                plt.figure(figsize=(7, 3))
                plt.hist(train_friction, bins=30, alpha=0.5, label="train randomized")
                plt.hist(real_friction, bins=30, alpha=0.5, label="real estimate")
                plt.legend()
                plt.grid(True, alpha=0.3)
                plt.show()
            else:
                plot_unavailable()
            """
        ),
        md("## Exercises\n\n1. Change weights for a vision-heavy task.\n2. Add Webots or Drake to the simulator table.\n3. Write a simulator choice memo for humanoid locomotion versus kitchen manipulation."),
    ]


def nb50():
    return [
        md(
            """
            ## Open Hardware Ladder

            The safest path toward Optimus-like robots is not to start with a full humanoid. Build capability in layers:

            1. Desktop interaction robot.
            2. Low-cost arm.
            3. Dexterous hand.
            4. Bimanual platform.
            5. Small humanoid.
            6. Tethered full-body humanoid.
            """
        ),
        code(COMMON_IMPORTS),
        code(
            """
            hardware = [
                {"name": "Reachy Mini", "type": "desktop humanoid", "cost": 0.2, "safety": 0.95, "openness": 0.85, "dexterity": 0.15, "humanoid": 0.3},
                {"name": "SO-101 / low-cost arm", "type": "arm", "cost": 0.15, "safety": 0.85, "openness": 0.9, "dexterity": 0.35, "humanoid": 0.1},
                {"name": "OpenArm", "type": "7-DoF arm", "cost": 0.55, "safety": 0.65, "openness": 0.8, "dexterity": 0.55, "humanoid": 0.35},
                {"name": "RUKA-v2", "type": "dexterous hand", "cost": 0.45, "safety": 0.65, "openness": 0.9, "dexterity": 0.85, "humanoid": 0.55},
                {"name": "Reachy 2", "type": "bimanual humanoid", "cost": 0.95, "safety": 0.55, "openness": 0.85, "dexterity": 0.75, "humanoid": 0.75},
                {"name": "Berkeley Humanoid Lite", "type": "small humanoid", "cost": 0.55, "safety": 0.45, "openness": 0.9, "dexterity": 0.35, "humanoid": 0.85},
                {"name": "Unitree G1 + LeRobot", "type": "full humanoid", "cost": 0.9, "safety": 0.35, "openness": 0.55, "dexterity": 0.65, "humanoid": 0.95},
            ]

            def lab_value(item):
                affordability = 1 / (1 + item["cost"])
                return 0.25*item["openness"] + 0.25*item["safety"] + 0.2*item["dexterity"] + 0.2*item["humanoid"] + 0.1*affordability

            for h in sorted(hardware, key=lab_value, reverse=True):
                print(f"{lab_value(h):.3f} {h['name']:24} {h['type']}")
            """
        ),
        code(
            """
            lab_budget = 12000
            options = [
                ("desktop + arm + hand", 500 + 600 + 1800),
                ("OpenArm bimanual-ish lab", 6500),
                ("Berkeley Humanoid Lite", 5000),
                ("Reachy 2", 70000),
                ("Unitree G1", 16000),
            ]
            for name, cost in options:
                print(f"{name:28} cost=${cost:6,.0f} feasible={cost <= lab_budget}")
            """
        ),
        code(
            """
            safety_gates = [
                "bench test with motors disabled",
                "single-joint low-speed motion",
                "workspace limits active",
                "watchdog active",
                "emergency stop tested",
                "teleop shadow mode",
                "policy shadow mode",
                "tethered or constrained hardware test",
            ]
            for i, gate in enumerate(safety_gates, start=1):
                print(i, gate)
            """
        ),
        md("## Exercises\n\n1. Build your own hardware ladder for your budget.\n2. Add maintenance difficulty as a score.\n3. Write a no-go list for experiments you will not run without supervision."),
    ]


def main():
    NOTEBOOK_DIR.mkdir(exist_ok=True)
    notebooks = [
        ("46_open_source_robotics_frontier_radar.ipynb", "46 - Open-Source Robotics Frontier Radar", nb46()),
        ("47_open_vla_models_action_heads.ipynb", "47 - Open VLA Models And Action Heads", nb47()),
        ("48_open_benchmarks_evaluation_harnesses.ipynb", "48 - Open Benchmarks And Evaluation Harnesses", nb48()),
        ("49_open_simulators_synthetic_data.ipynb", "49 - Open Simulators And Synthetic Data", nb49()),
        ("50_open_hardware_humanoids_dexterity.ipynb", "50 - Open Hardware, Humanoids, And Dexterity", nb50()),
    ]
    for filename, title, cells in notebooks:
        write_notebook(filename, title, cells)


if __name__ == "__main__":
    main()
