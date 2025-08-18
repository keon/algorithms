"""
Python arrays - lists
"""


# Creating a list
empty_list = []  # Empty list
list_with_values = [1, 2, 3, 4, 5, 6]  # List with integers
list_with_mixed_values = [1, "hello", 2, "world", 3]  # Lists with different data types


"""
The below example will use the following list to show commmon list operations
"""

my_list = []

# Inserting into a list - the append method is used to insert an item at the end of a list
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
print(my_list)  # Prints -> [1, 2, 3, 4, 5]


# The insert method is used to insert a value at a particular index in the list.
# Below, we insert the value of 10 at position 3 (remember Python lists start at 0)
my_list.insert(3, 10)
print(my_list)  # Prints -> [1, 2, 3, 10, 4, 5]


# Getting from a particular location
# Python lists are '0-based', so the first item is at position 0
print(my_list[0])  # Prints -> 1
print(my_list[3])  # Prints -> 4


# Deleting from a list
# The remove method removes the first item from the list whose value is equal to x.
# It raises a ValueError if there is no such item.
my_list.remove(2)
print(my_list)  # Prints -> [1, 3, 10, 4, 5]

# The 'pop' method removes the value at a particular index and returns it
first_value = my_list.pop(0)
print(first_value)  # Prints -> 1
print(my_list)  # Prints [3, 10, 4, 5]


# Sort - The sort method is used to sort the list
my_list.sort()
print(my_list)  # Prints [3, 4, 5, 10]

# Iterating over a list
# To loop over a list, we use Python's 'for-in' syntax
for item in my_list:
    print(item)  # Prints each number on a new line

# Iterating and getting index
# To loop over list and get index, use enumerate
for index, item in enumerate(my_list):
    print(index, item)  # See output below

"""
(0, 3)
(1, 4)
(2, 5)
(3, 10)
"""


# Reverse the elements in a list
my_list.reverse()
print(my_list)  # Prints -> [10, 5, 4, 3]

# Empty/Clear a list
del my_list[:]  # From Python 3.3 onwards, you can use my_list.clear() to empty a list
print(my_list)  # Prints -> []
