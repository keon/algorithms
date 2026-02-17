"""
Pretty Print Tree

Prints a dictionary-based tree structure in a human-readable format showing
keys and their nested elements.

Reference: https://en.wikipedia.org/wiki/Tree_(data_structure)

Complexity:
    Time:  O(n) where n is total number of elements
    Space: O(1) additional space
"""

from __future__ import annotations


def tree_print(tree: dict) -> list[str]:
    """Format a dictionary tree as a list of readable strings.

    Each top-level key maps to a list of sub-elements. The output
    represents each key followed by its sub-elements joined with arrows.

    Args:
        tree: A dictionary mapping keys to lists of sub-elements.

    Returns:
        A list of formatted strings representing each tree branch.

    Examples:
        >>> tree_print({"a": ["Adam", "Book", 4]})
        ['a -> Adam -> Book -> 4']
    """
    lines: list[str] = []
    for key in tree:
        parts = [str(key)]
        tree_element = tree[key]
        for sub_elem in tree_element:
            parts.append(str(sub_elem))
        lines.append(" -> ".join(parts))
    return lines
