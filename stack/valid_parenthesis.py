"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

import unittest

def is_valid(s: str) -> bool:
    stack = []
    dic = { ")":"(",
            "}":"{",
            "]":"["}
    for char in s:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if stack == []:
                return False
            s = stack.pop()
            if dic[char] != s:
                return False
    return stack == []


class TestSuite (unittest.TestCase):
    """
        test suite for the function (above)
    """
    def test_is_valid(self):
        self.assertTrue(is_valid("[]"))
        self.assertTrue(is_valid("[]()[]"))
        self.assertFalse(is_valid("[[[]]"))
        self.assertTrue(is_valid("{([])}"))
        self.assertFalse(is_valid("(}"))


if __name__ == "__main__":
    unittest.main()
