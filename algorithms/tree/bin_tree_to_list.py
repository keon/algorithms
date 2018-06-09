class Node():
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

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

tree = Node(10)
tree.left = Node(12)
tree.right = Node(15)
tree.left.left  = Node(25)
tree.left.left.right  = Node(100)
tree.left.right = Node(30)
tree.right.left = Node(36)

head = bin_tree_to_list(tree)
print_tree(head)
