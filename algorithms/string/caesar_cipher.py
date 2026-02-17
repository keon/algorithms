"""
Caesar Cipher

Caesar's cipher shifts each letter by a fixed number of positions in the
alphabet. Letters wrap around when they pass the end of the alphabet.

Reference: https://en.wikipedia.org/wiki/Caesar_cipher

Complexity:
    Time:  O(n) where n is the length of the input string
    Space: O(n)
"""

from __future__ import annotations


def caesar_cipher(text: str, shift: int) -> str:
    """Encrypt a string using the Caesar cipher with the given shift.

    Args:
        text: The plaintext string to encrypt.
        shift: The number of positions to shift each letter.

    Returns:
        The encrypted string with shifted letters.

    Examples:
        >>> caesar_cipher("Hello_World!", 4)
        'Lipps_Asvph!'
    """
    result = ""
    for char in text:
        code = ord(char)
        if 64 < code < 91:
            code = ((code - 65 + shift) % 26) + 65
        if 96 < code < 123:
            code = ((code - 97 + shift) % 26) + 97
        result = result + chr(code)
    return result
