"""
This algorithm removes any duplicates from an array and returns a new array with those duplicates
removed.

For example:

Input: [1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]
Output: [1, 2, 3, 4, 'hey', 'hello']

Time Complexity: O(n) where n is the length of the input array
Space Complexity: O(n) for the seen set and result array
"""

def remove_duplicates(array):
    seen = set()
    new_array = []

    for item in array:
        if item not in seen:
            seen.add(item)
            new_array.append(item)

    return new_array
