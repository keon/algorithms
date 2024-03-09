"""
Elias γ code or Elias gamma code is a universal code
encoding positive integers.
It is used most commonly when coding integers whose
upper-bound cannot be determined beforehand.
Elias δ code or Elias delta code is a universal code
 encoding the positive integers,
that includes Elias γ code when calculating.
Both were developed by Peter Elias.

"""
from math import log

log2 = lambda x: log(x, 2)

# Calculates the binary number
def binary(x, l=1):
	fmt = '{0:0%db}' % l
	return fmt.format(x)

# Calculates the unary number
def unary(x):
	return (x-1)*'1'+'0'

def elias_generic(lencoding, x):
	"""
	The compressed data is calculated in two parts.
	The first part is the unary number of 1 + ⌊log2(x)⌋.
	The second part is the binary number of x - 2^(⌊log2(x)⌋).
	For the final result we add these two parts.
	"""
	if x == 0:
		return '0'
	
	first_part = 1 + int(log2(x))
	
	a = x - 2**(int(log2(x)))
	
	k = int(log2(x))

	return lencoding(first_part) + binary(a, k)

def elias_gamma(x):
	"""
	For the first part we put the unary number of x.
	"""
	return elias_generic(unary, x)

def elias_delta(x):
	"""
	For the first part we put the elias_g of the number.
	"""
	return elias_generic(elias_gamma, x)
