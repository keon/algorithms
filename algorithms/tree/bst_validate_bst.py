# ===============================================================================
# Validate Binary Search Tree
"""
To check if the given binary tree is a valid binary search
tree (BST), we need to ensure that:
    1. The left subtree of a node contains only nodes with
       keys less than the node's key.
    2. The right subtree of a node contains only nodes with
       keys greater than the node's key.
    3. Both the left and right subtrees must also be binary
       search trees.
"""
# ===============================================================================


# Tree class definition
class TreeNode:
    def __init__(self, value):

        self.val = value
        self.left = None
        self.right = None


# Function to validate if a binary tree is a BST
def validate_bst(node):
    """
    Validate if a binary tree is a binary search tree (BST).
    Input params : Tree Node to be validated
    Returns : Tuple (
        is_bst: bool,
        min_value: int | None,
        max_value: int | None
    )
    """

    # Base case: An empty tree is a valid BST
    if not node:
        return (True, None, None)

    # Validate the left and right subtrees
    valid_left, minn_left, maxx_left = validate_bst(node.left)
    valid_right, minn_right, maxx_right = validate_bst(node.right)

    # If either subtree is not valid, the whole tree is not a valid BST
    if not valid_left or not valid_right:
        return (
            False,
            minn_left if minn_left else node.val,
            maxx_right if maxx_right else node.val,
        )

    # Check the current node's value against the max of the left subtree
    if maxx_left is not None and maxx_left > node.val:
        return (
            False,
            minn_left if minn_left else node.val,
            maxx_right if maxx_right else node.val,
        )

    # Check the current node's value against the min of the right subtree
    if minn_right is not None and minn_right < node.val:
        return (
            False,
            minn_left if minn_left else node.val,
            maxx_right if maxx_right else node.val,
        )

    # If all checks pass, the tree/subtree is a valid BST
    return (
        True,
        minn_left if minn_left is not None else node.val,
        maxx_right if maxx_right is not None else node.val,
    )


# Example usage
if __name__ == "__main__":
    # Constructing a simple binary tree
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    """
          10
         /  \
        5    15
            /  \
           12   20
    """

    # Validate if the constructed tree is a BST
    is_bst, _, _ = validate_bst(root)
    print(f"The tree is a valid BST: {is_bst}")
