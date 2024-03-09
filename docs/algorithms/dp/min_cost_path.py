"""
author @goswami-rahul

To find minimum cost path
from station 0 to station N-1,
where cost of moving from ith station to jth station is given as:

Matrix of size (N x N)
where Matrix[i][j] denotes the cost of moving from
station i --> station j   for i < j

NOTE that values where Matrix[i][j] and i > j does not
mean anything, and hence represented by -1 or INF

For the input below (cost matrix),
Minimum cost is obtained as from  { 0 --> 1 --> 3}
                                  = cost[0][1] + cost[1][3] = 65
the Output will be:

The Minimum cost to reach station 4 is 65

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

INF = float("inf")


def min_cost(cost):
    """Find minimum cost.

    Keyword arguments:
    cost -- matrix containing costs
    """
    length = len(cost)
    # dist[i] stores minimum cost from 0 --> i.
    dist = [INF] * length

    dist[0] = 0   # cost from 0 --> 0 is zero.

    for i in range(length):
        for j in range(i+1,length):
            dist[j] = min(dist[j], dist[i] + cost[i][j])

    return dist[length-1]


if __name__ == '__main__':
    costs = [ [ 0, 15, 80, 90],         # cost[i][j] is the cost of
             [-1,  0, 40, 50],         # going from i --> j
             [-1, -1,  0, 70],
             [-1, -1, -1,  0] ]        # cost[i][j] = -1 for i > j
    TOTAL_LEN = len(costs)

    mcost = min_cost(costs)
    assert mcost == 65

    print(f"The minimum cost to reach station {TOTAL_LEN} is {mcost}")
