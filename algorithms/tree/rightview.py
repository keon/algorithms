
# Python3 program to print right
# view of Binary Tree
from collections import deque

# A binary tree node


class Node:

	# A constructor to create a new
	# Binary tree Node
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

# Function to print Right view of
# binary tree


def rightView(root):

	if root is None:
		return

	q = deque()
	q.append(root)

	while q:

		# Get number of nodes for each level
		n = len(q)

		# Traverse all the nodes of the
		# current level

		while n > 0:
			n -= 1

			# Get the front node in the queue
			node = q.popleft()

			# Print the last node of each level
			if n == 0:
				print(node.data, end=" ")

			# If left child is not null push it
			# into the queue
			if node.left:
				q.append(node.left)

			# If right child is not null push
			# it into the queue
			if node.right:
				q.append(node.right)

# Driver code


# Let's construct the tree as
# shown in example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

rightView(root)

# This code is contributed by Pulkit Pansari
