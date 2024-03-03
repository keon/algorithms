# uses modular inversion
def ncr(n, r):
    if (r > n): return 0
         
    mod = 1000000007
    inv = [0 for i in range(r + 1)]
    inv[0] = 1
    if(r+1>=2): inv[1] = 1

    for i in range(2, r + 1):
        inv[i] = mod - (mod // i) * inv[mod % i] % mod
 
    ans = 1
    for i in range(2, r + 1):
        ans = ((ans % mod) * (inv[i] % mod)) % mod
 
    for i in range(n, n - r, -1):
        ans = ((ans % mod) * (i % mod)) % mod
         
    return ans

def ncr(n, r):
    sum = 1
    for i in range(1, r + 1):
        sum *= ((n - r + i) / i)
    return int(sum)
'''Refer geeks for geeks binomial coefficient'''