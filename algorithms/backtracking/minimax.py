"""Minimax — game-tree search with alpha-beta pruning.

The minimax algorithm finds the optimal move for a two-player zero-sum
game. Alpha-beta pruning reduces the search space by eliminating branches
that cannot influence the final decision.

Inspired by PR #860 (DD2480-group16).
"""

from __future__ import annotations

import math


def minimax(
    depth: int,
    is_maximizing: bool,
    scores: list[int],
    alpha: float = -math.inf,
    beta: float = math.inf,
) -> float:
    """Return the minimax value of a perfect binary game tree.

    *scores* contains the leaf values (length must be a power of 2).
    *depth* is the current depth (start with log2(len(scores))).

    >>> minimax(2, True, [3, 5, 2, 9])
    5
    >>> minimax(3, True, [3, 5, 2, 9, 12, 5, 23, 23])
    12
    """
    if depth == 0:
        return scores[0]
    mid = len(scores) // 2
    if is_maximizing:
        value = -math.inf
        value = max(
            value,
            minimax(depth - 1, False, scores[:mid], alpha, beta),
        )
        alpha = max(alpha, value)
        if alpha < beta:
            value = max(
                value,
                minimax(depth - 1, False, scores[mid:], alpha, beta),
            )
        return value
    else:
        value = math.inf
        value = min(
            value,
            minimax(depth - 1, True, scores[:mid], alpha, beta),
        )
        beta = min(beta, value)
        if alpha < beta:
            value = min(
                value,
                minimax(depth - 1, True, scores[mid:], alpha, beta),
            )
        return value
