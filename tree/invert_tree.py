# invert a binary tree

def reverse(root):
    temp = root.right
    root.right = root.left
    root.left = temp
    # alternatively, root.left, root.right = root.right, root.left
    if root.left is not None:
        reverse(root.left)
    if root.right is not None:
        reverse(root.right)


