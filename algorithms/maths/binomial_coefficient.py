# Python program to calculate C(n, k) 
  
# Returns value of Binomial Coefficient 
# C(n, k) 
def binomialCoefficient(n, k): 
    # since C(n, k) = C(n, n - k) 
    if(k > n - k): 
        k = n - k 
    # initialize result 
    res = 1
    # Calculate value of  
    # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1] 
    for i in range(k): 
        res = res * (n - i) 
        res = res / (i + 1) 
    return res 
  
# Driver program to test above function  
n,k= map(int, input().split())
res = binomialCoefficient(n, k) 
print("Value of C(% d, % d) is % d" %(n, k, res))




'''
TEST CASES

Input =
5 3
Output = 
Value of C( 5,  3) is  10

Input =
8 1
Output = 
Value of C( 8,  1) is  8

'''


