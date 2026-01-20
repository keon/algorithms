"""
Manacher's Algorithm to find the longest palindromic substring in linear time (O(n)).

The algorithm transforms the string by inserting special characters (#) between
characters to handle both odd and even length palindromes uniformly. Then it expands
around each possible center to find the longest palindromic substring.
"""

def manacher(s):
    # Transform the string to insert special characters between each character and at the start and end
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # Array to store the length of the palindrome centered at each character
    c = 0  # Current center
    r = 0  # Right boundary of the current longest palindrome

    for i in range(n):
        mirror = 2 * c - i  # Mirror position of i with respect to center c

        if i < r:
            p[i] = min(r - i, p[mirror])  # Use the previously calculated palindrome length if possible

        # Attempt to expand the palindrome centered at i
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # Update the center and right boundary if we've expanded beyond the current right boundary
        if i + p[i] > r:
            c = i
            r = i + p[i]

    # Find the maximum length palindrome
    max_len = max(p)
    center_index = p.index(max_len)

    # Extract the original palindrome from the transformed string
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

