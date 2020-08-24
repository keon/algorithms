"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""

# return list
def flatten(input_arr, output_arr=None):
	if output_arr is None:
		output_arr = []
	for ele in input_arr:
		try:
			if len(ele) > 0:
				flatten(ele, output_arr)    #tail-recursion
		except:output_arr.append(ele)      #produce the result
	return output_arr


# returns iterator
def flatten_iter(iterable):
	"""
	Takes as input multi dimensional iterable and
	returns generator which produces one dimensional output.
	"""
	for element in iterable:
		try:
			if len(element) > 0:
				yield from flatten_iter(element)    
		except:yield element
