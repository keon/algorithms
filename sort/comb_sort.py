"""

https://en.wikipedia.org/wiki/Comb_sort

Worst-case performance: O(N^2)

"""

from math import floor


def comb_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(floor(gap/shrink))
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                swap(i, i + gap)
                sorted = False
            i = i + 1


array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
         4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
print(array)
comb_sort(array)
print(array)
