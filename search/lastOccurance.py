def lastOccurance(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if (array[mid] == query and mid == len(array)-1) or \
           (array[mid] == query and array[mid+1] > query):
               return mid
        elif (array[mid] <= query):
            lo = mid + 1
        else:
            hi = mid - 1


array = [1,2,3,3,3,3,4,4,4,4,5,6,6,6]
print(array)
print("-----SEARCH-----")
query = 3
print("found last: ", query, " in index:" , lastOccurance(array, query))
print("-----SEARCH-----")
query = 5
print("found last: ", query, " in index:" , lastOccurance(array, query))
print("-----SEARCH-----")
query = 7
print("found last: ", query, " in index:" , lastOccurance(array, query))
print("-----SEARCH-----")
query = 1
print("found last: ", query, " in index:" , lastOccurance(array, query))
print("-----SEARCH-----")
query = -1
print("found last: ", query, " in index:" , lastOccurance(array, query))
print("-----SEARCH-----")
query = 9
print("found last: ", query, " in index:" , lastOccurance(array, query))
print("-----SEARCH-----")
query = 6
print("found last: ", query, " in index:" , lastOccurance(array, query))
