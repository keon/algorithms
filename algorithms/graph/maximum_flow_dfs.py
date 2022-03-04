"""
Given a n*n adjacency array.
it will give you a maximum flow.
This version use DFS to search path.

Assume the first is the source and the last is the sink.

Time complexity - O(Ef)

example

graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

answer should be

23

"""
import copy
import math

def maximum_flow_dfs(adjacency_matrix):
    """
    Get the maximum flow through a graph using a depth first search
    """

    #initial setting
    new_array = copy.deepcopy(adjacency_matrix)
    total = 0

    while True:
        #setting min to max_value
        min = math.inf
        #save visited nodes
        visited = [0]*len(new_array)
        #save parent nodes
        path = [0]*len(new_array)

        #initialize stack for DFS
        stack = []

        #initial setting
        visited[0] = 1
        stack.append(0)

        #DFS to find path
        while len(stack) > 0:
            #pop from queue
            src = stack.pop()
            for k in range(len(new_array)):
                #checking capacity and visit
                if new_array[src][k] > 0 and visited[k] == 0:
                    #if not, put into queue and chage to visit and save path
                    visited[k] = 1
                    stack.append(k)
                    path[k] = src

        #if there is no path from src to sink
        if visited[len(new_array) - 1] == 0:
            break

        #initial setting
        tmp = len(new_array) - 1

        #Get minimum flow
        while tmp != 0:
            #find minimum flow
            if min > new_array[path[tmp]][tmp]:
                min = new_array[path[tmp]][tmp]
            tmp = path[tmp]

        #initial setting
        tmp = len(new_array) - 1

        #reduce capacity
        while tmp != 0:
            new_array[path[tmp]][tmp] = new_array[path[tmp]][tmp] - min
            tmp = path[tmp]

        total = total + min

    return total

