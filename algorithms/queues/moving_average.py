from __future__ import division
from collections import deque


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)


# Given a stream of integers and a window size,
# calculate the moving average of all integers in the sliding window.
if __name__ == '__main__':
    m = MovingAverage(3)
    assert m.next(1) == 1
    assert m.next(10) == (1 + 10) / 2
    assert m.next(3) == (1 + 10 + 3) / 3
    assert m.next(5) == (10 + 3 + 5) / 3
