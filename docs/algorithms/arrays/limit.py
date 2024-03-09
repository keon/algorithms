"""
Sometimes you need to limit array result to use. Such as you only need the 
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value

If array, Min, Max value was given, it returns array that contains values of 
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.

ex) limit([1,2,3,4,5], None, 3) = [1,2,3]

Complexity = O(n)
"""

# tl:dr -- array slicing by value
def limit(arr, min_lim=None, max_lim=None):
    if len(arr) == 0:
        return arr

    if min_lim is None:
        min_lim = min(arr)
    if max_lim is None:
        max_lim = max(arr)

    return list(filter(lambda x: (min_lim <= x <= max_lim), arr))
