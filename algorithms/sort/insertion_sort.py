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
    covered = 0
    print("branch coverage for `insertion_sort`:")
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
        if hit: covered += 1;
    print(f"Branch coverage: {covered / len(branch_coverage) * 100}")

insertion_sort([])
insertion_sort([1])
insertion_sort([69, 420])
insertion_sort([420, 69])
insertion_sort([0, 1, 2, 3, 4, 3, 2, 1, 0])
insertion_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], True)
insertion_sort([0, 1, 2, 3, 4, 3, 2, 1, 0], True)
print_coverage()
