from random import uniform as u
from matplotlib import pyplot as plt

def f(x): return 4*x**5 +5 * x**4 +2*x**3 + x**2 + x

lower =1 
upper = 10000
integral =[]

for n in range (lower, upper):
    P= [0] +sorted([u(0,1) for i in range(n)])+[1]
    S=0
    for j in range(1, len(P)):
        w=P[j]-P[j-1]
        h=f(u(P[j-1], P[j]))
        S += w*h
    integral.append(S)
    
plt.plot(list (range(lower+1, upper+1 )), integral)   
plt.show