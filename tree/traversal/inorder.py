

def inorder(root):
    res = []
    if not root:
        return res
    stack = []
    while root and stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.add(root.val)
        root = root.right
    return res
