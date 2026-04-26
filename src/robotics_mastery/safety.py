from __future__ import annotations

import numpy as np


def limit_norm(vector: np.ndarray, max_norm: float) -> np.ndarray:
    vector = np.asarray(vector, dtype=float)
    norm = np.linalg.norm(vector)
    if norm <= max_norm or norm == 0:
        return vector.copy()
    return vector * (max_norm / norm)


def velocity_obstacle_safe(
    relative_position: np.ndarray,
    relative_velocity: np.ndarray,
    combined_radius: float,
    horizon: float,
) -> bool:
    """Return False if current relative velocity may collide within horizon."""
    p = np.asarray(relative_position, dtype=float)
    v = np.asarray(relative_velocity, dtype=float)
    vv = float(v @ v)
    if vv < 1e-12:
        return np.linalg.norm(p) > combined_radius
    t_star = float(np.clip(-(p @ v) / vv, 0.0, horizon))
    closest = p + t_star * v
    return bool(np.linalg.norm(closest) > combined_radius)
