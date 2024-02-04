def zfunc(s):
    N = len(s)
    z = [0 for x in range(N)]
    l, r = 0,0
    for i in range(1, N):
        if i <= r:
            z[i] = min(r - i +1, z[i-l])
        while i + z[i] < N and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z