def f(X): return [str(len(x)) for x in X if len(x) >0]

def p(n):
    l = ["+".join (sorted (f(x.split("0")),reverse=True))
    for x in [bin(n)[2:] for n in range (2**(2*n-1))] if x.count("1")==n]

    for idx, u in enumerate(sorted(list(set(l)),reverse=True)):
        print(f"{str(idx+1).zfill(2)}.{u}")
        
    print(f"\np({n})={idx+1}")
    
p(13)

