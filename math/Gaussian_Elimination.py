from numpy import array, column_stack, zeros
from sys import exit

n=3

X= array((3,2,1), dtype="f")
Y= array((2,3,2), dtype="f")
Z= array((1,1,3), dtype="f")
C= array((90,77,46), dtype="f")

a=column_stack((X,Y,Z,C))
x=zeros(n)

for i in range(n):
    if a[i][i]==0:
        sys.exit("No Solution")
        
    for j in range(i+1, n):
        ratio= a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] -=ratio*a[i][k] 

x[n-1]=a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i]=a[i][n]
    
    for j in range(i+1,n):
        x[i]-=a[i][j]*x[j]
        
    x[i]= x[i]/a[i][i]
