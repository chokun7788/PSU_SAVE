"""Small, deterministic character-distance helper for bounded typo recovery."""

from __future__ import annotations


def osa_distance(observed: str, expected: str) -> int:
    """Edit distance allowing one adjacent transposition as a single edit."""
    left, right = str(observed or ""), str(expected or "")
    distances = [[0] * (len(right) + 1) for _ in range(len(left) + 1)]
    for row in range(len(left) + 1):
        distances[row][0] = row
    for column in range(len(right) + 1):
        distances[0][column] = column
    for row in range(1, len(left) + 1):
        for column in range(1, len(right) + 1):
            distances[row][column] = min(
                distances[row - 1][column] + 1,
                distances[row][column - 1] + 1,
                distances[row - 1][column - 1] + (left[row - 1] != right[column - 1]),
            )
            if (
                row > 1 and column > 1
                and left[row - 1] == right[column - 2]
                and left[row - 2] == right[column - 1]
            ):
                distances[row][column] = min(
                    distances[row][column], distances[row - 2][column - 2] + 1
                )
    return distances[-1][-1]
