"""
B-tree is used to disk operations. Each node (except root) contains
at least t-1 keys (t children) and at most 2*t - 1 keys (2*t children)
where t is the degree of b-tree. It is not a kind of typical bst tree, because
this tree grows up.
B-tree is balanced which means that the difference between height of left subtree and right subtree is at most 1.

Complexity
    n - number of elements
    t - degree of tree
    Tree always has height at most logt (n+1)/2
    Algorithm        Average        Worst case
    Space            O(n)           O(n)
    Search           O(log n)       O(log n)
    Insert           O(log n)       O(log n)
    Delete           O(log n)       O(log n)
"""


class Node:
    def __init__(self):
        # self.is_leaf = is_leaf
        self.keys = []
        self.children = []

    def __repr__(self):
        return "<id_node: {0}>".format(self.keys)

    @property
    def is_leaf(self):
        return len(self.children) == 0


class BTree:
    def __init__(self, t=2):
        self.min_numbers_of_keys = t - 1
        self.max_number_of_keys = 2 * t - 1

        self.root = Node()

    def _split_child(self, parent: Node, child_index: int):
        new_right_child = Node()
        half_max = self.max_number_of_keys // 2
        child = parent.children[child_index]
        middle_key = child.keys[half_max]
        new_right_child.keys = child.keys[half_max + 1:]
        child.keys = child.keys[:half_max]
        # child is left child of parent after splitting

        if not child.is_leaf:
            new_right_child.children = child.children[half_max + 1:]
            child.children = child.children[:half_max + 1]

        parent.keys.insert(child_index, middle_key)
        parent.children.insert(child_index + 1, new_right_child)

    def insert_key(self, key):
        if len(self.root.keys) >= self.max_number_of_keys:  # overflow, tree increases in height
            new_root = Node()
            new_root.children.append(self.root)
            self.root = new_root
            self._split_child(new_root, 0)
            self._insert_to_nonfull_node(self.root, key)
        else:
            self._insert_to_nonfull_node(self.root, key)

    def _insert_to_nonfull_node(self, node: Node, key):
        i = len(node.keys) - 1
        while i >= 0 and node.keys[i] >= key:  # find position where insert key
            i -= 1

        if node.is_leaf:
            node.keys.insert(i + 1, key)
        else:
            if len(node.children[i + 1].keys) >= self.max_number_of_keys:  # overflow
                self._split_child(node, i + 1)
                if node.keys[i + 1] < key:  # decide which child is going to have a new key
                    i += 1

            self._insert_to_nonfull_node(node.children[i + 1], key)

    def find(self, key) -> bool:
        current_node = self.root
        while True:
            i = len(current_node.keys) - 1
            while i >= 0 and current_node.keys[i] > key:
                i -= 1

            if i >= 0 and current_node.keys[i] == key:
                return True
            elif current_node.is_leaf:
                return False
            else:
                current_node = current_node.children[i + 1]

    def remove_key(self, key):
        self._remove_key(self.root, key)

    def _remove_key(self, node: Node, key) -> bool:
        try:
            key_index = node.keys.index(key)
            if node.is_leaf:
                node.keys.remove(key)
                return True
            else:
                self._remove_from_nonleaf_node(node, key_index)

            return True

        except ValueError:  # key not found in node
            if node.is_leaf:
                print("Key not found.")
                return False  # key not found
            else:
                i = 0
                number_of_keys = len(node.keys)
                while i < number_of_keys and key > node.keys[i]:  # decide in which subtree may be key
                    i += 1

                action_performed = self._repair_tree(node, i)
                if action_performed:
                    return self._remove_key(node, key)
                else:
                    return self._remove_key(node.children[i], key)

    def _repair_tree(self, node: Node, child_index: int) -> bool:
        child = node.children[child_index]
        if self.min_numbers_of_keys < len(child.keys) <= self.max_number_of_keys:  # The leaf/node is correct
            return False

        if child_index > 0 and len(node.children[child_index - 1].keys) > self.min_numbers_of_keys:
            self._rotate_right(node, child_index)
            return True

        if (child_index < len(node.children) - 1 and
                len(node.children[child_index + 1].keys) > self.min_numbers_of_keys):  # 0 <-- 1
            self._rotate_left(node, child_index)
            return True

        if child_index > 0:
            # merge child with brother on the left
            self._merge(node, child_index - 1, child_index)
        else:
            # merge child with brother on the right
            self._merge(node, child_index, child_index + 1)

        return True

    def _rotate_left(self, parent_node: Node, child_index: int):
        """
        Take key from right brother of the child and transfer to the child
        """
        new_child_key = parent_node.keys[child_index]
        new_parent_key = parent_node.children[child_index + 1].keys.pop(0)
        parent_node.children[child_index].keys.append(new_child_key)
        parent_node.keys[child_index] = new_parent_key

        if not parent_node.children[child_index + 1].is_leaf:
            ownerless_child = parent_node.children[child_index + 1].children.pop(0)
            # make ownerless_child as a new biggest child (with highest key) -> transfer from right subtree to left subtree
            parent_node.children[child_index].children.append(ownerless_child)

    def _rotate_right(self, parent_node: Node, child_index: int):
        """
        Take key from left brother of the child and transfer to the child
        """
        parent_key = parent_node.keys[child_index - 1]
        new_parent_key = parent_node.children[child_index - 1].keys.pop()
        parent_node.children[child_index].keys.insert(0, parent_key)
        parent_node.keys[child_index - 1] = new_parent_key

        if not parent_node.children[child_index - 1].is_leaf:
            ownerless_child = parent_node.children[child_index - 1].children.pop()
            # make ownerless_child as a new lowest child (with lowest key) -> transfer from left subtree to right subtree
            parent_node.children[child_index].children.insert(0, ownerless_child)

    def _merge(self, parent_node: Node, to_merge_index: int, transfered_child_index: int):
        from_merge_node = parent_node.children.pop(transfered_child_index)
        parent_key_to_merge = parent_node.keys.pop(to_merge_index)
        to_merge_node = parent_node.children[to_merge_index]
        to_merge_node.keys.append(parent_key_to_merge)
        to_merge_node.keys.extend(from_merge_node.keys)

        if not to_merge_node.is_leaf:
            to_merge_node.children.extend(from_merge_node.children)

        if parent_node == self.root and not parent_node.keys:
            self.root = to_merge_node

    def _remove_from_nonleaf_node(self, node: Node, key_index: int):
        key = node.keys[key_index]
        left_subtree = node.children[key_index]
        if len(left_subtree.keys) > self.min_numbers_of_keys:
            largest_key = self._find_largest_and_delete_in_left_subtree(left_subtree)
        elif len(node.children[key_index + 1].keys) > self.min_numbers_of_keys:
            largest_key = self._find_largest_and_delete_in_right_subtree(node.children[key_index + 1])
        else:
            self._merge(node, key_index, key_index + 1)
            return self._remove_key(node, key)

        node.keys[key_index] = largest_key

    def _find_largest_and_delete_in_left_subtree(self, node: Node):
        if node.is_leaf:
            return node.keys.pop()
        else:
            ch_index = len(node.children) - 1
            self._repair_tree(node, ch_index)
            largest_key_in_subtree = self._find_largest_and_delete_in_left_subtree(
                node.children[len(node.children) - 1])
            # self._repair_tree(node, ch_index)
            return largest_key_in_subtree

    def _find_largest_and_delete_in_right_subtree(self, node: Node):
        if node.is_leaf:
            return node.keys.pop(0)
        else:
            ch_index = 0
            self._repair_tree(node, ch_index)
            largest_key_in_subtree = self._find_largest_and_delete_in_right_subtree(node.children[0])
            # self._repair_tree(node, ch_index)
            return largest_key_in_subtree

    def traverse_tree(self):
        self._traverse_tree(self.root)
        print()

    def _traverse_tree(self, node: Node):
        if node.is_leaf:
            print(node.keys, end=" ")
        else:
            for i, key in enumerate(node.keys):
                self._traverse_tree(node.children[i])
                print(key, end=" ")
            self._traverse_tree(node.children[-1])
