import numpy

def distance(x,y):
    """[summary]
    HELPER-FUNCTION
    calculates the (eulidean) distance between vector x and y.
    
    We use the numpy libriary

    Arguments:
        x {[tuple]} -- [vector]
        y {[tuple]} -- [vector]
    """
    assert len(x) == len(y), "The vector must have same length"
    result = ()
    for i in range(len(x)):
        result += (x[i] -y[i],)
    return numpy.linalg.norm(result)

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
    min_d = numpy.inf
    for key in tSet:
        d = distance(x, key)
        if d < min_d:
            min_d = d
            current_key = key
    return tSet[current_key]