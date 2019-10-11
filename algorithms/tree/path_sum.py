"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf
path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


def has_path_sum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root is None:
        return False
    if root.left is None and root.right is None and root.val == sum:
        return True
    sum -= root.val
    return has_path_sum(root.left, sum) or has_path_sum(root.right, sum)


# DFS with stack
def has_path_sum2(root, sum):
    if root is None:
        return False
    stack = [(root, root.val)]
    while stack:
        node, val = stack.pop()
        if node.left is None and node.right is None:
            if val == sum:
                return True
        if node.left is not None:
            stack.append((node.left, val+node.left.val))
        if node.right is not None:
            stack.append((node.right, val+node.right.val))
    return False


# BFS with queue
def has_path_sum3(root, sum):
    if root is None:
        return False
    queue = [(root, sum-root.val)]
    while queue:
        node, val = queue.pop(0)  # popleft
        if node.left is None and node.right is None:
            if val == 0:
                return True
        if node.left is not None:
            queue.append((node.left, val-node.left.val))
        if node.right is not None:
            queue.append((node.right, val-node.right.val))
    return False
