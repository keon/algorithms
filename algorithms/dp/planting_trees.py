"""
An even number of trees are left along one side of a country road. You've been
assigned the job to plant these trees at an even interval on both sides of the
road. The length and width of the road are variable, and a pair of trees must
be planted at the beginning (at 0) and at the end (at length) of the road. Only
one tree can be moved at a time. The goal is to calculate the lowest amount of
distance that the trees have to be moved before they are all in a valid
position.
"""

from math import sqrt

def planting_trees(trees, length, width):
    """
    Returns the minimum distance that trees have to be moved before they
    are all in a valid state.

        Parameters:
            tree (list<int>): A sorted list of integers with all trees'
                              position along the road.
            length (int): An integer with the length of the road.
            width (int): An integer with the width of the road.

        Returns:
            A float number with the total distance trees have been moved.
    """
    trees = [0] + trees

    n_pairs = int(len(trees)/2)

    space_between_pairs = length/(n_pairs-1)

    target_locations = [location*space_between_pairs for location in range(n_pairs)]

    cmatrix = [[0 for _ in range(n_pairs+1)] for _ in range(n_pairs+1)]
    for r_i in range(1, n_pairs+1):
        cmatrix[r_i][0] = cmatrix[r_i-1][0] + sqrt(
                width + abs(trees[r_i]-target_locations[r_i-1])**2)
    for l_i in range(1, n_pairs+1):
        cmatrix[0][l_i] = cmatrix[0][l_i-1] + abs(trees[l_i]-target_locations[l_i-1])

    for r_i in range(1, n_pairs+1):
        for l_i in range(1, n_pairs+1):
            cmatrix[r_i][l_i] = min(
                cmatrix[r_i-1][l_i] + sqrt(width + (trees[l_i + r_i]-target_locations[r_i-1])**2),
                cmatrix[r_i][l_i-1] + abs(trees[l_i + r_i]-target_locations[l_i-1])
            )

    return cmatrix[n_pairs][n_pairs]
