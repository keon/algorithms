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
    _, maximum = _helper(root)
    return maximum


def _helper(root: TreeNode | None) -> tuple[float, float]:
    """Compute the best branch and overall path sums below ``root``.

    Args:
        root: The current node.
    Returns:
        A tuple containing the best downward branch and the best complete
        path found in the subtree.
    """
    if root is None:
        return 0, float("-inf")

    left_branch, left_maximum = _helper(root.left)
    right_branch, right_maximum = _helper(root.right)
    branch = root.val + max(0, left_branch, right_branch)
    through_root = root.val + max(0, left_branch) + max(0, right_branch)
    maximum = max(through_root, left_maximum, right_maximum)
    return branch, maximum
