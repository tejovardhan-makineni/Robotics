from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .geometry import wrap_angle
from .safety import limit_norm


@dataclass
class PID:
    kp: float
    ki: float = 0.0
    kd: float = 0.0
    output_limit: float | None = None
    integral: float = 0.0
    previous_error: float | None = None

    def reset(self) -> None:
        self.integral = 0.0
        self.previous_error = None

    def step(self, error: float, dt: float) -> float:
        self.integral += error * dt
        derivative = 0.0 if self.previous_error is None else (error - self.previous_error) / dt
        self.previous_error = error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        if self.output_limit is not None:
            output = float(np.clip(output, -self.output_limit, self.output_limit))
        return output


def dlqr(a: np.ndarray, b: np.ndarray, q: np.ndarray, r: np.ndarray, iterations: int = 100) -> np.ndarray:
    """Discrete-time LQR gain by Riccati iteration."""
    p = q.copy()
    for _ in range(iterations):
        bt_p = b.T @ p
        gain = np.linalg.solve(r + bt_p @ b, bt_p @ a)
        p = q + a.T @ p @ (a - b @ gain)
    return gain


def pure_pursuit_control(
    pose: np.ndarray,
    waypoint: np.ndarray,
    lookahead: float = 0.8,
    speed: float = 0.6,
) -> tuple[float, float]:
    x, y, theta = pose
    dx, dy = waypoint[0] - x, waypoint[1] - y
    distance = max(np.hypot(dx, dy), 1e-6)
    alpha = wrap_angle(np.arctan2(dy, dx) - theta)
    curvature = 2.0 * np.sin(alpha) / max(lookahead, distance)
    return speed, float(speed * curvature)


def resolved_rate_step(
    q: np.ndarray,
    target_xy: np.ndarray,
    fk,
    jacobian,
    gain: float = 1.0,
    max_step: float = 0.08,
    damping: float = 1e-3,
) -> np.ndarray:
    _, current = fk(q)
    error = target_xy - current
    j = jacobian(q)
    jj_t = j @ j.T
    dq = j.T @ np.linalg.solve(jj_t + damping * np.eye(2), gain * error)
    return q + limit_norm(dq, max_step)
