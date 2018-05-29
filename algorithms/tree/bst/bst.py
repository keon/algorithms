"""
Implement Binary Search Tree. It has method:
    1. Insert
    2. Search
    3. Size
    4. Traversal (Preorder, Inorder, Postorder)
"""

import unittest

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    """
        Get the number of elements
        Using recursion. Complexity O(logN)
    """
    def size(self):
        return self.recur_size(self.root)

    def recur_size(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.recur_size(root.left) + self.recur_size(root.right)

    """
        Search data in bst
        Using recursion. Complexity O(logN)
    """
    def search(self, data):
        return self.recur_search(self.root, data)

    def recur_search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        elif data > root.data:     # Go to right root
            return self.recur_search(root.right, data)
        else:                      # Go to left root
            return self.recur_search(root.left, data)

    """
        Insert data in bst
        Using recursion. Complexity O(logN)
    """
    def insert(self, data):
        if self.root:
            return self.recur_insert(self.root, data)
        else:
            self.root = Node(data)
            return True

    def recur_insert(self, root, data):
        if root.data == data:      # The data is already there
            return False
        elif data < root.data:     # Go to left root
            if root.left:          # If left root is a node
                return self.recur_insert(root.left, data)
            else:                  # left root is a None
                root.left = Node(data)
                return True
        else:                      # Go to right root
            if root.right:         # If right root is a node
                return self.recur_insert(root.right, data)
            else:
                root.right = Node(data)
                return True

    """
        Preorder, Postorder, Inorder traversal bst
    """
    def preorder(self, root):
        if root:
            print(str(root.data), end = ' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(str(root.data), end = ' ')
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.data), end = ' ')

"""
    The tree is created for testing:

                    10
                 /      \
               6         15
              / \       /   \
            4     9   12      24
                 /          /    \
                7         20      30
                         /
                       18
"""

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        self.tree.insert(10)
        self.tree.insert(15)
        self.tree.insert(6)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(12)
        self.tree.insert(24)
        self.tree.insert(7)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(18)

    def test_search(self):
        self.assertTrue(self.tree.search(24))
        self.assertFalse(self.tree.search(50))

    def test_size(self):
        self.assertEqual(11, self.tree.size())

if __name__ == '__main__':
    unittest.main()
