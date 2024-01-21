def rolling_hash(s, W, base = 26, mod = 100000000069):
    n = len(s)
    power = [1] * (n + 1)
    for i in range(1, n + 1):
        power[i] = (power[i - 1] * base) % mod
    
    res = [0] * (n - W + 1)
    curr_hash = 0

    for i in range(W):
        curr_hash = (curr_hash * base + ord(s[i])) % mod
    
    # return hash for needle
    if n == W: return curr_hash
    
    # roll for haystack
    res[0] = curr_hash
    for i in range(1, n - W + 1):
        curr_hash = (curr_hash - power[W - 1] * ord(s[i - 1])) % mod
        curr_hash = (curr_hash * base + ord(s[i + W - 1])) % mod
        res[i] = curr_hash

    return res





"""
    Calculates the rolling hash values of all substrings of length window_size in string s.
    Uses the polynomial rolling hash algorithm with base and mod as constants.
 
    :param s: the input string
    :param window_size: the size of the rolling window
    :param base: the base for the polynomial hash function
    :param mod: the modulus for the polynomial hash function
    :return: a list of hash values of all substrings of length window_size in s
    """