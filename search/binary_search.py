#
# Binary search works for a sorted array.
# Note: The code logic is written for an array sorted in
#       increasing order.
# T(n): O(log n)
#


def binary_search(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = array[mid]
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def main():
    array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
    print(array)
    print("-----SEARCH-----")
    print("found: ", 5, " in index:", binary_search(array, 5))
    print("-----SEARCH-----")
    print("found: ", 6, " in index:", binary_search(array, 6))
    print("-----SEARCH-----")
    print("found: ", 7, " in index:", binary_search(array, 7))
    print("-----SEARCH-----")
    print("found: ", -1, " in index:", binary_search(array, -1))
    print("-----SEARCH-----")

if __name__ == "__main__":
    main()
