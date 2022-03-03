from algorithms.maths.polynomial import (
    Polynomial,
    Monomial
)
from fractions import Fraction
import math


import unittest

class TestSuite(unittest.TestCase):

    def setUp(self):
        self.p0 = Polynomial([
            Monomial({})
        ])
        self.p1 = Polynomial([
            Monomial({}), Monomial({})
        ])
        self.p2 = Polynomial([
            Monomial({1: 1}, 2)
        ])
        self.p3 = Polynomial([
            Monomial({1: 1}, 2),
            Monomial({1: 2, 2: -1}, 1.5)
        ])
        self.p4 = Polynomial([
            Monomial({2: 1, 3: 0}, Fraction(2, 3)),
            Monomial({1: -1, 3: 2}, math.pi),
            Monomial({1: -1, 3: 2}, 1)
        ])
        self.p5 = Polynomial([
            Monomial({150: 5, 170: 2, 10000:3}, 0),
            Monomial({1: -1, 3: 2}, 1), 
        ])
        self.p6 = Polynomial([
            2,
            -3,
            Fraction(1, 7),
            2**math.pi,
            Monomial({2: 3, 3: 1}, 1.25)
        ])
        self.p7 = Polynomial([
            Monomial({1: 1}, -2),
            Monomial({1: 2, 2: -1}, -1.5)
        ])

        # x^3 - 2x^2 - 4
        self.p8 = Polynomial([
            Monomial({1:3}, 1),
            Monomial({1:2}, -2),
            -4
        ])
        # x - 3
        self.p9 = Polynomial([
            Monomial({1:1}, 1),
            -3,
        ])

        self.m1 = Monomial({1: 2, 2: 3}, -1)

    def test_polynomial_addition(self):
        
        # The zero polynomials should add up to
        # itselves only.
        self.assertEqual(self.p0 + self.p1, self.p0)
        self.assertEqual(self.p0 + self.p1, self.p1)
        
        # Additive inverses should add up to the
        # zero polynomial.
        self.assertEqual(self.p3 + self.p7, self.p0)
        self.assertEqual(self.p3 + self.p7, self.p1)

        # Like terms should combine.
        # The order of monomials should not matter.
        self.assertEqual(self.p2 + self.p3, Polynomial([
            Monomial({1: 1}, 4),
            Monomial({1: 2, 2: -1}, 1.5)
        ]))
        self.assertEqual(self.p2 + self.p3, Polynomial([
            Monomial({1: 2, 2: -1}, 1.5),
            Monomial({1: 1}, 4),
        ]))

        # Another typical computation.
        self.assertEqual(self.p5 + self.p6, Polynomial([
            Monomial({}, 7.96783496993343),
            Monomial({2: 3, 3: 1}, 1.25),
            Monomial({1: -1, 3: 2})
        ]))

    def test_polynomial_subtraction(self):

        self.assertEqual(self.p3 - self.p2, Polynomial([
            Monomial({1: 2, 2: -1}, 1.5)
        ]))

        self.assertEqual(self.p3 - self.p3, Polynomial([]))

        self.assertEqual(self.p2 - self.p3, Polynomial([
            Monomial({1: 2, 2: -1}, -1.5)
        ]))

    def test_polynomial_multiplication(self):
        self.assertEqual(self.p0 * self.p2, Polynomial([]))
        self.assertEqual(self.p1 * self.p2, Polynomial([]))

        self.assertEqual(self.p2 * self.p3, Polynomial([
            Monomial({1: 2}, 4),
            Monomial({1: 3, 2: -1}, Fraction(3, 1))
        ]))

    def test_polynomial_division(self):
        # Should raise a ValueError if any polynomial contains negative exponent
        self.assertRaises(ValueError, lambda x, y: x / y, self.p5, self.p3)

        self.assertEqual(self.p3 / self.p2, Polynomial([
            Monomial({}, 1),
            Monomial({1: 1, 2: -1}, 0.75)
        ]))
        self.assertEqual(self.p7 / self.m1, Polynomial([
            Monomial({1: -1, 2: -3}, 2),
            Monomial({1: 0, 2: -4}, 1.5)
        ]))
        self.assertEqual(self.p7 / self.m1, Polynomial([
            Monomial({1: -1, 2: -3}, 2),
            Monomial({2: -4}, 1.5)
        ]))

    def test_polynomial_division_by_polynomial(self):
        """
        Make sure that we can devide two polynomials when there's only one variable
        """
        quotient, remainder = self.p8.polynomial_division(self.p9)
        self.assertEqual(quotient, Polynomial([
            Monomial({1: 2}, 1),
            Monomial({1: 1}, 1),
            3
        ]))
        self.assertEqual(remainder, Polynomial([5]))

    def test_polynomial_division_three_variables(self):
        """
        Makes sure that we can divide polynomials when there are three different
        variables in the denominator
        """
        # see: https://math.stackexchange.com/questions/2167213/polynomial-division-in-3-variables
        # x^3 - xyz - 2x^2 + 2xy + yz
        dividend = Polynomial([
            Monomial({'x': 3}, 1), 
            Monomial({'x': 1, 'y': 1, 'z': 1}, -1),
            Monomial({'x': 2}, -2),
            Monomial({'x': 1, 'y': 1}, 2),
            Monomial({'y': 1, 'z': 1}, 1),
            ])
        # x - 2
        divisor = Polynomial([Monomial({'x': 1}, 1), -2])
        quotient, remainder = dividend.polynomial_division(divisor)

        # Should equal: x^2 - yz + 2y
        self.assertEqual(quotient, Polynomial([
            Monomial({'x': 2}, 1),
            Monomial({'y': 1, 'z': 1}, -1),
            Monomial({'y': 1}, 2),
        ]))

        # Should equal: 4y - yz
        self.assertEqual(remainder, Polynomial([
            Monomial({'y': 1}, 4),
            Monomial({'y': 1, 'z': 1}, -1),
        ]))
        
    def test_polynomial_division_cubic(self):
        """
        Makes sure that we can divide polynomials when there are three different
        variables in the denominator and numerator
        """
        pxyz = Polynomial([
            Monomial({'x':1}, 1),
            Monomial({'y':1}, 1),
            Monomial({'z':1}, 1)
        ])
        pxyz2 = pxyz * pxyz
        pxyz3 = pxyz * pxyz * pxyz

        # Test that (x + y + z)^3 / (x + y + z)^2 = (x + y + z)
        quotient, remainder = pxyz3.polynomial_division(pxyz2)
        self.assertEqual(quotient, pxyz)
        self.assertEqual(remainder, Polynomial([]))

        # Test that (x + y + z)^3 / (x + y + z) = (x + y + z)^2
        quotient, remainder = pxyz3.polynomial_division(pxyz)
        self.assertEqual(quotient, pxyz2)
        self.assertEqual(remainder, Polynomial([]))

    def test_polynomial_variables(self):
        # The zero polynomial has no variables.

        self.assertEqual(self.p0.variables(), set())
        self.assertEqual(self.p1.variables(), set())

        # The total variables are the union of the variables
        # from the monomials.
        self.assertEqual(self.p4.variables(), {1, 2, 3})

        # The monomials with coefficient 0 should be dropped.
        self.assertEqual(self.p5.variables(), {1, 3})

    def test_polynomial_subs(self):
        # Anything substitued in the zero polynomial
        # should evaluate to 0.
        self.assertEqual(self.p1.subs(2), 0)
        self.assertEqual(self.p0.subs(-101231), 0)

        # Should raise a ValueError if not enough variables are supplied.
        self.assertRaises(ValueError, lambda x, y: x.subs(y), self.p4, {1: 3, 2: 2})
        self.assertRaises(ValueError, lambda x, y: x.subs(y), self.p4, {})

        # Should work fine if a complete subsitution map is provided.
        self.assertAlmostEqual(self.p4.subs({1: 1, 2: 1, 3: 1}), (1 + math.pi + Fraction(2, 3)), delta=1e-9)
        # Should work fine if more than enough substitutions are provided.
        self.assertAlmostEqual(self.p4.subs({1: 1, 2: 1, 3: 1, 4: 1}), (1 + math.pi + Fraction(2, 3)), delta=1e-9)

    def test_polynomial_clone(self):

        # The zero polynomial always clones to itself.
        self.assertEqual(self.p0.clone(), self.p0)
        self.assertEqual(self.p1.clone(), self.p0)
        self.assertEqual(self.p0.clone(), self.p1)
        self.assertEqual(self.p1.clone(), self.p1)

        # The polynomial should clone nicely.
        self.assertEqual(self.p4.clone(), self.p4)

        # The monomial with a zero coefficient should be dropped
        # in the clone.
        self.assertEqual(self.p5.clone(), Polynomial([
            Monomial({1: -1, 3: 2}, 1)
        ]))
