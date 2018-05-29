"""
Given a binary tree and a sum, find all root-to-leaf
paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


def path_sum(root, sum):
    if not root:
        return []
    res = []
    dfs(root, sum, [], res)
    return res

def dfs(root, sum, ls, res):
    if not root.left and not root.right and root.val == sum:
        ls.append(root.val)
        res.append(ls)
    if root.left:
        dfs(root.left, sum-root.val, ls+[root.val], res)
    if root.right:
        dfs(root.right, sum-root.val, ls+[root.val], res)


# DFS with stack
def path_sum2(root, s):
    if not root:
        return []
    res = []
    stack = [(root, [root.val])]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right and sum(ls) == s:
            res.append(ls)
        if node.left:
            stack.append((node.left, ls+[node.left.val]))
        if node.right:
            stack.append((node.right, ls+[node.right.val]))
    return res


# BFS with queue
def path_sum3(root, sum):
    if not root:
        return []
    res = []
    queue = [(root, root.val, [root.val])]
    while queue:
        node, val, ls = queue.pop(0)  # popleft
        if not node.left and not node.right and val == sum:
            res.append(ls)
        if node.left:
            queue.append((node.left, val+node.left.val, ls+[node.left.val]))
        if node.right:
            queue.append((node.right, val+node.right.val, ls+[node.right.val]))
    return res
