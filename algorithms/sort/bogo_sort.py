import random

def bogo_sort(arr):
    '''Bogo Sort
        Best Case Complexity: O(n)
        Worst Case Complexity: O(∞)
        Average Case Complexity: O(n-n!)
    '''
    while not inorder(arr):
        print(arr)
        random.shuffle(arr)
    return arr

def inorder(arr):
    #check the array is inorder
    i = 0
    arr_len = len(arr)
    while i+1< arr_len:
        if arr[i] > arr[i+1]:
            return False
        i += 1
    return True
