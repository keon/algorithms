"""
cycle_sort
This is based on the idea that the permutations to be sorted
can be decomposed into cycles,
and the results can be individually sorted by cycling.

reference: https://en.wikipedia.org/wiki/Cycle_sort

Average time complexity : O(N^2)
Worst case time complexity : O(N^2)
"""
def cycle_sort(arr):
    # writes = 0
    for cycleStart in range(0, len(arr)-1):
        currElement = arr[cycleStart]
        currPos = cycleStart
        for i in range(cycleStart+1, len(arr)):
            if arr[i] < currElement:
                currPos += 1
        if currPos == cycleStart:
            continue
        while currElement == arr[currPos]:
            currPos += 1
        arr[currPos], currElement = currElement, arr[currPos]
        # writes += 1

        while currPos != cycleStart:
            currPos = cycleStart
            for j in range(cycleStart+1, len(arr)):
                if arr[j] < currElement:
                    currPos += 1
            while currElement == arr[currPos]:
                currPos += 1
            arr[currPos], currElement = currElement, arr[currPos]
            # writes += 1
    # print(writes)
    return arr
