"""
Subtree Check

Given two binary trees s and t, check whether t is a subtree of s. A subtree
of s is a tree consisting of a node in s and all of its descendants.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(m * n) where m and n are sizes of the two trees
    Space: O(m) due to BFS queue
"""

from __future__ import annotations

import collections

from algorithms.tree.tree import TreeNode


def is_subtree(big: TreeNode, small: TreeNode) -> bool:
    """Check whether the small tree is a subtree of the big tree.

    Args:
        big: The root of the larger tree.
        small: The root of the potential subtree.

    Returns:
        True if small is a subtree of big, False otherwise.

    Examples:
        >>> node = TreeNode(1)
        >>> is_subtree(node, node)
        True
    """
    flag = False
    queue: collections.deque[TreeNode] = collections.deque()
    queue.append(big)
    while queue:
        node = queue.popleft()
        if node.val == small.val:
            flag = _comp(node, small)
            break
        else:
            queue.append(node.left)
            queue.append(node.right)
    return flag


def _comp(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Recursively compare two trees for structural and value equality.

    Args:
        p: A node from the first tree.
        q: A node from the second tree.

    Returns:
        True if both subtrees are identical, False otherwise.
    """
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        return p.val == q.val and _comp(p.left, q.left) and _comp(p.right, q.right)
    return False
