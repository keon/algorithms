# A Dynamic Programming based Python Program for the Egg Dropping Puzzle
INT_MAX = 32767
 
# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def egg_drop(n, k):
    # A 2D table where entery eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    egg_floor = [[0 for x in range(k+1)] for x in range(n+1)]
 
    # We need one trial for one floor and0 trials for 0 floors
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
