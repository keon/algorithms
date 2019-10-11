"""
Given a strings s and int k, return a string that rotates k times

For example,
rotate("hello", 2) return "llohe"
rotate("hello", 5) return "hello"
rotate("hello", 6) return "elloh"
rotate("hello", 7) return "llohe"

accepts two strings
returns bool
"""
def rotate(s, k):
    double_s = s + s
    if k <= len(s):
        return double_s[k:k + len(s)]
    else:
        return double_s[k-len(s):k]
