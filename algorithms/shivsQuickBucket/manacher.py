''' Find longest palindrome substring in O(N) time '''

def manacher(s):
    news = '#'.join('&{}|'.format(s))

    c = r = 0
    n = len(news)
    P = [0] * n

    for i in range(1, n - 1):
        if i < r:
            P[i] = min(r - i, P[2 * c - i])
        while news[i + P[i] + 1] == news[i - P[i] - 1]:
            P[i] += 1
        if i + P[i] > r:
            c, r = i, i + P[i]
    
    res = resid = 0
    for id, val in enumerate(P):
        if val > res:
            res = val
            resid = id
    
    return res, s[(resid - res) >> 1: (resid + res) >> 1]