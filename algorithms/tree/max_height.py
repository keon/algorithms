"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.
"""


class Node():
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

# def max_height(root):
    # if not root:
        # return 0
    # return max(maxDepth(root.left), maxDepth(root.right)) + 1

# iterative
def max_height(root):
    if not root:
        return 0
    height = 0
    queue = [root]
    while queue:
        height += 1
        level = []
        while queue:
            node = queue.pop(0)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        queue = level
    return height

def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)

tree = Node(10)
tree.left = Node(12)
tree.right = Node(15)
tree.left.left  = Node(25)
tree.left.left.right  = Node(100)
tree.left.right = Node(30)
tree.right.left = Node(36)

height = max_height(tree)
print_tree(tree)
print("height:", height)
