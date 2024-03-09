def cycle_sort(arr):
    """
    cycle_sort
    This is based on the idea that the permutations to be sorted
    can be decomposed into cycles,
    and the results can be individually sorted by cycling.
    
    reference: https://en.wikipedia.org/wiki/Cycle_sort
    
    Average time complexity : O(N^2)
    Worst case time complexity : O(N^2)
    """
    len_arr = len(arr)
    # Finding cycle to rotate.
    for cur in range(len_arr - 1):
        item = arr[cur]

        # Finding an indx to put items in.
        index = cur
        for i in range(cur + 1, len_arr):
            if arr[i] < item:
                index += 1

        # Case of there is not a cycle
        if index == cur:
            continue

        # Putting the item immediately right after the duplicate item or on the right.
        while item == arr[index]:
            index += 1
        arr[index], item = item, arr[index]

        # Rotating the remaining cycle.
        while index != cur:

            # Finding where to put the item.
            index = cur
            for i in range(cur + 1, len_arr):
                if arr[i] < item:
                    index += 1

            # After item is duplicated, put it in place or put it there.
            while item == arr[index]:
                index += 1
            arr[index], item = item, arr[index]
    return arr
