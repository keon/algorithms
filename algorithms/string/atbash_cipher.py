"""
Atbash Cipher

Atbash cipher maps each letter of the alphabet to its reverse.
The first letter 'a' maps to 'z', 'b' maps to 'y', and so on.

Reference: https://en.wikipedia.org/wiki/Atbash

Complexity:
    Time:  O(n) where n is the length of the input string
    Space: O(n)
"""

from __future__ import annotations


def atbash(text: str) -> str:
    """Encrypt or decrypt a string using the Atbash cipher.

    Args:
        text: The input string to transform.

    Returns:
        The Atbash-transformed string.

    Examples:
        >>> atbash("abcdefghijklmno")
        'zyxwvutsrqponml'
    """
    translated = ""
    for char in text:
        code = ord(char)
        if char.isalpha():
            if char.isupper():
                offset = code - ord("A")
                translated += chr(ord("Z") - offset)
            elif char.islower():
                offset = code - ord("a")
                translated += chr(ord("z") - offset)
        else:
            translated += char
    return translated
