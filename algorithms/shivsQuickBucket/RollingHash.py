"""
    Calculates the rolling hash values of all substrings of length window_size in string s.
    Uses the polynomial rolling hash algorithm with base and mod as constants.
"""
base = 26
mod = 10 ** 9 + 69

def get_hash(s, W):
    hash = 0
    for i in range(W):
        hash = (hash * base + ord(s[i])) % mod
    return hash

def rolling_hash(s, W):
    n = len(s)
    power = [1] * (n + 1)
    for i in range(1, n + 1):
        power[i] = (power[i - 1] * base) % mod
    
    res = [0] * (n - W + 1)

    curr = get_hash(s, W)
    
    # roll for haystack
    res[0] = curr
    for i in range(1, n - W + 1):
        curr = (curr - power[W - 1] * ord(s[i - 1])) % mod
        curr = (curr * base + ord(s[i + W - 1])) % mod
        res[i] = curr

    return res