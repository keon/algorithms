branch_coverage = {
    "simulation": False,
    "for": False,
    "while": False,
    "simulation-nested": False,
}

def insertion_sort(arr, simulation=False):
    """ Insertion Sort
        Complexity: O(n^2)
    """
    
    iteration = 0
    if simulation:
        branch_coverage["simulation"] = True
        print("iteration",iteration,":",*arr)
        
    for i in range(len(arr)):
        branch_coverage["for"] = True
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            branch_coverage["while"] = True
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
        
        if simulation:
                branch_coverage["simulation-nested"] = True
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)

    return arr

def print_coverage():
    print("branch coverage for `insertion_sort`:")
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

