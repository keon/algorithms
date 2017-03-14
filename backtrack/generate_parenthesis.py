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

def gen_parenthesis(n:"int")->"List[str]":
    res = []
    add_pair(res, "", n, 0)
    return res

def add_pair(res, s, left, right):
    if left == 0 and right == 0:
        res.append(s)
        return
    if right > 0:
        add_pair(res, s+")", left, right-1)
    if left > 0:
        add_pair(res, s+"(", left-1, right+1)


if __name__=="__main__":
    print(gen_parenthesis(3))
