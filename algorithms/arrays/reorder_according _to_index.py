"""
Python 3 program to sort an array according to given indexes.

Given two integer arrays of same size, “arr[]” and “index[]”,
reorder elements in “arr[]” according to given index array.

- Example:
    arr = [50, 40, 70, 60, 90]
    index = [3, 0, 4, 1, 2]
    (Reordered) arr = [40, 60, 90, 50, 70]

- Solution Approach:
    * Use an auxiliary array temp[] of same size as given arrays.
    * Traverse the given array.
    * Put all elements at their correct place in temp[] using index[].
    * Finally copy temp[] to arr[] and set all values of index[i] as i.

- Time Complexity: O(n)
- Space Complexity: O(n)

"""


def reorder(arr, index):

    n = len(arr)
    temp = [0] * n

    # arr[i] should be present at index[i] index
    for i in range(0, n):
        temp[index[i]] = arr[i]

    # Copy temp[] to arr[]
    for i in range(0, n):
        arr[i] = temp[i]
        index[i] = i
