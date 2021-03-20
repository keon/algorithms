from algorithms.maths.polynomial import Monomial
from fractions import Fraction
import math


import unittest

class TestSuite(unittest.TestCase):
	
	def setUp(self):
		self.m1 = Monomial({})
		self.m2 = Monomial({1: 1}, 2)
		self.m3 = Monomial({1: 2, 2: -1}, 1.5)
		self.m4 = Monomial({1: 1, 2: 2, 3: -2}, 3)
		self.m5 = Monomial({2: 1, 3: 0}, Fraction(2, 3))
		self.m6 = Monomial({1: 0, 2: 0, 3: 0}, -2.27)
		self.m7 = Monomial({1: 2, 7: 2}, -math.pi)
		self.m8 = Monomial({150: 5, 170: 2, 10000:3}, 0)
		self.m9 = 2
		self.m10 = math.pi
		self.m11 = Fraction(3, 8)
		self.m12 = 0
		self.m13 = Monomial({1: 1}, -2)
		self.m14 = Monomial({1: 2}, 3)
		self.m15 = Monomial({1: 1}, 3)
		self.m16 = Monomial({1: 2, 7: 2}, math.pi)
		self.m17 = Monomial({1: -1})

	def test_monomial_addition(self):

		# Monomials with different underlying variables or
		# even different power of those variables must not be added!
		self.assertRaises(ValueError, lambda x, y: x + y, self.m1, self.m2)
		self.assertRaises(ValueError, lambda x, y: x + y, self.m2, self.m3)
		self.assertRaises(ValueError, lambda x, y: x + y, self.m2, self.m14)

		# Additive inverses of each other should produce the zero monomial.
		self.assertEqual(self.m13 + self.m2, self.m1)

		# Zero monomial + Zero monomial = Zero monomial
		self.assertEqual(self.m1 + self.m1, self.m1)
		
		# Coefficient float.
		self.assertEqual(self.m7 + self.m7, Monomial({1: 2, 7: 2}, -2*math.pi))
		
		# Coefficient 0 so should equal the zero monomial.
		self.assertEqual(self.m8, self.m1)

		# The constant term cannot be added to any monomial
		# that has any variables.
		self.assertRaises(ValueError, lambda x, y: x + y, self.m2, self.m9)

		# Any literal cannot be added to a Monomial. However, a monomial
		# can be added to any int, float, Fraction, or Monomial.

		# So 2 + Monomial is raises TypeError but Monomial + 2 may work fine!
		self.assertRaises(TypeError, lambda x, y: x + y, self.m9, self.m2)

		# Any constant added to a zero monomial produces
		# a monomial.
		self.assertEqual(self.m1 + self.m9, Monomial({}, 2))
		self.assertEqual(self.m1 + self.m12, Monomial({}, 0))

		return

	def test_monomial_subtraction(self):

		# Monomials with different underlying variables or
		# even different power of those variables must not be subtracted!
		self.assertRaises(ValueError, lambda x, y: x - y, self.m1, self.m2)
		self.assertRaises(ValueError, lambda x, y: x - y, self.m2, self.m3)
		self.assertRaises(ValueError, lambda x, y: x - y, self.m2, self.m14)

		# Additive inverses of each other should produce the zero monomial.
		self.assertEqual(self.m2 - self.m2, self.m1)
		self.assertEqual(self.m2 - self.m2, Monomial({}, 0))

		# Zero monomial - Zero monomial = Zero monomial
		self.assertEqual(self.m1 - self.m1, self.m1)
		
		# Coefficient int.
		self.assertEqual(self.m2 - self.m15, Monomial({1: 1}, -1))
		
		# Coefficient float.
		self.assertEqual(self.m16 - self.m7, Monomial({1: 2, 7: 2}, 2*math.pi))


		# The constant term cannot be added to any monomial
		# that has any variables.
		self.assertRaises(ValueError, lambda x, y: x - y, self.m2, self.m9)

		# Any literal cannot be added to a Monomial. However, a monomial
		# can be added to any int, float, Fraction, or Monomial.

		# So 2 + Monomial is raises TypeError but Monomial + 2 may work fine!
		self.assertRaises(TypeError, lambda x, y: x - y, self.m9, self.m2)

		# Any constant added to a zero monomial produces
		# a monomial.
		self.assertEqual(self.m1 - self.m9, Monomial({}, -2))
		self.assertEqual(self.m1 - self.m12, Monomial({}, 0))

		return

	def test_monomial_multiplication(self):
		
		# Usual multiplication.
		# The positive and negative powers of the same variable
		# should cancel out.
		self.assertEqual(self.m2 * self.m13, Monomial({1: 2}, -4))
		self.assertEqual(self.m2 * self.m17, Monomial({}, 2))

		# A coefficient of zero should make the product zero.
		# Zero monomial * any int, float, Fraction, or Monomial = Zero monomial
		self.assertEqual(self.m8 * self.m5, self.m1)
		self.assertEqual(self.m1 * self.m2, self.m1)

		# Test usual float multiplication.
		self.assertEqual(self.m7 * self.m3, Monomial({1: 4, 2: -1, 7: 2}, -1.5*math.pi))

		return

	def test_monomial_inverse(self):

		# The Zero monomial is not invertible.
		self.assertRaises(ValueError, lambda x: x.inverse(), self.m1)
		self.assertRaises(ValueError, lambda x: x.inverse(), self.m8)
		self.assertRaises(ValueError, lambda x: x.inverse(), Monomial({},self.m12))

		# Check some inverses.
		self.assertEqual(self.m7.inverse(), Monomial({1: -2, 7: -2}, -1/math.pi))

		# Doesn't matter if the coefficient is Fraction or float.
		# Both should be treated as same.
		self.assertEqual(self.m5.inverse(), Monomial({2: -1}, Fraction(3, 2)))
		self.assertEqual(self.m5.inverse(), Monomial({2: -1}, 1.5))

		# Should work fine without variables too!
		self.assertTrue(self.m6.inverse(), Monomial({}, Fraction(-100, 227)))
		self.assertEqual(self.m6.inverse(), Monomial({}, -1/2.27))
		return

	def test_monomial_division(self):
		# Any monomial divided by the Zero Monomial should raise a ValueError.
		self.assertRaises(ValueError, lambda x, y: x.__truediv__(y), self.m2, self.m1)
		self.assertRaises(ValueError, lambda x, y: x.__truediv__(y), self.m2, self.m8)
		self.assertRaises(ValueError, lambda x, y: x.__truediv__(y), self.m2, self.m12)

		# Test some usual cases.
		self.assertEqual(self.m7 / self.m3, Monomial({2: 1, 7: 2}, -2*math.pi/3))
		self.assertEqual(self.m14 / self.m13, Monomial({1: 1}) * Fraction(-3, 2))

		return

	def test_monomial_substitution(self):
		# Test with int.
		self.assertAlmostEqual(self.m7.substitute(2), -16*math.pi, delta=1e-9)
		# Test with float.
		self.assertAlmostEqual(self.m7.substitute(1.5), (1.5 ** 4)* -math.pi, delta=1e-9)
		# Test with Fraction.
		self.assertAlmostEqual(self.m7.substitute(Fraction(-1, 2)), (Fraction(-1, 2) ** 4)*-math.pi, delta=1e-9)
		# Test with a complete substitution map.
		self.assertAlmostEqual(self.m7.substitute({1: 3, 7: 0}), (3 ** 2) * (0 ** 2) * -math.pi, delta=1e-9)
		# Test with a more than complete substitution map.
		self.assertAlmostEqual(self.m7.substitute({1: 3, 7: 0, 2: 2}), (3 ** 2) * (0 ** 2) * -math.pi, delta=1e-9)
		
		# Should raise a ValueError if not enough variables are supplied!
		self.assertRaises(ValueError, lambda x, y: x.substitute(y), self.m7, {1: 3, 2: 2})
		self.assertRaises(ValueError, lambda x, y: x.substitute(y), self.m7, {2: 2})

		# The zero monomial always gives zero upon substitution.
		self.assertEqual(self.m8.substitute(2), 0)
		self.assertEqual(self.m8.substitute({1231: 2, 1: 2}), 0)

		return

	def test_monomial_all_variables(self):

		# Any variable with zero power should not exist in the set
		# of variables.
		self.assertEqual(self.m5.all_variables(), {2})
		self.assertEqual(self.m6.all_variables(), set())

		# The zero monomial should output empty set.
		self.assertEqual(self.m8.all_variables(), set())

		return

	def test_monomial_clone(self):

		# A monomial should produce its copy
		# with same underlying variable dictionary
		# and same coefficient.
		self.assertEqual(self.m3, self.m3.clone())

		# The zero monomial is identified and 
		# always clones to itself.
		self.assertEqual(self.m1, self.m8.clone())
		self.assertEqual(self.m1, self.m1.clone())
		self.assertEqual(self.m8, self.m1.clone())
		self.assertEqual(self.m8, self.m8.clone())
		return


if __name__ == '__main__':
	unittest.main()