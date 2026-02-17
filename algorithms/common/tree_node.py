"""Binary tree node shared across all tree algorithms.

This module provides the universal TreeNode used by every tree algorithm
in this library. Using a single shared type means you can compose
algorithms freely: build a BST, invert it, then traverse it.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    """A node in a binary tree.

    Attributes:
        val: The value stored in this node.
        left: Reference to the left child.
        right: Reference to the right child.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> root.left.val
        2
        >>> root.right.val
        3
    """

    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None
