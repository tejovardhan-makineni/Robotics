from __future__ import annotations

import numpy as np


def kalman_1d_update(
    mean: float,
    variance: float,
    control_delta: float,
    measurement: float,
    process_variance: float,
    measurement_variance: float,
) -> tuple[float, float, float]:
    predicted_mean = mean + control_delta
    predicted_variance = variance + process_variance
    gain = predicted_variance / (predicted_variance + measurement_variance)
    updated_mean = predicted_mean + gain * (measurement - predicted_mean)
    updated_variance = (1.0 - gain) * predicted_variance
    return float(updated_mean), float(updated_variance), float(gain)


def systematic_resample(weights: np.ndarray, rng: np.random.Generator | None = None) -> np.ndarray:
    rng = np.random.default_rng() if rng is None else rng
    weights = np.asarray(weights, dtype=float)
    weights = weights / weights.sum()
    n = len(weights)
    positions = (rng.random() + np.arange(n)) / n
    indexes = np.zeros(n, dtype=int)
    cumulative_sum = np.cumsum(weights)
    i = j = 0
    while i < n:
        if positions[i] < cumulative_sum[j]:
            indexes[i] = j
            i += 1
        else:
            j += 1
    return indexes
