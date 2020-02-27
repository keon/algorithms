from algorithms.heap import (
    BinaryHeap,
    get_skyline,
    max_sliding_window,
    k_closest,
    fibonacci_heap
)

import unittest


class TestBinaryHeap(unittest.TestCase):
    """
        Test suite for the binary_heap data structures
    """

    def setUp(self):
        self.min_heap = BinaryHeap()
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
        self.assertEqual(4, ret)
        self.assertEqual([0, 7, 50, 87, 55, 90],
                         self.min_heap.heap)
        self.assertEqual(5, self.min_heap.currentSize)


class TestSuite(unittest.TestCase):
    def test_get_skyline(self):
        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12],
                     [15, 20, 10], [19, 24, 8]]
        # Expect output
        output = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10],
                  [20, 8], [24, 0]]
        self.assertEqual(output, get_skyline(buildings))

    def test_max_sliding_window(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        self.assertEqual([3, 3, 5, 5, 6, 7], max_sliding_window(nums, 3))

    def test_k_closest_points(self):
        points = [(1, 0), (2, 3), (5, 2), (1, 1), (2, 8), (10, 2), (-1, 0), (-2, -2)]
        self.assertEqual([(-1, 0), (1, 0)], k_closest(points, 2))
        self.assertEqual([(1, 1), (-1, 0), (1, 0)], k_closest(points, 3))
        self.assertEqual([(-2, -2), (1, 1), (1, 0), (-1, 0)], k_closest(points, 4))
        self.assertEqual([(10, 2), (2, 8), (5, 2), (-2, -2), (2, 3),
                          (1, 0), (-1, 0), (1, 1)], k_closest(points, 8))

class TestFibonacciHeap(unittest.TestCase):
    """
    Test the fibonacci heap and all the interfaces of the data structure
    """
    def test_fibonacci_heap_find_min(self):
        """
        Test that the find_min method of the fibonacci heap returns:
        1. None if the heap is empty
        2. the smallest data node if there is data in the heap
        """
        fh = fibonacci_heap.FibonacciHeap()

        # test case 1
        self.assertEqual(None, fh.find_min()) 

        data = [4, 5, 7, 1, 3, 6, 10, 30]
        for x in data:
            fh.insert(x)

        # test case 2
        self.assertEqual(1, fh.find_min().key) 

    def test_fibonacci_heap_extract_min(self):
        """
        Test that the extract_min_node method returns the node with
        the smallest data from the heap and removes it from the heap
        """
        fh = fibonacci_heap.FibonacciHeap()
        
        data = [4, 5, 7, 1, 3, 6, 10, 30]
        for x in data:
            fh.insert(x)

        self.assertEqual(fh.total_nodes, len(data))
        self.assertEqual(fh.find_min().key, 1)

        n = fh.extract_min_node()
        self.assertEqual(n.key, 1)

        self.assertEqual(fh.total_nodes, len(data) - 1)
        self.assertEqual(fh.find_min().key, 3)

    def test_fibonacci_heap_insert(self):
        """
        Test that the insert method inserts an element and doe:
        1. if the heap is empty
            1.1. sets the min_node to the inserted node
            1.2. sets the size of the heap to 1
        2. if the heap is not empty
            2.1. increase the size of the heap by 1
            2.2. leave the min_node unchanged if the node is larger
            2.3. change the min_node if the node is smaller than min_node
        """
        fh = fibonacci_heap.FibonacciHeap()
        self.assertEqual(fh.total_nodes, 0)
        self.assertEqual(fh.find_min(), None)

        # test case 1:
        fh.insert(2)
        self.assertEqual(fh.total_nodes, 1)
        self.assertEqual(fh.find_min().key, 2)

        # test case 2.1 and 2.2:
        fh.insert(4)
        self.assertEqual(fh.total_nodes, 2)
        self.assertEqual(fh.find_min().key, 2)

        # test case 2.1 and 2.3:
        fh.insert(1)
        self.assertEqual(fh.total_nodes, 3)
        self.assertEqual(fh.find_min().key, 1)

    def test_fibonacci_heap_decrease_key(self):
        """
        Test the decrease_key method of the fibonacci heap
        1. Should return the new min value after decreased key.
        2. Verifies that the heap looks as expected after decreased key.
        3. Checks to see that it the heap does not still contain the value 
            that has been decreased.
        4. Expects an expection to be thrown when decrease key value is 
            larger than min. 
        5. Decreases the key of a child so that it is smaller than the parent,
            then verifies that the node with decreased key (which is now min_node) is in root_list.
        """
        fh = fibonacci_heap.FibonacciHeap()
        data = [4, 7, 6, 3, 5]
        for x in data:
            fh.insert(x)
        fh.decrease_key(fh.find_min(), 2)
        
        # test case 1
        self.assertEqual(fh.find_min().key, 2)

        # test case 2: Positive
        decrease_data = [4, 7, 6, 2, 5]
        for x in fh.iterate(fh.root_list):
            self.assertTrue(x.key in decrease_data)

        # test case 3: Negative
        nodes = self.get_all_nodes(fh, fh.root_list)
        for i in nodes:
            self.assertFalse(i.key == 3)

        # test case 4: Exception
        with self.assertRaises(Exception):
            fh.decrease_key(fh.find_min(), 8)

        # test case 5: After extract 
        fh.extract_min_node()
        self.assertEqual(fh.root_list.child.right.key, 5)
        fh.decrease_key(fh.root_list.child, 1)
        self.assertEqual(fh.root_list.child.key, 5)
        self.assertEqual(fh.find_min().key, 1)
        self.assertTrue(fh.find_min() in fh.iterate(fh.root_list))

        # test case 6: Only one child
        fh2 = fibonacci_heap.FibonacciHeap()
        fh2.insert(4)
        fh2.insert(7)
        fh2.extract_min_node()
        fh2.decrease_key(fh2.find_min(), 2)
        self.assertEqual(fh2.root_list.child, None)

        
    def test_fibonacci_heap_merge(self):
        """
        Test that the merge method of the fibonacci heap merges two
        seperate heaps correctly
        1. the resulting heap's root_list shoulc be a concatenation
            of heap1's and heap2's root_lists
        2. merging a heap with another empty heap should not change
            the original heap
        3. mergin an empty heap with another non-empty heap should
            change the heap's min_node to the min_node of the merged
            heap
        """
        a = fibonacci_heap.FibonacciHeap()
        b = fibonacci_heap.FibonacciHeap()
        empty_heap = fibonacci_heap.FibonacciHeap()

        # Fill two heaps with data
        a_data = [4, 2, 6, 3, 5]
        for x in a_data:
            a.insert(x)
        b_data = [10, 12, 16, 100]
        for x in b_data:
            b.insert(x)

        # test case 1
        a.merge(b)
        for x in a.iterate(a.root_list):
            self.assertTrue(x.key in a_data or x.key in b_data)

        # test case 2
        min_key_before = int(b.find_min().key)
        numel_before = b.total_nodes
        b.merge(empty_heap)
        self.assertEqual(b.find_min().key, min_key_before)
        self.assertEqual(b.total_nodes, numel_before)

        # test case 3
        self.assertEqual(empty_heap.find_min(), None)
        empty_heap.merge(b)
        self.assertEqual(b.find_min().key, empty_heap.find_min().key)
        self.assertEqual(empty_heap.total_nodes, b.total_nodes)

    def test_fibonacci_heap_delete(self):
        """
        Test that the delete method of the fibonacci heap deletes nodes
        from the heap with test cases
        1. delete a root element and keep structure of tree
        2. delete a child in the tree and keep structure of tree
        """
        fh = fibonacci_heap.FibonacciHeap()
        data = [1, 10, 25, 0, 2]
        for x in data:
            fh.insert(x)

        # At this point, all elements of the tree are root elements
        self.assertEqual(fh.total_nodes, 5)

        # test case 1
        del_node_key = fh.root_list.key
        fh.delete(fh.root_list)
        self.assertEqual(fh.total_nodes, 4)
        nodes = self.get_all_nodes(fh, fh.root_list)
        for node in nodes:
            self.assertTrue(node.key != del_node_key)

        # test case 2
        del_node_key = fh.root_list.child.key
        fh.delete(fh.root_list.child)
        self.assertEqual(fh.total_nodes, 3)
        nodes = self.get_all_nodes(fh, fh.root_list)
        for node in nodes:
            self.assertTrue(node.key != del_node_key)

    def get_all_nodes(self, heap, node):
        nodes = []
        for node in heap.iterate(node):
            nodes.append(node)
            if node.child:
                nodes += self.get_all_nodes(heap, node.child)
        return nodes


if __name__ == "__main__":
    unittest.main()
