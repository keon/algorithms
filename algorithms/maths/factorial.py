#
# This function calculates n!
# Factorial function not works in less than 0
#

def factorial(n):

    result = 1
    for i in range(2, n+1):
        result *= i

    return result


def factorial_recur(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)
    
