from __future__ import annotations

import numpy as np


def lipm_step(
    com_position: float,
    com_velocity: float,
    zmp: float,
    height: float = 0.8,
    gravity: float = 9.81,
    dt: float = 0.01,
) -> tuple[float, float]:
    """One linear inverted-pendulum step in a single horizontal axis."""
    omega_sq = gravity / height
    acceleration = omega_sq * (com_position - zmp)
    com_velocity = com_velocity + acceleration * dt
    com_position = com_position + com_velocity * dt
    return float(com_position), float(com_velocity)


def capture_point(com_position: float, com_velocity: float, height: float = 0.8, gravity: float = 9.81) -> float:
    """Instantaneous capture point for the linear inverted pendulum model."""
    omega = np.sqrt(gravity / height)
    return float(com_position + com_velocity / omega)


def footstep_sequence(step_length: float, step_width: float, count: int) -> np.ndarray:
    """Alternating left/right footsteps in the ground plane."""
    steps = []
    for i in range(count):
        x = (i + 1) * step_length
        y = step_width * (1 if i % 2 == 0 else -1)
        steps.append((x, y))
    return np.array(steps, dtype=float)


def support_polygon_margin(point_xy: np.ndarray, polygon_xy: np.ndarray) -> float:
    """Signed margin for a convex polygon with counterclockwise vertices.

    Positive means the point is inside all half-spaces. Negative means outside.
    """
    point = np.asarray(point_xy, dtype=float)
    polygon = np.asarray(polygon_xy, dtype=float)
    margins = []
    for i in range(len(polygon)):
        a = polygon[i]
        b = polygon[(i + 1) % len(polygon)]
        edge = b - a
        inward_normal = np.array([-edge[1], edge[0]])
        inward_normal = inward_normal / (np.linalg.norm(inward_normal) + 1e-12)
        margins.append(float((point - a) @ inward_normal))
    return min(margins)


def retarget_joint_angles(
    human_angles: np.ndarray,
    human_limits: np.ndarray,
    robot_limits: np.ndarray,
) -> np.ndarray:
    """Map human joint angles into robot joint limits by normalized range position."""
    human_angles = np.asarray(human_angles, dtype=float)
    human_limits = np.asarray(human_limits, dtype=float)
    robot_limits = np.asarray(robot_limits, dtype=float)
    human_low, human_high = human_limits[:, 0], human_limits[:, 1]
    robot_low, robot_high = robot_limits[:, 0], robot_limits[:, 1]
    alpha = (human_angles - human_low) / (human_high - human_low + 1e-12)
    alpha = np.clip(alpha, 0.0, 1.0)
    return robot_low + alpha * (robot_high - robot_low)


def actuator_power(torque_nm: np.ndarray, velocity_rad_s: np.ndarray) -> np.ndarray:
    torque_nm = np.asarray(torque_nm, dtype=float)
    velocity_rad_s = np.asarray(velocity_rad_s, dtype=float)
    return torque_nm * velocity_rad_s
