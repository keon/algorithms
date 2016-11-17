def binarySearch(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        print("--------")
        mid = lo + (hi - lo) // 2
        print("lo: ", lo)
        print("hi: ", hi)
        print("mid: ", mid)
        val = array[mid]
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

array = [1,2,3,3,3,3,4,4,4,4,5,6]
print(array)
print("-----SEARCH-----")
print("found: ", 5, " in index:" , binarySearch(array, 5))
print("-----SEARCH-----")
print("found: ", 6, " in index:" , binarySearch(array, 6))
print("-----SEARCH-----")
print("found: ", 7, " in index:" , binarySearch(array, 7))
print("-----SEARCH-----")
print("found: ", -1, " in index:" , binarySearch(array, -1))
print("-----SEARCH-----")
