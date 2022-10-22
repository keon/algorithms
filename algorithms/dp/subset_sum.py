"""
A recursive solution for subset sum problem

Returns true if there is a subset of set[] with sum equal to given sum

Example:
Input: 
set = [3, 34, 4, 12, 5, 2]
sum = 21
Output: True
Explanation: There is a subset (3, 4, 12, 2) with sum 21 

Note:

In the worst case the solution will try all possible subsets. Hence time complexity is exponential.
The problem is NP-Complete i.e. there is no known polynomial time solution for this problem.
"""

def isSubsetSum(set, n, sum):

	# Base Cases
	if (sum == 0):
		return True
	if (n == 0):
		return False
    
	# If last element is greater than sum, then ignore it
	if (set[n - 1] > sum):
		return isSubsetSum(set, n - 1, sum)

	return isSubsetSum(
		set, n-1, sum) or isSubsetSum(
		set, n-1, sum-set[n-1])