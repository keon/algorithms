

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    def build_string(node):
        if node:
            vals.append(str(node.val))
            build_string(node.left)
            build_string(node.right)
        else:
            vals.append("#")
    vals = []
    build_string(root)
    return " ".join(vals)


def deserialize(data):
    def build_tree():
        val = next(vals)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = build_tree()
        node.right = build_tree()
        return node
    vals = iter(data.split())
    return build_tree()
