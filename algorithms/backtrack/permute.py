# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
  # [1,2,3],
  # [1,3,2],
  # [2,1,3],
  # [2,3,1],
  # [3,1,2],
  # [3,2,1]
# ]

def permute(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
                print(i, perm[:i], [n], perm[i:], ">>>>", new_perms)
        perms = new_perms
    return perms

# DFS Version
# def permute(nums):
    # res = []
    # dfs(res, nums, [])
    # return res

# def dfs(res, nums, path):
    # if not nums:
        # res.append(path)
    # for i in range(len(nums)):
        # print(nums[:i]+nums[i+1:])
        # dfs(res, nums[:i]+nums[i+1:], path+[nums[i]])

test = [1,2,3]
print(test)
print(permute(test))
