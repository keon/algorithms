def partition(nums, l, r):
    pivot = nums[r]
    i = l - 1

    for j in range(l, r):
        if nums[j] <= pivot:
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1

    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1


def quick(nums, l, r):
    if l < r:
        pi = partition(nums, l, r)
        quick(nums, l, pi - 1)
        quick(nums, pi + 1, r)


nums = [5, 4, 3, 2, 1]
quick(nums, 0, len(nums) - 1)
# Worst case - (N^2)
