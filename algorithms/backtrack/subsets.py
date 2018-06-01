# Given a set of distinct integers, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
  # [3],
  # [1],
  # [2],
  # [1,2,3],
  # [1,3],
  # [2,3],
  # [1,2],
  # []
# ]


# O(2**n)


def subsets(nums):
    res = []
    backtrack(res, nums, [], 0)
    return res

def backtrack(res, nums, stack, pos):
    if pos == len(nums):
        res.append(list(stack))
    else:
        # take nums[pos]
        stack.append(nums[pos])
        backtrack(res, nums, stack, pos+1)
        stack.pop()
        # dont take nums[pos]
        backtrack(res, nums, stack, pos+1)


# simplified backtrack

# def backtrack(res, nums, cur, pos):
    # if pos >= len(nums):
        # res.append(cur)
    # else:
        # backtrack(res, nums, cur+[nums[pos]], pos+1)
        # backtrack(res, nums, cur, pos+1)


# Iteratively
def subsets2(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res

test = [1,2,3]
print(test)
print(subsets(test))
