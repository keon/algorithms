"""
    Largest Sum of Contiguous Subarray (Kadane’s Algorithm)
    Returns Largest sum of elements of a contiguous subarray.
    Time Complexity: O(n)

    ex.-
        Input: 2 3 4 -1 -2 1 5 -3
        Output: 7 
        Logic: 4+(-1)+(-2)+1+5

    largestContSum(arr) -- 
        returns the Largest Sum of Contiguous Subarray. 
        Warning: since python3 does not have limits on its variable it might give wrong result on very high negative values.

    
    largestContSum(arr,lowerLimit) --
        Does the same as above but fixes the Warning by providing additional parameter "lowerLimit" to set the lower limit in case
        of extreme negative values.
    

"""
from sys import maxsize

def largestContSum(arr,lowerLimit=-maxsize - 1):
    result=lowerLimit
    currentSum=0
    for i in arr:
        currentSum+=i
        print(currentSum)
        result=max(result,currentSum)
        if(currentSum<0):
            currentSum=0
    return result

