'''Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.'''

######   O(N^3)  ######

from itertools import accumulate


def dp(a,acc,n):
    cost = [[float('inf')]*n for i in range(n)]
    st = [[0]*n for i in range(n)]

    for i in range(n):
        cost[i][i] = a[i][1]

    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            for r in range(i,j+1):

                if i!=0:
                    c =  (lambda r:cost[i][r-1] if r>i else 0)(r) + (lambda r:cost[r+1][j] if r<j else 0)(r) + acc[j] - acc[i-1]
                else:
                    c = (lambda r: cost[i][r - 1] if r > i else 0)(r) + (lambda r: cost[r + 1][j] if r < j else 0)(r) + acc[j]
                if c<cost[i][j]:
                    cost[i][j]=c
                    st[i][j]=r
    ans = []
    prStruct(a,0,n-1,st,ans)
    return ans
    #return cost[0][n-1]

def prStruct(a,i,j,st,ans):
    if j<i:
        return
    elif i==j:
         ans.append(a[i][0])
         return
    else:
        ans.append(a[st[i][j]][0])
        prStruct(a,i,st[i][j]-1,st,ans)
        prStruct(a,st[i][j]+1,j,st,ans)



keys = [12, 20, 10, 22]
wt = [34, 30, 50, 5]
n=4
a = list(sorted(zip(keys,wt),key=lambda x:x[0]))

acc = list(accumulate([i[1] for i in a]))

ans = dp(a,acc,4)

print(*ans)
