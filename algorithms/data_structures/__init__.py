"""Reusable data structure implementations.

This package contains the core data structures used throughout the library.
Each module provides a self-contained implementation suitable for study.

    >>> from algorithms.data_structures import BinaryHeap, ArrayStack
"""

from algorithms.data_structures.graph import DirectedEdge, DirectedGraph, Node
from algorithms.data_structures.hash_table import HashTable, ResizableHashTable
from algorithms.data_structures.heap import AbstractHeap, BinaryHeap
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
from algorithms.data_structures.separate_chaining_hash_table import (
    SeparateChainingHashTable,
)
from algorithms.data_structures.stack import (
    AbstractStack,
    ArrayStack,
    LinkedListStack,
    StackNode,
)
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
]
