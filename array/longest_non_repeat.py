"""
Given a string, find the length of the longest substring
without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""
import unittest


def longest_non_repeat(string):
    """
    Finds the length of the longest substring
    without repeating characters.
    """
    if string is None:
        return 0
    temp = []
    max_len = 0
    for i in string:
        if i in temp:
            temp = []
        temp.append(i)
        max_len = max(max_len, len(temp))
    return max_len


def longest_non_repeat_two(string):
    """
    Finds the length of the longest substring
    without repeating characters.
    Uses alternative algorithm.
    """
    if string is None:
        return 0
    start, max_len = 0, 0
    used_char = {}
    for index, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            max_len = max(max_len, index - start + 1)
        used_char[char] = index
    return max_len


class TestLongestNonRepeat(unittest.TestCase):

    def test_longest_non_repeat(self):

        string = "abcabcbb"
        self.assertEqual(longest_non_repeat(string), 3)

        string = "bbbbb"
        self.assertEqual(longest_non_repeat(string), 1)
        
        string = "pwwkew"
        self.assertEqual(longest_non_repeat(string), 3)

    def test_longest_non_repeat_two(self):
        
        string = "abcabcbb"
        self.assertEqual(longest_non_repeat_two(string), 3)

        string = "bbbbb"
        self.assertEqual(longest_non_repeat_two(string), 1)
        
        string = "pwwkew"
        self.assertEqual(longest_non_repeat_two(string), 3)
        

if __name__ == "__main__":
    
    unittest.main()
