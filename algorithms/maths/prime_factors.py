def primeList(n):
    n+=1
    li =[]
    booList = [True]*n
    for i in range(2,n):
        if booList[i]:
            li.append(i)
            booList[i] =False
            for j in range(i*i,n,i):
                booList[j] =False
    return li

'''
prime_factors will return a dict of factors with value of elements
being the elements' exponent
eg
prime_factors(6) = {2:1, 3:1}
'''
def prime_factors(n):
    primes = primeList(n)
    factordict = {}
    idx = 0
    length = len(primes)
    while n!=1 :
        if n%primes[idx] ==0:
            n//=primes[idx]
            if primes[idx] in factordict:
                factordict[primes[idx]] +=1
            else:
                factordict[primes[idx]] =1
        else:
            idx +=1
    return factordict

print(prime_factors(6))
    
