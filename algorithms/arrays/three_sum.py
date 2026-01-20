"""
Given an array S of n integers, are there three distinct elements
a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
{
  (-1, 0, 1),
  (-1, -1, 2)
}
"""
''' used two pointer apporach'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        
        for i in range(len(nums)-2):
            first= i
            left = i+1
            right = len(nums)-1
            
            while left < right:
                
                if nums[first] + nums[left] + nums[right] == 0:
                    if ([nums[first] , nums[left] , nums[right]]) not in sol:
                        sol.append([nums[first] , nums[left] , nums[right]])
                    right -=1
                    left +=1
                    
                elif nums[first] + nums[left] + nums[right] > 0:
                    right -=1
                
                elif nums[first] + nums[left] + nums[right] < 0:
                    left +=1
        return sol
