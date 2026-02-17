"""
Word Search II

Given a board of characters and a list of words, find all words that can
be constructed from adjacent cells (horizontally or vertically). Each cell
may only be used once per word. Uses a trie for efficient prefix matching.

Reference: https://leetcode.com/problems/word-search-ii/

Complexity:
    Time:  O(M * N * 4^L) where M*N is board size, L is max word length
    Space: O(W * L) for the trie, where W is number of words
"""

from __future__ import annotations


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    """Find all words from the list that exist on the board.

    Builds a trie from the word list, then uses backtracking to search
    the board for each word.

    Args:
        board: A 2D grid of characters.
        words: A list of words to search for.

    Returns:
        A list of words found on the board.

    Examples:
        >>> board = [['o','a','a','n'], ['e','t','a','e']]
        >>> sorted(find_words(board, ['eat', 'oath']))
        ['eat']
    """
    trie: dict = {}
    for word in words:
        current_node = trie
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node["#"] = "#"

    found: set[str] = set()
    used = [[False] * len(board[0]) for _ in range(len(board))] if board else []

    for row in range(len(board)):
        for col in range(len(board[0])):
            _backtrack(board, row, col, trie, "", used, found)

    return list(found)


def _backtrack(
    board: list[list[str]],
    row: int,
    col: int,
    trie: dict,
    prefix: str,
    used: list[list[bool]],
    found: set[str],
) -> None:
    """Recursively search the board for words matching the trie."""
    if "#" in trie:
        found.add(prefix)

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return

    if not used[row][col] and board[row][col] in trie:
        used[row][col] = True
        next_char = board[row][col]
        _backtrack(board, row + 1, col, trie[next_char],
                   prefix + next_char, used, found)
        _backtrack(board, row, col + 1, trie[next_char],
                   prefix + next_char, used, found)
        _backtrack(board, row - 1, col, trie[next_char],
                   prefix + next_char, used, found)
        _backtrack(board, row, col - 1, trie[next_char],
                   prefix + next_char, used, found)
        used[row][col] = False
