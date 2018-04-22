class Node():
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


def min_depth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    if not root.left or not root.right:
        return max(self.minDepth(root.left), self.minDepth(root.right))+1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# iterative
def min_height(root):
    if not root:
        return 0
    height = 0
    level = [root]
    while level:
        height += 1
        new_level = []
        for node in level:
            if not node.left and not node.right:
                return height
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        level = new_level
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

height = min_height(tree)
print_tree(tree)
print("height:", height)
