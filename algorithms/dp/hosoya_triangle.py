"""
Hosoya triangle (originally Fibonacci triangle) is a triangular arrangement
of numbers, where if you take any number it is the sum of 2 numbers above.
First line is always 1, and second line is always {1     1}.

This printHosoya function takes argument n which is the height of the triangle
(number of lines).

For example:
printHosoya( 6 ) would return:
1 
1 1 
2 1 2 
3 2 2 3 
5 3 4 3 5 
8 5 6 6 5 8

The complexity is O(n^3).

"""


def hosoya(n, m): 
    if ((n == 0 and m == 0) or (n == 1 and m == 0) or
        (n == 1 and m == 1) or (n == 2 and m == 1)): 
        return 1
    if n > m: 
        return hosoya(n - 1, m) + hosoya(n - 2, m) 
    elif m == n: 
        return hosoya(n - 1, m - 1) + hosoya(n - 2, m - 2) 
    else: 
        return 0
          
def print_hosoya(n): 
    for i in range(n): 
        for j in range(i + 1): 
            print(hosoya(i, j) , end = " ") 
        print ("\n", end = "")

def hosoya_testing(n):
    x = []
    for i in range(n): 
        for j in range(i + 1): 
            x.append(hosoya(i, j))
    return x
