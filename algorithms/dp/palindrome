'''
N natural numbers are listed. Then try M total times.

Each attempt can be represented by two integers, S and E, 
asking whether the numbers S through E make up the palindrome, 
and for each question it prints whether the palindrome is or not.

For example, suppose the number listed is 1, 2, 1, 3, 1, 2, 1.\
When S = 1 and E = 3, 
  1, 2, 1 is a palindrome.
When S = 2 and E = 5, 
  2, 1, 3, 1 are not a palindrome.
When S = 3 and E = 3,
  1 is a palindrome.
When S = 5 and E = 7, 
  1, 2, 1 is a palindrome.
  

The first row is given the size of the sequence N (1 ≤ N ≤ 2,000).
In the second line, N numbers are given in order.
The third line gives the number of trials M (1 ≤ M ≤ 1,000,000).
From line 4, M lines are given one S and one E for each line.

ex 1)
input :
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7

output :
1
0
1
1

ex 2)
input :
9
1 2 3 1 5 1 3 3 1
5
1 3
2 5
4 6
6 9
3 7

output :
0
0
1
1
1
'''
pld=[]
output=[]
n=eval(input())
d=[[0 for i in range(n)] for j in range(n)]

pld=list(map(int,(input().split())))
for i in range(n) :
        d[i][i]=1
     
for i in range(n-1):
        if (pld[i]==pld[i+1]) :
                d[i][i+1]=1
                
for i in range(1,n-1):
        for j in range(n-i):
                   if (pld[j] == pld[i + j] and d[j + 1][i + j - 1]):
                        d[j][i + j] = 1

m=eval(input())
while m :   
        s,e = map(int, input().split())
        output.append(d[s-1][e-1])
        m-=1

for i in output:
        print(i)
