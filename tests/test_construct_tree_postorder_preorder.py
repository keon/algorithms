from algorithms.tree import construct_tree_postorder_preorder
import unittest

class TestDemo(unittest.TestCase):
    def test_demo(self):
        pre = [1, 2, 4, 8, 9, 5, 3, 6, 7]
        post = [8, 9, 4, 5, 2, 6, 7, 3, 1]
        size = len(pre)

        self.assertEqual(demo.constructTree(pre, post, size), [8,4,9,2,5,1,6,3,7])

        pre = [1,2,4,5,3,6,7]
        post = [4,5,2,6,7,3,1]
        size = len(pre)

        self.assertEqual(demo.constructTree(pre, post, size), [4,2,5,1,6,3,7])

        pre = [12,7,16,21,5,1,9]
        post = [16,21,7,1,9,5,12]
        size = len(pre)

        self.assertEqual(demo.constructTree(pre, post, size), [16,7,21,12,1,5,9])


if __name__ == "__main__":
    unittest.main()
