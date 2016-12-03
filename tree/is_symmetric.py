
def is_symmetric(root):
    if not root:
        return True
    return helper(root.left, root.right)

def helper(p, q):
    if not p and not q:
        return True
    if not p or not q or q.val != p.val:
        return False
    return helper(p.left, q.right) and helper(p.right, q.left)


