"""
Same Tree

Given two binary trees, check if they are structurally identical and the
nodes have the same values.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(min(n, m)) where n and m are sizes of the trees
    Space: O(min(h1, h2)) where h1 and h2 are the heights
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def is_same_tree(tree_p: TreeNode | None, tree_q: TreeNode | None) -> bool:
    """Check whether two binary trees are identical.

    Args:
        tree_p: The root of the first binary tree.
        tree_q: The root of the second binary tree.

    Returns:
        True if both trees are structurally identical with equal node
        values, False otherwise.

    Examples:
        >>> is_same_tree(None, None)
        True
    """
    if tree_p is None and tree_q is None:
        return True
    if tree_p is not None and tree_q is not None and tree_p.val == tree_q.val:
        return is_same_tree(tree_p.left, tree_q.left) and is_same_tree(
            tree_p.right, tree_q.right
        )
    return False
