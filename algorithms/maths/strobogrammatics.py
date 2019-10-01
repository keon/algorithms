"""
A strobogrammatic number is a number that looks
the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.
Write a function to determine if a number is strobogrammatic.
The number is represented as a string.

Given n = 2, return ["11","69","88","96"].
The numbers "69", "88", and "818" are all strobogrammatic.
"""

def gen_strobogrammatic(n):
	"""
    :type n: int
    :rtype: List[str]
    """
	global inverse # dict of numbers rotated 180*
	inverse = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
	global valid_numbers # dict of rotatable numbers
	valid_numbers = ['0', '1', '6', '8', '9']

	if n > 2 :
		res = gen_strobogrammatic(n-2) # recurse
		ret = []
		for i in valid_numbers:
			if i != '0': # cannot have a number start with zero
				for r in res:
					ret.append(i + r + inverse[i]) # eg. 6+0+9
					if not i in ['1', '8']:
						ret.append(inverse[i] + r + i) # eg. 9+0+6
		return ret

	else:
		if n == 2: # return a pair of invertable numbers
			return [valid_numbers[i] + inverse[valid_numbers[i]] for i in range(0, len(valid_numbers))]
		elif n == 1: # return all rotatable numbers
			return ['1', '8', '0'] 
		else:
			return []

def strobogrammatic_in_range(low, high):
	"""
    :type low: str
    :type high: str
    :rtype: int
    """
	total = 0
	for i in range(len(low), len(high)):
		total += len(gen_strobogrammatic(i))
	return total

def is_strobogrammatic(s):
	"""
    :type num: str
    :rtype: bool
    """
	gen_strobogrammatic(0) # globals
	compare = ''
	for i in s:
		try:
			compare = inverse[i] + compare
		except KeyError:
			return False
	return s == compare
