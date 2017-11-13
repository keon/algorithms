//Given a value N, if we want to make change for N Cents, and we have infinite supply of each of S(coins) = { S1, S2, .. , Sm}, 
//how many ways can we make the change? 

//For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
//For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}

coins = map(int, raw_input().split(','))
n = int(input())

combs = {}
def combinations(n, coins ,k):
    ways = 0
    if n == 0:
        return 1  // if n=0 there is only one way(no coin change)
    
    if k >= len(coins) and n != 0:     
        return 0              
    
    if (n, k) in combs:
        return combs[(n, k)]
    
    c = 0
    while(n-c>=0):
        ways += combinations(n-c,coins,k+1)
        c += coins[k]
    
    combs[(n, k)] = ways
    return ways


print combinations(n, coins, 0)
