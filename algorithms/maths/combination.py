def combination(n, r):
    # This function calculates nCr
    if n == r or r == 0:
        return 1
    else:
        return combination(n-1, r-1) + combination(n-1, r)
def combination_memo(n, r, c):
    # This function calculates nCr, memoization method
    if n == r or r == 0:
        return 1
    if None != c.get((n, r)):
        return c[(n, r)]
    elif None == c.get((n, r)):
        c[(n-1, r-1)] = combination_memo(n-1, r-1, c)
        c[(n-1, r)] = combination_memo(n-1, r, c)
        c[(n, r)] = c[(n-1, r-1)] + c[(n-1, r)]
        return c[(n, r)]    