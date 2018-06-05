#
# Linear search works in any array.
#
# T(n): O(n)
#

def linear_search(array, query):
    length = len(array)
    for i in range(length):
        if array[i] == query:
            return i

    return -1
