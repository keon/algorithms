"""
Given a n*n adjacency array.
it will give you all pairs shortest path length.
use deepcopy to preserve the original information.

Time complexity : O(E^3)

example

a = [[0, 0.1, 0.101, 0.142, 0.277], [0.465, 0, 0.191, 0.192, 0.587], [0.245, 0.554, 0, 0.333, 0.931], [1.032, 0.668, 0.656, 0, 0.151], [0.867, 0.119, 0.352, 0.398, 0]]

result 

[[0, 0.1, 0.101, 0.142, 0.277], [0.436, 0, 0.191, 0.192, 0.34299999999999997], [0.245, 0.345, 0, 0.333, 0.484], [0.706, 0.27, 0.46099999999999997, 0, 0.151], [0.5549999999999999, 0.119, 0.31, 0.311, 0]]

"""
import copy

def all_pairs_shortest_path(adjacency_matrix):
    new_array = copy.deepcopy(adjacency_matrix)

    for k in range(len(new_array)):
        for i in range(len(new_array)):
            for j in range(len(new_array)):
                if new_array[i][j] > new_array[i][k] + new_array[k][j]:
                    new_array[i][j] = new_array[i][k] + new_array[k][j]           
    
    return new_array