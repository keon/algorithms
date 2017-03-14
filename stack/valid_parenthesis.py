"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


def is_valid(s:"str")->"bool":
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


if __name__ == "__main__":
    paren = "[]"
    print(paren, is_valid(paren))
    paren = "[]()[]"
    print(paren, is_valid(paren))
    paren = "[[[]]"
    print(paren, is_valid(paren))
    paren = "{([])}"
    print(paren, is_valid(paren))
    paren = "(}"
    print(paren, is_valid(paren))
