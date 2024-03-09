def binary_tree_paths(root):
    res = []
    if root is None:
        return res
    dfs(res, root, str(root.val))
    return res


def dfs(res, root, cur):
    if root.left is None and root.right is None:
        res.append(cur)
    if root.left:
        dfs(res, root.left, cur+'->'+str(root.left.val))
    if root.right:
        dfs(res, root.right, cur+'->'+str(root.right.val))
