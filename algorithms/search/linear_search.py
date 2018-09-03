#
# Linear search works in any array.
#
# T(n): O(n)
#

def linear_search(array, query):
    for i in range(len(array)):
        if array[i] == query:
            return i

    return -1
