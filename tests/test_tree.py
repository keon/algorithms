from algorithms.tree.traversal import (
    preorder,
    preorder_rec,
    postorder,
    postorder_rec,
    inorder,
    inorder_rec
)
from algorithms.tree.b_tree import BTree

from algorithms.tree import construct_tree_postorder_preorder as ctpp

from algorithms.tree.fenwick_tree.fenwick_tree import Fenwick_Tree

from algorithms.tree.red_black_tree.red_black_tree import RBNode, RBTree

import unittest


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestTraversal(unittest.TestCase):

    def test_preorder(self):
        tree = create_tree()
        self.assertEqual([100, 50, 25, 75, 150, 125, 175], preorder(tree))
        self.assertEqual([100, 50, 25, 75, 150, 125, 175], preorder_rec(tree))

    def test_postorder(self):
        tree = create_tree()
        self.assertEqual([25, 75, 50, 125, 175, 150, 100], postorder(tree))
        self.assertEqual([25, 75, 50, 125, 175, 150, 100], postorder_rec(tree))

    def test_inorder(self):
        tree = create_tree()
        self.assertEqual([25, 50, 75, 100, 125, 150, 175], inorder(tree))
        self.assertEqual([25, 50, 75, 100, 125, 150, 175], inorder_rec(tree))


def create_tree():
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
    return n1


class TestBTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        import random
        random.seed(18719)
        cls.random = random
        cls.range = 10000

    def setUp(self):
        self.keys_to_insert = [self.random.randrange(-self.range, self.range)
                               for i in range(self.range)]

    def test_insertion_and_find_even_degree(self):
        btree = BTree(4)
        for i in self.keys_to_insert:
            btree.insert_key(i)

        for i in range(100):
            key = self.random.choice(self.keys_to_insert)
            self.assertTrue(btree.find(key))

    def test_insertion_and_find_odd_degree(self):
        btree = BTree(3)
        for i in self.keys_to_insert:
            btree.insert_key(i)

        for i in range(100):
            key = self.random.choice(self.keys_to_insert)
            self.assertTrue(btree.find(key))

    def test_deletion_even_degree(self):
        btree = BTree(4)
        key_list = set(self.keys_to_insert)
        for i in key_list:
            btree.insert_key(i)

        for key in key_list:
            btree.remove_key(key)
            self.assertFalse(btree.find(key))

        self.assertEqual(btree.root.keys, [])
        self.assertEqual(btree.root.children, [])

    def test_deletion_odd_degree(self):
        btree = BTree(3)
        key_list = set(self.keys_to_insert)
        for i in key_list:
            btree.insert_key(i)

        for key in key_list:
            btree.remove_key(key)
            self.assertFalse(btree.find(key))

        self.assertEqual(btree.root.keys, [])
        self.assertEqual(btree.root.children, [])


class TestConstructTreePreorderPostorder(unittest.TestCase):
    def test_construct_tree(self):

        # Test 1
        ctpp.pre_index = 0
        pre1 = [1, 2, 4, 8, 9, 5, 3, 6, 7]
        post1 = [8, 9, 4, 5, 2, 6, 7, 3, 1]
        size1 = len(pre1)

        self.assertEqual(ctpp.construct_tree(pre1, post1, size1),
                         [8, 4, 9, 2, 5, 1, 6, 3, 7])

        # Test 2
        ctpp.pre_index = 0
        pre2 = [1, 2, 4, 5, 3, 6, 7]
        post2 = [4, 5, 2, 6, 7, 3, 1]
        size2 = len(pre2)

        self.assertEqual(ctpp.construct_tree(pre2, post2, size2),
                         [4, 2, 5, 1, 6, 3, 7])

        # Test 3
        ctpp.pre_index = 0
        pre3 = [12, 7, 16, 21, 5, 1, 9]
        post3 = [16, 21, 7, 1, 9, 5, 12]
        size3 = len(pre3)

        self.assertEqual(ctpp.construct_tree(pre3, post3, size3),
                         [16, 7, 21, 12, 1, 5, 9])


