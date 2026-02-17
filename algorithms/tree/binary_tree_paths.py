"""
Binary Tree Paths

Given a binary tree, return all root-to-leaf paths as a list of strings
in the format "root->...->leaf".

Reference: https://en.wikipedia.org/wiki/Binary_tree#Combinatorics

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def binary_tree_paths(root: TreeNode | None) -> list[str]:
    """Return all root-to-leaf paths in the binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        A list of strings representing each root-to-leaf path.

    Examples:
        >>> binary_tree_paths(None)
        []
    """
    result: list[str] = []
    if root is None:
        return result
    _dfs(result, root, str(root.val))
    return result


def _dfs(result: list[str], root: TreeNode, current: str) -> None:
    """Perform depth-first search to collect all root-to-leaf paths.

    Args:
        result: The list accumulating path strings.
        root: The current node being visited.
        current: The path string built so far.
    """
    if root.left is None and root.right is None:
        result.append(current)
    if root.left:
        _dfs(result, root.left, current + '->' + str(root.left.val))
    if root.right:
        _dfs(result, root.right, current + '->' + str(root.right.val))
