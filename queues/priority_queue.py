"""
Implementation of priority queue using linear array.
Insertion - O(n)
Extract min/max Node - O(1)
"""
import collections


class PriorityQueueNode:
	def __init__(self, data, priority):
		self.data = data
		self.priority = priority

	def __repr__(self):
		return str(self.data) + ": " + str(self.priority)

class PriorityQueue:
	def __init__(self):
		self.priority_queue_list = collections.deque()

	def __repr__(self):
	    return "PriorityQueue({!r})".format(list(self.priority_queue_list))

	def size(self):
		return len(self.priority_queue_list)

	def push(self, item, priority=None):
		priority = item if priority is None else priority
		node = PriorityQueueNode(item, priority)
		for index, current in enumerate(self.priority_queue_list):
			if current.priority > node.priority:
				self.priority_queue_list.insert(index, node)
				return
		# when traversed complete queue
		self.priority_queue_list.append(node)

	def pop(self):
		# remove and return the first node from the queue
		return self.priority_queue_list.popleft()
