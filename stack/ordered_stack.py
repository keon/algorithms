#The stack remains always ordered such that the highest value is at the top and the lowest at the bottom

class OrderedStack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def pushT(self, item):
         self.items.append(item)

     def push(self, item): #push method to maintain order when pushing new elements
         temp = OrderedStack()
         if self.isEmpty() or item > self.peek():
             self.pushT(item)
             return self.items
         else:
             while (item < self.peek()) and (not self.isEmpty()):
                 temp.pushT(self.pop())
             self.pushT(item)
             while not(temp.isEmpty()):
                 self.pushT(temp.pop())
             return self.items

     def pop(self):
         if self.isEmpty():
             raise IndexError("Stack is empty")
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items) - 1]

     def size(self):
         return len(self.items)
