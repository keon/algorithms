import unittest
from algorithms.tree import binary_tree_from_preorder_postorder as btpp

class TestbinaryTreeFromPreorderPostorder(unittest.TestCase):

    def test_constructTree(self):
        root = btpp.constructTree([1,2,4,5,3,6,8,9,7],[4,5,2,8,9,6,7,3,1],9,0)        
        self.assertEqual([4,2,5,1,8,6,9,3,7],btpp.inorder(root))

    def test_constructTree(self):
        root = btpp.constructTree([1,2,4,5,3,6,7],[4,5,2,6,7,3,1],7,0)
        self.assertEqual([4,2,5,1,6,3,7],btpp.inorder(root))

    def test_constructTree(self):
        root = btpp.constructTree([12,7,16,21,5,1,9],[16,21,7,1,9,5,12],7,0)
        self.assertEqual([16,7,21,12,1,5,9],btpp.inorder(root))


if __name__ == "__main__":
    unittest.main()
