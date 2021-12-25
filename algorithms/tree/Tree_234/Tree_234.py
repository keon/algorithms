"""
Implementation of 2-3-4 Tree.
"""


class Tree234Node:
    # Constructor of a 2-3-4 Tree Node
    def __init__(self, val_a, val_b=None, val_c=None,
                 less_node=None, between_ab_node=None,
                 between_bc_node=None, greater_node=None):
        self.A = val_a
        self.B = val_b
        self.C = val_c
        self.less = less_node
        self.betweenAB = between_ab_node
        self.betweenBC = between_bc_node
        self.greater = greater_node

    # Return True if any value contain the key
    def contains_key(self, key):
        if self.C and self.C == key:
            return True
        if self.B and self.B == key:
            return True
        if self.A == key:
            return True
        return False

    # Return the value if any value is equal the key, else return None
    def finds_key(self, key):
        if self.C and self.C == key:
            return self.C
        if self.B and self.B == key:
            return self.B
        if self.A == key:
            return self.A
        return None

    # Empty the data contained in the value
    def delete_data(self):
        self.A = None
        self.B = None
        self.C = None

    # Return True if all data are not None, else False.
    def is_full(self):
        return (self.A is not None) and (self.B is not None) and (self.C is not None)

    # Return True if all child pointers are None
    def is_leaf(self):
        return (self.less is None) and (self.betweenAB is None) and (self.betweenBC is None) and (self.greater is None)

    # Each node maximum has 3 value. Return the number of value contained in the node
    def value_count(self):
        if self.C:
            return 3
        elif self.B:
            return 2
        elif self.A:
            return 1
        # Empty node
        return 0


