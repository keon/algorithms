"""
Unique Morse Code Representations

Given a list of words, determine the number of unique Morse code
transformations among all the words.

Reference: https://leetcode.com/problems/unique-morse-code-words/

Complexity:
    Time:  O(n * k) where n is the number of words, k is average word length
    Space: O(n)
"""

from __future__ import annotations

_MORSE_CODE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def convert_morse_word(word: str) -> str:
    """Convert a word to its Morse code representation.

    Args:
        word: The word to convert (case-insensitive).

    Returns:
        The Morse code string for the word.

    Examples:
        >>> convert_morse_word("gin")
        '--...-.'
    """
    morse_word = ""
    word = word.lower()
    for char in word:
        morse_word = morse_word + _MORSE_CODE[char]
    return morse_word


def unique_morse(words: list[str]) -> int:
    """Count the number of unique Morse code transformations.

    Args:
        words: A list of words to transform and count.

    Returns:
        The number of distinct Morse code representations.

    Examples:
        >>> unique_morse(["gin", "zen", "gig", "msg"])
        2
    """
    unique_transformations: list[str] = []
    for word in words:
        morse_word = convert_morse_word(word)
        if morse_word not in unique_transformations:
            unique_transformations.append(morse_word)
    return len(unique_transformations)
