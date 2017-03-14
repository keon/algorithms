"""
Given n, how many structurally unique BST's
(binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


"""
Taking 1~n as root respectively:
1 as root: # of trees = F(0) * F(n-1)  // F(0) == 1
2 as root: # of trees = F(1) * F(n-2)
3 as root: # of trees = F(2) * F(n-3)
...
n-1 as root: # of trees = F(n-2) * F(1)
n as root:   # of trees = F(n-1) * F(0)

So, the formulation is:
F(n) = F(0) * F(n-1) + F(1) * F(n-2) + F(2) * F(n-3) + ... + F(n-2) * F(1) + F(n-1) * F(0)
"""

def num_trees(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(i+1):
            dp[i] += dp[i-j] * dp[j-1]
    return dp[-1]
