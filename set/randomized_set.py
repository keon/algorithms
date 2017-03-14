"""
Design a data structure that supports all following operations
in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
get_random: Returns a random element from current set of elements.
           Each element must have the same probability of being returned.
"""


class RandomizedSet():
    """
    idea:
        shit
    """
    def __init__(self):
        pass

    def insert(self, val):
        pass

    def remove(self, val):
        pass

    def get_random(self):
        pass


if __name__ == "__main__":
    rset = RandomizedSet()
    rset.insert(1)
    rset.insert(2)
    rset.insert(3)

    rset.remove(2)

    print(rset.get_random())
    print(rset.get_random())
    print(rset.get_random())
