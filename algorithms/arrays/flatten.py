"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections.abc import  Iterable

def flatten(arr,output = None):
	if output is None:
		output = []
	
	for ele in arr:
		try: 	
			if len(ele) > 0:
				flatten(ele,output)		#tail recursion 
		except:
			output.append(ele)
	return output

#return iterator
def flatten_iter(iterable):
	"""
	Takes as input multi dimensional iterable and
	returns generator which produces one dimensional output.
	"""
	for element in iterable:
		try:
			if len(element) > 0:
				yield from flatten_iter(element)	    	  
		except:
			yield element            
