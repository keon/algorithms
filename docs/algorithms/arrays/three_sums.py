#this code is provided by a youtuber ALGOENGINE

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # this sorts the array 
        answer = [] # this stores the triplets 
        
        for i in range(len(nums)-2): #here we have to iterate last second elemnt because of triplet condition
            if i > 0 and nums[i] == nums[i-1]:  # this will move the i pointer from the current pointer to next to run the 
                continue
            
            l = i + 1  # here we are using three pointer so this is second pointer 
            r = len(nums) - 1 # here we assigning third pointer but this is at end
            
            while l < r:
                total = nums[i] + nums[l] + nums[r] # this one adds the number which are pointed by the pointers 
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triplet = [nums[i], nums[l], nums[r]]
                    answer.append(triplet)
                    
                    while l < r and nums[l] == triplet[1]:
                        l += 1
                    while l < r and nums[r] == triplet[2]:
                        r -= 1
        
        return answer