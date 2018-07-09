"""
Sometimes you need to limit array result to use. Such as you only need the value over
10 or, you need value under than 100. By use this algorithms, you can limit your array
to specific value

If array, Min, Max value was given, it returns array that contains values of given array
which was larger than Min, and lower than Max. You need to give 'unlimit' to use only Min
or Max.

ex) limit([1,2,3,4,5], None, 3) = [1,2,3]

Complexity = O(n)
"""


def limit(arr, min_lim=None, max_lim=None):
    result = []
    if min_lim is None and max_lim:
        for i in arr:
            if i <= max_lim:
                result.append(i)
    elif min_lim and max_lim is None:
        for i in arr:
            if i >= min_lim:
                result.append(i)
    elif min_lim and max_lim:
        for i in arr:
            if i < min_lim:
                continue
            if i > max_lim:
                continue
            result.append(i)
    else:
        result = arr[::]

    return result
