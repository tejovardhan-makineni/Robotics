from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from robotics_mastery import (  # noqa: E402
    PID,
    apply_transform2,
    astar_grid,
    dlqr,
    kalman_1d_update,
    quaternion_from_axis_angle,
    quaternion_multiply,
    transform2,
    velocity_obstacle_safe,
)


def test_geometry():
    transform = transform2(np.pi / 2, 1.0, 2.0)
    point = apply_transform2(transform, np.array([1.0, 0.0]))
    assert np.allclose(point, [1.0, 3.0])


def test_quaternion_identity():
    q = quaternion_from_axis_angle(np.array([0.0, 0.0, 1.0]), 0.0)
    r = quaternion_from_axis_angle(np.array([1.0, 0.0, 0.0]), 0.0)
    assert np.allclose(quaternion_multiply(q, r), [1.0, 0.0, 0.0, 0.0])


def test_planning_and_control():
    grid = np.zeros((4, 4), dtype=int)
    grid[1, 1] = 1
    path = astar_grid(grid, (0, 0), (3, 3))
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)

    controller = PID(kp=2.0, output_limit=1.0)
    assert controller.step(error=10.0, dt=0.1) == 1.0

    a = np.array([[1.0, 1.0], [0.0, 1.0]])
    b = np.array([[0.0], [1.0]])
    gain = dlqr(a, b, np.eye(2), np.array([[0.1]]))
    assert gain.shape == (1, 2)


def test_estimation_and_safety():
    mean, variance, gain = kalman_1d_update(0, 1, 1, 1.2, 0.1, 0.2)
    assert 1.0 < mean < 1.2
    assert 0.0 < variance < 1.0
    assert 0.0 < gain < 1.0

    assert velocity_obstacle_safe(np.array([5.0, 0.0]), np.array([1.0, 0.0]), 1.0, 2.0)
    assert not velocity_obstacle_safe(np.array([1.0, 0.0]), np.array([-1.0, 0.0]), 0.5, 2.0)


if __name__ == "__main__":
    test_geometry()
    test_quaternion_identity()
    test_planning_and_control()
    test_estimation_and_safety()
    print("core tests passed")
