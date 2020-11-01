from algorithms.tree import construct_tree_postorder_preorder
import unittest

class TestDemo(unittest.TestCase):
    def test_demo(self):

        # Test 1
        construct_tree_postorder_preorder.preIndex = 0
        pre1 = [1, 2, 4, 8, 9, 5, 3, 6, 7]
        post1 = [8, 9, 4, 5, 2, 6, 7, 3, 1]
        size1 = len(pre1)

        self.assertEqual(construct_tree_postorder_preorder.constructTree(pre1, post1, size1), [8,4,9,2,5,1,6,3,7])

        # Test 2
        construct_tree_postorder_preorder.preIndex = 0
        pre2 = [1, 2, 4, 5, 3, 6, 7]
        post2 = [4, 5, 2, 6, 7, 3, 1]
        size2 = len(pre2)

        self.assertEqual(construct_tree_postorder_preorder.constructTree(pre2, post2, size2), [4,2,5,1,6,3,7])

        # Test 3
        construct_tree_postorder_preorder.preIndex = 0
        pre3 = [12, 7, 16, 21, 5, 1, 9]
        post3 = [16, 21, 7, 1, 9, 5, 12]
        size3 = len(pre3)

        self.assertEqual(construct_tree_postorder_preorder.constructTree(pre3, post3, size3), [16,7,21,12,1,5,9])


if __name__ == "__main__":
    unittest.main()
