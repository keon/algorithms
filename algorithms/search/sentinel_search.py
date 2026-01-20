def SentinelSearch(arr, len, target):
 
    # Get last element of the array
    lastEle = arr[len - 1]
 
    # Element to be searched is placed at the last index known as "Sentinel"
    arr[len - 1] = target
    i = 0
    # Traverse through array 
    while (arr[i] != target):
        i += 1
 
    # Put the last element back
    arr[len - 1] = lastEle
 
    if ((i < len - 1) or (arr[len - 1] == target)):
        return i
    else:
        return -1
