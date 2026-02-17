"""
Binary Tree Node

Defines the base TreeNode class used across tree algorithms.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(1) for node creation
    Space: O(1) per node
"""

from __future__ import annotations


class TreeNode:
    """A node in a binary tree.

    Args:
        val: The value stored in this node.

    Examples:
        >>> node = TreeNode(5)
        >>> node.val
        5
    """

    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
