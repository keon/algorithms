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


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome using two pointers on the original.
    This version is optimized for space (O(1)) and correctly handles strings
    with no alphanumeric characters.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("Otto")
        True
        >>> is_palindrome("!!!")
        True
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
    """Remove punctuation, case sensitivity and spaces from a string.

    Args:
        text: The input string to clean.

    Returns:
        A lowercase string with only alphanumeric characters.
    """
    return "".join(char.lower() for char in text if char.isalnum())


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
    clean_text = _remove_punctuation(text)
    return clean_text == clean_text[::-1]


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
    n = len(text)
    for index in range(n // 2):
        if text[index] != text[n - index - 1]:
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
    text = _remove_punctuation(text)
    n = len(text)
    stack = list(text[:n // 2])
    
    # Skip middle element for odd length strings
    start_second_half = n // 2 if n % 2 == 0 else n // 2 + 1
    
    for i in range(start_second_half, n):
        if text[i] != stack.pop():
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
    character_deque = deque(text)

    while len(character_deque) > 1:
        if character_deque.popleft() != character_deque.pop():
            return False

    return True
