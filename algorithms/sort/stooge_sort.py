"""
Stooge Sort Implementation, Recursive Sorting Algorithm
Reference: https://www.geeksforgeeks.org/stooge-sort/

"""

def stooge_sort(arr, l, h):
	if l >= h: 
			return
	
	if arr[l]>arr[h]: 
			t = arr[l] 
			arr[l] = arr[h] 
			arr[h] = t 
	
	# If there are more than 2 elements in the array 
	if h-l + 1 > 2: 
			t = (int)((h-l + 1)/3) 
	
			# Recursively sort first 2 / 3 elements 
			stooge_sort(arr, l, (h-t)) 
	
			# Recursively sort last 2 / 3 elements 
			stooge_sort(arr, l + t, (h)) 
	
			# Recursively sort first 2 / 3 elements again to confirm 
			stooge_sort(arr, l, (h-t))
	return arr

