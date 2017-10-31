# Python program to find min cost path 
# from station 0 to station N-1
 
global N
N = 4
def minCostRec(cost, s, d):
 
    if s == d or s+1 == d:
        return cost[s][d]
 
    min = cost[s][d]
 
    for i in range(s+1, d):
        c = minCostRec(cost,s, i) + minCostRec(cost, i, d)
        if c < min:
            min = c
    return min
 
def minCost(cost):
    return minCostRec(cost, 0, N-1)
cost = [ [0, 15, 80, 90],
         [float("inf"), 0, 40, 50],
         [float("inf"), float("inf"), 0, 70],
         [float("inf"), float("inf"), float("inf"), 0]
        ]
print "The Minimum cost to reach station %d is %d" % \
                                    (N, minCost(cost))
