"""
Simplify Path

Given an absolute Unix-style file path, simplify it by resolving '.'
(current directory), '..' (parent directory), and multiple slashes.

Reference: https://leetcode.com/problems/simplify-path/

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def simplify_path(path: str) -> str:
    """Simplify a Unix-style absolute path.

    Args:
        path: An absolute file path string.

    Returns:
        The simplified canonical path.

    Examples:
        >>> simplify_path("/home/")
        '/home'
        >>> simplify_path("/a/./b/../../c/")
        '/c'
    """
    skip = {"..", ".", ""}
    stack: list[str] = []
    tokens = path.split("/")
    for token in tokens:
        if token == "..":
            if stack:
                stack.pop()
        elif token not in skip:
            stack.append(token)
    return "/" + "/".join(stack)
