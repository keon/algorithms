
#functions for matrix power and multiplication
def matr_mult(x,y): #returns product of 2x2 matrices
    return [[x[0][0]*y[0][0] + x[0][1]*y[1][0],     x[0][0]*y[0][1] + x[0][1]*y[1][1]],
            [x[0][0]*y[1][0] + x[1][0]*y[1][1],     x[0][1]*y[1][0] + x[1][1]*y[1][1]]]

def matr_pow(A,k): #returns A^k for integer k > 0 
    if k == 1:
        return A
    else:
        X = matr_pow(A,k/2)
        if k % 2 == 0:
            return matr_mult(X,X)
        else:
            return matr_mult(matr_mult(X,X),A)
def fib_matr(n):
    """[summary]
    Computes nth fibonacci number in O(logn) time by using powers of the Fibonacci Q-Matrix.
    Arguments:
        n {[int]} -- [description]
    
    Returns:
        [int] -- [description]
    """
    Explanation:
    The Q-Matrix is   Q = | 1 1 | and it can be shown that Q^n = | Fn+1 Fn   | where Fn is the 
                          | 1 0 |                                | Fn   Fn+1 |
    nth Fibonacci number. See http://mathworld.wolfram.com/FibonacciQ-Matrix.html for more information.
    Since computing the nth power of a 2x2 matrix takes O(logn) time, we can compute Fn in O(logn).
    """
    # precondition
    assert n >= 0, 'n must be positive integer'
    Q = [[1,1],[1,0]]
    if n == 0:
        return 0
    return matr_pow(Q,n)[0][1]
'''
inp = [0,1,2,3,4,5,6,7,8,9,10,14,17,19,44,100]
res = [fib_matr(x) for x in inp]
print res == [0,1,1,2,3,5,8,13,21,34,55,377,1597,4181,701408733,354224848179261915075]
'''
