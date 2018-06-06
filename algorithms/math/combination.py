def combination(n, r):
    # This function calculates nCr
    if n == r or r == 0:
        return 1
    else:
        return combination(n-1, r-1) + combination(n-1, r)
