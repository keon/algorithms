'''

Stooge Sort
Time Complexity : O(n2.709)
Reference: https://www.geeksforgeeks.org/stooge-sort/

'''



def stoogesort(arr, l, h): 
    if l >= h: 
        return
   
    # If first element is smaller 
    # than last, swap them 
    if arr[l]>arr[h]: 
        t = arr[l] 
        arr[l] = arr[h] 
        arr[h] = t 
   
    # If there are more than 2 elements in 
    # the array 
    if h-l + 1 > 2: 
        t = (int)((h-l + 1)/3) 
   
        # Recursively sort first 2 / 3 elements 
        stoogesort(arr, l, (h-t)) 
   
        # Recursively sort last 2 / 3 elements 
        stoogesort(arr, l + t, (h)) 
   
        # Recursively sort first 2 / 3 elements 
        # again to confirm 
        stoogesort(arr, l, (h-t)) 
        

if __name__ == "__main__":
    array = [1,3,64,5,7,8]
    n = len(array) 
    stoogesort(array, 0, n-1) 
    for i in range(0, n): 
        print(array[i], end = ' ') 
