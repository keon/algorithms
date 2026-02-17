"""
Path Sum II

Given a binary tree and a target sum, find all root-to-leaf paths where each
path's sum equals the given sum. Provides recursive, DFS, and BFS solutions.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def path_sum(root: TreeNode | None, sum: int) -> list[list[int]]:
    """Find all root-to-leaf paths with the given sum (recursive DFS).

    Args:
        root: The root of the binary tree.
        sum: The target sum.

    Returns:
        A list of paths, where each path is a list of node values.

    Examples:
        >>> path_sum(None, 0)
        []
    """
    if root is None:
        return []
    result: list[list[int]] = []
    _dfs(root, sum, [], result)
    return result


def _dfs(root: TreeNode, sum: int, path: list[int], result: list[list[int]]) -> None:
    """Recursively collect paths that sum to the target value.

    Args:
        root: The current node.
        sum: The remaining target sum.
        path: The path accumulated so far.
        result: The list accumulating valid paths.
    """
    if root.left is None and root.right is None and root.val == sum:
        path.append(root.val)
        result.append(path)
    if root.left is not None:
        _dfs(root.left, sum - root.val, path + [root.val], result)
    if root.right is not None:
        _dfs(root.right, sum - root.val, path + [root.val], result)


def path_sum2(root: TreeNode | None, target: int) -> list[list[int]]:
    """Find all root-to-leaf paths with the given sum (DFS with stack).

    Args:
        root: The root of the binary tree.
        target: The target sum.

    Returns:
        A list of paths, where each path is a list of node values.

    Examples:
        >>> path_sum2(None, 0)
        []
    """
    if root is None:
        return []
    result: list[list[int]] = []
    stack: list[tuple[TreeNode, list[int]]] = [(root, [root.val])]
    while stack:
        node, path = stack.pop()
        if node.left is None and node.right is None and sum(path) == target:
            result.append(path)
        if node.left is not None:
            stack.append((node.left, path + [node.left.val]))
        if node.right is not None:
            stack.append((node.right, path + [node.right.val]))
    return result


def path_sum3(root: TreeNode | None, sum: int) -> list[list[int]]:
    """Find all root-to-leaf paths with the given sum (BFS with queue).

    Args:
        root: The root of the binary tree.
        sum: The target sum.

    Returns:
        A list of paths, where each path is a list of node values.

    Examples:
        >>> path_sum3(None, 0)
        []
    """
    if root is None:
        return []
    result: list[list[int]] = []
    queue: list[tuple[TreeNode, int, list[int]]] = [(root, root.val, [root.val])]
    while queue:
        node, val, path = queue.pop(0)
        if node.left is None and node.right is None and val == sum:
            result.append(path)
        if node.left is not None:
            queue.append((node.left, val + node.left.val, path + [node.left.val]))
        if node.right is not None:
            queue.append((node.right, val + node.right.val, path + [node.right.val]))
    return result