class TestFenwickTree(unittest.TestCase):
    def test_construct_tree_with_update_1(self):
        freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
        ft = Fenwick_Tree(freq)
        bit_tree = ft.construct()
        self.assertEqual(12, ft.get_sum(bit_tree, 5))

        freq[3] += 6
        ft.update_bit(bit_tree, 3, 6)
        self.assertEqual(18, ft.get_sum(bit_tree, 5))

    def test_construct_tree_with_update_2(self):
        freq = [1, 2, 3, 4, 5]
        ft = Fenwick_Tree(freq)
        bit_tree = ft.construct()
        self.assertEqual(10, ft.get_sum(bit_tree, 3))

        freq[3] -= 5
        ft.update_bit(bit_tree, 3, -5)
        self.assertEqual(5, ft.get_sum(bit_tree, 3))

    def test_construct_tree_with_update_3(self):
        freq = [2, 1, 4, 6, -1, 5, -32, 0, 1]
        ft = Fenwick_Tree(freq)
        bit_tree = ft.construct()
        self.assertEqual(12, ft.get_sum(bit_tree, 4))

        freq[2] += 11
        ft.update_bit(bit_tree, 2, 11)
        self.assertEqual(23, ft.get_sum(bit_tree, 4))


class TestRBTree(unittest.TestCase):
    def _initialize_tree(self):
        tree = RBTree()
        tree.insert(RBNode(val=9))
        tree.insert(RBNode(val=18))
        tree.insert(RBNode(val=7))
        return tree

    def test_insertion(self):
        node_1 = RBNode(val=9)
        node_2 = RBNode(val=18)
        node_3 = RBNode(val=7)

        # First insertion
        tree = RBTree()
        tree.insert(node_1)
        self.assertIs(tree.root, node_1)

        self.assertIsNone(node_1.parent)
        self.assertIsNone(node_1.left)
        self.assertIsNone(node_1.right)
        self.assertEqual(node_1.color, 0)

        # Second insertion
        tree.insert(node_2)

        self.assertIsNone(node_1.parent)
        self.assertIsNone(node_1.left)
        self.assertIs(node_1.right, node_2)
        self.assertEqual(node_1.color, 0)

        self.assertIs(node_2.parent, node_1)
        self.assertIsNone(node_2.left)
        self.assertIsNone(node_2.right)
        self.assertEqual(node_2.color, 1)

        # Third insertion
        tree.insert(node_3)

        self.assertIsNone(node_1.parent)
        self.assertIs(node_1.left, node_3)
        self.assertIs(node_1.right, node_2)
        self.assertEqual(node_1.color, 0)

        self.assertIs(node_2.parent, node_1)
        self.assertIsNone(node_2.left)
        self.assertIsNone(node_2.right)
        self.assertEqual(node_2.color, 1)

        self.assertIs(node_3.parent, node_1)
        self.assertIsNone(node_3.left)
        self.assertIsNone(node_3.right)
        self.assertEqual(node_3.color, 1)

    def test_deletion(self):
        tree = self._initialize_tree()

        # First deletion
        tree.delete(tree.root)

        self.assertIsNone(tree.root.parent)
        self.assertIsNotNone(tree.root.left)
        self.assertIsNone(tree.root.right)
        self.assertEqual(tree.root.color, 0)
        self.assertEqual(tree.root.val, 18)

        self.assertIs(tree.root.left.parent, tree.root)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertEqual(tree.root.left.color, 1)
        self.assertEqual(tree.root.left.val, 7)

        # Second deletion
        tree.delete(tree.root)

        self.assertIsNone(tree.root.parent)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)
        self.assertEqual(tree.root.color, 0)
        self.assertEqual(tree.root.val, 7)

        # Third deletion
        tree.delete(tree.root)

        self.assertIsNone(tree.root)

    def test_find_maximum(self):
        tree = self._initialize_tree()
        node = tree.maximum(tree.root)
        self.assertEqual(node.val, 18)

    def test_find_minimum(self):
        tree = self._initialize_tree()
        node = tree.minimum(tree.root)
        self.assertEqual(node.val, 7)

    def test_inorder(self):
        tree = self._initialize_tree()
        self.assertEqual(tree.inorder(), [
            {"color": 1, "val": 7},
            {"color": 0, "val": 9},
            {"color": 1, "val": 18},
        ])


if __name__ == '__main__':
    unittest.main()
