"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.
"""

# def max_height(root):
#     if not root:
#         return 0
#     return max(maxDepth(root.left), maxDepth(root.right)) + 1

# iterative

from tree import TreeNode


def max_height(root):
    if root is None:
        return 0
    height = 0
    queue = [root]
    while queue:
        height += 1
        level = []
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                level.append(node.left)
            if node.right is not None:
                level.append(node.right)
        queue = level
    return height


def print_tree(root):
    if root is not None:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)


if __name__ == '__main__':
    tree = TreeNode(10)
    tree.left = TreeNode(12)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(25)
    tree.left.left.right = TreeNode(100)
    tree.left.right = TreeNode(30)
    tree.right.left = TreeNode(36)

    height = max_height(tree)
    print_tree(tree)
    print("height:", height)
