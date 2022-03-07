'''
In mathematics, the Fibonacci numbers, commonly denoted Fn,
form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones,
starting from 0 and 1.
That is,
    F0=0 , F1=1
and
    Fn= F(n-1) + F(n-2)
The Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …….

In mathematical terms, the sequence Fn of Fibonacci numbers is
defined by the recurrence relation

Here, given a number n, print n-th Fibonacci Number.
'''


def fib_recursive(n):
    """[summary]
    Computes the n-th fibonacci number recursive.
    Problem: This implementation is very slow.
    approximate O(2^n)

    Arguments:
        n {[int]} -- [description]

    Returns:
        [int] -- [description]
    """

    # precondition
    assert n >= 0, 'n must be a positive integer'

    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# print(fib_recursive(35)) # => 9227465 (slow)


def fib_list(n):
    """[summary]
    This algorithm computes the n-th fibbonacci number
    very quick. approximate O(n)
    The algorithm use dynamic programming.

    Arguments:
        n {[int]} -- [description]

    Returns:
        [int] -- [description]
    """

    # precondition
    assert n >= 0, 'n must be a positive integer'

    list_results = [0, 1]
    for i in range(2, n+1):
        list_results.append(list_results[i-1] + list_results[i-2])
    return list_results[n]

# print(fib_list(100)) # => 354224848179261915075


def fib_iter(n):
    """[summary]
    Works iterative approximate O(n)

    Arguments:
        n {[int]} -- [description]

    Returns:
        [int] -- [description]
    """

    # precondition
    assert n >= 0, 'n must be positive integer'

    fib_1 = 0
    fib_2 = 1
    res = 0
    if n <= 1:
        return n
    for _ in range(n-1):
        res = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = res
    return res

# print(fib_iter(100)) # => 354224848179261915075
