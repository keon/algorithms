"""
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it
can trap after raining.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is
represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.
"""

#  xn > xi > 0
# xi = max(height[:i])
# xn >= xi always and  xn-1 < xn > xn+1
def trap1(self, height: List[int]) -> int:
    n = len(height)
    if n == 0:
        return 0
    r_max = {}
    l_max = {}
    res = 0
    l_max[0] = height[0]
    for i in range(1,n):
        l_max[i] = max(height[i],l_max[i-1])
    r_max[n-1] = height[n-1]
    for i in range(n-2,-1,-1):
        r_max[i] = max(height[i], r_max[i+1] )

    for i in range(1,n-1):
        res += min(l_max[i],r_max[i])-height[i]

    return res


"""
another way to solve the problem
"""
#  xn > xi > 0
# xi = max(height[:i])
# xn >= xi always and  xn-1 < xn > xn+1
def trap2(self, height: List[int]) -> int:
    n = len(height)
    if n == 0:
        return 0
    left = 0
    right = n-1
    res = 0
    l_max, r_max =0,0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= l_max:
                l_max = height[left]
            else:
                res += l_max - height[left]
            left += 1
        else:
            if height[right] >= r_max:
                r_max = height[right]
            else:
                res += r_max - height[right]
            right -= 1

    return res
