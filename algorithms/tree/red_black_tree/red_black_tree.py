"""
Implementation of Red-Black tree.
"""


class RBNode:
    def __init__(self, val, is_red, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.color = is_red


class RBTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, node):
        # set the node as the left child node of the current node's right node
        right_node = node.right
        if right_node is None:
            return
        else:
            # right node's left node become the right node of current node
            node.right = right_node.left
            if right_node.left is not None:
                right_node.left.parent = node
            right_node.parent = node.parent
            # check the parent case
            if node.parent is None:
                self.root = right_node
            elif node is node.parent.left:
                node.parent.left = right_node
            else:
                node.parent.right = right_node
            right_node.left = node
            node.parent = right_node

    def right_rotate(self, node):
        # set the node as the right child node of the current node's left node
        left_node = node.left
        if left_node is None:
            return
        else:
            # left node's right  node become the left node of current node
            node.left = left_node.right
            if left_node.right is not None:
                left_node.right.parent = node
            left_node.parent = node.parent
            # check the parent case
            if node.parent is None:
                self.root = left_node
            elif node is node.parent.left:
                node.parent.left = left_node
            else:
                node.parent.right = left_node
            left_node.right = node
            node.parent = left_node

    def insert(self, node):
        # the inserted node's color is default is red
        root = self.root
        insert_node_parent = None
        # find the position of inserted node
        while root is not None:
            insert_node_parent = root
            if insert_node_parent.val < node.val:
                root = root.right
            else:
                root = root.left
        # set the n ode's parent node
        node.parent = insert_node_parent
        if insert_node_parent is None:
            # case 1  inserted tree is null
            self.root = node
        elif insert_node_parent.val > node.val:
            # case 2 not null and find left or right
            insert_node_parent.left = node
        else:
            insert_node_parent.right = node
        node.left = None
        node.right = None
        node.color = 1
        # fix the tree to 
        self.fix_insert(node)

    def fix_insert(self, node):
        # case 1 the parent is null, then set the inserted node as root and color = 0
        if node.parent is None:
            node.color = 0
            self.root = node
            return
            # case 2 the parent color is black, do nothing
        # case 3 the parent color is red
        while node.parent and node.parent.color == 1:
            if node.parent is node.parent.parent.left:
                uncle_node = node.parent.parent.right
                if uncle_node and uncle_node.color == 1:
                    # case 3.1 the uncle node is red
                    # then set parent and uncle color is black and grandparent is red
                    # then node => node.parent
                    node.parent.color = 0
                    node.parent.parent.right.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                    continue
                elif node is node.parent.right:
                    # case 3.2 the uncle node is black or null, and the node is right of parent
                    # then set his parent node is current node
                    # left rotate the node and continue the next
                    node = node.parent
                    self.left_rotate(node)
                # case 3.3 the uncle node is black and parent node is left
                # then parent node set black and grandparent set red
                node.parent.color = 0
                node.parent.parent.color = 1
                self.right_rotate(node.parent.parent)
            else:
                uncle_node = node.parent.parent.left
                if uncle_node and uncle_node.color == 1:
                    # case 3.1 the uncle node is red
                    # then set parent and uncle color is black and grandparent is red
                    # then node => node.parent
                    node.parent.color = 0
                    node.parent.parent.left.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                    continue
                elif node is node.parent.left:
                    # case 3.2 the uncle node is black or null, and the node is right of parent
                    # then set his parent node is current node
                    # left rotate the node and continue the next
                    node = node.parent
                    self.right_rotate(node)
                # case 3.3 the uncle node is black and parent node is left
                # then parent node set black and grandparent set red
                node.parent.color = 0
                node.parent.parent.color = 1
                self.left_rotate(node.parent.parent)
        self.root.color = 0

    def transplant(self, node_u, node_v):
        """
        replace u with v
        :param node_u: replaced node
        :param node_v: 
        :return: None
        """
        if node_u.parent is None:
            self.root = node_v
        elif node_u is node_u.parent.left:
            node_u.parent.left = node_v
        elif node_u is node_u.parent.right:
            node_u.parent.right = node_v
        # check is node_v is None 
        if node_v:
            node_v.parent = node_u.parent

    def maximum(self, node):
        """
        find the max node when node regard as a root node   
        :param node: 
        :return: max node 
        """
        temp_node = node
        while temp_node.right is not None:
            temp_node = temp_node.right
        return temp_node

    def minimum(self, node):
        """
        find the minimum node when node regard as a root node   
        :param node:
        :return: minimum node 
        """
        temp_node = node
        while temp_node.left:
            temp_node = temp_node.left
        return temp_node

    def delete(self, node):
        # find the node position
        node_color = node.color
        if node.left is None:
            temp_node = node.right
            self.transplant(node, node.right)
        elif node.right is None:
            temp_node = node.left
            self.transplant(node, node.left)
        else:
            # both child exits ,and find minimum child of right child
            node_min = self.minimum(node.right)
            node_color = node_min.color
            temp_node = node_min.right
            ## 
            if node_min.parent is not node:
                self.transplant(node_min, node_min.right)
                node_min.right = node.right
                node_min.right.parent = node_min
            self.transplant(node, node_min)
            node_min.left = node.left
            node_min.left.parent = node_min
            node_min.color = node.color
        # when node is black, then need to fix it with 4 cases
        if node_color == 0:
            self.delete_fixup(temp_node)

    def delete_fixup(self, node):
        # 4 cases
        while node is not self.root and node.color == 0:
            # node is not root and color is black
            if node is node.parent.left:
                # node is left node
                node_brother = node.parent.right

                # case 1: node's red, can not get black node
                # set brother is black and parent is red 
                if node_brother.color == 1:
                    node_brother.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    node_brother = node.parent.right

                # case 2: brother node is black, and its children node is both black
                if (node_brother.left is None or node_brother.left.color == 0) and (
                                node_brother.right is None or node_brother.right.color == 0):
                    node_brother.color = 1
                    node = node.parent
                else:

                    # case 3: brother node is black , and its left child node is red and right is black
                    if node_brother.right is None or node_brother.right.color == 0:
                        node_brother.color = 1
                        node_brother.left.color = 0
                        self.right_rotate(node_brother)
                        node_brother = node.parent.right

                    # case 4: brother node is black, and right is red, and left is any color
                    node_brother.color = node.parent.color
                    node.parent.color = 0
                    node_brother.right.color = 0
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                node_brother = node.parent.left
                if node_brother.color == 1:
                    node_brother.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    node_brother = node.parent.right
                if (node_brother.left is None or node_brother.left.color == 0) and (
                                node_brother.right is None or node_brother.right.color == 0):
                    node_brother.color = 1
                    node = node.parent
                else:
                    if node_brother.left is None or node_brother.left.color == 0:
                        node_brother.color = 1
                        node_brother.right.color = 0
                        self.left_rotate(node_brother)
                        node_brother = node.parent.left
                    node_brother.color = node.parent.color
                    node.parent.color = 0
                    node_brother.left.color = 0
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = 0

    def inorder(self):
        res = []
        if not self.root:
            return res
        stack = []
        root = self.root
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append({'val': root.val, 'color': root.color})
            root = root.right
        return res


if __name__ == "__main__":
    rb = RBTree()
    children = [11, 2, 14, 1, 7, 15, 5, 8, 4]
    for child in children:
        node = RBNode(child, 1)
        print(child)
        rb.insert(node)
    print(rb.inorder())
