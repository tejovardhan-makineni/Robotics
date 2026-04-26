from __future__ import annotations

import heapq
from collections.abc import Iterable

import numpy as np


GridCell = tuple[int, int]


def manhattan(a: GridCell, b: GridCell) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def grid_neighbors(grid: np.ndarray, cell: GridCell, diagonal: bool = False) -> Iterable[GridCell]:
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if diagonal:
        moves += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    rows, cols = grid.shape
    r, c = cell
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 0:
            yield (nr, nc)


def astar_grid(grid: np.ndarray, start: GridCell, goal: GridCell, diagonal: bool = False) -> list[GridCell]:
    frontier = [(0.0, start)]
    came_from: dict[GridCell, GridCell | None] = {start: None}
    cost_so_far = {start: 0.0}

    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            break

        for nxt in grid_neighbors(grid, current, diagonal=diagonal):
            step_cost = np.hypot(nxt[0] - current[0], nxt[1] - current[1])
            new_cost = cost_so_far[current] + step_cost
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost + manhattan(nxt, goal)
                heapq.heappush(frontier, (priority, nxt))
                came_from[nxt] = current

    if goal not in came_from:
        return []

    path = []
    current: GridCell | None = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    return path[::-1]
