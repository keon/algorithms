# Pros
# Linked Lists have constant-time insertions and deletions in any position,
# in comparison, arrays require O(n) time to do the same thing.
# Linked lists can continue to expand without having to specify
# their size ahead of time (remember our lectures on Array sizing
# from the Array Sequence section of the course!)

# Cons
# To access an element in a linked list, you need to take O(k) time
# to go from the head of the list to the kth element.
# In contrast, arrays have constant time operations to access
# elements in an array.

class NodeD:

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class Doublelinkedlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.ctr = 0

    def Insert(self, Data):

        newNode = NodeD(Data)

        if (self.head == None):

            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None


        else:

            self.head.previous = newNode
            newNode.next = self.head
            newNode.previous = None
            self.head = newNode


    def deletearbitary(self, index):

        node_del = NodeD(index)
        if self.head == None:
            print("Node is Empty")
        else:
            if  self.head == node_del:
                self.head = self.head.next
                self.head.previous = None
                self.ctr -= 1

            else:
                temp = self.head

                while temp.next is not None:
                    
                  if temp == node_del:
                    break
                  else:
                    print(temp.data,"\n")
                    temp = temp.next

                print("Node deleted", temp.data)
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                temp.next = None
                temp.previous = None
                self.ctr -= 1
                return

    def search_book(self):

        curNode = self.head
        if (self.head == None):
            print("This Library Has No Book Like this : Sorry")
            return

        while (curNode is not None):
            #if curNode.data == booktosearch:
            print(f"The Book You Looking for is Available {curNode.data}")
                #break
            #else:
            curNode = curNode.next
            
 d = Doublelinkedlist()

d.Insert("Book1")
d.Insert("Book2")
d.Insert("Book3")
d.Insert("Book4")
d.Insert("Book5")
d.Insert("Book6")
d.search_book()
d.deletearbitary("Book5")
d.search_book()
#Single Link List 

class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__ (self):
        self.head = None

    def listprint(self):
        temp = self.head
        count = 0
        while (temp is not None):
            count += 1
            print(f"This Item  {temp.data} is at Postion {count-1}")
            temp = temp.next
        print("\n")
    def AppendatEnd(self, data):

        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        Last = self.head
        while (Last.next):
            Last = Last.next
        Last.next = NewNode


    def AppendatFrist(self, data):

        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def Node_Position(self,val):

        count = 0
        temp = self.head
        while (temp != None):
            if temp.data == val :
                return count
            else:
                count += 1
                temp = temp.next


    def isEmpty(self):
        return self.head.next == None

    def sizeoflist(self):
        count = 0
        temp = self.head
        while (temp != None):
            count += 1
            temp = temp.next
        return count

    def AppendatArbitrary(self,pos, item ):
        if  self.isEmpty():
            print("No Item in the List")
        else:
            if (pos == 0):
                NewNode = Node(item)
                NewNode.next = self.head
                self.head = NewNode
            else:
                count = 0
                temp = self.head
                while (temp != None and count != pos):
                    temp = temp.next
                    count += 1
                NewNode = Node(item)
                NewNode.next = temp.next
                temp.next = NewNode
                return True

    def Delatfront(self):

        if (self.head != None):
            temp = self.head
            self.head = temp.next
            temp = None

    def Delatlast(self):

        if (self.head != None):
            if (self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while (temp.next.next != None):
                    temp = temp.next
                LastNode = temp.next
                temp.next = None
                LastNode = None

    def NodetoDelete(self,pos):

        if  self.isEmpty():
            print("No Item In The List")
        else:
            if (pos == 1):
                NodetoDel = self.head
                self.head = NodetoDel.next
                NodetoDel = None
            else:
                count = 0
                temp = self.head
                while (temp != None and count != pos):
                    temp = temp.next
                    count += 1
                Nodetodel = temp
                temp = temp.next
                Nodetodel = None
                return True

List = LinkedList()

sizef = int(input("How Many Elements You Want to Enter in the LinkList from Front: "))
for i in range(0,sizef):
    List.AppendatFrist(input("Enter Three Value At First In a Link List: "))
List.listprint()

sizel = int(input("How Many Elements You Want to Enter in the LinkList from End: "))
for i in range(0,sizel):
    List.AppendatEnd(input("Enter Three Value At Last In a Link List: "))
List.listprint()

x,y = input("Enter Index After which  you want to Add the Node and the the Value (Separate it by comma ','):").split(",")
if int(x) > List.sizeoflist():
    print("No Index Found")
else:
    List.AppendatArbitrary(int(x),y)
    List.listprint()

print("Deleting a Node From The Front: ")
List.Delatfront()
List.listprint()

print("Deleting a Node From The End: ")
List.Delatlast()
List.listprint()

z = int(input("Enter a Postion From which You want to remove the Node: "))
List.NodetoDelete(z)
List.listprint()

        
