def merge_sort(arr):
    """ Merge Sort
        Complexity: O(n log(n))
    """
    # Our recursive base case
    if len(arr)<= 1:
        return arr
    mid = len(arr)/2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[mid:]), merge_sort(arr[:mid])

    # Merge each side together
    return merge(left, right)

def merge(left, right):
    """ Merge helper
        Complexity: O(n)
    """
    arr = []
    left_cursor, right_cursor = 0,0
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            arr.append(left[left_cursor])
            left_cursor+=1
        else:
            arr.append(right[right_cursor])
            right_cursor+=1
    # Add the left overs if there's any left to the result
    if left:
        arr.extend(left[left_cursor:])
    if right:
        arr.extend(right[right_cursor:])
    return arr

array = [1,5, 7,4,3,2,1,9,0,10,43,64]
print(array)
print(merge_sort(array, 0, len(array)-1))
print(array)
