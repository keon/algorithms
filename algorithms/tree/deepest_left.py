# Given a binary tree, find the deepest node
# that is the left child of its parent node.

# Example:

     # 1
   # /   \
  # 2     3
 # / \     \
# 4   5     6
           # \
            # 7
# should return 4.


class Node:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val

class DeepestLeft:
    def __init__(self):
        self.depth = 0
        self.Node = None

def find_deepest_left(root, is_left, depth, res):
    if not root:
        return
    if is_left and depth > res.depth:
        res.depth = depth
        res.Node = root
    find_deepest_left(root.left, True, depth + 1, res)
    find_deepest_left(root.right, False, depth + 1, res)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.right = Node(7)

res = DeepestLeft()
find_deepest_left(root, True, 1, res)
if res.Node:
    print(res.Node.val)
