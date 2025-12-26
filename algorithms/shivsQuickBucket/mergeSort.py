def merge(nums, l, m, r, inv):
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
            inv += (len(L) - i)
        k += 1
    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1
    return inv

def mergeSort(nums, l, r, inv):
    if l < r:
        m = (l + r) >> 1
        inv = mergeSort(nums, l, m, inv)
        inv = mergeSort(nums, m + 1, r, inv)
        inv = merge(nums, l, m, r, inv)
    return inv


nums = [5, 4, 3, 2, 1]
# Count the total number of inversions
inv = 0
mergeSort(nums, 0, len(nums) - 1, inv)
# Worst case - (NlogN)
