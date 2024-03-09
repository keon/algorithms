import math

def distance(x,y):
    """[summary]
    HELPER-FUNCTION
    calculates the (eulidean) distance between vector x and y.

    Arguments:
        x {[tuple]} -- [vector]
        y {[tuple]} -- [vector]
    """
    assert len(x) == len(y), "The vector must have same length"
    result = ()
    sum = 0
    for i in range(len(x)):
        result += (x[i] -y[i],)
    for component in result:
        sum += component**2
    return math.sqrt(sum)


def nearest_neighbor(x, tSet):
    """[summary]
    Implements the nearest neighbor algorithm

    Arguments:
        x {[tupel]} -- [vector]
        tSet {[dict]} -- [training set]

    Returns:
        [type] -- [result of the AND-function]
    """
    assert isinstance(x, tuple) and isinstance(tSet, dict)
    current_key = ()
    min_d = float('inf')
    for key in tSet:
        d = distance(x, key)
        if d < min_d:
            min_d = d
            current_key = key
    return tSet[current_key]
