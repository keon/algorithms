"""
Find All Distinct Longest Common Subsequences

Complexity:
    Time:  Exponential in the number of LCSs
    Space: O(m * n) + O(number of LCSs)
"""


def print_all_longest_common_subsequence(s: str, t: str) -> list[str]:
    """Compute all distinct longest common subsequences of two strings.

    Args:
        s: First string.
        t: Second string.

    Returns:
        A list containing all distinct longest common subsequences.

    Examples:
        >>> print_all_longest_common_subsequence('rajroy', 'rxoyxraxj')
            ['raj', 'roy']
    """

    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    res = set()
    memo = {}

    def solve(i: int, j: int, current: str) -> None:
        if i < 1 or j < 1:
            res.add(current[::-1])
            return

        key = (i, j, current)
        if key in memo:
            res.update(memo[key])
            return

        if s[i - 1] == t[j - 1]:
            solve(i - 1, j - 1, current + s[i - 1])
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                solve(i - 1, j, current)
            elif dp[i][j - 1] > dp[i - 1][j]:
                solve(i, j - 1, current)
            else:
                solve(i - 1, j, current)
                solve(i, j - 1, current)

        memo[key] = set(res)

    solve(n, m, "")
    return list(res)
