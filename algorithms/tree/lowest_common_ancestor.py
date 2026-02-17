"""
Lowest Common Ancestor

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes.
The LCA is the lowest node that has both nodes as descendants (a node can be a
descendant of itself).

Reference: https://en.wikipedia.org/wiki/Lowest_common_ancestor

Complexity:
    Time:  O(n)
    Space: O(n) due to recursion stack
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def lca(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """Find the lowest common ancestor of two nodes in a binary tree.

    Args:
        root: The root of the binary tree.
        p: The first target node.
        q: The second target node.

    Returns:
        The lowest common ancestor node, or None if not found.

    Examples:
        >>> node = TreeNode(1)
        >>> lca(node, node, node).val
        1
    """
    if root is None or root is p or root is q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left is not None and right is not None:
        return root
    return left if left else right
