"""
This algorithm removes any duplicates from an array and returns a new array with those duplicates
removed.

For example:

Input: [1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]
Output: [1, 2, 3, 4, 'hey', 'hello']
"""

def remove_duplicates(array):
    new_array = []

    for item in array:
        if item not in new_array:
            new_array.append(item)

    return new_array