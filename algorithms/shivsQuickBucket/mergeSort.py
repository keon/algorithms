def merge(nums, l, m, r):
    L, R = nums[l: m + 1], nums[m + 1: r + 1]

    i = j = 0
    k = l
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1


def mergeSort(nums, l, r):
    if l < r:
        m = (l + r) >> 1
        mergeSort(nums, l, m)
        mergeSort(nums, m + 1, r)
        merge(nums, l, m, r)


nums = [5, 4, 3, 2, 1]
mergeSort(nums, 0, len(nums) - 1)
# Worst case - (NlogN)
