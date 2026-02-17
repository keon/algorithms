"""
Breaking Bad Symbol Matching

Given an array of words and an array of symbols, display each word with its
matched symbol surrounded by square brackets. If a word matches more than one
symbol, choose the one with the longest length.

Reference: https://en.wikipedia.org/wiki/Trie

Complexity:
    Time:  O(n * m) for brute force, O(n * k) for trie-based approach
    Space: O(n * m) for storing results
"""

from __future__ import annotations

import re
from functools import reduce


def match_symbol(words: list[str], symbols: list[str]) -> list[str]:
    """Match symbols in words using regex and surround matches with brackets.

    Args:
        words: List of words to search through.
        symbols: List of symbols to match within the words.

    Returns:
        List of words with matched symbols surrounded by square brackets.

    Examples:
        >>> match_symbol(['Google'], ['le'])
        ['Goog[le]']
    """
    combined = []
    for symbol in symbols:
        for word in words:
            match = re.search(symbol, word)
            if match:
                combined.append(re.sub(symbol, f"[{symbol}]", word))
    return combined


def match_symbol_1(words: list[str], symbols: list[str]) -> list[str]:
    """Match the longest symbol in each word using sorted symbol list.

    Args:
        words: List of words to search through.
        symbols: List of symbols to match, sorted by length descending.

    Returns:
        List of words with the longest matched symbol bracketed.

    Examples:
        >>> match_symbol_1(['Microsoft'], ['i', 'cro'])
        ['Mi[cro]soft']
    """
    result = []
    symbols = sorted(symbols, key=lambda item: len(item), reverse=True)
    for word in words:
        word_replaced = ""
        for symbol in symbols:
            if word.find(symbol) != -1:
                word_replaced = word.replace(symbol, "[" + symbol + "]")
                result.append(word_replaced)
                break
        if word_replaced == "":
            result.append(word)
    return result


class _TrieNode:
    """Internal trie node for the bracket function."""

    def __init__(self) -> None:
        self.children: dict[str, _TrieNode] = {}
        self.symbol: str | None = None


def bracket(words: list[str], symbols: list[str]) -> tuple[str, ...]:
    """Match the longest symbol in each word using a trie-based approach.

    Args:
        words: List of words to search through.
        symbols: List of symbols to build the trie from.

    Returns:
        Tuple of words with the longest matched symbol bracketed.

    Examples:
        >>> bracket(['Amazon', 'Microsoft', 'Google'], ['Am', 'cro', 'le'])
        ('[Am]azon', 'Mi[cro]soft', 'Goog[le]')
    """
    root = _TrieNode()
    for symbol in symbols:
        node = root
        for char in symbol:
            if char not in node.children:
                node.children[char] = _TrieNode()
            node = node.children[char]
        node.symbol = symbol

    matched = {}
    for word in words:
        index = 0
        symbol_list = []
        while index < len(word):
            cursor, node = index, root
            while cursor < len(word) and word[cursor] in node.children:
                node = node.children[word[cursor]]
                if node.symbol is not None:
                    symbol_list.append(
                        (cursor + 1 - len(node.symbol), cursor + 1, node.symbol)
                    )
                cursor += 1
            index += 1
        if len(symbol_list) > 0:
            best = reduce(
                lambda x, y: x if x[1] - x[0] >= y[1] - y[0] else y,
                symbol_list,
            )
            matched[word] = f"{word[: best[0]]}[{best[2]}]{word[best[1] :]}"

    return tuple(matched.get(word, word) for word in words)
