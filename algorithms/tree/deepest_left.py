"""
Deepest Left Leaf

Given a binary tree, find the deepest node that is the left child of its
parent node.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(n)
    Space: O(n) due to recursion stack
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


class DeepestLeft:
    """Container to track the deepest left node found during traversal.

    Examples:
        >>> dl = DeepestLeft()
        >>> dl.depth
        0
    """

    def __init__(self) -> None:
        self.depth: int = 0
        self.Node: TreeNode | None = None


def find_deepest_left(root: TreeNode | None, is_left: bool,
                      depth: int, res: DeepestLeft) -> None:
    """Recursively find the deepest left child in a binary tree.

    Args:
        root: The current node being examined.
        is_left: Whether the current node is a left child.
        depth: The current depth in the tree.
        res: A DeepestLeft instance tracking the best result so far.

    Examples:
        >>> res = DeepestLeft()
        >>> find_deepest_left(None, True, 1, res)
    """
    if not root:
        return
    if is_left and depth > res.depth:
        res.depth = depth
        res.Node = root
    find_deepest_left(root.left, True, depth + 1, res)
    find_deepest_left(root.right, False, depth + 1, res)
