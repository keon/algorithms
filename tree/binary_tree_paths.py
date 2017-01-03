def binaryTreePaths(root):
    res = []
    if not root:
        return res
    DFS(res, root, str(root.val))
    return res

def DFS(res, root, cur):
    if not root.left and not root.right:
        res.append(cur)
    if root.left:
        DFS(res, root.left, cur+'->'+str(root.left.val))
    if root.right:
        DFS(res, root.right, cur+'->'+str(root.right.val))
