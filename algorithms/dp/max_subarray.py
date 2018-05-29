
def max_subarray(array):
    max_so_far = max_now = array[0]
    for i in range(1, len(array)):
        max_now = max(array[i], max_now + array[i])
        max_so_far = max(max_so_far, max_now)
    return max_so_far

a = [1, 2, -3, 4, 5, -7, 23]
print(a)
print(max_subarray(a))
