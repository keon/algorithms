def couting_sort(arr,k):
	"""Couting_sort
		Sorting a array which has no element greater than k
		Complexity: 0(n)
	"""
	temp_arr = [0]*(k+1)
	for i in range(0,len(arr)):
		temp_arr[arr[i]] = temp_arr[arr[i]]+1
	#temp_array[i] is the times the number i appear in arr
	print(temp_arr)
	for i in range(1, k+1):
		temp_arr[i] = temp_arr[i] + temp_arr[i-1]
	#temp_array[i] is the number of element less than or equal i in arr
	result_arr = [0]*len(arr)
	#creating a result_arr an put the element in a correct positon
	for i in range(len(arr)-1,-1,-1):
		result_arr[temp_arr[arr[i]]-1] = arr[i]
		temp_arr[arr[i]] = temp_arr[arr[i]]-1

	return result_arr 


x =couting_sort([2,5,3,0,2,3,0,3],9)
print (x)
