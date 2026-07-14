# Research Reading Roadmap

Use this after notebook 6. Before that, papers may feel too abstract.

## Phase 1: Robot Learning Basics

Read:
- [Diffusion Policy](https://arxiv.org/abs/2303.04137)
- [Mobile ALOHA](https://arxiv.org/abs/2401.02117)

Questions:
- What is the observation space?
- What is the action space?
- How many demonstrations are used?
- What are the baselines?
- What failure modes are shown?

## Phase 2: Generalist Policies

Read:
- [Open X-Embodiment](https://arxiv.org/abs/2310.08864)
- [Octo](https://arxiv.org/abs/2405.12213)
- [OpenVLA](https://arxiv.org/abs/2406.09246)

Questions:
- What does cross-embodiment mean?
- How are actions represented across robots?
- What transfers and what does not?
- What is actually open: code, weights, data, training recipe?

## Phase 3: VLA And Flow Policies

Read:
- [pi0](https://arxiv.org/abs/2410.24164)
- [SmolVLA](https://arxiv.org/abs/2506.01844)
- [LeRobot](https://arxiv.org/abs/2602.22818)

Questions:
- Why use action chunks?
- Why use diffusion or flow instead of mean regression?
- What hardware is required?
- What can a hobbyist reproduce?

## Phase 4: Humanoids And Embodied Reasoning

Read:
- [GR00T N1](https://arxiv.org/abs/2503.14734)
- [Gemini Robotics](https://deepmind.google/models/gemini-robotics/)
- [Gemini Robotics-ER 1.6 model card](https://deepmind.google/models/model-cards/gemini-robotics-er-1-6/)

Questions:
- Which model plans?
- Which model controls?
- What safety evaluations are reported?
- What tasks are still brittle?

## Phase 5: 2026 Frontier Watchlist

Read:
- [VLA-Thinker](https://arxiv.org/abs/2603.14523)
- [ABot-M0](https://arxiv.org/abs/2602.11236)
- [VLA datasets, benchmarks, and data engines survey](https://openreview.net/forum?id=tAaWFpvnmm)

Questions:
- Is the main contribution data, architecture, reasoning, or evaluation?
- What is the most convincing experiment?
- What is missing for deployment?

## Phase 6: Open-Source Robotics Frontier

Read:
- [Latest open-source advancements in this repo](latest_open_source_advancements_2026.md)
- [LeRobot v0.5.0](https://huggingface.co/blog/lerobot-release-v050)
- [OpenPI](https://github.com/Physical-Intelligence/openpi)
- [Xiaomi-Robotics-0](https://xiaomi-robotics-0.github.io/)
- [Dexora](https://github.com/dexoravla/Dexora)
- [vla-evaluation-harness](https://github.com/allenai/vla-evaluation-harness)
- [ManiSkill](https://www.maniskill.ai/)
- [RoboTwin 2.0](https://robotwin-platform.github.io/)
- [RUKA-v2](https://ruka-hand-v2.github.io/)

Questions:
- What is actually open: code, weights, data, hardware files, or only a paper?
- What benchmark or robot does the project target?
- What would it cost to reproduce the smallest useful result?
- What safety gates would be required before hardware deployment?
- Which notebook from 46-50 helps you evaluate it?

## Paper Review Template

For every paper, write:

- One-sentence claim.
- Robot embodiment.
- Observations.
- Actions.
- Dataset.
- Training method.
- Baselines.
- Metrics.
- Strongest result.
- Weakest assumption.
- Reproduction plan.
- What you would test next.
