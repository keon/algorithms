"""
A message containing letters from A-Z is being
encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits,
determine the total number of ways to decode it.

For example,
Given encoded message "12",
it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


def num_decodings(enc_mes):
    """
    :type s: str
    :rtype: int
    """
    if not enc_mes or enc_mes[0] == "0":
        return 0
    last_char, last_two_chars = 1, 1
    for i in range(1, len(enc_mes)):
        last = last_char if enc_mes[i] != "0" else 0
        last_two = last_two_chars if int(enc_mes[i-1:i+1]) < 27 and enc_mes[i-1] != "0" else 0
        last_two_chars = last_char
        last_char = last+last_two
    return last_char


def num_decodings2(enc_mes):
    """
    :type s: str
    :rtype: int
    """
    if not enc_mes or enc_mes.startswith('0'):
        return 0
    stack = [1, 1]
    for i in range(1, len(enc_mes)):
        if enc_mes[i] == '0':
            if enc_mes[i-1] == '0' or enc_mes[i-1] > '2':
                # only '10', '20' is valid
                return 0
            stack.append(stack[-2])
        elif 9 < int(enc_mes[i-1:i+1]) < 27:
            # '01 - 09' is not allowed
            stack.append(stack[-2]+stack[-1])
        else:
            # other case '01, 09, 27'
            stack.append(stack[-1])
    return stack[-1]
    
    
    
# ----------------- TESTS -------------------------

"""
    Testsuite for the project
"""

import unittest


class TestNum_decodings2(unittest.TestCase):
    def testMCC(self):
        self.assertEqual(0, num_decodings2(""))
        self.assertEqual(0, num_decodings2("011"))
        self.assertEqual(2, num_decodings2("12"))
        self.assertEqual(0, num_decodings2("00"))
        self.assertEqual(0, num_decodings2("30"))
        self.assertEqual(2, num_decodings2("1110"))
        self.assertEqual(2, num_decodings2("23"))
        self.assertEqual(1, num_decodings2("31"))
        self.assertEqual(1, num_decodings2("8"))
        self.assertEqual(1, num_decodings2("9"))
        self.assertEqual(1, num_decodings2("27"))


    def testAllDUpath(self):
        self.assertEqual(0, num_decodings2(""))
        self.assertEqual(0, num_decodings2("00"))
        self.assertEqual(2, num_decodings2("1110"))
        self.assertEqual(0, num_decodings2("30"))
        self.assertEqual(2, num_decodings2("21"))
        self.assertEqual(3, num_decodings2("123"))
        


if __name__ == "__main__":
    unittest.main()
