# Corrected grammatical errors.
# result -> results, need the -> need to, need value -> need a value, under than 100 -> remove than
# By use this algorithms -> By using this algorithm, specific -> a specific, array -> an array
# of given -> of a given, 'unlimit' -> unlimited
"""
Sometimes you need to limit array results to use. Such as you only need to
 value over 10 or, you need a value under 100. By using this algorithm, you
 can limit your array to a specific value

If an array, Min, Max value was given, it returns an array that contains values of 
 a given array which was larger than Min, and lower than Max. You need to give
 'unlimited' to use only Min or Max.

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
