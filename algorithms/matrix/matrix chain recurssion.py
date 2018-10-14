from sys import maxint
import time
def matrix(p,i,j):
    if i==j:
        return 0
    min=maxint
    for k in range(i,j):
        count= matrix(p,i,k)+matrix(p,k+1,j)+p[i-1]*p[k]*p[j]
        if count < min:
            min=count
    return min

mat_size=[1,2,3,4,3]
n=len(mat_size)/mat_size[0]
a=time.clock()
print matrix(mat_size,1,n-1)
print "Time taken is "+str(time.clock()-a)
