"""Queue-based algorithm implementations."""

from __future__ import annotations

from .max_sliding_window import max_sliding_window
from .moving_average import MovingAverage
from .priority_queue import PriorityQueue, PriorityQueueNode
from .queue import AbstractQueue, ArrayQueue, LinkedListQueue, QueueNode
from .reconstruct_queue import reconstruct_queue
from .zigzagiterator import ZigZagIterator

__all__ = [
    "AbstractQueue",
    "ArrayQueue",
    "LinkedListQueue",
    "MovingAverage",
    "PriorityQueue",
    "PriorityQueueNode",
    "QueueNode",
    "ZigZagIterator",
    "max_sliding_window",
    "reconstruct_queue",
]
