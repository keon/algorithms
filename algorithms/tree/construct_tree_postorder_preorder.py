"""
Construct Tree from Preorder and Postorder Traversal

Given preorder and postorder traversals of a full binary tree, construct the
tree and return its inorder traversal. A full binary tree has either zero or
two children per node.

Reference: https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees

Complexity:
    Time:  O(n^2) due to linear search in postorder array
    Space: O(n) for the constructed tree
"""

from __future__ import annotations


class TreeNode:
    """A node in a binary tree.

    Args:
        val: The value stored in this node.
        left: The left child node.
        right: The right child node.
    """

    def __init__(self, val: int, left: TreeNode | None = None,
                 right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


pre_index = 0


def construct_tree_util(pre: list[int], post: list[int],
                        low: int, high: int, size: int) -> TreeNode | None:
    """Recursively construct a binary tree from preorder and postorder arrays.

    Uses a global pre_index to track the current position in the preorder
    array during recursive construction.

    Args:
        pre: The preorder traversal array.
        post: The postorder traversal array.
        low: The lower bound index in the postorder array.
        high: The upper bound index in the postorder array.
        size: The total number of elements.

    Returns:
        The root of the constructed subtree, or None if bounds are invalid.

    Examples:
        >>> construct_tree_util([1, 2, 3], [2, 3, 1], 0, 2, 3) is not None
        True
    """
    global pre_index

    if pre_index == -1:
        pre_index = 0

    if pre_index >= size or low > high:
        return None

    root = TreeNode(pre[pre_index])
    pre_index += 1

    if low == high or pre_index >= size:
        return root

    i = low
    while i <= high:
        if pre[pre_index] == post[i]:
            break
        i += 1

    if i <= high:
        root.left = construct_tree_util(pre, post, low, i, size)
        root.right = construct_tree_util(pre, post, i + 1, high, size)

    return root


def construct_tree(pre: list[int], post: list[int], size: int) -> list[int]:
    """Construct a full binary tree and return its inorder traversal.

    Args:
        pre: The preorder traversal array.
        post: The postorder traversal array.
        size: The number of elements.

    Returns:
        A list of values representing the inorder traversal of the
        constructed tree.

    Examples:
        >>> construct_tree([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1], 7)
        [4, 2, 5, 1, 6, 3, 7]
    """
    root = construct_tree_util(pre, post, 0, size - 1, size)
    return _inorder(root)


def _inorder(root: TreeNode | None, result: list[int] | None = None) -> list[int]:
    """Return the inorder traversal of a binary tree.

    Args:
        root: The root of the tree to traverse.
        result: Accumulator list for the traversal values.

    Returns:
        A list of node values in inorder sequence.
    """
    if root is None:
        return []
    if result is None:
        result = []

    _inorder(root.left, result)
    result.append(root.val)
    _inorder(root.right, result)
    return result
