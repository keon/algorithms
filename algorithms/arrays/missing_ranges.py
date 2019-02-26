"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""

'''
def missing_ranges(arr, lo, hi):

    res = []
    start = lo

    for n in arr:

        if n == start:
            start += 1
        elif n > start:
            res.append((start, n-1))
            start = n + 1

    if start <= hi:                 # after done iterating thru array,
        res.append((start, hi))     # append remainder to list

    return res
'''

# May be this would be good approach

def missingRanges(arr , low , high):
    result = []
    if arr[0] == start:
        result.append( (arr[1] + 1 , high) )
    elif arr[1] == high:
        result.append( (low , arr[0] - 1) ) 
    else:
        result.append( low , arr[0] - 1) )
        if arr[0] != arr[1]:
            result.append( (arr[0] + 1 , arr[1] - 1) )
        result.append( (arr[1] + 1 , high) )
    # return all possible missing ranges     
    return result

'''
Space Complexity : O(1)
Time Complexity : O(1)

Possible Example : 1 - [3, 5] low = 1 high = 10 -> answer: [(1, 2), (4, 4), (6, 10)]
                   2 - [2 , 10]  low = 1 , high = 20 -> answer : [ (1 ,1) , (3,9) , (11 , 20)]
                   
Assumptions : - Only one range given in the array
              - Array range lies between low and high
'''




"""
This could be one of the best solution if only one range is given in the array. 
If more ranges are given in the array , then we need to use loop for that.
Approach : In that Case
- Sort the given Array according to lower part of a range
- Assumption - there should not be any overlapping ranges
- Use this Program in loop
"""
