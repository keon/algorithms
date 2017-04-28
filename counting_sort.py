  def counting_sort(arr):
	"""Couting_sort
		Sorting a array which has no element greater than k
		Complexity: 0(n)
	"""
	
	k = max(arr)
	m = min(arr)
	if m < 0:
		different = m
		for i in range (len(arr)):
			arr[i]+= m
	else:
		different = 0
	temp_arr = [0]*(k+1)
	for i in range(0,len(arr)):
		temp_arr[arr[i]]= temp_arr[arr[i]]+1
	#temp_array[i] is the times the number i appear in arr
	for i in range(1, k+1):
		temp_arr[i] = temp_arr[i] + temp_arr[i-1]
	#temp_array[i] is the number of element less than or equal i in arr
	result_arr = [0]*len(arr)
	#creating a result_arr an put the element in a correct positon
	for i in range(len(arr)-1,-1,-1):
		result_arr[temp_arr[arr[i]]-1] = arr[i]-different
		temp_arr[arr[i]] = temp_arr[arr[i]]-1
	
	return result_arr 


x =counting_sort([1,2,3,4,9,1,2,8,3,5,7,0,9,8,1,7,4,5])
print (x)
