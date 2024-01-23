''' Find longest palindrome substring in O(N) time '''

def manacher(s):
    news = '#'.join('&{}|'.format(s))

    c = r = 0
    n = len(news)
    P = [0] * n

    for i in range(1, n - 1):
        if i < r: # update P[i] from it's mirror seen before centre
            P[i] = min(r - i, P[2 * c - i])
        while news[i + P[i] + 1] == news[i - P[i] - 1]:
            P[i] += 1
        if i + P[i] > r: # if we have come after r update r for future Is
            c, r = i, i + P[i]
    
    resL = resid = 0
    for id, val in enumerate(P):
        if val > resL:
            resL = val
            resid = id
    
    return resL, s[(resid - resL) >> 1: (resid + resL) >> 1]