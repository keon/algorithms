"""
Find the start of a linked list loop

Some constraints:
* It is gonna be a singly linked list.
* The parameter is not always gonna be a circular linked list.
* Once the loop is found, return the node.

Test Cases:
* Empty list -> None
* Not a circular linked list -> None
	* One element
	* Two or more elements
* Circular linked list general case
"""
class LinkedList:

	def __init__(self):
		self.root = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node	

	def find_loop_start(self):
		if self.root is None or self.root.next is None:
			return None

		# Detect loop using Floyd’s Cycle detection algorithm 
		slow = fast = self.root
		while fast.root is not None:
			slow = slow.next
			fast = fast.next.next

			if fast is None:
				return None

			if fast == slow:
				break

		# check for the starting node
		slow = self.root
		while slow != fast:
			slow = slow.next
			fast = fast.next

			if fast is None:
				return None
		return slow	

class Node:
	
	def __init__(self, _value):
		self.value = _value
		self.next = None							 


linked_list = LinkedList()
linked_list.push(10)
linked_list.push(4)
linked_list.push(15)
linked_list.push(20)
linked_list.push(50)

# Make it a circular linked list
linked_list.root.next.next.next.next.next = linked_list.root.next.next
