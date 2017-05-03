def heap_sort(arr):
    """ Heapsort
        Complexity: O(n log(n))
    """

    for i in range(len(arr)-1,-1,-1):
        heapify(arr, i)

        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp


def heapify(arr, end):
    """ Max heapify helper for heap_sort
    """
    last_parent = int((end-1)/2)

    # Iterate from last parent to first
    for parent in range(last_parent,-1,-1):
        current_parent = parent

        # Iterate from current_parent to last parent
        while current_parent <= last_parent:
            # Find greatest child of current_parent
            child = 2*current_parent + 1
            if child + 1 <= end and arr[child] < arr[child+1]:
                child = child + 1

            # Swap if child is greater than parent
            if arr[child] > arr[current_parent]:
                temp = arr[current_parent]
                arr[current_parent] = arr[child]
                arr[child] = temp

                # Update current_parent
                current_parent = child
            # If no swap occured, no need to continue iterating
            else:
                break

array = [1,5,65,23,57,1232,-1,-5,-2,242,100,4,423,2,564,9,0,10,43,64]
print(array)
print("After first heapify:")
is_heap = True
end = len(array)-2
heapify(array, end)
for i in range(0, int((end-1)/2)+1):
    if array[i] < array[2*i+1]:
        is_heap = False
    if 2*i + 2 <= end and array[i] < array[2*i + 2]:
        is_heap = False
print(array)
print(is_heap)
heap_sort(array)
print(array)