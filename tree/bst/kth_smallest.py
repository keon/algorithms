class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            break
        root = root.right
    return root.val


class Solution(object):
    def kth_smallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.helper(root, count)
        return count[k-1]

    def helper(self, node, count):
        if not node:
            return

        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)

if __name__ == '__main__':
    n1 = Node(100)
    n2 = Node(50)
    n3 = Node(150)
    n4 = Node(25)
    n5 = Node(75)
    n6 = Node(125)
    n7 = Node(175)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    print(kth_smallest(n1, 2))
    print(Solution().kth_smallest(n1, 2))
