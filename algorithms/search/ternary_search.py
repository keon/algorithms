
def ternary_search(arr, to_find):
    left = 0
    right = len(arr) - 1
    while left <= right:
        temp2 = left + (right - left) // 3
        temp3 = left + 2 * (right - left) // 3
        if to_find == arr[left]:
            return left
        elif to_find == arr[right]:
            return right
        elif to_find < arr[left] or to_find > arr[right]:
            return -1
        elif to_find <= arr[temp2]:
            right = temp2
        elif to_find > arr[temp2] and to_find <= arr[temp3]:
            left = temp2 + 1
            right = temp3
        else:
            left = temp3 + 1
    return -1
