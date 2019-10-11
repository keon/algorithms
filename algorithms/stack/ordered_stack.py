#The stack remains always ordered such that the highest value is at the top and the lowest at the bottom

class OrderedStack:
     def __init__(self):
         self.items = []

     def is_empty(self):
         return self.items == []

     def push_t(self, item):
         self.items.append(item)

     def push(self, item): #push method to maintain order when pushing new elements
         temp_stack = OrderedStack()
         if self.is_empty() or item > self.peek():
             self.push_t(item)
         else:
             while item < self.peek() and not self.is_empty():
                 temp_stack.push_t(self.pop())
             self.push_t(item)
             while not temp_stack.is_empty():
                 self.push_t(temp_stack.pop())

     def pop(self):
         if self.is_empty():
             raise IndexError("Stack is empty")
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items) - 1]

     def size(self):
         return len(self.items)
