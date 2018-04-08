"""
Binary Heap. A min heap is a complete binary tree where each node is smaller
its childen. The root, therefore, is the minimum element in the tree. The min
heap use array to represent the data and operation. For example a min heap:

     4
   /   \
  50    7
 / \   /
55 90 87

Heap [0, 4, 50, 7, 55, 90, 87]

Method in class: insert, remove_min
For example insert(2) in a min heap:

     4                     4                     2
   /   \                 /   \                 /   \
  50    7      -->     50     2       -->     50    4
 / \   /  \           /  \   / \             /  \  /  \
55 90 87   2         55  90 87  7           55  90 87  7

For example remove_min() in a min heap:

     4                     87                    7
   /   \                 /   \                 /   \
  50    7      -->     50     7       -->     50    87
 / \   /              /  \                   /  \
55 90 87             55  90                 55  90

"""
import unittest
from abc import ABCMeta, abstractmethod

class AbstractHeap(metaclass=ABCMeta):
    """Abstract Class for Binary Heap."""
    def __init__(self):
        pass
    @abstractmethod
    def perc_up(self, i):
        pass
    @abstractmethod
    def insert(self, val):
        pass
    @abstractmethod
    def perc_down(self,i):
        pass
    @abstractmethod
    def min_child(self,i):
        pass
    @abstractmethod
    def remove_min(self,i):
        pass
class Binary_Heap(AbstractHeap):
    def __init__(self):
        self.currentSize = 0
        self.heap = [(0)]

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                # Swap value of child with value of its parent
                tmp = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = tmp
            i = i // 2

    """
        Method insert always start by inserting the element at the bottom.
        it inserts rightmost spot so as to maintain the complete tree property
        Then, it fix the tree by swapping the new element with its parent,
        until it finds an appropriate spot for the element. It essentially
        perc_up the minimum element
        Complexity: O(logN)
    """
    def insert(self, val):
        self.heap.append(val)
        self.currentSize = self.currentSize + 1
        self.perc_up(self.currentSize)

    """
        Method min_child returns index of smaller 2 childs of its parent
    """
    def min_child(self, i):
        if 2 * i + 1 > self.currentSize:  # No right child
            return 2 * i
        else:
            # left child > right child
            if self.heap[2 * i] > self.heap[2 * i +1]:
                return 2 * i + 1
            else:
                return 2 * i

    def perc_down(self, i):
        while 2 * i < self.currentSize:
            min_child = self.min_child(i)
            if self.heap[min_child] < self.heap[i]:
                # Swap min child with parent
                tmp = self.heap[min_child]
                self.heap[min_child] = self.heap[i]
                self.heap[i] = tmp
            i = min_child
    """
        Remove Min method removes the minimum element and swap it with the last
        element in the heap( the bottommost, rightmost element). Then, it
        perc_down this element, swapping it with one of its children until the
        min heap property is restored
        Complexity: O(logN)
    """
    def remove_min(self):
        ret = self.heap[1]      # the smallest value at beginning
        self.heap[1] = self.heap[self.currentSize] # Repalce it by the last value
        self.currentSize = self.currentSize - 1
        self.heap.pop()
        self.perc_down(1)
        return ret

class TestSuite(unittest.TestCase):
    """
        Test suite for the Binary_Heap data structures
    """
    def setUp(self):
        self.min_heap = Binary_Heap()
        self.min_heap.insert(4)
        self.min_heap.insert(50)
        self.min_heap.insert(7)
        self.min_heap.insert(55)
        self.min_heap.insert(90)
        self.min_heap.insert(87)

    def test_insert(self):
        # Before insert 2: [0, 4, 50, 7, 55, 90, 87]
        # After insert:  [0, 2, 50, 4, 55, 90, 87, 7]
        self.min_heap.insert(2)
        self.assertEqual([0, 2, 50, 4, 55, 90, 87, 7],
                          self.min_heap.heap)
        self.assertEqual(7, self.min_heap.currentSize)

    def test_remove_min(self):
        ret = self.min_heap.remove_min()
        # Before remove_min : [0, 4, 50, 7, 55, 90, 87]
        # After remove_min: [7, 50, 87, 55, 90]
        # Test return value
        self.assertEqual(4,ret)
        self.assertEqual([0, 7, 50, 87, 55, 90],
                          self.min_heap.heap)
        self.assertEqual(5, self.min_heap.currentSize)

if __name__ == "__main__":
    unittest.main()
