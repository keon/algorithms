"""
Given two binary trees, write a function to check
if they are equal or not.

Two binary trees are considered equal if they are
structurally identical and the nodes have the same value.
"""


def is_same_tree(tree_p, tree_q):
    if tree_p is None and tree_q is None:
        return True
    if tree_p is not None and tree_q is not None and tree_p.val == tree_q.val:
        return is_same_tree(tree_p.left, tree_q.left) and is_same_tree(tree_p.right, tree_q.right)
    return False

# Time Complexity O(min(N,M))
# where N and M are the number of nodes for the trees.

# Space Complexity O(min(height1, height2))
# levels of recursion is the mininum height between the two trees.
