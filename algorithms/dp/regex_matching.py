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
import unittest

class Solution(object):
    def is_match(self, s, p):
        m, n = len(s) + 1, len(p) + 1
        matches = [[False] * n  for _ in range(m)]

        # Match empty string with empty pattern
        matches[0][0] = True

        # Match empty string with .*
        for i, element in enumerate(p[1:], 2):
            matches[0][i] = matches[0][i - 2] and element == '*'

        for i, ss in enumerate(s, 1):
            for j, pp in enumerate(p, 1):
                if pp != '*':
                    # The previous character has matched and the current one
                    # has to be matched. Two possible matches: the same or .
                    matches[i][j] = matches[i - 1][j - 1] and \
                                    (ss == pp or pp == '.')
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
                    if ss == p[j - 2] or p[j - 2] == '.':
                        matches[i][j] |= matches[i - 1][j]

        return matches[-1][-1]

class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(Solution().is_match(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(Solution().is_match(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(Solution().is_match(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(Solution().is_match(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(Solution().is_match(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(Solution().is_match(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(Solution().is_match(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(Solution().is_match(s, p))


if __name__ == "__main__":
    unittest.main()
