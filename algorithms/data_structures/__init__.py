"""Reusable data structure implementations.

This package contains the core data structures used throughout the library.
Each module provides a self-contained implementation suitable for study.

    >>> from algorithms.data_structures import BinaryHeap, ArrayStack
"""

# Tree data structures (moved from tree/ subdirectories in Phase 8)
from algorithms.data_structures.avl_tree import AvlTree
from algorithms.data_structures.b_tree import BTree
from algorithms.data_structures.bst import BST
from algorithms.data_structures.fenwick_tree import Fenwick_Tree
from algorithms.data_structures.graph import DirectedEdge, DirectedGraph, Node
from algorithms.data_structures.hash_table import HashTable, ResizableHashTable
from algorithms.data_structures.heap import AbstractHeap, BinaryHeap
from algorithms.data_structures.iterative_segment_tree import SegmentTree
from algorithms.data_structures.linked_list import (
    DoublyLinkedListNode,
    SinglyLinkedListNode,
)
from algorithms.data_structures.priority_queue import PriorityQueue, PriorityQueueNode
from algorithms.data_structures.queue import (
    AbstractQueue,
    ArrayQueue,
    LinkedListQueue,
    QueueNode,
)
from algorithms.data_structures.red_black_tree import RBTree
from algorithms.data_structures.segment_tree import SegmentTree as SegmentTreeRecursive
from algorithms.data_structures.separate_chaining_hash_table import (
    SeparateChainingHashTable,
)
from algorithms.data_structures.stack import (
    AbstractStack,
    ArrayStack,
    LinkedListStack,
    StackNode,
)
from algorithms.data_structures.trie import Trie
from algorithms.data_structures.union_find import Union

__all__ = [
    "AbstractHeap",
    "AbstractQueue",
    "AbstractStack",
    "ArrayQueue",
    "ArrayStack",
    "BinaryHeap",
    "DirectedEdge",
    "DirectedGraph",
    "DoublyLinkedListNode",
    "HashTable",
    "LinkedListQueue",
    "LinkedListStack",
    "Node",
    "PriorityQueue",
    "PriorityQueueNode",
    "QueueNode",
    "ResizableHashTable",
    "SeparateChainingHashTable",
    "SinglyLinkedListNode",
    "StackNode",
    "Union",
    # Tree data structures
    "AvlTree",
    "BTree",
    "BST",
    "Fenwick_Tree",
    "RBTree",
    "SegmentTree",
    "SegmentTreeRecursive",
    "Trie",
]
