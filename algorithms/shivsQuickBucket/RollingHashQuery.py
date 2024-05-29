class prefixHash:
    def __init__(self ,s):
        self.mod = mod = 344555666677777
        self.basePower = basePower = 10 ** 7 + 7
        #fermat's little theorem since basePower and mod are co-prime
        self.invbase = invbase = pow(basePower, mod - 2, mod)
        self.prefix = prefix = [0] # r - l in query so for 1st prefix -> l needs to be 0 right?
        self.invprefix = invprefix = [1]
        hash, power, invpower = 0, 1, 1

        for x in s:
            hash = (hash + x * power) % mod
            power = (power * basePower) % mod
            invpower = (invpower * invbase) % mod
            prefix.append(hash)
            invprefix.append(invpower)
    
    def query(self, l, r):
        return ((self.prefix[r] - self.prefix[l]) * self.invprefix[l]) % self.mod
