from __future__ import annotations

import numpy as np


def wrap_angle(theta: float | np.ndarray) -> float | np.ndarray:
    return np.arctan2(np.sin(theta), np.cos(theta))


def rot2(theta: float) -> np.ndarray:
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=float)


def transform2(theta: float, tx: float, ty: float) -> np.ndarray:
    transform = np.eye(3)
    transform[:2, :2] = rot2(theta)
    transform[:2, 2] = [tx, ty]
    return transform


def compose_transform2(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b


def apply_transform2(transform: np.ndarray, points_xy: np.ndarray) -> np.ndarray:
    points = np.asarray(points_xy, dtype=float)
    single_point = points.ndim == 1
    points = np.atleast_2d(points)
    homogeneous = np.c_[points, np.ones(len(points))]
    result = (transform @ homogeneous.T).T[:, :2]
    return result[0] if single_point else result


def quaternion_from_axis_angle(axis: np.ndarray, angle: float) -> np.ndarray:
    axis = np.asarray(axis, dtype=float)
    norm = np.linalg.norm(axis)
    if norm == 0:
        raise ValueError("axis must be nonzero")
    axis = axis / norm
    half = 0.5 * angle
    return np.r_[np.cos(half), axis * np.sin(half)]


def quaternion_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    aw, ax, ay, az = np.asarray(a, dtype=float)
    bw, bx, by, bz = np.asarray(b, dtype=float)
    return np.array(
        [
            aw * bw - ax * bx - ay * by - az * bz,
            aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw,
        ],
        dtype=float,
    )
