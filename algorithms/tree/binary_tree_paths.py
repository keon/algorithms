def binary_tree_paths(root):
    res = []
    if not root:
        return res
    dfs(res, root, str(root.val))
    return res

def dfs(res, root, cur):
    if not root.left and not root.right:
        res.append(cur)
    if root.left:
        dfs(res, root.left, cur+'->'+str(root.left.val))
    if root.right:
        dfs(res, root.right, cur+'->'+str(root.right.val))
