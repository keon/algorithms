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
    else:
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
