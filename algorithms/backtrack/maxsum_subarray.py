#time complexity : O(nlogn)
#space complexity : O(n)

# Returns sum of maximum sum subarray in arr[low.....high]
def maxSumSubArray(arr, low, high) :
    # Base Case
    if (low == high) :
        return arr[low]
    # Find middle element
    mid = low + ((high - low) // 2)
    # Return maximum of left ,right and mid crossing
    return max(maxSumSubArray(arr, low, mid),
               maxSumSubArray(arr, mid+1, high),
               maxSumCrossing(arr, low, mid, high))

# Find the maximum possible sum in arr[] such that arr[m] is part of it
def maxSumCrossing(arr, low, mid, high) :
    # Include elements on left of mid.
    summ = 0; left_sum = -10000
    for i in range(mid, low-1, -1) :
        summ = summ + arr[i]
        if (summ > left_sum) :
            left_sum = summ
    # Include elements on right of mid
    summ = 0; right_sum = -1000
    for i in range(mid + 1, high + 1) :
        summ = summ + arr[i]
        if (summ > right_sum) :
            right_sum = summ
    return max(left_sum + right_sum, left_sum, right_sum)

# Driver Code
# creating an empty list
listt = []
# number of elements as input
n = int(input("Enter number of elements in arr : "))
# iterating till the range
for i in range(0, n):
    element = int(input())
    listt.append(element) # adding the element
print("input array is : ",listt)
n = len(listt)
max_sum = maxSumSubArray(listt, 0, n-1)
print("Maximum contiguous sum is ", max_sum)

#sample test case 
#input array : [1, 3, 2, 4, 7]     [1,-1,2,3,-2]    [0,1,-1,0,0]     [2]     [-1,-1,-1,-1,-1]
#output      :  17                  5                1                2       -1
