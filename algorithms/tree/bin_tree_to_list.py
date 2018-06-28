from tree.tree import TreeNode


def bin_tree_to_list(root):
    """
    type root: root class
    """
    if not root:
        return root
    root = bin_tree_to_list_util(root)
    while root.left:
        root = root.left
    return root


def bin_tree_to_list_util(root):
    if not root:
        return root
    if root.left:
        left = bin_tree_to_list_util(root.left)
        while left.right:
            left = left.right
        left.right = root
        root.left = left
    if root.right:
        right = bin_tree_to_list_util(root.right)
        while right.left:
            right = right.left
        right.left = root
        root.right = right
    return root


def print_tree(root):
    while root:
        print(root.val)
        root = root.right


if __name__ == '__main__':
    tree = TreeNode(10)
    tree.left = TreeNode(12)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(25)
    tree.left.left.right = TreeNode(100)
    tree.left.right = TreeNode(30)
    tree.right.left = TreeNode(36)

    head = bin_tree_to_list(tree)
    print_tree(head)
