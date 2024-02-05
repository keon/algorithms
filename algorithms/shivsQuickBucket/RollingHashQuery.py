class prefixHash:
    def __init__(self ,s):
        self.mod = mod = 344555666677777
        self.base = base = 10 ** 7 + 7
        #fermat's little theorem since base  and mod are co-prime
        self.invbase = invbase = pow(base, mod - 2, mod)
        self.pref = pref = [0]
        self.invpref = invpref = [1]
        power, invpower, hash = 1, 1, 0

        for x in s:
            hash = (hash + x * power) % mod
            power = (power * base) % mod
            invpower = (invpower * invbase) % mod
            pref.append(hash)
            invpref.append(invpower)
    
    def query(self, l, r):
        return ((self.pref[r] - self.pref[l]) * self.invpref[l]) % self.mod
