class Solution:
    """
    https://leetcode.com/problems/minimum-size-subarray-sum/solution/
    """
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # in this algo everytime we get greater than target sum we take it length and i it less than previous one we take minimum.

            n = len(nums)
            left = 0;
            sum = 0;
            ans=float('inf')
            for i in range(0,n):
                sum += nums[i]
                while (sum >= s):
                    ans = min(ans, i + 1 - left);
                    sum -= nums[left]
                    left+=1
                
            if ans!=float('inf'):
                return ans
            else:
                return 0
            # return (ans != INT_MAX) ? ans : 0;
