"""
Given a strings s and int k, return a string that rotates k times

For example,
rotate("hello", 2) return "llohe"
rotate("hello", 5) return "hello"
rotate("hello", 6) return "elloh"
rotate("hello", 7) return "llohe"


"""
def rotate(s, k):
    long_string = s
    while k >= len(long_string):
        long_string += s
    if k <= len(s):
        return long_string[k:k + len(s)]
    else:
        return long_string[k-len(s):k]
