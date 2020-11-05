
"""
Given an array of integers, square them, and put them back into an array

For Example, if array = [1,2,5,9,12] it will be squared to [1,4,25,81,144]
"""

def square_array(array):
	out = []

	for i in array:
		out.append(i**2)
	
	return out

print(square_array([1,2,5,9,12]))
print(square_array([-10,20]))