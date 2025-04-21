"""
This module demonstrates multiple methods for reversing a string in Python.

Summary of String Reversal Implementations

| Function         | Time Complexity | Space Complexity | Notes                              |
|------------------|------------------|------------------|------------------------------------|
| recursive        | O(n log n)       | O(n)             | Recursive with slicing and concat  |
| iterative        | O(n)             | O(n)             | In-place list swapping             |
| pythonic         | O(n)             | O(n)             | Uses reversed() and join()         |
| ultra_pythonic   | O(n)             | O(n)             | Uses slicing (s[::-1])             |

All functions return the reversed version of the input string.
Note: Strings in Python are immutable, so all methods produce a new string.
"""

def recursive(s):
    """
    Reverses a given string using a recursive divide-and-conquer approach.

    This function recursively splits the input string `s` into two halves,
    reverses each half by further recursive calls, and then concatenates
    them in reverse order to form the final reversed string.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Example:
        >>> recursive("hello")
        'olleh'

    Note:
        - This approach is primarily educational.
        - Time complexity is O(n log n) due to repeated slicing and concatenation.
        - Space complexity is also higher because of the call stack and substring creation.
        - It may hit Python's recursion depth limit on very long strings.
    """
    l = len(s)
    if l < 2:
        return s
    return recursive(s[l//2:]) + recursive(s[:l//2])

def iterative(s):
    """
    Reverses a given string using an iterative approach with two-pointer swapping.

    This function converts the string `s` into a list of characters and then iteratively swaps
    the characters from the start and end of the list, moving towards the center. The process
    continues until the entire string is reversed.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Example:
        >>> iterative("hello")
        'olleh'

    Note:
        - Time complexity is O(n), where n is the length of the string `s`.
        - Space complexity is O(n) due to the list copy of the string.
        - The actual reversal is performed in-place on the list using O(1) additional working space.
    """
    r = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1
    return "".join(r)

def pythonic(s):
    """
    Reverses a given string using the built-in `reversed()` function.

    This function returns a new string that is the reverse of the input string `s`.
    It uses the `reversed()` function to create an iterator over the input string,
    and then joins the elements of the iterator to form the reversed string.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Example:
        >>> pythonic("hello")
        'olleh'

    Note:
        This function has a time complexity of O(n), where n is the length of the string `s`.
        It does not modify the original string, as strings in Python are immutable.
    """
    return "".join(reversed(s))

def ultra_pythonic(s):
    """
    Reverses a given string using Python's slicing feature.

    This function utilizes Python's slicing syntax to reverse the input string `s`.
    It returns a new string where the characters of `s` are arranged in reverse order.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Example:
        >>> ultra_pythonic("hello")
        'olleh'

    Note:
        This function is concise and efficient, with a time complexity of O(n),
        where n is the length of the string `s`. It does not modify the original string.
    """
    return s[::-1]
