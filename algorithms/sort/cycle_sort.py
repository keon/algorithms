def cycle_sort(arr):
    """
    Sorts an array in place using the Cycle Sort algorithm.

    Cycle Sort is a comparison-based, in-place, and non-comparing sorting algorithm that is particularly useful for
    minimizing the number of writes to the original array. It is based on the idea of dividing the array into
    cycles and rotating the elements in each cycle to their correct positions.

    Parameters:
    arr (list): A list of elements (numbers) to be sorted. The function modifies this list in place.

    Returns:
    list: The sorted list.

    Complexity:
    - Time Complexity: O(n^2) in the worst case, where n is the number of elements in the array.
    - Space Complexity: O(1) since the sorting is done in place.

    Algorithm Steps:
    1. Iterate through each element in the array using a variable `cycleStart`.
    2. For each element, determine its correct position in the sorted array by counting how many elements
       are less than the current element (`currElement`).
    3. If the current position (`currPos`) is the same as `cycleStart`, it means the element is already in
       the correct position, so continue to the next element.
    4. If not, swap the current element with the element at its correct position.
    5. Repeat the process until the cycle is complete and all elements are in their sorted position.

    Note: This implementation currently does not count the number of writes made to the array, as indicated by
    the commented-out `writes` variable.
    """
    for cycleStart in range(0, len(arr)-1):
        currElement = arr[cycleStart]
        currPos = cycleStart

        # Determine the position where the current element should go
        for i in range(cycleStart+1, len(arr)):
            if arr[i] < currElement:
                currPos += 1

        # If the element is already in the correct position, skip to the next
        if currPos == cycleStart:
            continue

        # Find the next position of the current element, in case of duplicates
        while currElement == arr[currPos]:
            currPos += 1

        # Swap the current element to its correct position
        arr[currPos], currElement = currElement, arr[currPos]

        # Continue the cycle for the element moved to its correct position
        while currPos != cycleStart:
            currPos = cycleStart

            # Determine the new position for the current element
            for j in range(cycleStart+1, len(arr)):
                if arr[j] < currElement:
                    currPos += 1

            # Find the next position of the current element, in case of duplicates
            while currElement == arr[currPos]:
                currPos += 1

            # Swap the current element to its correct position
            arr[currPos], currElement = currElement, arr[currPos]

    return arr
