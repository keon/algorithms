"""
Is Palindrome

Determine if a string is a palindrome, considering only alphanumeric
characters and ignoring cases. Multiple approaches are provided.

Reference: https://en.wikipedia.org/wiki/Palindrome

Complexity:
    Time:  O(n) for all variations
    Space: O(n) for variations that create new strings, O(1) for two-pointer
"""

from __future__ import annotations

from collections import deque
from string import ascii_letters


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome using two pointers on the original.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("Otto")
        True
    """
    left = 0
    right = len(text) - 1
    while left < right:
        while not text[left].isalnum():
            left += 1
        while not text[right].isalnum():
            right -= 1
        if text[left].lower() != text[right].lower():
            return False
        left, right = left + 1, right - 1
    return True


def _remove_punctuation(text: str) -> str:
    """Remove punctuation, case sensitivity and spaces from a string.

    Args:
        text: The input string to clean.

    Returns:
        A lowercase string with only alphabetic characters.
    """
    return "".join(char.lower() for char in text if char in ascii_letters)


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

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_reverse("Otto")
        True
    """
    text = _remove_punctuation(text)
    if text == _string_reverse(text):
        return True
    return False


def is_palindrome_two_pointer(text: str) -> bool:
    """Check if a string is a palindrome using two pointers from both ends.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_two_pointer("Otto")
        True
    """
    text = _remove_punctuation(text)
    for index in range(0, len(text) // 2):
        if text[index] != text[len(text) - index - 1]:
            return False
    return True


def is_palindrome_stack(text: str) -> bool:
    """Check if a string is a palindrome using a stack.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_stack("Otto")
        True
    """
    stack: list[str] = []
    text = _remove_punctuation(text)
    for index in range(len(text) // 2, len(text)):
        stack.append(text[index])
    for index in range(0, len(text) // 2):
        if text[index] != stack.pop():
            return False
    return True


def is_palindrome_deque(text: str) -> bool:
    """Check if a string is a palindrome using a deque.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_deque("Otto")
        True
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
