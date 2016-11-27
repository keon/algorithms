class Node():
    def __init__(self, val = None):
        self.val = val
        self.next = None

def printKthToLast(head):
    """
    Time Complexity: O()
    Space Complexity: O()
    """
    pass

def printLinkedList(head):
    string = ""
    while head.next:
        string += head.val + " -> "
        head = head.next
    string += head.val
    print(string)

# A A B C D C F G

a1 = Node("A")
a2 = Node("A")
b = Node("B")
c1 = Node("C")
d = Node("D")
c2 = Node("C")
f = Node("F")
g = Node("G")

a1.next = a2
a2.next = b
b.next = c1
c1.next = d
d.next = c2
c2.next = f
f.next = g

# removeDups(a1)
# printLinkedList(a1)
# removeDupsWithoutSet(a1)
# printLinkedList(a1)

