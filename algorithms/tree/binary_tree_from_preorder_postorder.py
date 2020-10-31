"""
    Given two arrays representing preorder and postorder traversal of a full
    binary tree, construct the binary tree and print the inorder traversal of the
    tree.

    A full binary tree has either 0 or 2 children.

    Algorithm:
        1. Assign the first element of preorder array as root of the tree.
        2. Find the same element in the postorder array and divide the postorder
            array into left and right subtree.
        3. Repeat the above steps for all the elements and construct the tree.

    Eg: pre[] = {1, 2, 4, 8, 9, 5, 3, 6, 7}
        post[] = {8, 9, 4, 5, 2, 6, 7, 3, 1}

        Tree:

                1
              /   \
             2     3
            / \   / \
           4   5 6   7
          / \
         8   9

      Output: 8 4 9 2 5 1 6 3 7
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructTreeUtil(pre: list, post: list, low: int, high: int, size: int) -> TreeNode:
    """
        Recursive function that constructs tree from preorder and postorder array.
        
        preIndex is a global variable that keeps track of the index in preorder
        array.

        low and high are the indices for the postorder array.
    """
    global preIndex

    #Base case
    if(preIndex >= size or low > high):
        return None

    root = TreeNode(pre[preIndex])
    preIndex += 1

    #If only one element in the subarray return root
    if(low == high or preIndex >= size):
        return root

    #Find the next element of pre[] in post[]
    i = low
    while i <= high:
        if(pre[preIndex] == post[i]):
            break

        i += 1


    #Use index of element present in postorder to divide postorder array
    #to two parts: left subtree and right subtree
    if(i <= high):
        root.left = constructTreeUtil(pre, post, low, i, size)
        root.right = constructTreeUtil(pre, post, i+1, high, size)

    return root


def constructTree(pre: list, post: list, size: int) -> TreeNode:
    """
        Main Function that will construct the full binary tree from given preorder
        and postorder array.
    """

    global preIndex

    return constructTreeUtil(pre, post, 0, size-1, size)



def printInorder(node: TreeNode) -> None:
    """
        Prints the tree constructed in inorder format
    """
    if(node is None):
        return

    printInorder(node.left)
    print(node.val, end = " ")

    printInorder(node.right)


if __name__ == "__main__":
    #pre = [1, 2, 4, 8, 9, 5, 3, 6, 7]
    #post = [8, 9, 4, 5, 2, 6, 7, 3, 1]
    #size = len(pre)

    pre = [12,7,16,21,5,1,9]
    post = [16,21,7,1,9,5,12]
    size = 7

    preIndex = 0

    root = constructTree(pre, post, size)

    print("InorderTraversal : ")
    printInorder(root)

        
    
