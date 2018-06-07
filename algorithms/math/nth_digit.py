"""
find nth digit
1. find the length of the number where the nth digit is from.
2. find the actual number where the nth digit is from
3. find the nth digit and return
"""


def find_nth_digit(n):
    len = 1
    count = 9
    start = 1
    while n > len * count:
        n -= len * count
        len += 1
        count *= 10
        start *= 10
    start += (n-1) / len
    s = str(start)
    return int(s[(n-1) % len])
