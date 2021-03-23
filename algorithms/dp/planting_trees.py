"""
An even number of trees are left along one side of a country road. You've been assigned the job to
plant these trees at an even interval on both sides of the road. The length L and width W of the road
are variable, and a pair of trees must be planted at the beginning (at 0) and at the end (at L) of
the road. Only one tree can be moved at a time. The goal is to calculate the lowest amount of
distance that the trees have to be moved before they are all in a valid position.
"""

from math import sqrt
import sys

def planting_trees(trees, L, W):
    """
    Returns the minimum distance that trees have to be moved before they are all in a valid state.

        Parameters:
            tree (list<int>): A sorted list of integers with all trees' position along the road.
            L (int): An integer with the length of the road.
            W (int): An integer with the width of the road.

        Returns:
            A float number with the total distance trees have been moved.
    """
    trees = [0] + trees

    n_pairs = int(len(trees)/2)

    space_between_pairs = L/(n_pairs-1)

    target_locations = [location*space_between_pairs for location in range(n_pairs)]

    cmatrix = [[0 for _ in range(n_pairs+1)] for _ in range(n_pairs+1)]
    for ri in range(1, n_pairs+1):
        cmatrix[ri][0] = cmatrix[ri-1][0] + sqrt(W + abs(trees[ri]-target_locations[ri-1])**2)
    for li in range(1, n_pairs+1):
        cmatrix[0][li] = cmatrix[0][li-1] + abs(trees[li]-target_locations[li-1])

    for ri in range(1, n_pairs+1):
        for li in range(1, n_pairs+1):
            cmatrix[ri][li] = min(
                cmatrix[ri-1][li] + sqrt(W + (trees[li + ri]-target_locations[ri-1])**2),
                cmatrix[ri][li-1] + abs(trees[li + ri]-target_locations[li-1])
            )

    return cmatrix[n_pairs][n_pairs]