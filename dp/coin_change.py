"""
Problem
Given a value N, if we want to make change for N cents, and we have infinite supply of each of 
S = { S1, S2, .. , Sm} valued //coins, how many ways can we make the change? 
The order of coins doesn’t matter.
For example, for N = 4 and S = [1, 2, 3], there are four solutions: 
[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3]. 
So output should be 4. 

For N = 10 and S = [2, 5, 3, 6], there are five solutions: 
[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5]. 
So the output should be 5.
"""

def count(s, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    m = len(s)
    table = [[0 for x in range(m)] for x in range(n+1)]
 
    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1
 
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - s[j]][j] if i-s[j] >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
 
            # total count
            table[i][j] = x + y
 
    return table[n][m-1]


if __name__ == '__main__':
    
    coins = [1, 2, 3]
    n = 4
    assert count(coins, n) == 4
    
    coins = [2, 5, 3, 6]
    n = 10
    assert count(coins, n) == 5
