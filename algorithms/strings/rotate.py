"""
Given a strings s and int k, return a string that rotates k times

k can be any positive integer.

For example,
rotate("hello", 2) return "llohe"
rotate("hello", 5) return "hello"
rotate("hello", 6) return "elloh"
rotate("hello", 7) return "llohe"
rotate("hello", 102) return "lohel"

"""
def rotate(s, k):
    long_string = s * (k // len(s) + 2)
    if k <= len(s):
        return long_string[k:k + len(s)]
    else:
        return long_string[k-len(s):k]
    
def rotate_alt(string, k):
    k = k % len(string)
    return string[k:] + string[:k]
