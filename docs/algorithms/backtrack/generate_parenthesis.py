"""
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generate_parenthesis_v1(n):
    def add_pair(res, s, left, right):
        if left == 0 and right == 0:
            res.append(s)
            return
        if right > 0:
            add_pair(res, s + ")", left, right - 1)
        if left > 0:
            add_pair(res, s + "(", left - 1, right + 1)

    res = []
    add_pair(res, "", n, 0)
    return res


def generate_parenthesis_v2(n):
    def add_pair(res, s, left, right):
        if left == 0 and right == 0:
            res.append(s)
        if left > 0:
            add_pair(res, s + "(", left - 1, right)
        if right > 0 and left < right:
            add_pair(res, s + ")", left, right - 1)

    res = []
    add_pair(res, "", n, n)
    return res
