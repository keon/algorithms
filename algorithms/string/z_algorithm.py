"""Z-algorithm — linear-time pattern matching via the Z-array.

The Z-array for a string S stores at Z[i] the length of the longest
substring starting at S[i] that is also a prefix of S. By concatenating
pattern + '$' + text, occurrences of the pattern correspond to positions
where Z[i] == len(pattern).

Inspired by PR #930 (Simranstha045).
"""

from __future__ import annotations


def compute_z_array(s: str) -> list[int]:
    """Compute the Z-array for string *s* in O(n) time."""
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    z[0] = n
    left = right = 0
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def z_search(text: str, pattern: str) -> list[int]:
    """Return all starting indices where *pattern* occurs in *text*."""
    if not pattern or not text:
        return []
    concat = pattern + "$" + text
    z = compute_z_array(concat)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(concat)) if z[i] == m]
