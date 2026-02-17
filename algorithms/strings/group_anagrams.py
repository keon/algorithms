"""
Group Anagrams

Given an array of strings, group anagrams together. Anagrams are words that
contain the same letters in a different order.

Reference: https://leetcode.com/problems/group-anagrams/

Complexity:
    Time:  O(n * k log k) where n is the number of strings and k is max length
    Space: O(n * k)
"""

from __future__ import annotations


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Group a list of strings by anagram equivalence.

    Args:
        strings: A list of strings to group.

    Returns:
        A list of groups, where each group contains strings that are anagrams.

    Examples:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    anagram_map: dict[str, int] = {}
    groups: list[list[str]] = []
    group_index = 0
    for word in strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = group_index
            group_index += 1
            groups.append([])
            groups[-1].append(word)
        else:
            groups[anagram_map[sorted_word]].append(word)
    return groups
