"""
Implementation of priority queue
"""

class PriorityQueueNode:	
	def __init__(self, data, priority):
		self.data = data
		self.priority = priority

	def __repr__(self):
		return str(self.data) + ": " + str(self.priority)

class PriorityQueue:
	def __init__(self):
		self.priority_queue_list = []

	def size(self):
		return len(self.priority_queue_list)

	def insert(self, node):
		# if queue is empty
		if self.size() == 0:
			self.priority_queue_list.append(node)
		else:
			 # traverse the queue to find the right place for new node
			 for index, current in enumerate(self.priority_queue_list):
			 	if current.priority < node.priority:
			 		# if we have traversed the complete queue
			 		if index == self.size() - 1:
			 			# add new node at the end
			 			self.priority_queue_list.insert(index + 1, node)
			 		else:
			 			continue
			 	else:
			 		self.priority_queue_list.insert(index, node)
			 		return True

	def delete(self):
		# remove the first node from the queue
		return self.priority_queue_list.pop(0)
										