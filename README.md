# Robotics Mastery Path

This is a structured, notebook-based learning project for getting from robotics fundamentals to modern robot learning and training.

The curriculum is designed around a simple principle: learn the classical stack first, then use it to understand how current robot-learning systems are trained, evaluated, and deployed.

## Start Here

```bash
cd Robotics
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Open the notebooks in order from `notebooks/01_...ipynb` through `notebooks/10_...ipynb`.

The code uses NumPy as the core dependency. Matplotlib is used for plots when installed. Without Matplotlib, the notebooks still run and print numeric results.

To regenerate and smoke-check the notebooks:

```bash
python3 scripts/generate_notebooks.py
python3 scripts/generate_advanced_notebooks.py
MPLBACKEND=Agg python3 scripts/smoke_check_notebooks.py
python3 tests/test_core.py
```

## Learning Path

This project now has 30 notebooks. The short index is below; the full guide is [docs/notebook_index.md](docs/notebook_index.md).

| Range | Theme | Outcome |
|---:|---|---|
| 1-10 | Core robotics | Build a small plan-estimate-control-learn stack |
| 11-14 | Math, spatial reasoning, dynamics, trajectories | Understand the equations behind robot motion |
| 15-20 | Advanced control, mobile robots, manipulation, vision, lidar | Build stronger robot behaviors and diagnose failures |
| 21-23 | ROS 2 architecture, simulation, datasets | Think like a robotics systems engineer |
| 24-26 | Robot learning | Train and evaluate policies from data or reward |
| 27-30 | Safety, multi-robot systems, research, capstone | Move toward real-world and research-ready projects |

## Project Structure

```text
Robotics
├── README.md
├── requirements.txt
├── requirements-advanced.txt
├── docs/
├── exercises/
├── projects/
├── notebooks/
├── research/
│   └── latest_research_brief.md
├── scripts/
│   ├── generate_notebooks.py
│   ├── generate_advanced_notebooks.py
│   └── smoke_check_notebooks.py
├── src/
│   └── robotics_mastery/
├── tests/
└── data/
```

## Mastery Docs

- [Mastery map](docs/00_mastery_map.md)
- [Notebook index](docs/notebook_index.md)
- [24-week schedule](docs/study_schedule_24_weeks.md)
- [Software toolchain 2026](docs/software_toolchain_2026.md)
- [Robot learning stack](docs/robot_learning_stack.md)
- [Safety guide](docs/safety_first.md)
- [Hardware lab guide](docs/hardware_lab_guide.md)
- [Research reading roadmap](docs/research_reading_roadmap.md)
- [Glossary](docs/glossary.md)
- [Mastery rubric](docs/mastery_rubric.md)
- [Exercise bank](exercises/exercise_bank.md)
- [Project briefs](projects/project_briefs.md)

## 24-Week Roadmap

Weeks 1-4: Foundations. Work through notebooks 1, 2, 3, 11, 12, 13, 14.

Weeks 5-8: Estimation, mapping, planning, and mobile robots. Work through notebooks 4, 5, 6, 10, 16.

Weeks 9-12: Manipulation and perception. Work through notebooks 17, 18, 19, 20.

Weeks 13-16: Robot software, control, simulation, and safety. Work through notebooks 15, 21, 22, 27, 28.

Weeks 17-20: Robot learning. Work through notebooks 7, 8, 23, 24, 25, 26.

Weeks 21-24: Frontier research and capstone. Work through notebooks 9, 29, 30 and complete one project brief.

## What "Training A Robot" Means

Training usually means one or more of these:

1. Calibrating hardware: sensors, cameras, joints, coordinate frames.
2. Designing controllers: PID, MPC, impedance, whole-body control.
3. Collecting demonstrations: teleoperation or scripted expert data.
4. Learning a policy: behavior cloning, action chunking, diffusion/flow policy, VLA fine-tuning.
5. Training in simulation: RL, domain randomization, curriculum learning.
6. Evaluating safely: success rate, failure modes, latency, uncertainty, human safety constraints.
7. Deploying with guardrails: fallback controllers, collision checks, emergency stops, logging.

## Current Research Map

Read [research/latest_research_brief.md](research/latest_research_brief.md) after notebook 6, then revisit it after notebook 9.

Key sources used to shape this path:
- [Open X-Embodiment](https://arxiv.org/abs/2310.08864)
- [Diffusion Policy](https://arxiv.org/abs/2303.04137)
- [Octo](https://arxiv.org/abs/2405.12213)
- [OpenVLA](https://arxiv.org/abs/2406.09246)
- [pi0](https://arxiv.org/abs/2410.24164)
- [SmolVLA](https://arxiv.org/abs/2506.01844)
- [LeRobot](https://arxiv.org/abs/2602.22818)
- [GR00T N1](https://arxiv.org/abs/2503.14734)
- [Gemini Robotics-ER 1.6](https://deepmind.google/models/model-cards/gemini-robotics-er-1-6/)
- [ROS 2 distributions](https://docs.ros.org/en/ros2_documentation/kilted/Releases.html)

## After The Notebooks

Build one physical or simulated robot project. The fastest beginner path is:

1. Finish notebooks 1-6.
2. Build a simulated differential-drive robot.
3. Add noisy sensors and localization.
4. Add A* or RRT planning.
5. Add a learned policy for one narrow skill.
6. Move to ROS 2 Jazzy or Kilted once the concepts feel clear.

For real hardware, add physical safety from day one: low speeds, soft limits, current limits, collision checks, emergency stop, logs, and a human outside the robot workspace during tests.
