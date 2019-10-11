"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node
in the tree along the parent-child connections.
The longest consecutive path need to be from parent to child
(cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
"""


def longest_consecutive(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    max_len = 0
    dfs(root, 0, root.val, max_len)
    return max_len


def dfs(root, cur, target, max_len):
    if root is None:
        return
    if root.val == target:
        cur += 1
    else:
        cur = 1
    max_len = max(cur, max_len)
    dfs(root.left, cur, root.val+1, max_len)
    dfs(root.right, cur, root.val+1, max_len)
