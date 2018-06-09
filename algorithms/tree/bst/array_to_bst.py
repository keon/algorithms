"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums)//2
    node = TreeNode(nums[mid])
    node.left = array_to_bst(nums[:mid])
    node.right = array_to_bst(nums[mid+1:])
    return node