class Tree234:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = Tree234Node(data)
            return True

        key = data
        ptr = self.root
        parent = ptr

        while ptr:
            # Check for duplicates
            if ptr.contains_key(key):
                return False

            """
            There are 3 cases:
            Case 1: There are 3 values, split it
            Case 2: It is a leaf node
            Case 3: It is not a leaf node
            """

            # Case 1
            if ptr.is_full():
                # Case 1a: if parent node has 1 key
                if parent.value_count() == 1:
                    if parent.A < ptr.B:
                        parent.B = ptr.B
                        parent.betweenAB = Tree234Node(ptr.A, None, None, ptr.less, ptr.betweenAB)
                        parent.betweenBC = Tree234Node(ptr.C, None, None, ptr.betweenBC, ptr.greater)
                    else:
                        parent.B = parent.A
                        parent.betweenBC = parent.betweenAB
                        parent.A = ptr.B
                        parent.less = Tree234Node(ptr.A, None, None, ptr.less, ptr.betweenAB)
                        parent.betweenAB = Tree234Node(ptr.C, None, None, ptr.betweenBC, ptr.greater)

                    if key < parent.A:
                        ptr = parent.less
                    elif key < parent.B:
                        ptr = parent.betweenAB
                    elif key > parent.B:
                        ptr = parent.betweenBC
                    else:
                        # A value is a duplicate of key
                        # print("Tree234: add(key): Case 1a: duplicated")
                        return False

                # Case 1b: if parent node has 2 keys
                elif parent.value_count() == 2:
                    if parent.B < ptr.A:
                        parent.C = ptr.B
                        parent.betweenBC = Tree234Node(ptr.A, None, None, ptr.less, ptr.betweenAB)
                        parent.greater = Tree234Node(ptr.C, None, None, ptr.betweenBC, ptr.greater)
                    elif parent.A < ptr.B:
                        parent.C = parent.B
                        parent.greater = parent.betweenBC
                        parent.B = ptr.B
                        parent.betweenAB = Tree234Node(ptr.A, None, None, ptr.less, ptr.betweenAB)
                        parent.betweenBC = Tree234Node(ptr.C, None, None, ptr.betweenBC, ptr.greater)
                    else:
                        parent.C = parent.B
                        parent.greater = parent.betweenBC
                        parent.B = parent.A
                        parent.betweenBC = parent.betweenAB
                        parent.A = ptr.B
                        parent.less = Tree234Node(ptr.A, None, None, ptr.less, ptr.betweenAB)
                        parent.betweenAB = Tree234Node(ptr.C, None, None, ptr.betweenBC, ptr.greater)

                    if key < parent.A:
                        ptr = parent.less
                    elif key < parent.B:
                        ptr = parent.betweenAB
                    elif key < parent.C:
                        ptr = parent.betweenBC
                    elif key > parent.C:
                        ptr = parent.greater
                    else:
                        # A value is a duplicate of key
                        # print("Tree234: add(key): Case 1b: duplicated")
                        return False

                # Case 1c: if parent node has 3 keys
                else:
                    self.root = Tree234Node(ptr.B)
                    self.root.less = Tree234Node(ptr.A, None, None, ptr.less, ptr.betweenAB)
                    self.root.betweenAB = Tree234Node(ptr.C, None, None, ptr.betweenBC, ptr.greater)

                    parent = self.root

                    if key < self.root.A:
                        ptr = self.root.less
                    elif key > self.root.A:
                        ptr = self.root.betweenAB
                    else:
                        # A value is a duplicate of key
                        # print("Tree234: add(key): Case 1c: duplicated")
                        return False

            # Case 2
            if ptr.is_leaf():
                # Case 2a: ptr has 1 key
                if ptr.value_count() == 1:
                    if ptr.A < key:
                        ptr.B = data
                        return True
                    elif ptr.A > key:
                        ptr.B = ptr.A
                        ptr.A = data
                        return True

                # Case 2b: ptr has 2 keys
                elif ptr.value_count() == 2:
                    if ptr.B < key:
                        ptr.C = data
                        return True
                    elif ptr.A < key:
                        ptr.C = ptr.B
                        ptr.B = data
                        return True
                    elif ptr.A > key:
                        ptr.C = ptr.B
                        ptr.B = ptr.A
                        ptr.A = data
                        return True

            # Case 3
            else:
                # Assigns parent node
                parent = ptr

                # Case 3a: ptr has 1 key
                if ptr.value_count() == 1:
                    if ptr.A > key:
                        ptr = ptr.less
                    else:
                        ptr = ptr.betweenAB

                # Case 3b: ptr has 2 keys
                elif ptr.value_count() == 2:
                    if ptr.A > key:
                        ptr = ptr.less
                    elif ptr.B > key:
                        ptr = ptr.betweenAB
                    else:
                        ptr = ptr.betweenBC

        # Should never get to this point
        return False

    # Insert integer to the tree function
    def insert(self, data):
        if not self.add(data):
            # Unsuccessfully insert data
            # print("Tree234: insert(data): Unsuccessfully insert data", data)
            return

    # Initialize the recursive call for finding the key
    def find_ptr(self, key, num_node_searched, ptr):
        """
        Recursively find the key if it exists in the tree
        PARAMETERS:
            key: the value we are searching for
            num_node_searched: the number of node search in finding the key
            ptr: the pointer that is searched
        RETURN:
            a tuple of (found_key, num_node_searched)
            found_key: equals key if found, else None
        """
        if ptr is None:
            result = (None, num_node_searched)
            return result

        found_key = ptr.finds_key(key)
        num_node_searched += 1

        if found_key:
            result = (found_key, num_node_searched)
            return result
        else:
            if ptr.C and ptr.C < key:
                return self.find_ptr(key, num_node_searched, ptr.greater)
            elif ptr.B and ptr.B < key:
                return self.find_ptr(key, num_node_searched, ptr.betweenBC)
            elif ptr.A < key:
                return self.find_ptr(key, num_node_searched, ptr.betweenAB)
            else:
                return self.find_ptr(key, num_node_searched, ptr.less)

    # Recursively Search for the node that contains the key
    def find(self, key, num_node_searched):
        """
        Initialize the finding process and find the key if it exists in the tree
        PARAMETERS:
            key: the value we are searching for
            num_node_searched: the number of node search in finding the key
        RETURN:
            a tuple of (found_key, num_node_searched)
            found_key: equals key if found, else None
        """
        if not self.root:
            result = (None, num_node_searched)
            return result

        ptr = self.root

        found_key = ptr.finds_key(key)
        num_node_searched += 1

        if found_key:
            result = (found_key, num_node_searched)
            return result
        else:
            if ptr.C and ptr.C < key:
                return self.find_ptr(key, num_node_searched, ptr.greater)
            elif ptr.B and ptr.B < key:
                return self.find_ptr(key, num_node_searched, ptr.betweenBC)
            elif ptr.A < key:
                return self.find_ptr(key, num_node_searched, ptr.betweenAB)
            else:
                return self.find_ptr(key, num_node_searched, ptr.less)

    # Print the number of node searched for a key
    def search(self, key):
        num_node_searched = 0
        result = self.find(key, num_node_searched)

        if result[0] is None:
            # Unsuccess in finding the key
            # print(f"Tree234: search(key): Unsuccess in finding the key after searching {result[1]} node")
            return
        elif result[0] and result[0] == key:
            # Successfully find the key
            # print(f"Tree234: search(key): Successfully find the key by searching {result[1]} node")
            return