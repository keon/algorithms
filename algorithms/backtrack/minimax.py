from cmath import inf as inf

class Node:                         #node class used for binary tree
    def __init__(self):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node2:             #node class used for genral tree structure with possibility for several key
    def __init__(self):
        # self.is_leaf = is_leaf
        self.keys = []
        self.children = []

    def __repr__(self):
        return "<id_node: {0}>".format(self.keys)

    @property
    def is_leaf(self):
        return len(self.children) == 0


def binary_minimax(node, depth, maxing, alpha, beta):
    """
        @function       binary_minimax(node, depth, maxing, alpha, beta)
        @description    Performs Minimax on a TreeNode. (TreeNode class found in /tree/tree.py)
        @arg            TreeNode    node
        @arg            int         depth
        @arg            bool        maxing
        @arg            real        alpha
        @arg            real        beta
    """
    # if max depth has been reached or node is a leaf, return node value
    if (depth == 0) or (node.left is None and node.right is None):
        return node.val

    if maxing:  # Maximize Values
        max_value = -inf
        # Check Left Child
        evaluation = binary_minimax(node.left, depth-1, False, alpha, beta)
        max_value = max(max_value, evaluation)
        alpha = max(alpha, evaluation)
        if beta > alpha:  # Prune Right side
            # Check right Child
            evaluation = binary_minimax(node.right, depth-1, False, alpha, beta)
            max_value = max(alpha, evaluation)

        return max_value

    else:
        min_value = inf
        # Check Left
        evaluation = binary_minimax(node.left, depth - 1, True, alpha, beta)
        min_value = min(min_value, evaluation)
        beta = min(beta, evaluation)
        if beta > alpha:  # Prune Right side
            # Check right Side
            evaluation = binary_minimax(node.right, depth - 1, True, alpha, beta)
            min_value = min(beta, evaluation)

        return min_value


def minimax(b_tree_node, heuristic_key, depth, maxing, alpha=-inf, beta=inf):
    """
        @function       minimax(b_tree_node, heuristic_key, depth, maxing, alpha, beta)
        @description    Performs Minimax on a BTree. (BTree class found in /tree/b_tree.py)
        @arg            Btree       b_tree_node
        @arg            dict_key    heuristic_key
        @arg            int         depth
        @arg            bool        maxing
        @arg            real        alpha
        @arg            real        beta
    """
    # if max depth has been reached or node is a leaf, return node value
    if (depth == 0) or b_tree_node.is_leaf:
        return b_tree_node.keys[heuristic_key]

    if maxing:  # Maximize Values
        max_value = -inf
        for child in b_tree_node.children:  # Loop through all children of node
            evaluation = minimax(child, heuristic_key, depth-1, False, alpha, beta)
            max_value = max(max_value, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:  # Prune Remaining Branches
                break
        return max_value

    else:  # Minimize Values
        min_value = inf
        for child in b_tree_node.children:  # Loop through all children of node
            evaluation = minimax(child, heuristic_key, depth - 1, True, alpha, beta)
            min_value = min(min_value, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:  # Prune Remaining Branches
                break
        return min_value
