import numpy

# train set for the AND-function
trainSetAND = {(0,0) : 0, (0,1) :0, (1,0) : 0, (1,1) : 1} 

# train set for light or dark colors
trainSetLight = {(11, 98, 237) : 'L', (3, 39, 96) : 'D', (242, 226, 12) : 'L', (99, 93, 4) : 'D',
(232, 62, 32) : 'L', (119, 28, 11) : 'D', (25, 214, 47) : 'L', (89, 136, 247) : 'L',
(21, 34, 63) : 'D', (237, 99, 120) : 'L', (73, 33, 39) : 'D'}

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
    import math
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
    currentKey = ()
    MAX = 32768 # max value 
    minD = MAX
    for key in tSet:
        d = distance(x, key)
        if d < minD:
            minD = d
            currentKey = key
    return tSet[currentKey]

# Some test cases

# print(nearest_neighbor((1,1), trainSetAND)) # => 1
# print(nearest_neighbor((0,1), trainSetAND)) # => 0
# print(nearest_neighbor((31, 242, 164), trainSetLight)) # => L
# print(nearest_neighbor((13, 94, 64), trainSetLight)) # => D
# print(nearest_neighbor((230, 52, 239), trainSetLight)) # => L