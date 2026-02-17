"""
Write a function num_empty returns returns the number of empty branches in a
tree. Function should count the total number of empty branches among the nodes
of the tree. A leaf node has two empty branches. In the case, if root is None,
it considered as a 1 empty branch
For example: the following tree has 10 empty branch (* is empty branch)

                    9 __
                 /      \___
               6            12
              / \          /   \
            3     8       10      15
          /  \   / \     /  \    /   \
         *    * 7   *   *    *  *    18
               / \                   /  \
              *   *                 *    *

    empty_branch = 10

"""
import unittest
from bst import Node
from bst import bst

def num_empty(root):
    if root is None:
        return 1
    elif root.left is None and root.right:
        return 1 + num_empty(root.right)
    elif root.right is None and root.left:
        return 1 + num_empty(root.left)
    else:
        return num_empty(root.left) + num_empty(root.right)

"""
    The tree is created for testing:

                    9
                 /      \
               6         12
              / \       /   \
            3     8   10      15
                 /              \
                7                18

    num_empty = 10

"""

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.tree = bst()
        self.tree.insert(9)
        self.tree.insert(6)
        self.tree.insert(12)
        self.tree.insert(3)
        self.tree.insert(8)
        self.tree.insert(10)
        self.tree.insert(15)
        self.tree.insert(7)
        self.tree.insert(18)

    def test_num_empty(self):
        self.assertEqual(10, num_empty(self.tree.root))

if __name__ == '__main__':
    unittest.main()
