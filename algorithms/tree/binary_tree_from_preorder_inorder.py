"""
Given the inorder and preorder traversal of the tree
return the construted binary tree.

Assuming no duplicate elements

Eg.
Inorder = [100,5,1,8,9,10]
Preorder = [8,5,100,1,10,9]

Generated Tree:

              8
             / \
            5   10
           / \  /
          100 1 9

"""

class TreeNode( object ):
    def __init__( self, x ):
        self.val = x
        self.left = None
        self.right = None


def generate_tree( inorder, preorder ):

    if len( preorder ) <= 0 or len(inorder) <= 0:
        return None

    curr_node = TreeNode( preorder[0] )
    index = inorder.index( preorder[0] )
    preorder.pop(0)
    curr_node.left = generate_tree( inorder[:index], preorder )
    curr_node.right = generate_tree( inorder[ index + 1 : ], preorder )
    return curr_node
