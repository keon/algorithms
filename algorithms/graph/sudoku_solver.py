"""
Sudoku Solver (DFS / Backtracking)

Solves a Sudoku puzzle using constraint propagation and depth-first search
with backtracking, starting from the cell with the fewest possible values.

Reference: https://leetcode.com/problems/sudoku-solver/

Complexity:
    Time:  O(9^(empty cells)) worst case
    Space: O(N^2)
"""

from __future__ import annotations


class Sudoku:
    """A Sudoku board solver."""

    def __init__(
        self,
        board: list[list[str]],
        row: int,
        col: int,
    ) -> None:
        """Initialise the solver with the given board.

        Args:
            board: 2D list of digits or '.' for empty cells.
            row: Number of rows.
            col: Number of columns.
        """
        self.board = board
        self.row = row
        self.col = col
        self.val = self._possible_values()

    def _possible_values(self) -> dict[tuple[int, int], list[str]]:
        """Compute possible values for each empty cell.

        Returns:
            Mapping from (row, col) to list of candidate digits.
        """
        a = "123456789"
        d: dict[tuple[str, int] | tuple[int, int], list[str]] = {}
        val: dict[tuple[int, int], list[str]] = {}
        for i in range(self.row):
            for j in range(self.col):
                ele = self.board[i][j]
                if ele != ".":
                    d[("r", i)] = d.get(("r", i), []) + [ele]
                    d[("c", j)] = d.get(("c", j), []) + [ele]
                    d[(i // 3, j // 3)] = d.get((i // 3, j // 3), []) + [ele]
                else:
                    val[(i, j)] = []
        for i, j in val.keys():
            inval = (
                d.get(("r", i), [])
                + d.get(("c", j), [])
                + d.get((i / 3, j / 3), [])
            )
            val[(i, j)] = [n for n in a if n not in inval]
        return val

    def solve(self) -> bool:
        """Attempt to solve the board in place.

        Returns:
            True if a solution was found.
        """
        if len(self.val) == 0:
            return True
        kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
        nums = self.val[kee]
        for n in nums:
            update: dict[tuple[int, int], str | list[str]] = {kee: self.val[kee]}
            if self._valid_one(n, kee, update):
                if self.solve():
                    return True
            self._undo(kee, update)
        return False

    def _valid_one(
        self,
        n: str,
        kee: tuple[int, int],
        update: dict[tuple[int, int], str | list[str]],
    ) -> bool:
        """Place digit *n* at *kee* and propagate constraints.

        Args:
            n: Digit to place.
            kee: (row, col) coordinate.
            update: Undo log (modified in place).

        Returns:
            True if placement is valid.
        """
        self.board[kee[0]][kee[1]] = n
        del self.val[kee]
        i, j = kee
        for ind in list(self.val.keys()):
            if n in self.val[ind]:
                if (
                    ind[0] == i
                    or ind[1] == j
                    or (ind[0] / 3, ind[1] / 3) == (i / 3, j / 3)
                ):
                    update[ind] = n
                    self.val[ind].remove(n)
                    if len(self.val[ind]) == 0:
                        return False
        return True

    def _undo(
        self,
        kee: tuple[int, int],
        update: dict[tuple[int, int], str | list[str]],
    ) -> None:
        """Revert the placement at *kee* using *update*.

        Args:
            kee: (row, col) coordinate.
            update: Undo log.
        """
        self.board[kee[0]][kee[1]] = "."
        for k in update:
            if k not in self.val:
                self.val[k] = update[k]
            else:
                self.val[k].append(update[k])

    def __str__(self) -> str:
        """Return a string representation of the board.

        Returns:
            Formatted board string.
        """
        resp = ""
        for i in range(self.row):
            for j in range(self.col):
                resp += f" {self.board[i][j]} "
            resp += "\n"
        return resp
