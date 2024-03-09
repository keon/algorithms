"""
You are given K eggs, and you have access to a building with N floors
from 1 to N. Each egg is identical in function, and if an egg breaks,
you cannot drop it again. You know that there exists a floor F with
0 <= F <= N such that any egg dropped at a floor higher than F will
break, and any egg dropped at or below floor F will not break.
Each move, you may take an egg (if you have an unbroken one) and drop
it from any floor X (with 1 <= X <= N). Your goal is to know with
certainty what the value of F is. What is the minimum number of moves
that you need to know with certainty what F is, regardless of the
initial value of F?

Example:
Input: K = 1, N = 2
Output: 2
Explanation:
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with
certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
"""

# A Dynamic Programming based Python Program for the Egg Dropping Puzzle
INT_MAX = 32767


def egg_drop(n, k):
    """
    Keyword arguments:
    n -- number of floors
    k -- number of eggs
    """
    # A 2D table where entery eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    egg_floor = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # We need one trial for one floor and 0 trials for 0 floors
    for i in range(1, n+1):
        egg_floor[i][1] = 1
        egg_floor[i][0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, k+1):
        egg_floor[1][j] = j

    # Fill rest of the entries in table using optimal substructure
    # property
    for i in range(2, n+1):
        for j in range(2, k+1):
            egg_floor[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1 + max(egg_floor[i-1][x-1], egg_floor[i][j-x])
                if res < egg_floor[i][j]:
                    egg_floor[i][j] = res

    # eggFloor[n][k] holds the result
    return egg_floor[n][k]
