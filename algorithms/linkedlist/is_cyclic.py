"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
class Node:

    def __init__(self, x):
        self.val = x
        self.next = None

def is_cyclic(head):
    """
    :type head: Node
    :rtype: bool
    """
    if not head:
        return False
    runner = head
    walker = head
    while runner.next and runner.next.next:
        runner = runner.next.next
        walker = walker.next
        if runner == walker:
            return True
    return False

# Approach 2 : using Floyd's cycle finding algorithm
# Node class:
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def strnode (self):
        print(self.data)

# LinkedList class:
class LinkedList:
    def __init__(self):
        self.numnodes = 0
        self.head = None

    def insertLast(self, data):
        newnode = Node(data)
        newnode.next = None
        if self.head == None:
            self.head = newnode
            return

        lnode = self.head
        while lnode.next != None :
            lnode = lnode.next
        lnode.next = newnode # new node is now the last node
        self.numnodes += 1

   # Cycle/Loop detection function: (returns boolean true/false)
    def has_cycle(self):    
        slow, fast = self.head ,self.head  
        while fast != None:       
            if fast.next != None:
                 fast = fast.next.next
            else:
                 return False
            slow = slow.next  
            if slow == fast:
                print("--slow",slow.data, "fast",fast.data) 
                return True    
        return False

# Create a LinkedList:
linkedList = LinkedList()
linkedList.insertLast("12")
linkedList.insertLast("5")
linkedList.insertLast("13")

# Create a loop for testing:
linkedList.head.next.next.next = linkedList.head; 
# Check for cycle/loop:
print(linkedList.has_cycle())
