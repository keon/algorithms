"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
def is_valid(s: str) -> bool:
    stack = []
    dic = {")": "(",
           "}": "{",
           "]": "["}
    for char in s:
        if char in dic.values():
            stack.append(char)
        elif char in dic:
            if not stack or dic[char] != stack.pop():
                return False
    return not stack
