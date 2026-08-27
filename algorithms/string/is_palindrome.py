"""Is Palindrome.

Determine if a string is a palindrome, considering only alphanumeric
characters and ignoring cases. Multiple approaches are provided.

Reference: https://en.wikipedia.org/wiki/Palindrome

Complexity:
    Time:  O(n) for all variations
    Space: O(n) for variations that create new strings, O(1) for two-pointer
"""

from __future__ import annotations

from collections import deque


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome using two pointers on the original.

    Considers only alphanumeric characters and ignores case.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("Otto")
        True
        >>> is_palindrome("12321")
        True
        >>> is_palindrome("a1b2a")
        False

    """
    left = 0
    right = len(text) - 1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left].lower() != text[right].lower():
            return False
        left, right = left + 1, right - 1
    return True


def _remove_punctuation(text: str) -> str:
    """Remove non-alphanumeric characters and normalise case.

    Args:
        text: The input string to clean.

    Returns:
        A lowercase string containing only alphanumeric characters.

    """
    return "".join(char.lower() for char in text if char.isalnum())


def _string_reverse(text: str) -> str:
    """Reverse a string using slicing.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.

    """
    return text[::-1]


def is_palindrome_reverse(text: str) -> bool:
    """Check if a string is a palindrome by comparing with its reverse.

    Considers only alphanumeric characters and ignores case.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_reverse("Otto")
        True
        >>> is_palindrome_reverse("12321")
        True
        >>> is_palindrome_reverse("a1b2a")
        False

    """
    text = _remove_punctuation(text)
    return text == _string_reverse(text)


def is_palindrome_two_pointer(text: str) -> bool:
    """Check if a string is a palindrome using two pointers from both ends.

    Considers only alphanumeric characters and ignores case.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_two_pointer("Otto")
        True
        >>> is_palindrome_two_pointer("12321")
        True
        >>> is_palindrome_two_pointer("a1b2a")
        False

    """
    text = _remove_punctuation(text)
    for index in range(len(text) // 2):
        if text[index] != text[len(text) - index - 1]:
            return False
    return True


def is_palindrome_stack(text: str) -> bool:
    """Check if a string is a palindrome using a stack.

    Considers only alphanumeric characters and ignores case.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_stack("Otto")
        True
        >>> is_palindrome_stack("12321")
        True
        >>> is_palindrome_stack("a1b2a")
        False

    """
    stack: list[str] = []
    text = _remove_punctuation(text)
    for index in range(len(text) // 2, len(text)):
        stack.append(text[index])
    return all(text[index] == stack.pop() for index in range(len(text) // 2))


def is_palindrome_deque(text: str) -> bool:
    """Check if a string is a palindrome using a deque.

    Considers only alphanumeric characters and ignores case.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_deque("Otto")
        True
        >>> is_palindrome_deque("12321")
        True
        >>> is_palindrome_deque("a1b2a")
        False

    """
    text = _remove_punctuation(text)
    character_deque: deque[str] = deque()
    for char in text:
        character_deque.appendleft(char)

    equal = True
    while len(character_deque) > 1 and equal:
        first = character_deque.pop()
        last = character_deque.popleft()
        if first != last:
            equal = False

    return equal
