"""
Word Ladder (Bidirectional BFS)

Given two words and a dictionary, find the length of the shortest
transformation sequence where only one letter changes at each step and
every intermediate word must exist in the dictionary.

Reference: https://leetcode.com/problems/word-ladder/

Complexity:
    Time:  O(N * L^2)  where N = size of word list, L = word length
    Space: O(N * L)
"""

from __future__ import annotations

from collections.abc import Iterator


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    """Return the shortest transformation length, or -1 if impossible.

    Args:
        begin_word: Starting word.
        end_word: Target word.
        word_list: Allowed intermediate words.

    Returns:
        Length of the shortest transformation sequence, or -1.

    Examples:
        >>> ladder_length('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'])
        5
    """
    if len(begin_word) != len(end_word):
        return -1

    if begin_word == end_word:
        return 0

    if sum(c1 != c2 for c1, c2 in zip(begin_word, end_word, strict=False)) == 1:
        return 1

    begin_set: set[str] = set()
    end_set: set[str] = set()
    begin_set.add(begin_word)
    end_set.add(end_word)
    result = 2
    while begin_set and end_set:
        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set

        next_begin_set: set[str] = set()
        for word in begin_set:
            for ladder_word in _word_range(word):
                if ladder_word in end_set:
                    return result
                if ladder_word in word_list:
                    next_begin_set.add(ladder_word)
                    word_list.remove(ladder_word)
        begin_set = next_begin_set
        result += 1
    return -1


def _word_range(word: str) -> Iterator[str]:
    """Yield all words that differ from *word* by exactly one letter.

    Args:
        word: The source word.

    Yields:
        Words with a single character changed.
    """
    for ind in range(len(word)):
        temp = word[ind]
        for c in [chr(x) for x in range(ord("a"), ord("z") + 1)]:
            if c != temp:
                yield word[:ind] + c + word[ind + 1 :]
