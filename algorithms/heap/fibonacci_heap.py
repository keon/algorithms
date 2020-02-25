import math

class FibonacciHeap:

    class Node:
        def __init__(self, data):
            self.data = data
            self.parent = None
            self.child = None
            self.left = None
            self.right = None
            self.degree = 0
            self.mark = False
        
        def __str__(self):
                return f'data: {self.data}, child: {self.child.data if self.child != None else None}, left: {self.left.data if self.left != None else None}, right: {self.right.data if self.right != None else None}'

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.min_node = self.root_list = None
        self.total_nodes = 0

    def _append_root(self, node):
        """
        Append a node to the end of the
        root list.
        """
        last_node = self.root_list.left
        node.right = self.root_list
        node.left = last_node
        last_node.right = node
        self.root_list.left = node

    def _remove_root(self, node):
        """
        Remove the root node from the root list.
        """
        # nothing to remove
        if node == None or self.root_list == None:
            return

        # only one node
        if node == self.root_list and node.left == self.root_list and node.right == self.root_list:
            self.root_list = None
            return
        
        # length of root_list >= 2
        node.left.right = node.right
        node.right.left = node.left
        # update root list reference if the
        # removed node was the reference
        if node == self.root_list:
            self.root_list = node.right
        return node

    def _iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    def find_min(self):
        """
        Return the minimum node in the heap.
        """
        return self.min_node

    def merge(self, heap2):
        """
        Merge two fib heaps. It works by placing heap2's root list
        at the end of this heap's root list and connecting the heads 
        and tails.
        """
        tail = self.root_list.left
        heap2_tail = heap2.root_list.left

        # the tail of heap 2 is now the end of the list
        self.root_list.left = heap2_tail
        heap2_tail.right = self.root_list

        # heap2 starts at the end of the old list
        tail.right = heap2.root_list
        heap2.root_list.left = tail

        if self.min_node is None or (heap2.root_list != None and heap2.min_node.data < self.min_node.data):
            self.min_node = heap2.min_node
        self.total_nodes += heap2.total_nodes

    def insert(self, data):
        """
        Insert a node into the heap.
        """
        node = self.Node(data)
        node.right = node
        node.left = node

        if self.min_node is None:
            self.root_list = node
            self.min_node = node
        else:
            self._append_root(node)

            # node with data lower than the min_node is the new min_node
            if node.data < self.min_node.data:
                self.min_node = node
        self.total_nodes += 1

    def extract_min_node(self):
        z = self.min_node
        if z != None:
            # add children to the root list
            child = z.child
            while child != None:
                self._append_root(child)

                child = child.right
                if child == z.child:
                    break
                    
            self._remove_root(z)
            # only node and no children
            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self._consolidate()
            self.total_nodes -= 1
        return z

    def _consolidate(self):
        A = [None] * self.total_nodes
        # process root list
        root_nodes = [x for x in self._iterate(self.root_list)]
        for root in root_nodes:
            x = root
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.data > y.data:
                    # exchange x and y to ensure x is root
                    # after linking them
                    temp = x
                    x, y = y, temp
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        
        # find new min node
        self.min_node = None
        for a in A:
            if a != None:
                if self.min_node == None:
                    self.min_node = a
                else:
                    if (a.data < self.min_node.data):
                        self.min_node = a

    def _append_child(self, parent, child):
        if parent.child == None:
            parent.child = child
            child.left = child
            child.right = child
        else:
            p_child = parent.child

            last_node = p_child.left
            child.right = p_child
            child.left = last_node
            last_node.right = child
            p_child.left = child
        parent.degree += 1
        child.parent = parent

    def _link(self, y, x):
        #print(f'linking: {y.data} to {x.data}')
        self._remove_root(y)
        # make y a child of x
        self._append_child(x, y)
        y.mark = False

    def _cut(self, x, y):
        pass
    
    def _cascading_cut(self, y):
        pass

    def decrease_key(self, node, data):
        if data > node.key: 
            raise Exception("Key value larger than the nodes key")
        node.key = data
        parent = node.parent

        if parent != None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if data < self.min_node.data:
            self.min_node = node

    def __str__(self):
        node = self.root_list
        if node is None:
            return "heap is empty"
        else:
            result = "==========\nroot list: "
            nodes = [x for x in self._iterate(self.root_list)]
            for node in nodes:
                if node != self.root_list:
                    result += " --> "
                result += str(node.data)
                node = node.right

                if node == self.root_list:
                    break
            result += f"\nHeap has {self.total_nodes} nodes"
            result += f"\nmin_node-node: {self.find_min().data} \n=========="
            return result


if __name__ == "__main__":
    fheap = FibonacciHeap()
    fheap.insert(4)
    fheap.insert(3)
    fheap.insert(7)
    node = fheap.extract_min_node()
    fheap.insert(1)
    fheap.insert(10)
    fheap.insert(15)
    node = fheap.extract_min_node()
    print(fheap.root_list)
    print(fheap.root_list.child)
    print(fheap.root_list.child.left)
    print(fheap)
