"""
Print any longest common subsequence

Complexity:
    Time:  O(n * m)
    Space: O(n * m)
"""


def print_any_longest_common_subsequence(s1: str, s2: str) -> str:
    """Return any one longest common subsequence of two strings.

    Args:
        s1: First string.
        s2: Second string.

    Returns:
        A string representing any one longest common subsequence.

    Example:
        >>> print_any_longest_common_subsequence('rajroy', 'rxoyxraxj')
            "raj" or "roy"
    """

    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    length = dp[n][m]
    i, j = n, m
    lcs_str = [""] * length
    index = length - 1

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str[index] = s1[i - 1]
            index -= 1
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_str)
