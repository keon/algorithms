from algorithms.tree.traversal import (
    preorder,
    preorder_rec,
    postorder,
    postorder_rec
)

import unittest

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class TestTraversal(unittest.TestCase):
    
    def test_preorder(self):
        n1 = Node(100)
        n2 = Node(50)
        n3 = Node(150)
        n4 = Node(25)
        n5 = Node(75)
        n6 = Node(125)
        n7 = Node(175)
        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, n5
        n3.left, n3.right = n6, n7
        self.assertEqual([100, 50, 25, 75, 150, 125, 175], preorder(n1))
        self.assertEqual([100, 50, 25, 75, 150, 125, 175], preorder_rec(n1))
        
    def test_postorder(self):
        n1 = Node(100)
        n2 = Node(50)
        n3 = Node(150)
        n4 = Node(25)
        n5 = Node(75)
        n6 = Node(125)
        n7 = Node(175)
        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, n5
        n3.left, n3.right = n6, n7
        self.assertEqual([25, 75, 50, 125, 175, 150, 100], postorder(n1))
        self.assertEqual([25, 75, 50, 125, 175, 150, 100], postorder_rec(n1))
