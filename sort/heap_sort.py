def max_heap_sort(arr):
    """ Heap Sort that uses a max heap to sort an array in ascending order
        Complexity: O(n log(n))
    """
    for i in range(len(arr)-1,0,-1):
        max_heapify(arr, i)
        
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

	
def max_heapify(arr, end):
    """ Max heapify helper for max_heap_sort
    """
    last_parent = int((end-1)/2)

    # Iterate from last parent to first
    for parent in range(last_parent,-1,-1):
        current_parent = parent

        # Iterate from current_parent to last_parent
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

                current_parent = child
            # If no swap occured, no need to keep iterating
            else:
                break
		

def min_heap_sort(arr):
    """ Heap Sort that uses a min heap to sort an array in ascending order
        Complexity: O(n log(n))
    """
    for i in range(0, len(arr)-1):
        min_heapify(arr, i)
	

def min_heapify(arr, start):
    """ Min heapify helper for min_heap_sort
    """
    # Offset last_parent by the start (last_parent calculated as if start index was 0)
    # All array accesses need to be offet by start
    end = len(arr)-1
    last_parent = int((end-start-1)/2)

    # Iterate from last parent to first
    for parent in range(last_parent,-1,-1):
        current_parent = parent

        # Iterate from current_parent to last_parent
        while current_parent <= last_parent:
            # Find lesser child of current_parent
            child = 2*current_parent + 1
            if child + 1 <= end-start and arr[child+start] > arr[child+1+start]:
                child = child + 1

            # Swap if child is less than parent
            if arr[child+start] < arr[current_parent+start]:
                temp = arr[current_parent+start]
                arr[current_parent+start] = arr[child+start]
                arr[child+start] = temp

                current_parent = child
            # If no swap occured, no need to keep iterating
            else:
                break

if __name__ == '__main__':
	import timeit

	array = [1,5,65,23,57,1232,-1,-5,-2,242,100,4,423,2,564,9,0,10,43,64]
	print("array:")
	print(array)
	print("Max Heapify:")
	max_heap_sort(array)
	print(array)
	array = [1,5,65,23,57,1232,-1,-5,-2,242,100,4,423,2,564,9,0,10,43,64]
	print("Min Heapify:")
	min_heap_sort(array)
	print(array)
	print("Max Heapify Time:", timeit.timeit('max_heap_sort(array)', setup="from __main__ import max_heap_sort, array",number=10000))
	print("Min Heapify Time:", timeit.timeit('min_heap_sort(array)', setup="from __main__ import min_heap_sort, array",number=10000))
