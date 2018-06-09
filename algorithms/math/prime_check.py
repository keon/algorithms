"""
prime_test(n) returns a True if n is a prime number else it returns False
"""

def prime_check(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 5
    while j * j <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True


def prime_check2(n):
    # prime numbers are greater than 1
    if n > 1:
        # check for factors
        for i in range(2, int(n ** 0.5) + 1):
            if (n % i) == 0:
                # print(num, "is not a prime number")
                # print(i, "times", num//i, "is", num)
                return False

        # print(num, "is a prime number")
        return True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False
