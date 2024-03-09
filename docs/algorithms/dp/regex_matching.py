"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool is_match(const char *s, const char *p)

Some examples:
is_match("aa","a") → false
is_match("aa","aa") → true
is_match("aaa","aa") → false
is_match("aa", "a*") → true
is_match("aa", ".*") → true
is_match("ab", ".*") → true
is_match("aab", "c*a*b") → true
"""

def is_match(str_a, str_b):
    """Finds if `str_a` matches `str_b`

    Keyword arguments:
    str_a -- string
    str_b -- string
    """
    len_a, len_b = len(str_a) + 1, len(str_b) + 1
    matches = [[False] * len_b  for _ in range(len_a)]

    # Match empty string with empty pattern
    matches[0][0] = True

    # Match empty string with .*
    for i, element in enumerate(str_b[1:], 2):
        matches[0][i] = matches[0][i - 2] and element == '*'

    for i, char_a in enumerate(str_a, 1):
        for j, char_b in enumerate(str_b, 1):
            if char_b != '*':
                # The previous character has matched and the current one
                # has to be matched. Two possible matches: the same or .
                matches[i][j] = matches[i - 1][j - 1] and \
                                char_b in (char_a, '.')
            else:
                # Horizontal look up [j - 2].
                # Not use the character before *.
                matches[i][j] |= matches[i][j - 2]

                # Vertical look up [i - 1].
                # Use at least one character before *.
                #   p a b *
                # s 1 0 0 0
                # a 0 1 0 1
                # b 0 0 1 1
                # b 0 0 0 ?
                if char_a == str_b[j - 2] or str_b[j - 2] == '.':
                    matches[i][j] |= matches[i - 1][j]

    return matches[-1][-1]
