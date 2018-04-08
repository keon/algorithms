import unittest
def counting_sort(arr):
	"""
    Counting_sort
	Sorting a array which has no element greater than k
	Creating a new temp_arr,where temp_arr[i] contain the number of
	element less than or equal to i in the arr
    Then placing the number i into a correct position in the result_arr
	return the result_arr
	Complexity: 0(n)
	"""

	m = min(arr)
	#in case there are negative elements, change the array to all positive element
	different = 0
	if m < 0:
		#save the change, so that we can convert the array back to all positive number
		different = -m
		for i in range (len(arr)):
			arr[i]+= -m
	k = max(arr)
	temp_arr = [0]*(k+1)
	for i in range(0,len(arr)):
		temp_arr[arr[i]] = temp_arr[arr[i]]+1
	#temp_array[i] contain the times the number i appear in arr

	for i in range(1, k+1):
		temp_arr[i] = temp_arr[i] + temp_arr[i-1]
	#temp_array[i] contain the number of element less than or equal i in arr

	result_arr = [0]*len(arr)
	#creating a result_arr an put the element in a correct positon
	for i in range(len(arr)-1,-1,-1):
		result_arr[temp_arr[arr[i]]-1] = arr[i]-different
		temp_arr[arr[i]] = temp_arr[arr[i]]-1

	return result_arr

class TestSuite(unittest.TestCase):
    """
        test suite for the function (above)
    """
    def test_counting_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         counting_sort([1, 5, 65, 23, 57, 1232]))
        self.assertEqual([-1232, -65, -57, -23, -5, -1],
                         counting_sort([-1, -5, -65, -23, -57, -1232]))
if __name__ == "__main__":
    unittest.main()
