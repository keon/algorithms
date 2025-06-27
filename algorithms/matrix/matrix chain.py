from sys import maxint
import time
def matrix(mat_size,n):
    m=[]
    for i in range(n):
        m.append([0]*n)
    
    min=maxint
    for L in range(2,n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = maxint
            for k in range(i, j):
                count= m[i][k]+m[k+1][j]+mat_size[i-1]*mat_size[k]*mat_size[j]
                if count < min:
                    min=count
    return min

mat_size=[10,20,30,50]
n=len(mat_size)
a=time.clock()
print matrix(mat_size,n)
print "Time taken is "+str(time.clock()-a)
