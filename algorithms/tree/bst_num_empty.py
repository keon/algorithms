r"""Write a function num_empty returns returns the number of empty branches in a
tree. Function should count the total number of empty branches among the nodes
of the tree. A leaf node has two empty branches. In the case, if root is None,
it considered as a 1 empty branch
For example: the following tree has 10 empty branch (* is empty branch).

                    9 __
                 /      \\___
               6            12
              / \\          /   \
            3     8       10      15
          /  \\   / \\     /  \\    /   \
         *    * 7   *   *    *  *    18
               / \\                   /  \
              *   *                 *    *

    empty_branch = 10

"""


def num_empty(root):
    if root is None:
        return 1
    if root.left is None and root.right:
        return 1 + num_empty(root.right)
    if root.right is None and root.left:
        return 1 + num_empty(root.left)
    return num_empty(root.left) + num_empty(root.right)
