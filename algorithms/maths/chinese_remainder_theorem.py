def solve_chinese_remainder(num : list[int], rem : list[int]):
    """
    Computes the smallest x that satisfies the chinese remainder theorem
    """
    if not len(num) == len(rem):
        raise Exception("num and rem should have equal length")
    if not check_coprime(num):
        raise Exception("All pairs of numbers in num are not coprime")
    k = len(num)
    x = 1
    while True:
        i = 0
        while i < k:
            if x % num[i] != rem[i]:
                break
            i += 1
        if i == k:
            return x
        else:
            x += 1
        
def check_coprime(l : list[int]):
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                continue
            if gcd(l[i], l[j]) != 1:
                return False
    return True

# From the gcd module
def gcd(a, b):
    """Computes the greatest common divisor of integers a and b using
    Euclid's Algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a