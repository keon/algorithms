"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""


def rotate_v1(array, k):
    """
    Rotate the entire array 'k' times
    T(n)- O(nk)

    :type array: List[int]
    :type k: int
    :rtype: void Do not return anything, modify array in-place instead.
    """
    array = array[:]
    n = len(array)
    for i in range(k):      # unused variable is not a problem
        temp = array[n - 1]
        for j in range(n-1, 0, -1):
            array[j] = array[j - 1]
        array[0] = temp
    return array


def rotate_v2(array, k):
    """
    Reverse segments of the array, followed by the entire array
    T(n)- O(n)
    :type array: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    array = array[:]

    def reverse(arr, a, b):
        while a < b:
            arr[a], arr[b] = arr[b], arr[a]
            a += 1
            b -= 1

    n = len(array)
    k = k % n
    reverse(array, 0, n - k - 1)
    reverse(array, n - k, n - 1)
    reverse(array, 0, n - 1)
    return array


def rotate_v3(array, k):
    if array is None:
        return None
    length = len(array)
    k = k % length
    return array[length - k:] + array[:length - k]
