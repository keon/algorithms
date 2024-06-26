'''

Stooge Sort
Time Complexity : O(n2.709)
Reference: https://www.geeksforgeeks.org/stooge-sort/

'''

branch_coverage = {
    "check_1": False,  # if branch for x > 0
    "check_2": False,   # else branch
    "check_3": False,
    "check_4": False,
}

def stoogesort(arr, l, h): 
    if l >= h: 
        branch_coverage["check_1"] = True
        return
   
    # If first element is smaller 
    # than last, swap them 
    if arr[l]>arr[h]: 
        branch_coverage["check_2"] = True
        t = arr[l] 
        arr[l] = arr[h] 
        arr[h] = t 
   
    # If there are more than 2 elements in 
    # the array 
    if h-l + 1 > 2: 
        branch_coverage["check_3"] = True
        t = (int)((h-l + 1)/3) 
   
        # Recursively sort first 2 / 3 elements 
        stoogesort(arr, l, (h-t)) 
   
        # Recursively sort last 2 / 3 elements 
        stoogesort(arr, l + t, (h)) 
   
        # Recursively sort first 2 / 3 elements 
        # again to confirm 
        stoogesort(arr, l, (h-t)) 

    branch_coverage["check_4"] = True

def print_coverage():
    total = len(branch_coverage)
    reached = sum(branch_coverage.values())
    coverage_percentage = (reached / total) * 100 
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
    print(f"coverage_percentage: {coverage_percentage}%")

arr1 = [10, -1, 2, 3, 0]
arr2 = []
result = stoogesort(arr1, 0, len(arr1) - 1)
result = stoogesort(arr1, 0, len(arr2) - 1)
print_coverage()
        

# if __name__ == "__main__":
#     array = [1,3,64,5,7,8]
#     n = len(array) 
#     stoogesort(array, 0, n-1) 
#     for i in range(0, n): 
#         print(array[i], end = ' ') 
