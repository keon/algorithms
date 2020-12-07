"""
Longest Palindrome Subsequence (LPS)

LPS is similar to longest palindrome substring, with the difference, 
that characters can be skipped, without changing the order.

For example, s1 = 'ACBDACDBA',
    LPS(s1) ='ABDCDBA'.

To see this clearly, we can align and capitalize the letters 
that are chosen to be a part of the LPS (ignore the spaces):

s1 =      'A c B D a C D B A',
           |   | |   | | | |
LPS(s1) = 'A   B D   C D B A'.

This uses a 2-D Dynamic Programming table. This function returns
a tuple of (LCS, table with numbers, table with backtracking arrows).

The table with arrows consists of three strings 'l', 'tl', and 't', which
represent 'left arrow', 'top-left diagonal arrow', and 'up (or top) arrow',
repectively.
"""

def longest_subsequence(str1):
    s1 = list(str1)
    s2 = s1[::-1]

    mat = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)] 
    arr = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)] 

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif i > 0 and j > 0 and s1[i-1] == s2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
                arr[i][j] = 'tl'
            elif i > 0 and j > 0 and s1[i-1] != s2[j-1]:
                top = mat[i-1][j]
                left = mat[i][j-1]
                if top > left:
                    arr[i][j] = 't'
                    mat[i][j] = top
                else:
                    arr[i][j] = 'l'
                    mat[i][j] = left

    lcs = []
    m = len(s1)
    n = len(s2)
    while m >= 1 and n >= 1:
            if s1[m-1] == s2[n-1]:
                lcs.append(s1[m-1])
            dir = arr[m][n]
            if dir == 't':
                m -= 1
            elif dir == 'tl':
                m -= 1
                n -= 1
            elif dir == 'l':
                n -= 1
            else:
                break
    lcs.reverse()
    return (''.join(lcs), mat, arr)

print(longest_subsequence('ACBDACDBA'))