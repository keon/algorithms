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

#  interpolation_search([2,3,4,5,6,7],4)
#  return 2 
 
