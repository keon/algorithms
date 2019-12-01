"""
Given a n*n array.
it will give you all pairs shortest path length.

Time complexity : O(n^3)
"""

def all_pairs_shortest_path(adjacency_matrix):
    new_array = adjacency_matrix[:][:]

    for k in range(len(new_array)):
        for i in range(len(new_array)):
            for j in range(len(new_array)):
                if new_array[i][j] > new_array[i][k] + new_array[k][j]:
                    new_array[i][j] = new_array[i][k] + new_array[k][j]           
    
    return new_array