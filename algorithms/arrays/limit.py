"""
Sometimes you need to limit array result to use. Such as you only need the value over
10 or, you need value under than 100. By use this algorithms, you can limit your array
to specific value

If array, Min, Max value was given, it returns array that contains values of given array
which was larger than Min, and lower than Max. You need to give 'unlimit' to use only Min
or Max.

ex) limit([1,2,3,4,5], 'unlimit', 3) = [1,2,3]

Complexity = O(n)
"""

def limit(arr, Min='unlimit', Max='unlimit'):
    result = []
    if Min == 'unlimit':
        for i in arr:
            if i<=Max:
                result.append(i)
    elif Max == 'unlimit':
        for i in arr:
            if i>=Min:
                result.append(i)
    else:
        for i in arr:
            if i>=Min and i<=Max:
                result.append(i)

    return result
