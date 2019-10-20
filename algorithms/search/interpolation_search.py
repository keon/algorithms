# interpolation search work for sorted list

def interpolation_search(numbersList,value):
    low = 0
    high = len(numbersList) - 1
    while numbersList[low] <= value and numbersList[high] >= value:
        mid = int(low + ((value - numbersList[low])*(high - low))/(numbersList[high] - numbersList[low]))
        if numbersList[mid]<value:
            low = mid + 1
        elif numbersList[mid]>value:
            high = mid - 1
        else:
            return mid
    if numbersList[low] == value:
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

 
