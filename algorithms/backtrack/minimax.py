from cmath import inf as inf  # This might be wrong


def binary_minimax(node, depth, maxing, alpha, beta):
    if (depth == 0) or (node.left is None and node.right is None):
        return node.value

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


def minimax(b_tree_node, heuristic_key, depth, maxing, alpha, beta):
    if (depth == 0) or b_tree_node.is_leaf():
        return b_tree_node.keys[heuristic_key]

    if maxing:  # Maximize Values
        max_value = -inf
        for child in b_tree_node.children:  # Loop through all children of node
            evaluation = binary_minimax(child, depth-1, False, alpha, beta)
            max_value = max(max_value, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:  # Prune Remaining Branches
                break
        return max_value

    else:  # Minimize Values
        min_value = inf
        for child in b_tree_node.children:  # Loop through all children of node
            evaluation = binary_minimax(child, depth - 1, True, alpha, beta)
            min_value = min(min_value, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:  # Prune Remaining Branches
                break

        return min_value

