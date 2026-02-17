"""
Garage Parking Rearrangement

There is a parking lot with only one empty spot (represented by 0). Given the
initial and final states, find the minimum number of moves to rearrange the lot.
Each move swaps a car into the empty spot.

Reference: https://en.wikipedia.org/wiki/15_puzzle

Complexity:
    Time:  O(n^2) worst case
    Space: O(n) for storing the sequence
"""

from __future__ import annotations


def garage(initial: list[int], final: list[int]) -> tuple[int, list[list[int]]]:
    """Find the minimum swaps to rearrange a parking lot from initial to final state.

    Args:
        initial: Starting arrangement where 0 represents the empty spot.
        final: Desired arrangement where 0 represents the empty spot.

    Returns:
        A tuple of (number_of_steps, sequence_of_states) showing each
        intermediate arrangement.

    Examples:
        >>> garage([1, 2, 3, 0, 4], [0, 3, 2, 1, 4])
        (4, [[0, 2, 3, 1, 4], [2, 0, 3, 1, 4], [2, 3, 0, 1, 4], [0, 3, 2, 1, 4]])
    """
    current = initial[::]
    sequence = []
    steps = 0

    while current != final:
        zero_pos = current.index(0)
        if zero_pos != final.index(0):
            target_car = final[zero_pos]
            target_pos = current.index(target_car)
            current[zero_pos], current[target_pos] = (
                current[target_pos],
                current[zero_pos],
            )
        else:
            for i in range(len(current)):
                if current[i] != final[i]:
                    current[zero_pos], current[i] = current[i], current[zero_pos]
                    break
        sequence.append(current[::])
        steps += 1

    return steps, sequence
