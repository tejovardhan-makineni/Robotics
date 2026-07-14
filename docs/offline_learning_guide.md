# Offline Learning Guide

This repository is designed so the 50 core notebooks can run offline with the core Python environment.

## What Is Required Offline

Required for the notebook course:
- Python 3.12 or compatible Python 3
- NumPy
- Matplotlib
- nbformat
- JupyterLab or Notebook
- ipykernel

Optional advanced packages:
- PyTorch
- Gymnasium
- Stable-Baselines3
- LeRobot

The optional advanced packages are useful once you start reproducing external robot-learning stacks. They are not required for the 50 notebooks in this repository.

## Local Offline Bundle

Use `scripts/build_offline_bundle.py` while you still have internet access. It creates:

- `offline/wheels/core/`: pip wheels for the core notebook environment
- `offline/papers/`: selected open robotics papers as PDFs
- `offline/repos/`: ZIP snapshots of selected open-source robotics repositories
- `offline/logs/`: download logs and manifest

The bundle intentionally does not download large model weights, large datasets, Docker images, simulator assets, or robot vendor SDKs. Those can be hundreds of gigabytes and are better downloaded only when you choose a specific project.

## Install Offline From The Bundle

After the bundle exists, you can recreate the course environment without internet:

```bash
cd /Users/tejo/projects/robotics
python3 -m venv .venv
source .venv/bin/activate
pip install --no-index --find-links offline/wheels/core -r requirements.txt
jupyter lab
```

Then open notebooks 1 through 50 in order.

## Verify Offline Readiness

```bash
source .venv/bin/activate
python3 tests/test_core.py
MPLBACKEND=Agg python3 scripts/smoke_check_notebooks.py
```

If those pass, the course itself is ready for offline learning.

## What To Download Later For Specific Projects

Only download these after selecting a project:

- LeRobot model checkpoints and datasets
- OpenPI model checkpoints
- VLA benchmark datasets
- Isaac Lab or simulator assets
- ROS 2 binary packages and system dependencies
- Hardware SDKs for a specific robot

This keeps the offline bundle practical instead of turning it into a giant archive you may never use.
