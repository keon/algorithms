"""
This algorithm removes any duplicates from an array and returns a new array with those duplicates
removed.

For example:

Input: [1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True, False]
Output: [1, 2, 3, 4, 'hey', 'hello', True, False]
"""


def remove_duplicates(array):
    """Removes duplicates from the input array while preserving the order of the first occurrence of each distinct item.

    Args:
        array (list): The input array containing elements with potential duplicates.

    Returns:
        list: A new array with duplicates removed, maintaining the order of the first occurrence of each item.

    Examples:
        >>> remove_duplicates([1, 1, 1, 2, 2, 3, 4, 4, "hey", "hey", "hello", True, True, False])
        [1, 2, 3, 4, 'hey', 'hello', True, False]
    """
    new_array = []  # Preserve order of first distinct item
    seen = set()  # Track the unique items

    for item in array:
        if all([item is not elem for elem in seen]):
            new_array.append(item)
            seen.add(item)

    return new_array
