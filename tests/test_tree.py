from tree.bst.array2bst import array2bst
from tree.bst.count_left_node import count_left_node
from tree.bst.bst_closest_value import closest_value
from tree.bst.depth_sum import depth_sum
from tree.bst.height import height
from tree.bst.is_bst import is_bst
from tree.bst.kth_smallest import Solution
from tree.bst.bst import BST, Node
import unittest


class TestBST(unittest.TestCase):

    def setUp(self):
        self.bst = create_bst_tree()

    def test_array2bst(self):
        array = range(1, 6)
        bst = array2bst(array)
        self.assertTrue(is_balanced(bst))
        self.assertEqual(bst.val, 3)

    def test_bst(self):
        # search
        self.assertTrue(self.bst.search(24))
        self.assertFalse(self.bst.search(50))
        # size
        self.assertEqual(11, self.bst.size())

    def test_closest_value(self):
        self.assertEqual(closest_value(self.bst.get_root(), 121.), 30)
        self.assertEqual(closest_value(self.bst.get_root(), 1.), 4)
        self.assertIn(closest_value(self.bst.get_root(), 22.), [24, 20])

    def test_count_left_node(self):
        # [6, 4, 7, 12, 20, 18]
        self.assertEqual(6, count_left_node(self.bst.get_root()))

    def test_delete_note(self):
        pass
        # solution = Solution()
        # Todo: delete_node should not be in master branch
        # self.bst = solution.delete_node(self.bst.root, 18)
        # self.assertFalse(self.bst.search(18))

    def test_depth_sum(self):
        # 10 + (6+15)*2 + (4+9+12+24)*3 + (7+20+30)*4 + (18*5) = 517
        self.assertEqual(517, depth_sum(self.bst.get_root()))

    def test_height(self):
        self.assertEqual(5, height(self.bst.get_root()))

    def test_is_bst(self):
        self.assertTrue(is_bst(self.bst.get_root()))

    def test_kth_smallest(self):
        solution = Solution()
        self.assertEqual(solution.kth_smallest(self.bst.get_root(), 5), 10)
        self.assertNotEqual(solution.kth_smallest(self.bst.get_root(), 1), 10)


def create_bst_tree():
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

    tree = BST()
    tree.insert(10)
    tree.insert(15)
    tree.insert(6)
    tree.insert(4)
    tree.insert(9)
    tree.insert(12)
    tree.insert(24)
    tree.insert(7)
    tree.insert(20)
    tree.insert(30)
    tree.insert(18)
    return tree




def is_balanced(tree):
    """"
       To check if a tree is height-balanced, get the height of left and right subtrees.
       Return true if difference between heights is not more than 1 and left and right subtrees are balanced, otherwise return false.
    """
    if tree.val:
        return abs(get_height(tree.left) - get_height(tree.right)) < 2


def get_height(tree):
    if not tree:
        return 0
    return 1 + get_height(tree.left) + get_height(tree.right)



if __name__ == '__name__':
    unittest.main()