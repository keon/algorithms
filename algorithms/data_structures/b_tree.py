"""
B-Tree

A self-balancing tree data structure optimized for disk operations. Each node
(except root) contains at least t-1 keys and at most 2t-1 keys, where t is the
minimum degree. The tree grows upward from the root.

Reference: https://en.wikipedia.org/wiki/B-tree

Complexity:
    Time:  O(log n) for search, insert, and delete
    Space: O(n)
"""

from __future__ import annotations


class Node:
    """A node in a B-tree containing keys and child pointers.

    Examples:
        >>> node = Node()
        >>> node.keys
        []
    """

    def __init__(self) -> None:
        self.keys: list = []
        self.children: list[Node] = []

    def __repr__(self) -> str:
        """Return a string representation of the node.

        Returns:
            A string showing the node's keys.
        """
        return f"<id_node: {self.keys}>"

    @property
    def is_leaf(self) -> bool:
        """Check whether this node is a leaf.

        Returns:
            True if the node has no children, False otherwise.
        """
        return len(self.children) == 0


class BTree:
    """A B-tree data structure supporting search, insertion, and deletion.

    Args:
        t_val: The minimum degree of the B-tree.

    Examples:
        >>> bt = BTree(2)
        >>> bt.insert_key(10)
        >>> bt.find(10)
        True
    """

    def __init__(self, t_val: int = 2) -> None:
        self.min_numbers_of_keys = t_val - 1
        self.max_number_of_keys = 2 * t_val - 1
        self.root = Node()

    def _split_child(self, parent: Node, child_index: int) -> None:
        """Split a full child node into two nodes.

        Args:
            parent: The parent node whose child is being split.
            child_index: The index of the child to split.
        """
        new_right_child = Node()
        half_max = self.max_number_of_keys // 2
        child = parent.children[child_index]
        middle_key = child.keys[half_max]
        new_right_child.keys = child.keys[half_max + 1 :]
        child.keys = child.keys[:half_max]

        if not child.is_leaf:
            new_right_child.children = child.children[half_max + 1 :]
            child.children = child.children[: half_max + 1]

        parent.keys.insert(child_index, middle_key)
        parent.children.insert(child_index + 1, new_right_child)

    def insert_key(self, key: int) -> None:
        """Insert a key into the B-tree.

        Args:
            key: The key to insert.
        """
        if len(self.root.keys) >= self.max_number_of_keys:
            new_root = Node()
            new_root.children.append(self.root)
            self.root = new_root
            self._split_child(new_root, 0)
            self._insert_to_nonfull_node(self.root, key)
        else:
            self._insert_to_nonfull_node(self.root, key)

    def _insert_to_nonfull_node(self, node: Node, key: int) -> None:
        """Insert a key into a non-full node.

        Args:
            node: The non-full node to insert into.
            key: The key to insert.
        """
        i = len(node.keys) - 1
        while i >= 0 and node.keys[i] >= key:
            i -= 1

        if node.is_leaf:
            node.keys.insert(i + 1, key)
        else:
            if len(node.children[i + 1].keys) >= self.max_number_of_keys:
                self._split_child(node, i + 1)
                if node.keys[i + 1] < key:
                    i += 1
            self._insert_to_nonfull_node(node.children[i + 1], key)

    def find(self, key: int) -> bool:
        """Search for a key in the B-tree.

        Args:
            key: The key to search for.

        Returns:
            True if the key is found, False otherwise.

        Examples:
            >>> bt = BTree(2)
            >>> bt.insert_key(5)
            >>> bt.find(5)
            True
            >>> bt.find(3)
            False
        """
        current_node = self.root
        while True:
            i = len(current_node.keys) - 1
            while i >= 0 and current_node.keys[i] > key:
                i -= 1
            if i >= 0 and current_node.keys[i] == key:
                return True
            if current_node.is_leaf:
                return False
            current_node = current_node.children[i + 1]

    def remove_key(self, key: int) -> None:
        """Remove a key from the B-tree.

        Args:
            key: The key to remove.
        """
        self._remove_key(self.root, key)

    def _remove_key(self, node: Node, key: int) -> bool:
        """Recursively remove a key from the subtree rooted at node.

        Args:
            node: The root of the subtree to remove from.
            key: The key to remove.

        Returns:
            True if the key was found and removed, False otherwise.
        """
        try:
            key_index = node.keys.index(key)
            if node.is_leaf:
                node.keys.remove(key)
            else:
                self._remove_from_nonleaf_node(node, key_index)
            return True

        except ValueError:
            if node.is_leaf:
                return False
            else:
                i = 0
                number_of_keys = len(node.keys)
                while i < number_of_keys and key > node.keys[i]:
                    i += 1

                action_performed = self._repair_tree(node, i)
                if action_performed:
                    return self._remove_key(node, key)
                else:
                    return self._remove_key(node.children[i], key)

    def _repair_tree(self, node: Node, child_index: int) -> bool:
        """Repair the tree after a deletion to maintain B-tree properties.

        Args:
            node: The parent node of the child that may need repair.
            child_index: The index of the child to check.

        Returns:
            True if a structural repair was performed, False otherwise.
        """
        child = node.children[child_index]
        if self.min_numbers_of_keys < len(child.keys) <= self.max_number_of_keys:
            return False

        if (
            child_index > 0
            and len(node.children[child_index - 1].keys) > self.min_numbers_of_keys
        ):
            self._rotate_right(node, child_index)
            return True

        if (
            child_index < len(node.children) - 1
            and len(node.children[child_index + 1].keys) > self.min_numbers_of_keys
        ):
            self._rotate_left(node, child_index)
            return True

        if child_index > 0:
            self._merge(node, child_index - 1, child_index)
        else:
            self._merge(node, child_index, child_index + 1)

        return True

    def _rotate_left(self, parent_node: Node, child_index: int) -> None:
        """Take a key from the right sibling and transfer it to the child.

        Args:
            parent_node: The parent node.
            child_index: The index of the child receiving the key.
        """
        new_child_key = parent_node.keys[child_index]
        new_parent_key = parent_node.children[child_index + 1].keys.pop(0)
        parent_node.children[child_index].keys.append(new_child_key)
        parent_node.keys[child_index] = new_parent_key

        if not parent_node.children[child_index + 1].is_leaf:
            ownerless_child = parent_node.children[child_index + 1].children.pop(0)
            parent_node.children[child_index].children.append(ownerless_child)

    def _rotate_right(self, parent_node: Node, child_index: int) -> None:
        """Take a key from the left sibling and transfer it to the child.

        Args:
            parent_node: The parent node.
            child_index: The index of the child receiving the key.
        """
        parent_key = parent_node.keys[child_index - 1]
        new_parent_key = parent_node.children[child_index - 1].keys.pop()
        parent_node.children[child_index].keys.insert(0, parent_key)
        parent_node.keys[child_index - 1] = new_parent_key

        if not parent_node.children[child_index - 1].is_leaf:
            ownerless_child = parent_node.children[child_index - 1].children.pop()
            parent_node.children[child_index].children.insert(0, ownerless_child)

    def _merge(
        self, parent_node: Node, to_merge_index: int, transferred_child_index: int
    ) -> None:
        """Merge two child nodes and a parent key into a single node.

        Args:
            parent_node: The parent node.
            to_merge_index: Index of the child that receives the merged data.
            transferred_child_index: Index of the child being merged in.
        """
        from_merge_node = parent_node.children.pop(transferred_child_index)
        parent_key_to_merge = parent_node.keys.pop(to_merge_index)
        to_merge_node = parent_node.children[to_merge_index]
        to_merge_node.keys.append(parent_key_to_merge)
        to_merge_node.keys.extend(from_merge_node.keys)

        if not to_merge_node.is_leaf:
            to_merge_node.children.extend(from_merge_node.children)

        if parent_node == self.root and not parent_node.keys:
            self.root = to_merge_node

    def _remove_from_nonleaf_node(
        self, node: Node, key_index: int
    ) -> None:
        """Remove a key from a non-leaf node by replacing with predecessor/successor.

        Args:
            node: The non-leaf node containing the key.
            key_index: The index of the key to remove.
        """
        key = node.keys[key_index]
        left_subtree = node.children[key_index]
        if len(left_subtree.keys) > self.min_numbers_of_keys:
            largest_key = self._find_largest_and_delete_in_left_subtree(left_subtree)
        elif len(node.children[key_index + 1].keys) > self.min_numbers_of_keys:
            largest_key = self._find_largest_and_delete_in_right_subtree(
                node.children[key_index + 1]
            )
        else:
            self._merge(node, key_index, key_index + 1)
            return self._remove_key(node, key)

        node.keys[key_index] = largest_key

    def _find_largest_and_delete_in_left_subtree(self, node: Node) -> int:
        """Find and remove the largest key in the left subtree.

        Args:
            node: The root of the subtree.

        Returns:
            The largest key that was removed.
        """
        if node.is_leaf:
            return node.keys.pop()
        else:
            ch_index = len(node.children) - 1
            self._repair_tree(node, ch_index)
            largest_key_in_subtree = self._find_largest_and_delete_in_left_subtree(
                node.children[len(node.children) - 1]
            )
            return largest_key_in_subtree

    def _find_largest_and_delete_in_right_subtree(self, node: Node) -> int:
        """Find and remove the smallest key in the right subtree.

        Args:
            node: The root of the subtree.

        Returns:
            The smallest key that was removed.
        """
        if node.is_leaf:
            return node.keys.pop(0)
        else:
            ch_index = 0
            self._repair_tree(node, ch_index)
            largest_key_in_subtree = self._find_largest_and_delete_in_right_subtree(
                node.children[0]
            )
            return largest_key_in_subtree

    def traverse_tree(self) -> list:
        """Traverse the B-tree in order and return all keys.

        Returns:
            A list of all keys in sorted order.

        Examples:
            >>> bt = BTree(2)
            >>> for k in [3, 1, 2]: bt.insert_key(k)
            >>> bt.traverse_tree()
            [1, 2, 3]
        """
        result: list = []
        self._traverse_tree(self.root, result)
        return result

    def _traverse_tree(self, node: Node, result: list) -> None:
        """Recursively traverse the subtree and collect keys.

        Args:
            node: The root of the subtree to traverse.
            result: The list to append keys to.
        """
        if node.is_leaf:
            result.extend(node.keys)
        else:
            for i, key in enumerate(node.keys):
                self._traverse_tree(node.children[i], result)
                result.append(key)
            self._traverse_tree(node.children[-1], result)
