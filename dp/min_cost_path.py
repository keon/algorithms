"""
To find min cost path 
from station 0 to station N-1,
where cost of moving from ith station to jth station is given as:

Matrix of size (N x N)
""" 

INF = float("inf")

def min_cost(cost):
 
    N = len(cost)
    # dist[i] stores minimum cost from 0 --> i.
    dist = [INF] * N

    dist[0] = 0   # cost from 0 --> 0 is zero.
  
    for i in range(N):
        for j in range(i+1,N):
            dist[j] = min(dist[j], dist[i] + cost[i][j])
  
    return dist[N-1]

if __name__ == '__main__':
    
    cost = [ [ 0, 15, 80, 90],         # cost[i][j] is the cost of
             [-1,  0, 40, 50],         # going from i --> j
             [-1, -1,  0, 70],         
             [-1, -1, -1,  0] ]        # cost[i][j] = -1 for i > j
    N = len(cost)
    print("The Minimum cost to reach station %d is %d" % (N, min_cost(cost)))
