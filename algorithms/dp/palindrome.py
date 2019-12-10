'''
N natural numbers are listed. Then try M total times.

Each attempt can be represented by two integers, S and E, 
asking whether the numbers S through E make up the palindrome, 
and for each question it prints whether the palindrome is or not.

For example, suppose the number listed is 1, 2, 1, 3, 1, 2, 1.
When S = 1 and E = 3, 
  1, 2, 1 is a palindrome.
When S = 2 and E = 5, 
  2, 1, 3, 1 are not a palindrome.
When S = 3 and E = 3,
  1 is a palindrome.
When S = 5 and E = 7, 
  1, 2, 1 is a palindrome.

Time complexity is O(n^2)

ex 1)

N1=[1,2,1,3,1,2,1]
M1=[[1,3],[2,5],[3,3],[5,7]]

output :
[1,0,1,1]

ex 2)
input :
N2=[1, 2, 3, 1, 5, 1, 3, 3, 1]
M2=[[1,3],[2,5],[4,6],[6,9],[3,7]]

output :
[0,0,1,1,1]


N1=[1,2,1,3,1,2,1]
M1=[[1,3],[2,5],[3,3],[5,7]]

N2=[1, 2, 3, 1, 5, 1, 3, 3, 1]
M2=[[1,3],[2,5],[4,6],[6,9],[3,7]]
'''

def palindrome(list_n,list_m) :
        n=len(list_n)
        output=[]
        d=[[0 for i in range(n)] for j in range(n)]
        for i in range(n) :
                d[i][i]=1

        for i in range(n-1):
                if (list_n[i]==list_n[i+1]) :
                        d[i][i+1]=1

        for i in range(1,n):
                for j in range(n-i):
                        if (list_n[j] == list_n[i + j] and d[j + 1][i + j - 1]):
                                d[j][i + j] = 1
        m=len(list_m)
        i=0
        while i<m :   
                s,e = map(int, list_m[i])
                output.append(d[s-1][e-1])
                i+=1
        return output
        
'''
palindrome(N1,M1)
palindrome(N2,M2)
'''
