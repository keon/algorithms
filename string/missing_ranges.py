## find missing ranges between low and high in the given array.
# ex) [3, 5] lo=1 hi=10 => answer: [1->2, 4, 6->10]

def missing_ranges(nums, lo, hi):
    res = []
    next_num = lo
    for num in nums:
        if num < next_num:
            continue
        if num == next_num:
            next_num += 1
            continue
        res.append(get_range(next_num, num-1))
        next_num = num + 1
    if next_num <= hi:
        res.append(get_range(next_num, hi))
    return res

def get_range(n1, n2):
    if n1 == n2:
        return str(n1)
    else:
        return str(n1) + "->" + str(n2)

nums = [3, 5, 10, 11, 12, 15, 19]
print("original:", nums)
print("missing range: ", missing_ranges(nums,0,20))
