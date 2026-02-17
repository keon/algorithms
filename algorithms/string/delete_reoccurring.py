"""
Delete Reoccurring Characters

Given a string, delete any reoccurring characters and return the new string
containing only the first occurrence of each character.

Reference: https://en.wikipedia.org/wiki/Duplicate_removal

Complexity:
    Time:  O(n) where n is the length of the string
    Space: O(n)
"""

from __future__ import annotations


def delete_reoccurring_characters(string: str) -> str:
    """Remove duplicate characters, keeping only the first occurrence of each.

    Args:
        string: The input string to process.

    Returns:
        A new string with duplicate characters removed.

    Examples:
        >>> delete_reoccurring_characters("aaabcccc")
        'abc'
    """
    seen_characters: set[str] = set()
    output_string = ''
    for char in string:
        if char not in seen_characters:
            seen_characters.add(char)
            output_string += char
    return output_string
