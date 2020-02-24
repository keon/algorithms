"""
Resource: https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf
Chapter 19, fibonacci heap
"""

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

    def find_min(self):
        pass

    def merge(self, heap2):
        pass

    def insert(self, data):
        pass

    def extract_min_node(self):
        pass

    def remove(self, node):
        pass

    def decrease_key(self, node, key):
        pass
