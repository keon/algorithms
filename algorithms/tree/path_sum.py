"""
Path Sum

Given a binary tree and a target sum, determine if the tree has a root-to-leaf
path such that adding up all values along the path equals the given sum.
Provides recursive, DFS, and BFS solutions.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def has_path_sum(root: TreeNode | None, sum: int) -> bool:
    """Check if a root-to-leaf path with the given sum exists (recursive).

    Args:
        root: The root of the binary tree.
        sum: The target sum.

    Returns:
        True if such a path exists, False otherwise.

    Examples:
        >>> has_path_sum(None, 0)
        False
    """
    if root is None:
        return False
    if root.left is None and root.right is None and root.val == sum:
        return True
    sum -= root.val
    return has_path_sum(root.left, sum) or has_path_sum(root.right, sum)


def has_path_sum2(root: TreeNode | None, sum: int) -> bool:
    """Check if a root-to-leaf path with the given sum exists (DFS with stack).

    Args:
        root: The root of the binary tree.
        sum: The target sum.

    Returns:
        True if such a path exists, False otherwise.

    Examples:
        >>> has_path_sum2(None, 0)
        False
    """
    if root is None:
        return False
    stack: list[tuple[TreeNode, int]] = [(root, root.val)]
    while stack:
        node, val = stack.pop()
        if node.left is None and node.right is None:
            if val == sum:
                return True
        if node.left is not None:
            stack.append((node.left, val + node.left.val))
        if node.right is not None:
            stack.append((node.right, val + node.right.val))
    return False


def has_path_sum3(root: TreeNode | None, sum: int) -> bool:
    """Check if a root-to-leaf path with the given sum exists (BFS with queue).

    Args:
        root: The root of the binary tree.
        sum: The target sum.

    Returns:
        True if such a path exists, False otherwise.

    Examples:
        >>> has_path_sum3(None, 0)
        False
    """
    if root is None:
        return False
    queue: list[tuple[TreeNode, int]] = [(root, sum - root.val)]
    while queue:
        node, val = queue.pop(0)
        if node.left is None and node.right is None:
            if val == 0:
                return True
        if node.left is not None:
            queue.append((node.left, val - node.left.val))
        if node.right is not None:
            queue.append((node.right, val - node.right.val))
    return False
