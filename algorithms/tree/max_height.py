"""
Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth. The maximum depth is the number
of nodes along the longest path from the root down to the farthest leaf.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def max_height(root: TreeNode | None) -> int:
    """Compute the maximum depth of a binary tree using iterative BFS.

    Args:
        root: The root of the binary tree.

    Returns:
        The maximum depth (number of levels) of the tree.

    Examples:
        >>> max_height(None)
        0
    """
    if root is None:
        return 0
    height = 0
    queue: list[TreeNode] = [root]
    while queue:
        height += 1
        level: list[TreeNode] = []
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                level.append(node.left)
            if node.right is not None:
                level.append(node.right)
        queue = level
    return height
