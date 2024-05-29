# if we find out where to jump to for matching a pattern in a big text we can reduce computations
# as pattern can have repeated values -> only works if this is true
# that is why we create pi table to store the jump values
def kmp(text, pattern):
    m, n = len(text), len(pattern)
    pi = [0] * n

    j = 0
    # making pi table -> finding the longest prefix that is also a suffix
    # Examples - P = ABCDABD π = (0, 0, 0, 0, 1, 2, 0)
    # pi table means -> agar yahan khtm hui matching to starting se start karo if 0 is there otherwise start
    # start with the position givne in pi table kyunki wahan tk ka matching already hogya tha
    for i in range(1, n):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    # finding pattern in text
    j = 0
    res = []
    for i in range(m):
        while j and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == n:
                res.append(i - n + 1)
                j = pi[j - 1]
                
    return res