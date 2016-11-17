def firstOccurance(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        print("lo: ", lo, " hi: ", hi, " mid: ", mid)
        if (mid == 0 and array[mid] == query) or \
                (array[mid] == query and array[mid-1] < query):
            return mid
        elif array[mid] <= query:
            lo = mid + 1
        else:
            hi = mid - 1

array = [1,2,3,3,3,3,4,4,4,4,5,6,6,6]
print(array)
print("-----SEARCH-----")
query = 3
print("found first: ", query, " in index:" , firstOccurance(array, query))
print("-----SEARCH-----")
query = 5
print("found first: ", query, " in index:" , firstOccurance(array, query))
print("-----SEARCH-----")
query = 7
print("found first: ", query, " in index:" , firstOccurance(array, query))
print("-----SEARCH-----")
query = 1
print("found first: ", query, " in index:" , firstOccurance(array, query))
print("-----SEARCH-----")
query = -1
print("found first: ", query, " in index:" , firstOccurance(array, query))
print("-----SEARCH-----")
query = 9
print("found first: ", query, " in index:" , firstOccurance(array, query))
