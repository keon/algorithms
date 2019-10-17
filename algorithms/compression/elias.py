from math import log,ceil

log2 = lambda x: log(x,2)

# Calculates the binary number
def binary(x,l=1):
	fmt = '{0:0%db}' % l
	return fmt.format(x)

# Calculates the unary number
def unary(x):
	return (x-1)*'1'+'0'

# Elias implementation for both gamma/delta
def elias_generic(lencoding, x):
	if x == 0: return '0'
	
	first_part = 1 + int(log2(x))
	
	a = x - 2**(int(log2(x)))
	
	k = int(log2(x))

	return lencoding(first_part) + binary(a,k)

def elias_gamma(x):
	return elias_generic(unary, x)

def elias_delta(x):
	return elias_generic(elias_gamma,x)
