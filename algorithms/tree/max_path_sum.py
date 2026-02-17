"""
Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum. A path is any sequence of nodes
from some starting node to any node in the tree along parent-child connections.
The path must contain at least one node.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(n)
    Space: O(n) due to recursion stack
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def max_path_sum(root: TreeNode | None) -> float:
    """Find the maximum path sum in a binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        The maximum sum of any path through the tree.

    Examples:
        >>> max_path_sum(TreeNode(1))
        1
    """
    maximum = float("-inf")
    _helper(root, maximum)
    return maximum


def _helper(root: TreeNode | None, maximum: float) -> float:
    """Recursively compute the maximum single-branch sum from each node.

    Args:
        root: The current node.
        maximum: The running maximum path sum.

    Returns:
        The maximum sum of a path extending from this node to a descendant.
    """
    if root is None:
        return 0
    left = _helper(root.left, maximum)
    right = _helper(root.right, maximum)
    maximum = max(maximum, left + right + root.val)
    return root.val + maximum
