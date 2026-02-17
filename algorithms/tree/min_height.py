"""
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth. The minimum depth is the number
of nodes along the shortest path from the root down to the nearest leaf.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def min_depth(self: object, root: TreeNode | None) -> int:
    """Compute the minimum depth of a binary tree using recursion.

    Args:
        self: Unused parameter (kept for backward compatibility).
        root: The root of the binary tree.

    Returns:
        The minimum depth of the tree.
    """
    if root is None:
        return 0
    if root.left is not None or root.right is not None:
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


def min_height(root: TreeNode | None) -> int:
    """Compute the minimum depth of a binary tree using iterative BFS.

    Args:
        root: The root of the binary tree.

    Returns:
        The minimum depth (number of levels to nearest leaf) of the tree.

    Examples:
        >>> min_height(None)
        0
    """
    if root is None:
        return 0
    height = 0
    level: list[TreeNode] = [root]
    while level:
        height += 1
        new_level: list[TreeNode] = []
        for node in level:
            if node.left is None and node.right is None:
                return height
            if node.left is not None:
                new_level.append(node.left)
            if node.right is not None:
                new_level.append(node.right)
        level = new_level
    return height
