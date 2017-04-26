from decimal import *

"""
Gauss-Legendre algorithm for calculating pi
the number of correct bits generated doubles with each extra iteration
"""
def gauss_legendre(bits, iterations):
	with localcontext() as ctx:
		ctx.prec = bits # set decimal precision

		a = 1
		b = Decimal(1) / Decimal(2).sqrt()
		t = Decimal(1) / Decimal(4)
		p = 1

		for _ in xrange(iterations):
			a_new = (a + b) / 2
			b = (a * b).sqrt()
			t -= p * (a - a_new) ** 2
			p *= 2
			a = a_new

		return ((a + b) ** 2) / (4 * t)