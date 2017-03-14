"""
Given a binary tree, return the level order traversal of
its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


def level_order(root):
    ans = []
    if not root:
        return ans
    level = [root]
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
        ans.append(current)
    return ans
