def countSetBits(n):
    # Brian Kernighan’s counts set bits in O(log(n))
    count = 0
    while n:
        n -= n & -n
        count += 1
    return count