def solve_chinese_remainder(num : list[int], rem : list[int]):
    """
    Computes the smallest x that satisfies the chinese remainder theorem
    for a system of equations. 
    The system of equations has the form:
    x % num[0] = rem[0]
    x % num[1] = rem[1]
    ...
    x % num[k - 1] = rem[k - 1]
    Where k is the number of elements in num and rem, k > 0.
    All numbers in num needs to be pariwise coprime otherwise an exception is raised
    returns x: the smallest value for x that satisfies the system of equations
    """
    if not len(num) == len(rem):
        raise Exception("num and rem should have equal length")
    if not len(num) > 0:
        raise Exception("Lists num and rem need to contain at least one element")
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