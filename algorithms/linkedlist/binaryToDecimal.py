# converts binary linked list to decimal value
# Eg : Linked List (Input): 1 -> 1 -> 1
#      Decimal value (Output): 7


#to represent each node of Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#to create linkedlist
class LinkedList:
    def __init__(self):
        self.head = None

    def getDecimal(self,head):
        ans = 0
        while head:
            ans = (ans * 2) + head.data
            head = head.next
        return ans

list = LinkedList()

list.head = Node(1);
list.head.next = Node(1);
list.head.next.next = Node(1);

print ("Decimal Value : {}".format(list.getDecimal(list.head)))
