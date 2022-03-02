from cmath import inf as inf #this might be wrong

def binary_minimax(node, depth, maxing, alpha, beta):
    if (depth == 0) or (node.left == None and node.right == None):
        return node.value

    if maxing:
        maxValue = -inf
        #Check Left
        evaluation = binary_minimax(node.left, depth-1, False, alpha, beta)
        maxValue = max(maxValue, evaluation)
        alpha = max(alpha, evaluation)
        if beta > alpha: # Prune Right side
            #Check right side
            evaluation = binary_minimax(node.right, depth-1, False, alpha, beta)
            maxValue = max(alpha, evaluation)
            alpha = max(alpha, evaluation)

            return maxValue

    else:
        minValue = inf
        # Check Left
        evaluation = binary_minimax(node.left, depth - 1, True, alpha, beta)
        minValue = min(minValue, evaluation)
        beta = min(beta, evaluation)
        if beta > alpha:  # Prune Right side
            # Check right side
            evaluation = binary_minimax(node.right, depth - 1, True, alpha, beta)
            minValue = min(beta, evaluation)
            beta = min(beta, evaluation)

            return minValue
