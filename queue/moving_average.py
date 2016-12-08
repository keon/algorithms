
class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = collections.deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.queue.popleft()
        sum = float(0)
        for num in self.queue:
            sum += num
        return sum / len(self.queue)

# Given a stream of integers and a window size,
# calculate the moving average of all integers in the sliding window.

# For example,
m = MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
