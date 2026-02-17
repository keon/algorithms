"""
Text Justification

Given an array of words and a max width, format the text such that each line
has exactly max_width characters and is fully justified. Extra spaces are
distributed as evenly as possible with left slots getting more.

Reference: https://leetcode.com/problems/text-justification/

Complexity:
    Time:  O(n) where n is the total number of characters
    Space: O(n)
"""

from __future__ import annotations


def text_justification(words: list[str], max_width: int) -> list[str]:
    """Justify text to a fixed width with evenly distributed spaces.

    Args:
        words: A list of words to justify.
        max_width: The maximum width of each line.

    Returns:
        A list of fully justified strings.

    Raises:
        ValueError: If any word is longer than max_width.

    Examples:
        >>> text_justification(["What", "must", "be"], 16)
        ['What   must   be']
    """
    result: list[str] = []
    row_length = 0
    row_words: list[str] = []
    index = 0
    is_first_word = True

    while index < len(words):
        while row_length <= max_width and index < len(words):
            if len(words[index]) > max_width:
                raise ValueError(
                    "there exists word whose length is larger than max_width"
                )
            tentative_length = row_length
            row_words.append(words[index])
            tentative_length += len(words[index])
            if not is_first_word:
                tentative_length += 1
            if tentative_length > max_width:
                row_words.pop()
                break
            row_length = tentative_length
            index += 1
            is_first_word = False

        row = ""
        if index == len(words):
            for word in row_words:
                row += (word + ' ')
            row = row[:-1]
            row += ' ' * (max_width - len(row))
        elif len(row_words) != 1:
            extra_spaces = max_width - row_length
            spaces_per_gap = extra_spaces // (len(row_words) - 1)
            remaining_spaces = (
                extra_spaces - spaces_per_gap * (len(row_words) - 1)
            )
            for word_index in range(len(row_words)):
                row += row_words[word_index]
                if word_index != len(row_words) - 1:
                    row += ' ' * (1 + spaces_per_gap)
                if remaining_spaces > 0:
                    row += ' '
                    remaining_spaces -= 1
        else:
            row += row_words[0]
            row += ' ' * (max_width - len(row))

        result.append(row)
        row_length = 0
        row_words = []
        is_first_word = True

    return result
