def modular_Exponential(base, power, mod):
    if power < 0:
    	return -1
    base %= mod
    result = 1

    while power > 0:
        #If the last bit is 1, add 2^k.
        if power & 1:
            result = (result * base) % mod
        power = power >> 1
        #Utilize modular multiplication properties to combine the computed mod C values.
        base = (base * base) % mod

    return result
