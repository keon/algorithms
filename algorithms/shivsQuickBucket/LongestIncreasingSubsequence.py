# 300. Longest Increasing Subsequence
   
''' 
Logic is: 
    If the curr element is greater the last element added to the subsequence: 
    append it to increase the size of the subsequence
    else 
    replace a greater element in the subsequence with this smaller element 
    which will open doors for us to add another element in future 
    # why else ? -> 
    we would want to minimize our elements in the subsequence as to 
    increase our chances of adding a newer element in future
    However this will not give the correct subsequence because of else statement
'''
import bisect


def lengthOfLIS(nums) -> int:
    sub = [nums[0]]
    for num in nums[1:]:
        id = bisect.bisect_left(sub, num) # bisect_left or bisect_right always give the first greater element if the num is not present in sub
        if id == len(sub): sub.append(num)
        else: sub[id] = num # increase our chances of adding a newer element in future
    return len(sub)