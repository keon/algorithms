class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def kth_smallest(root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        helper(root, count)
        return count[k-1]

def helper(node, count):
        if not node:
            return

        helper(node.left, count)
        count.append(node.val)
        helper(node.right, count)


