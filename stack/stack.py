# Stack Abstract Data Type (ADT)
# Stack() creates a new stack that is empty.
#    It needs no parameters and returns an empty stack.
# push(item) adds a new item to the top of the stack.
#    It needs the item and returns nothing.
# pop() removes the top item from the stack.
#    It needs no parameters and returns the item. The stack is modified.
# peek() returns the top item from the stack but does not remove it.
#    It needs no parameters. The stack is not modified.
# isEmpty() tests to see whether the stack is empty.
#    It needs no parameters and returns a boolean value.
# size() returns the number of items on the stack.
#    It needs no parameters and returns an integer.

class AbstractStack:
    def __init__(self):
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def __len__(self):
        return self.top

    def __str__(self):
        result = '------\n'
        for element in self:
            result += str(element) + '\n'
        return result[:-1] + '\n------'

class ArrayStack(AbstractStack):
    def __init__(self, size=10):
        """
        Initialize python List with size of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        AbstractStack.__init__(self)
        self.array = [None] * size

    def push(self, value):
        if self.top == len(self.array):
            self.expand()
        self.array[self.top] = value
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        value = self.array[self.top - 1]
        self.array[self.top - 1] = None
        self.top -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.array[self.top]

    def expand(self):
        """
         expands size of the array.
         Time Complexity: O(n)
        """
        newArray = [None] * len(self.array) * 2 # double the size of the array
        for i, element in enumerate(self.array):
            newArray[i] = element
        self.array = newArray

    def __iter__(self):
        probe = self.top - 1
        while True:
            if probe < 0:
                raise StopIteration
            yield self.array[probe]
            probe -= 1

class StackNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack(AbstractStack):
    def __init__(self):
        AbstractStack.__init__(self)
        self.head = None

    def push(self, value):
        node = StackNode(value)
        node.next = self.head
        self.head = node
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        value = self.head.value
        self.head = self.head.next
        self.top -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.head.value

    def __iter__(self):
        probe = self.head
        while True:
            if probe is None:
                raise StopIteration
            yield probe.value
            probe = probe.next
