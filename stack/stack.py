"""
Stack Abstract Data Type (ADT)
Stack() creates a new stack that is empty.
   It needs no parameters and returns an empty stack.
push(item) adds a new item to the top of the stack.
   It needs the item and returns nothing.
pop() removes the top item from the stack.
   It needs no parameters and returns the item. The stack is modified.
peek() returns the top item from the stack but does not remove it.
   It needs no parameters. The stack is not modified.
isEmpty() tests to see whether the stack is empty.
   It needs no parameters and returns a boolean value.
size() returns the number of items on the stack.
   It needs no parameters and returns an integer.
"""
from abc import ABCMeta, abstractmethod
class AbstractStack(metaclass=ABCMeta):
    """Abstract Class for Stacks."""
    def __init__(self):
        self._top = -1

    def __len__(self):
        return self._top + 1

    def __str__(self):
        result = " ".join(map(str, self))
        return 'Top-> ' + result

    def is_empty(self):
        return self._top == -1

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def push(self, value):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass


class ArrayStack(AbstractStack):
    def __init__(self, size=10):
        """
        Initialize python List with size of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        super().__init__()
        self._array = [None] * size

    def __iter__(self):
        probe = self._top
        while True:
            if probe == -1:
                return
            yield self._array[probe]
            probe -= 1

    def push(self, value):
        self._top += 1
        if self._top == len(self._array):
            self._expand()
        self._array[self._top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        value = self._array[self._top]
        self._top -= 1
        return value

    def peek(self):
        """returns the current top element of the stack."""
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._array[self._top]

    def _expand(self):
        """
         expands size of the array.
         Time Complexity: O(n)
        """
        self._array += [None] * len(self._array)  # double the size of the array


class StackNode:
    """Represents a single stack node."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack(AbstractStack):

    def __init__(self):
        super().__init__()
        self.head = None

    def __iter__(self):
        probe = self.head
        while True:
            if probe is None:
                return
            yield probe.value
            probe = probe.next

    def push(self, value):
        node = StackNode(value)
        node.next = self.head
        self.head = node
        self._top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.head.value
        self.head = self.head.next
        self._top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.value
