"""
Design a data structure that supports all following operations
in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements.
Each element must have the same probability of being returned.
"""


import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.idxs = {}

    def insert(self, val):
        if val not in self.idxs:
            self.nums.append(val)
            self.idxs[val] = len(self.nums)-1
            return True
        return False

    def remove(self, val):
        if val in self.idxs:
            idx, last = self.idxs[val], self.nums[-1]
            self.nums[idx], self.idxs[last] = last, idx
            self.nums.pop()
            self.idxs.pop(val, 0)
            return True
        return False

    def get_random(self):
        idx = random.randint(0, len(self.nums)-1)
        return self.nums[idx]


if __name__ == "__main__":
    rs = RandomizedSet()
    print("insert 1: ", rs.insert(1))
    print("insert 2: ", rs.insert(2))
    print("insert 3: ", rs.insert(3))
    print("insert 4: ", rs.insert(4))
    print("remove 3: ", rs.remove(3))
    print("remove 3: ", rs.remove(3))
    print("remove 1: ", rs.remove(1))
    print("random: ", rs.get_random())
    print("random: ", rs.get_random())
    print("random: ", rs.get_random())
    print("random: ", rs.get_random())
