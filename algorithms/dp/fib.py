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

def fib_recursive_memoization(n,memo):
    """[summary]
    This algorithm computes the n-th fibbonacci number
    in approximate O(n) time and O(n) space. 
    The algorithm use dynamic programming top down
    approach with memoization to save results for 
    avoiding recomputations.
    For example : fib(5) = fib(4)+fib(3)
                  fib(4) = fib(3)+fib(2)
                  where fib(3) will be recursively broken down into fib(2) 
                  and fib(1) twice.
    hence, fib(3) has to be computed twice.
    To avoid this, we save the results in a list called memo. We first
    check if the value is already available in the list, if yes, we return that
    value, else we perform the computation.
    
    
    Arguments:
        n {[int]} -- [description]
    
    Returns:
        [int] -- [description]
    """

    # precondition
    assert n >= 0, 'n must be a positive integer'
    if(memo[n-1]!=-1):  # check if value is already computed and stored
        return memo[n-1] 

    else: # if not then compute, store and return it.
        memo[n-1] = fib_recursive(n-1) + fib_recursive(n-2)
        return memo[n-1]

# initialise the memo list
# memo =[-1]*99 #if we want to find 100th fibonacci number
# memo[0]=0
# memo[1]=1
# print(fib_recursive_memoization(99,memo)) # => 354224848179261915075

def fib_list(n):
    """[summary]
    This algorithm computes the n-th fibbonacci number
    very quick. approximate O(n)
    The algorithm use dynamic programming with bottom up
    approach.
    
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
    sum = 0
    if n <= 1:
        return n
    for _ in range(n-1):
        sum = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = sum
    return sum

# print(fib_iter(100)) # => 354224848179261915075
