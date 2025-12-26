
def manacher(s):
    news = '#'.join('&{}|'.format(s))
    n = len(news)
    P = [0] * n
    r = c = 0

    for i in range(1, n - 1):
        if i < r:
            P[i] = min(r - i, P[2 * c - 1])
        while news[i - P[i] - 1] == news[i + P[i] + 1]:
            P[i] += 1
        if i + P[i] > r:
            c, r = i, i + P[i]
    
    resL = resid = 0
    for id, val in enumerate(P):
        if val > resL:
            resL = val
            resid = id
    
    return resL, s[(resid - resL) >> 1: (resid + resL) >> 1]