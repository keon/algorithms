"""Manacher's algorithm — find the longest palindromic substring in O(n).

Manacher's algorithm uses the symmetry of palindromes to avoid redundant
comparisons, achieving linear time. It transforms the input to handle
both odd- and even-length palindromes uniformly.

Inspired by PR #931 (Simranstha045).
"""


def manacher(s: str) -> str:
    """Return the longest palindromic substring of *s* in O(n) time."""
    # Transform "abc" -> "^#a#b#c#$" so every palindrome has odd length
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    p = [0] * n  # p[i] = radius of palindrome centred at i
    centre = right = 0
    for i in range(1, n - 1):
        mirror = 2 * centre - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right:
            centre, right = i, i + p[i]
    max_len, centre_index = max((v, i) for i, v in enumerate(p))
    start = (centre_index - max_len) // 2
    return s[start : start + max_len]
