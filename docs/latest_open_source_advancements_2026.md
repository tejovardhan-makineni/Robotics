# Latest Open-Source Robotics Advancements

Checked on 2026-06-11.

This document tracks open or publicly reproducible robotics work that should be part of a zero-to-hero robotics course. It favors primary sources: official docs, project pages, GitHub repositories, arXiv papers, and release posts.

## What Changed Since The Earlier Course Draft

### ROS 2 Lyrical Luth is now the latest LTS

ROS 2 Lyrical Luth was released in May 2026 and is supported until May 2031. It is now the default long-term-support ROS 2 target for new learners unless a specific robot stack requires Jazzy, Kilted, or Humble.

Sources:
- [ROS 2 Lyrical Luth release notes](https://docs.ros.org/en/lyrical/Releases/Release-Lyrical-Luth.html)
- [ROS docs home](https://docs.ros.org/)

Course impact:
- Update ROS 2 target guidance from Kilted/Jazzy to Lyrical LTS for new projects.
- Keep Jazzy/Humble only when hardware vendors still require them.

### LeRobot v0.5.0 is a major open robot-learning milestone

LeRobot v0.5.0 adds full Unitree G1 humanoid support, whole-body control workflows, Pi0-FAST, Real-Time Chunking, EnvHub, IsaacLab-Arena integration, streaming video encoding, and modernized Python 3.12+ support.

Sources:
- [LeRobot v0.5.0 release](https://huggingface.co/blog/lerobot-release-v050)
- [LeRobot GitHub](https://github.com/huggingface/lerobot)
- [Unitree G1 in LeRobot docs](https://huggingface.co/docs/lerobot/unitree_g1)

Course impact:
- Add LeRobot as the main practical open-source robot-learning stack.
- Include humanoid support and whole-body control as part of the advanced track.
- Teach EnvHub-style environment sharing and policy comparison.

### OpenPI / pi0 / pi0.5 are now part of the open VLA toolkit

Physical Intelligence's OpenPI repository provides code and model checkpoints for pi0, pi0-FAST, and pi0.5-style VLA policies. The repository includes examples for out-of-the-box use and fine-tuning on custom datasets, with caveats that transfer depends on platform and data.

Sources:
- [OpenPI GitHub](https://github.com/Physical-Intelligence/openpi)
- [Open-sourcing pi0](https://www.pi.website/blog/openpi)
- [LeRobot pi0.5 docs](https://huggingface.co/docs/lerobot/en/pi05)

Course impact:
- Teach flow matching, autoregressive action tokenization, and action chunking as separate policy families.
- Add practical caveats: GPU cost, robot embodiment mismatch, action-space alignment, and safety filters.

### SmolVLA makes VLA learning more accessible

SmolVLA is a compact open-source VLA model designed for affordability and efficient robotics experimentation. It is especially important for learners because it lowers the barrier compared with very large VLA systems.

Sources:
- [SmolVLA announcement](https://huggingface.co/blog/smolvla)
- [SmolVLA docs in LeRobot](https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx)

Course impact:
- Include smaller VLA models as the recommended first VLA fine-tuning target.
- Teach asynchronous inference and action chunks.

### Xiaomi-Robotics-0 adds an open real-time VLA direction

Xiaomi-Robotics-0 is a 4.7B-parameter open-sourced VLA model aimed at high-performance, smooth real-time execution. It reports strong results on LIBERO, SimplerEnv, CALVIN, and bimanual tasks, with code and model links on its project page and GitHub.

Sources:
- [Xiaomi-Robotics-0 project page](https://xiaomi-robotics-0.github.io/)
- [Xiaomi-Robotics-0 GitHub](https://github.com/XiaomiRobotics/Xiaomi-Robotics-0)
- [Xiaomi-Robotics-0 arXiv](https://arxiv.org/html/2602.12684v1)

Course impact:
- Add real-time chunk alignment and asynchronous execution to the VLA architecture discussion.
- Include it in the model comparison radar, not as a beginner target.

### Dexora pushes open-source VLA toward high-DoF bimanual dexterity

Dexora is an open-source VLA system for dual-arm, dual-hand, 36-DoF dexterous manipulation, with released training, inference, data-processing, and teleoperation code.

Sources:
- [Dexora GitHub](https://github.com/dexoravla/Dexora)
- [Dexora arXiv](https://arxiv.org/abs/2605.18722)

Course impact:
- Add dual-arm dual-hand data collection, high-DoF action spaces, and data-quality-aware training to the humanoid manipulation track.

### RUKA-v2 updates the open-source dexterous hand landscape

RUKA-v2 is a fully open-source tendon-driven humanoid hand with wrist and finger abduction/adduction, buildable for a low materials cost relative to commercial dexterous hands.

Sources:
- [RUKA-v2 project page](https://ruka-hand-v2.github.io/)
- [RUKA-v2 arXiv](https://arxiv.org/abs/2603.26660)

Course impact:
- Add accessible dexterous hardware to the open-source humanoid lab.
- Teach tendon-driven actuation, calibration, tactile/force needs, and maintenance.

### VLA evaluation is becoming a real open discipline

The AllenAI vla-evaluation-harness provides a unified open framework for evaluating VLA models across simulation benchmarks. Its May 2026 release reports a large model-by-benchmark matrix and a monthly updated leaderboard.

Sources:
- [vla-evaluation-harness GitHub](https://github.com/allenai/vla-evaluation-harness)
- [VLA leaderboard](https://allenai.github.io/vla-evaluation-harness/leaderboard/)
- [vla-eval OpenReview](https://openreview.net/forum?id=IpKQsHWaYS)

Course impact:
- Teach evaluation harnesses, not just training.
- Add confidence intervals, reproducibility, Docker isolation, and benchmark mismatch warnings.

### Open simulation benchmarks are broadening

Important open simulation and benchmark systems now include:

- [ManiSkill](https://www.maniskill.ai/) for GPU-accelerated manipulation simulation and data generation.
- [RoboCasa365](https://arxiv.org/html/2603.04356v1) for 365 household mobile-manipulation tasks.
- [RoboTwin 2.0](https://robotwin-platform.github.io/) for scalable bimanual data generation and benchmarking.
- [Genesis World](https://genesis-world.readthedocs.io/) for open Pythonic physical-AI simulation.
- [LIBERO](https://libero-project.github.io/main.html) for lifelong robot learning.
- [CALVIN](https://calvin.cs.uni-freiburg.de/) for language-conditioned long-horizon manipulation.

Course impact:
- Add a simulator/benchmark selection notebook.
- Teach that benchmark score, real-robot transfer, and safety are separate questions.

### Reachy and the Hugging Face robot ecosystem matter for accessible embodied AI

Pollen Robotics / Hugging Face Reachy 2 and Reachy Mini are open-source humanoid/humanoid-adjacent robots with LeRobot ecosystem relevance.

Sources:
- [Pollen Robotics Reachy](https://www.pollen-robotics.com/reachy/)
- [Reachy 2 in LeRobot docs](https://huggingface.co/docs/lerobot/en/reachy2)
- [Pollen Robotics on Hugging Face](https://huggingface.co/pollen-robotics)

Course impact:
- Include Reachy 2/Mini in the open-source humanoid lab options.
- Treat desktop and bimanual platforms as practical stepping stones before full-size humanoids.

## Frontier Watchlist

These are promising but should be treated carefully until code, weights, hardware files, and reproduction reports are mature:

- [OpenEAI-Platform](https://arxiv.org/abs/2606.03392), a June 2026 open-source hardware/software platform proposal whose paper says code and designs will be released after acceptance.
- DexFuture-style hierarchical future-state targeting for bimanual tool use, which is a strong research direction but not yet a beginner implementation target.
- World-action models and robotics world models, which are increasingly important but still hard to evaluate on real robots.

## What This Repository Now Includes

The course now includes a new frontier notebook block:

- 46 Open-source robotics frontier radar
- 47 Open VLA models and action heads
- 48 Open benchmarks and evaluation harnesses
- 49 Open simulators and synthetic data
- 50 Open hardware, humanoids, and dexterity

These notebooks are not a substitute for installing the projects. They teach how to choose, evaluate, and safely approach the open-source tools.
