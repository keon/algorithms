r"""Write a function count_left_node returns the number of left children in the
tree. For example: the following tree has four left children (the nodes
storing the values 6, 3, 7, and 10):

                    9
                 /      \
               6         12
              / \\       /   \
            3     8   10      15
                 /              \
                7                18

    count_left_node = 4

"""


def count_left_node(root):
    if root is None:
        return 0
    if root.left is None:
        return count_left_node(root.right)
    return 1 + count_left_node(root.left) + count_left_node(root.right)
