#! /usr/bin/env python3

"""
Design a data structure that supports all following operations
in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
random_element: Returns a random element from current set of elements.
           Each element must have the same probability of being returned.
"""

import random


class RandomizedSet():
    """
    idea: shoot
    """

    def __init__(self):
        self.elements = []
        self.index_map = {}  # element -> index

    def insert(self, new_one):
        if new_one in self.index_map:
            return
        self.index_map[new_one] = len(self.elements)
        self.elements.append(new_one)

    def remove(self, old_one):
        if not old_one in self.index_map:
            return
        index = self.index_map[old_one]
        last = self.elements.pop()
        self.index_map.pop(old_one)
        if index == len(self.elements):
            return
        self.elements[index] = last
        self.index_map[last] = index

    def random_element(self):
        return random.choice(self.elements)


def __test():
    rset = RandomizedSet()
    ground_truth = set()
    n = 64

    for i in range(n):
        rset.insert(i)
        ground_truth.add(i)

    # Remove a half
    for i in random.sample(range(n), n // 2):
        rset.remove(i)
        ground_truth.remove(i)

    print(len(ground_truth), len(rset.elements), len(rset.index_map))
    for i in ground_truth:
        assert(i == rset.elements[rset.index_map[i]])

    for i in range(n):
        print(rset.random_element(), end=' ')
    print()


if __name__ == "__main__":
    __test()
