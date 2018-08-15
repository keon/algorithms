import math

def jump_search(arr,target):
    """Jump Search
        Worst-case Complexity: O(√n) (root(n))
        All items in list must be sorted like binary search

        Find block that contains target value and search it linearly in that block
        It returns a first target value in array

        reference: https://en.wikipedia.org/wiki/Jump_search

    """
    n = len(arr)
    block_size = int(math.sqrt(n))
    block_prev = 0
    block= block_size

    # return -1 means that array doesn't contain taget value
    # find block that contains target value
    
    if arr[n - 1] < target:
        return -1  
    while block <= n and arr[block - 1] < target:
        block_prev = block
        block += block_size

    # find target value in block
    
    while arr[block_prev] < target :
        block_prev += 1
        if block_prev == min(block, n) :
            return -1

    # if there is target value in array, return it
    
    if arr[block_prev] == target :
        return block_prev
    else :
        return -1
