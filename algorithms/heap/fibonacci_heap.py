import math
import sys

"""
A Fibonacci heap is a collection of rooted trees that ar emin-heap ordered. That is, each tree obeys 
the min-heap property: the key of a node is greater than or equal to the key of its parent.

Using Fibonacci heaps for priority queues improves the asymptotic running time of important algorithms, 
such as Dijkstra's algorithm for computing the shortest path between two nodes in a graph, compared to
the same algorithm using other slower priority queue data structures. 

Time complexiity vs binomial heap:
|              	| Bin tree (worst-case) 	| Fib tree (amortized) 	|
|--------------	|-----------------------	|----------------------	|
| Make-Heap    	| Θ(1)                  	| Θ(1)                 	|
| Insert       	| Θ(logn)               	| Θ(1)                 	|
| Minimum      	| Θ(1)                  	| Θ(1)                 	|
| Extract-min  	| Θ(logn)               	| O(logn)              	|
| Merge/union  	| Θ(n)                  	| Θ(1)                 	|
| Decrease key 	| Θ(logn)               	| Θ(1)                 	|
| Delete       	| Θ(logn)               	| O(logn)              	|

However, notice that thee times are amortized and that memory consumption can be high. Subsequently, 
Fibonacci heaps have a reputation for being slow in practice due to large memory consumption per 
node and high constant factors on all operations.

Resource:
Introduction to Algorithms, third edition.
Chapter 19, Fibonacci heaps
"""


class FibonacciHeap:
    class Node:
        def __init__(self, key):
            self.key = key
            self.parent = None
            self.child = None
            self.left = None
            self.right = None
            self.degree = 0
            self.mark = False

    def __init__(self):
        # the root list is a list of rooted trees
        # the min_node is the node with lowest key value in the heap
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
        Remove the node from the head list.
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
            # replace the head contents with the node to the left
            # eliminating the node
            self.root_list = node.right
        return node

    def iterate(self, head):
        """
        Iterate the fib heap.
        """
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

        if self.min_node is None or (
            heap2.root_list != None and heap2.min_node.key < self.min_node.key
        ):
            self.min_node = heap2.min_node
        self.total_nodes += heap2.total_nodes

    def insert(self, key):
        """
        Insert a node into the heap.
        """
        node = self.Node(key)
        node.right = node
        node.left = node

        if self.min_node is None:
            self.root_list = node
            self.min_node = node
        else:
            self._append_root(node)

            # node with key lower than the min_node is the new min_node
            if node.key < self.min_node.key:
                self.min_node = node
        self.total_nodes += 1

    def extract_min_node(self):
        """
        Return and remove the minimum node
        in the tree.
        """
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
        """
        Combines roots of the same degree, consolidating
        the list into an unordered list of binomial trees.
        """
        A = [None] * self.total_nodes
        # process root list
        root_nodes = [x for x in self.iterate(self.root_list)]
        for root in root_nodes:
            x = root
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.key > y.key:
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
                    if a.key < self.min_node.key:
                        self.min_node = a

    def _append_child(self, parent, child):
        """
        Append a child to parent.
        """
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

    def _remove_child(self, parent, child):
        """
        Remove a child from parent.
        """
        #self._remove_node(parent.child, child)
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == child:
            parent.child = child.right
            child.right.parent = parent
        child.left.right = child.right
        child.right.left = child.left

        parent.degree -= 1

    def _link(self, y, x):
        """
        Link child x to parent y.
        """
        self._remove_root(y)
        # make y a child of x
        self._append_child(x, y)
        y.mark = False

    def _cut(self, x, y):
        """
        Cut the link between x and y and place
        x in the root list.
        """
        self._remove_child(y, x)
        self._append_root(x)
        if x.key < self.min_node.key:
            self.min_node = x
        x.parent = None
        x.mark = False

    def _cascading_cut(self, y):
        """
        Cascading cut of y to obtain good time bounds.
        """
        z = y.parent
        if z != None:
            if y.mark == False:
                y.mark = True
            else:
                self._cascading_cut(z)

    def decrease_key(self, node, key):
        """
        Decrease the key of a node in the heap.
        """
        if key > node.key:
            raise Exception("Key value larger than the nodes key")
        node.key = key
        parent = node.parent

        if parent != None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if key < self.min_node.key:
            self.min_node = node

    def delete(self, node):
        """
        Delete a node from the heap.
        """
        self.decrease_key(node, -sys.maxsize - 1)
        self.extract_min_node()

