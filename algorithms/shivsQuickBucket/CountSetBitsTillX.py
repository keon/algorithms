def check(N):
    count = 0
    for i in range(1, 64):
        cnt1 = 1 << (i * x) - 1 # count of 1s from 0 - 1000 on xth position
        cnt01 = 1 << (i * x) # count of 0s and 1s from 0 - 1000 on xth position
        d, r = divmod(N + 1, cnt01)
        count += d * cnt1 + max(0, r - cnt1)

return check(1000) # counts set bits for ith positions in binary representation