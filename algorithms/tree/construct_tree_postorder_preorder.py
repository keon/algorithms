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

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

preIndex = 0
        
def constructTreeUtil(pre: list, post: list, low: int, high: int, size: int):#, preIndex = -1):
    """
        Recursive function that constructs tree from preorder and postorder array.
        
        preIndex is a global variable that keeps track of the index in preorder
        array.
        preorder and postorder array are represented are pre[] and post[] respectively.
        low and high are the indices for the postorder array.
    """

    global preIndex

    if preIndex == -1:
        preIndex = 0
  
    
    #Base case
    if(preIndex >= size or low > high):
        return None

    root = Node(pre[preIndex])
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


def constructTree(pre: list, post: list, size: int):
    """
        Main Function that will construct the full binary tree from given preorder
        and postorder array.
    """

    global preIndex
    root = constructTreeUtil(pre, post, 0, size-1, size)

    return printInorder(root)



def printInorder(root: Node, res = None):
    """
        Prints the tree constructed in inorder format
    """
    if root is None:
        return []
    if res is None: 
        res = []
    printInorder(root.left, res)
    res.append(root.val)
    printInorder(root.right, res)
    return res

if __name__ == '__main__':
    pre = [1, 2, 4, 8, 9, 5, 3, 6, 7]
    post = [8, 9, 4, 5, 2, 6, 7, 3, 1]
    size = len(pre)

    res = constructTree(pre, post, size)

    print(res)

    
