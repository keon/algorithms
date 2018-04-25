"""
Write a function depthSum returns the sum of the values stored
in a binary search tree of integers weighted by the depth of each value.

For example:

                    9
                 /      \
               6         12
              / \       /   \
            3     8   10      15
                 /              \
                7                18

    depth_sum = 1*9 + 2*(6+12) + 3*(3+8+10+15) + 4*(7+18)

"""

def depth_sum(root):
    if root:
        return recur_depth_sum(root, 1)

def recur_depth_sum(root, n):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return root.data * n
    else:
        return n * root.data + recur_depth_sum(root.left, n+1) + recur_depth_sum(root.right, n+1)

"""
    The tree is created for testing:

                    9
                 /      \
               6         12
              / \       /   \
            3     8   10      15
                 /              \
                7                18

    depth_sum = 1*9 + 2*(6+12) + 3*(3+8+10+15) + 4*(7+18)

"""




