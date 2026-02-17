"""
Binary Tree Views

Compute different "views" of a binary tree — the nodes visible when looking
at the tree from a particular direction.

- **Left view**: first node at each level (leftmost).
- **Right view**: last node at each level (rightmost).
- **Top view**: nodes visible when looking from above.
- **Bottom view**: nodes visible when looking from below (last node at each
  horizontal distance).

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity (all views):
    Time:  O(n)  — each node is visited once
    Space: O(n)  — queue / dict storage
"""

from __future__ import annotations

from collections import deque

from algorithms.common.tree_node import TreeNode


def left_view(root: TreeNode | None) -> list[int]:
    """Return the values visible from the left side of the tree.

    Args:
        root: Root of the binary tree.

    Returns:
        List of node values, one per level, from the left.

    Examples:
        >>> from algorithms.common.tree_node import TreeNode
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        >>> left_view(root)
        [1, 2, 4]
    """
    if root is None:
        return []
    result: list[int] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


def right_view(root: TreeNode | None) -> list[int]:
    """Return the values visible from the right side of the tree.

    Args:
        root: Root of the binary tree.

    Returns:
        List of node values, one per level, from the right.

    Examples:
        >>> from algorithms.common.tree_node import TreeNode
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        >>> right_view(root)
        [1, 3, 4]
    """
    if root is None:
        return []
    result: list[int] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


def top_view(root: TreeNode | None) -> list[int]:
    """Return the values visible when looking at the tree from above.

    Nodes are ordered by horizontal distance from root (left to right).

    Args:
        root: Root of the binary tree.

    Returns:
        List of node values visible from the top.

    Examples:
        >>> from algorithms.common.tree_node import TreeNode
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
        ...                    TreeNode(3, None, TreeNode(6)))
        >>> top_view(root)
        [4, 2, 1, 3, 6]
    """
    if root is None:
        return []
    # Map: horizontal distance -> first node value seen (BFS ensures top-most)
    hd_map: dict[int, int] = {}
    queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])
    while queue:
        node, hd = queue.popleft()
        if hd not in hd_map:
            hd_map[hd] = node.val
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    return [hd_map[k] for k in sorted(hd_map)]


def bottom_view(root: TreeNode | None) -> list[int]:
    """Return the values visible when looking at the tree from below.

    Nodes are ordered by horizontal distance from root (left to right).
    When multiple nodes share the same horizontal distance, the last one
    encountered in level-order (bottommost) wins.

    Args:
        root: Root of the binary tree.

    Returns:
        List of node values visible from the bottom.

    Examples:
        >>> from algorithms.common.tree_node import TreeNode
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
        ...                    TreeNode(3, None, TreeNode(6)))
        >>> bottom_view(root)
        [4, 2, 5, 3, 6]
    """
    if root is None:
        return []
    hd_map: dict[int, int] = {}
    queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])
    while queue:
        node, hd = queue.popleft()
        hd_map[hd] = node.val  # overwrite → keeps bottommost
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    return [hd_map[k] for k in sorted(hd_map)]
