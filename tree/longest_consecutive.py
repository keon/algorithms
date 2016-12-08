# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to any node
# in the tree along the parent-child connections.
# The longest consecutive path need to be from parent to child
# (cannot be the reverse).

# For example,
   # 1
    # \
     # 3
    # / \
   # 2   4
        # \
         # 5
# Longest consecutive sequence path is 3-4-5, so return 3.
   # 2
    # \
     # 3
    # /
   # 2
  # /
 # 1


maxlen = 0
def longestConsecutive(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    DFS(root, 0, root.val)
    return maxlen

def DFS(root, cur, target):
    if not root: return
    if root.val == target:
        cur += 1
    else:
        cur = 1
    maxlen = max(cur, maxlen)
    DFS(root.left, cur, root.val+1)
    DFS(root.right, cur, root.val+1)
