# interpolation search work for sorted list

def interpolation_search(numbers_List,value):
    low = 0
    high = len(numbers_List) - 1
    while numbers_List[low] <= value and numbers_List[high] >= value:
        mid = int(low + ((value - numbers_List[low])*(high - low))/(numbers_List[high] - numbers_List[low]))
        if numbers_List[mid]<value:
            low = mid + 1
        elif numbers_List[mid]>value:
            high = mid - 1
        else:
            return mid
    if numbers_List[low] == value:
        return low
    return None

def test(x):
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    index = interpolation_search(arr, x)
    if index != -1:
        print ("The element", x, "is at the index", index)
    else:
        print ("Element", x, "not found!")
test(123)
test(16)
test(21)
test(274)
test(42)

 
