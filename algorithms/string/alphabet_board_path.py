"""Alphabet board path — find moves on a 5x5+1 letter board.

Given a board where 'a'-'z' are laid out in rows of 5:
    a b c d e
    f g h i j
    k l m n o
    p q r s t
    u v w x y
    z

Return the sequence of moves (U/D/L/R/!) to spell a target word
starting from 'a'.

Inspired by PR #897 (chnttx).
"""

from __future__ import annotations


def alphabet_board_path(target: str) -> str:
    """Return move string to spell *target* on the alphabet board."""
    moves: list[str] = []
    row, col = 0, 0
    for ch in target:
        idx = ord(ch) - ord("a")
        target_row, target_col = divmod(idx, 5)
        # Move up/left before down/right to avoid going off-board at 'z'
        if target_row < row:
            moves.append("U" * (row - target_row))
        if target_col < col:
            moves.append("L" * (col - target_col))
        if target_row > row:
            moves.append("D" * (target_row - row))
        if target_col > col:
            moves.append("R" * (target_col - col))
        moves.append("!")
        row, col = target_row, target_col
    return "".join(moves)
