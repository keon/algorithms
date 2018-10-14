import time
def rabin_karp(find, txt, d, q):
    n = len(find)
    m = len(txt)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []
    for i in range(m): 
        p = (d*p+ord(txt[i]))%q
        t = (d*t+ord(find[i]))%q
    for s in range(n-m+1): 
        if p == t:
            flag = 1
            for i in range(m):
                if txt[i] != find[s+i]:
                    flag = 0
                    break
            if flag:
                result.append(s)
        if s < n-m:
            t = (t-h*ord(find[s]))%q 
            t = (t*d+ord(find[s+m]))%q 
            t = (t+q)%q 
    if flag==1:
        print "Found at ",
        for i in result:
            print i,
    else:
        print "Not found"
    
        
a=time.clock()
rabin_karp("2146519156165", "12", 256, 11)
print "Time taken is "+str(time.clock()-a)
a=time.clock()
rabin_karp("ffffff", "ff", 255, 13)
print
print "Time taken is "+str(time.clock()-a)




