"""
Write a function height returns the height of a tree. The height is defined to
be the number of levels. The empty tree has height 0, a tree of one node has
height 1, a root node with one or two leaves as children has height 2, and so on
For example: height of tree is 4

                    9
                 /      \
               6         12
              / \       /   \
            3     8   10      15
                 /              \
                7                18

    height = 4

"""


def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

"""
    The tree is created for testing:

                    9
                 /      \
               6         12
              / \       /   \
            3     8   10      15
                 /              \
                7                18

    count_left_node = 4

"""



