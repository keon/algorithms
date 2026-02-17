def successor(root, node):
    succ = None
    while root:
        if node.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ
