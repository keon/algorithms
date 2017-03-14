"""
Given a binary tree, return the zigzag level order traversal
of its nodes' values.
(ie, from left to right, then right to left
for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


def zigzag_level(root):
    res = []
    if not root:
        return res
    level = [root]
    flag = 1
    while level:
        current = []
        new_level = []
        for node in level:
            current.append(node.val)
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        level = new_level
        res.append(current[::flag])
        flag *= -1
    return res
