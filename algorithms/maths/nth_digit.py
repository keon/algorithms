def find_nth_digit(n):
    """find the nth digit of given number.
    1. find the length of the number where the nth digit is from.
    2. find the actual number where the nth digit is from
    3. find the nth digit and return
    """
    length = 1
    count = 9
    start = 1
    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10
    start += (n-1) / length
    s = str(start)
    return int(s[(n-1) % length])
