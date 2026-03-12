"""Binary Search Tree implementation.

A BST is a node-based binary tree where each node's left subtree contains
only nodes with data less than the node's data, and the right subtree
contains only nodes with data greater than the node's data.

Operations and complexities (n = number of nodes):
    - insert:    O(log n) average, O(n) worst case
    - search:    O(log n) average, O(n) worst case
    - size:      O(n)
    - preorder:  O(n)
    - inorder:   O(n)
    - postorder: O(n)
"""
from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BST:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def get_root(self) -> Optional[Node]:
        return self.root

    def size(self) -> int:
        """Return the number of nodes in the tree. Complexity: O(n)."""
        return self._recur_size(self.root)

    def _recur_size(self, root: Optional[Node]) -> int:
        if root is None:
            return 0
        return 1 + self._recur_size(root.left) + self._recur_size(root.right)

    def search(self, data: int) -> bool:
        """Return True if data exists in the tree. Complexity: O(log n) average."""
        return self._recur_search(self.root, data)

    def _recur_search(self, root: Optional[Node], data: int) -> bool:
        if root is None:
            return False
        if root.data == data:
            return True
        elif data > root.data:
            return self._recur_search(root.right, data)
        else:
            return self._recur_search(root.left, data)

    def insert(self, data: int) -> bool:
        """Insert data into the tree. Return False if data already exists. Complexity: O(log n) average."""
        if self.root:
            return self._recur_insert(self.root, data)
        else:
            self.root = Node(data)
            return True

    def _recur_insert(self, root: Node, data: int) -> bool:
        if root.data == data:
            return False
        elif data < root.data:
            if root.left:
                return self._recur_insert(root.left, data)
            else:
                root.left = Node(data)
                return True
        else:
            if root.right:
                return self._recur_insert(root.right, data)
            else:
                root.right = Node(data)
                return True

    def preorder(self, root: Optional[Node]) -> list[int]:
        """Return list of node values in preorder (root, left, right)."""
        result: list[int] = []
        if root:
            result.append(root.data)
            result.extend(self.preorder(root.left))
            result.extend(self.preorder(root.right))
        return result

    def inorder(self, root: Optional[Node]) -> list[int]:
        """Return list of node values in inorder (left, root, right)."""
        result: list[int] = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.data)
            result.extend(self.inorder(root.right))
        return result

    def postorder(self, root: Optional[Node]) -> list[int]:
        """Return list of node values in postorder (left, right, root)."""
        result: list[int] = []
        if root:
            result.extend(self.postorder(root.left))
            result.extend(self.postorder(root.right))
            result.append(root.data)
        return result
