"""
Moving Average from Data Stream

Calculate the moving average of integers in a sliding window of fixed
size using a bounded deque.

Reference: https://leetcode.com/problems/moving-average-from-data-stream/

Complexity:
    Time:  O(1) per call to next
    Space: O(size)
"""

from __future__ import annotations

from collections import deque


class MovingAverage:
    """Computes the moving average over a sliding window.

    Examples:
        >>> m = MovingAverage(3)
        >>> m.next(1)
        1.0
        >>> m.next(10)
        5.5
    """

    def __init__(self, size: int) -> None:
        """Initialize the moving average calculator.

        Args:
            size: The window size for the moving average.
        """
        self.queue: deque[int] = deque(maxlen=size)

    def next(self, val: int) -> float:
        """Add a value and return the current moving average.

        Args:
            val: The next integer in the data stream.

        Returns:
            The current moving average as a float.
        """
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)
