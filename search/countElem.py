def count_elem(array, query):
    def first_occurance(array, query):
        lo, hi = 0, len(array) -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (array[mid] == query and mid == 0) or \
                (array[mid] == query and array[mid-1] < query):
                return mid
            elif (array[mid] <= query):
                lo = mid + 1
            else:
                hi = mid - 1
    def last_occurance(array, query):
        lo, hi = 0, len(array) -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (array[mid] == query and mid == len(array) - 1) or \
                (array[mid] == query and array[mid+1] > query):
                return mid
            elif (array[mid] <= query):
                lo = mid + 1
            else:
                hi = mid - 1

    first = first_occurance(array, query)
    last = last_occurance(array, query)
    if first is None or last is None:
        return None
    return last - first + 1



array = [1,2,3,3,3,3,4,4,4,4,5,6,6,6]
print(array)
print("-----COUNT-----")
query = 3
print("count: ", query, " :" , count_elem(array, query))
print("-----COUNT-----")
query = 5
print("count: ", query, " :" , count_elem(array, query))
print("-----COUNT-----")
query = 7
print("count: ", query, " :" , count_elem(array, query))
print("-----COUNT-----")
query = 1
print("count: ", query, " :" , count_elem(array, query))
print("-----COUNT-----")
query = -1
print("count: ", query, " :" , count_elem(array, query))
print("-----COUNT-----")
query = 9
print("count: ", query, " :" , count_elem(array, query))
