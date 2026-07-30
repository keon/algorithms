"""
Lempel-Ziv-Welch (LZW) Compression

A dictionary-based lossless compression algorithm. It builds a dictionary of
substrings during encoding and replaces repeated substrings with dictionary
codes. Decompression reconstructs the same dictionary on the fly to recover
the original data.

Reference: https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch

Complexity:
    Time:  O(n) for both encoding and decoding
    Space: O(n) for the dictionary/code table
"""

from __future__ import annotations


def _build_initial_dictionary(data: str) -> dict[str, int]:
    """Create the initial dictionary containing all unique input characters.

    Args:
        data: The input string.

    Returns:
        A dictionary mapping characters to integer codes.
    """
    return {char: index for index, char in enumerate(sorted(set(data)))}


def lzw_encode(data: str) -> tuple[list[int], dict[int, str]]:
    """Compress a string using the LZW algorithm.

    Args:
        data: The input string to compress.

    Returns:
        A tuple of the integer codes representing the compressed data and the
        initial code-to-character dictionary needed for decoding.

    Examples:
        >>> codes, dictionary = lzw_encode("ABABABA")
        >>> codes
        [0, 1, 2, 4]
        >>> dictionary
        {0: 'A', 1: 'B'}
        >>> lzw_encode("")
        ([], {})
    """
    if not data:
        return [], {}

    dictionary = _build_initial_dictionary(data)
    next_code = len(dictionary)
    encoded: list[int] = []
    current: str = ""

    for char in data:
        combined = current + char
        if combined in dictionary:
            current = combined
        else:
            encoded.append(dictionary[current])
            dictionary[combined] = next_code
            next_code += 1
            current = char

    if current:
        encoded.append(dictionary[current])

    initial_dictionary = {
        code: char
        for char, code in dictionary.items()
        if len(char) == 1
    }
    return encoded, initial_dictionary


def lzw_decode(encoded: list[int], initial_dictionary: dict[int, str]) -> str:
    """Decompress a list of LZW codes back into the original string.

    Args:
        encoded: The list of integer codes produced by lzw_encode.
        initial_dictionary: Mapping of initial codes to single-character
            strings, as returned by lzw_encode.

    Returns:
        The decoded original string.

    Examples:
        >>> lzw_decode([0, 1, 2, 4], {0: "A", 1: "B"})
        'ABABABA'
        >>> lzw_decode([], {})
        ''
    """
    if not encoded:
        return ""

    codes_to_strings = dict(initial_dictionary)
    next_code = max(codes_to_strings.keys()) + 1
    decoded: str = ""
    previous: str = ""

    for code in encoded:
        if code in codes_to_strings:
            current = codes_to_strings[code]
        elif code == next_code and previous:
            current = previous + previous[0]
        else:
            raise ValueError(f"Invalid LZW code: {code}")

        decoded += current

        if previous:
            codes_to_strings[next_code] = previous + current[0]
            next_code += 1

        previous = current

    return decoded
