"""
Hosoya triangle (originally Fibonacci triangle) is a triangular arrangement
of numbers, where if you take any number it is the sum of 2 numbers above.
First line is always 1, and second line is always {1     1}.

This printHosoya function takes argument n which is the height of the triangle
(number of lines).

For example:
printHosoya( 6 ) would return:
1
1 1
2 1 2
3 2 2 3
5 3 4 3 5
8 5 6 6 5 8

The complexity is O(n^3).

"""

def hosoya(height, width):
    """ Calculates the hosoya triangle

    height -- height of the triangle
    """
    if (width == 0) and (height in (0,1)):
        return 1
    if (width == 1) and (height in (1,2)):
        return 1
    if height > width:
        return hosoya(height - 1, width) + hosoya(height - 2, width)
    if width == height:
        return hosoya(height - 1, width - 1) + hosoya(height - 2, width - 2)
    return 0

def print_hosoya(height):
    """Prints the hosoya triangle

    height -- height of the triangle
    """
    for i in range(height):
        for j in range(i + 1):
            print(hosoya(i, j) , end = " ")
        print ("\n", end = "")

def hosoya_testing(height):
    """Test hosoya function

    height -- height of the triangle
    """
    res = []
    for i in range(height):
        for j in range(i + 1):
            res.append(hosoya(i, j))
    return res
