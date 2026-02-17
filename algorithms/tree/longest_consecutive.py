"""
Longest Consecutive Sequence in Binary Tree

Given a binary tree, find the length of the longest consecutive sequence path
from parent to child (values increasing by one).

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(n)
    Space: O(n) due to recursion stack
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def longest_consecutive(root: TreeNode | None) -> int:
    """Find the length of the longest parent-to-child consecutive sequence.

    Args:
        root: The root of the binary tree.

    Returns:
        The length of the longest consecutive sequence path.

    Examples:
        >>> longest_consecutive(None)
        0
    """
    if root is None:
        return 0
    max_len = 0
    _dfs(root, 0, root.val, max_len)
    return max_len


def _dfs(root: TreeNode | None, current: int, target: int, max_len: int) -> None:
    """Recursively search for the longest consecutive sequence.

    Args:
        root: The current node being visited.
        current: The current consecutive sequence length.
        target: The expected value for the current node to continue the sequence.
        max_len: The maximum sequence length found so far.
    """
    if root is None:
        return
    if root.val == target:
        current += 1
    else:
        current = 1
    max_len = max(current, max_len)
    _dfs(root.left, current, root.val + 1, max_len)
    _dfs(root.right, current, root.val + 1, max_len)
