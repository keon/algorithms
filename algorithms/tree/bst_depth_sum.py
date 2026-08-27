r"""Write a function depthSum returns the sum of the values stored
in a binary search tree of integers weighted by the depth of each value.

For example:

                    9
                 /      \
               6         12
              / \\       /   \
            3     8   10      15
                 /              \
                7                18

    depth_sum = 1*9 + 2*(6+12) + 3*(3+8+10+15) + 4*(7+18)

"""

import unittest

from algorithms.data_structures.bst import BST


def depth_sum(root, n):
    if root:
        return recur_depth_sum(root, 1)
    return None


def recur_depth_sum(root, n):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data * n
    return (
        n * root.data
        + recur_depth_sum(root.left, n + 1)
        + recur_depth_sum(root.right, n + 1)
    )


"""
    The tree is created for testing:

                    9
                 /      \
               6         12
              / \\       /   \
            3     8   10      15
                 /              \
                7                18

    depth_sum = 1*9 + 2*(6+12) + 3*(3+8+10+15) + 4*(7+18)

"""


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST()
        self.tree.insert(9)
        self.tree.insert(6)
        self.tree.insert(12)
        self.tree.insert(3)
        self.tree.insert(8)
        self.tree.insert(10)
        self.tree.insert(15)
        self.tree.insert(7)
        self.tree.insert(18)

    def test_depth_sum(self) -> None:
        assert depth_sum(self.tree.root, 4) == 253


if __name__ == "__main__":
    unittest.main()
