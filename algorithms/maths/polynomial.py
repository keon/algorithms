# from __future__ import annotations

from fractions import Fraction
from typing import Dict, Union, Set, Iterable
from numbers import Rational
from functools import reduce


class Monomial:
    """
    A simple Monomial class to
    record the details of all variables
    that a typical monomial is composed of.
    """
    def __init__(self, variables: Dict[int, int], coeff: Union[int, float, Fraction, None]=None) -> None:
        '''
        Create a monomial in the given variables:
        Examples:

            Monomial({1:1}) = (a_1)^1

            Monomial({
                1:3,
                2:2,
                4:1,
                5:0
            }, 12) = 12(a_1)^3(a_2)^2(a_4)

            Monomial({}) = 0

            Monomial({2:3, 3:-1}, 1.5) = (3/2)(a_2)^3(a_3)^(-1)

        '''
        self.variables = dict()

        if coeff is None:
            if len(variables) == 0:
                coeff = Fraction(0, 1)
            else:
                coeff = Fraction(1, 1)
        elif coeff == 0:
            self.coeff = Fraction(0, 1)
            return

        if len(variables) == 0:
            self.coeff = Monomial._rationalize_if_possible(coeff)
            return

        for i in variables:
            if variables[i] != 0:
                self.variables[i] = variables[i]
        self.coeff = Monomial._rationalize_if_possible(coeff)

    @staticmethod
    def _rationalize_if_possible(num):
        '''
        A helper for converting numbers
        to Fraction only when possible.
        '''
        if isinstance(num, Rational):
            res = Fraction(num, 1)
            return Fraction(res.numerator, res.denominator)
        else:
            return num


    # def equal_upto_scalar(self, other: Monomial) -> bool:
    def equal_upto_scalar(self, other) -> bool:
        """
        Return True if other is a monomial
        and is equivalent to self up to a scalar
        multiple.
        """
        if not isinstance(other, Monomial):
            raise ValueError('Can only compare monomials.')
        return other.variables == self.variables

    # def __add__(self, other: Union[int, float, Fraction, Monomial]):
    def __add__(self, other: Union[int, float, Fraction]):
        """
        Define the addition of two
        monomials or the addition of
        a monomial with an int, float, or a Fraction.
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            return self.__add__(Monomial({}, Monomial._rationalize_if_possible(other)))

        if not isinstance(other, Monomial):
            raise ValueError('Can only add monomials, ints, floats, or Fractions.')

        if self.variables == other.variables:
            mono = {i: self.variables[i] for i in self.variables}
            return Monomial(mono, Monomial._rationalize_if_possible(self.coeff + other.coeff)).clean()
        
        # If they don't share same variables then by the definition,
        # if they are added, the result becomes a polynomial and not a monomial.
        # Thus, raise ValueError in that case.

        raise ValueError(f'Cannot add {str(other)} to {self.__str__()} because they don\'t have same variables.')

    # def __eq__(self, other: Monomial) -> bool:
    def __eq__(self, other) -> bool:
        """
        Return True if two monomials
        are equal upto a scalar multiple.
        """
        return self.equal_upto_scalar(other) and self.coeff == other.coeff

    # def __mul__(self, other: Union[int, float, Fraction, Monomial]) -> Monomial:
    def __mul__(self, other: Union[int, float, Fraction]):
        """
        Multiply two monomials and merge the variables
        in both of them.

        Examples:

            Monomial({1:1}) * Monomial({1: -3, 2: 1}) = (a_1)^(-2)(a_2)
            Monomial({3:2}) * 2.5 = (5/2)(a_3)^2

        """
        if isinstance(other, float) or isinstance(other, int) or isinstance(other, Fraction):
            mono = {i: self.variables[i] for i in self.variables}
            return Monomial(mono, Monomial._rationalize_if_possible(self.coeff * other)).clean()

        if not isinstance(other, Monomial):
            raise ValueError('Can only multiply monomials, ints, floats, or Fractions.')
        else:
            mono = {i: self.variables[i] for i in self.variables}
            for i in other.variables:
                if i in mono:
                    mono[i] += other.variables[i]
                else:
                    mono[i] = other.variables[i]

            temp = dict()
            for k in mono:
                if mono[k] != 0:
                    temp[k] = mono[k]

            return Monomial(temp, Monomial._rationalize_if_possible(self.coeff * other.coeff)).clean()

    # def inverse(self) -> Monomial:
    def inverse(self):
        """
        Compute the inverse of a monomial.

        Examples:

            Monomial({1:1, 2:-1, 3:2}, 2.5).inverse() = Monomial({1:-1, 2:1, 3:-2} ,2/5)


        """
        mono = {i: self.variables[i] for i in self.variables if self.variables[i] != 0}
        for i in mono:
            mono[i] *= -1
        if self.coeff == 0:
            raise ValueError("Coefficient must not be 0.")
        return Monomial(mono, Monomial._rationalize_if_possible(1/self.coeff)).clean()

    # def __truediv__(self, other: Union[int, float, Fraction, Monomial]) -> Monomial:
    def __truediv__(self, other: Union[int, float, Fraction]):
        """
        Compute the division between two monomials
        or a monomial and some other datatype
        like int/float/Fraction.
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            mono = {i: self.variables[i] for i in self.variables}
            if other == 0:
                raise ValueError('Cannot divide by 0.')
            return Monomial(mono, Monomial._rationalize_if_possible(self.coeff / other)).clean()

        o = other.inverse()
        return self.__mul__(o)

    # def __floordiv__(self, other: Union[int, float, Fraction, Monomial]) -> Monomial:
    def __floordiv__(self, other: Union[int, float, Fraction]):
        """
        For monomials,
        floor div is the same as true div.
        """
        return self.__truediv__(other)

    # def clone(self) -> Monomial:
    def clone(self):
        """
        Clone the monomial.
        """
        temp_variables = {i: self.variables[i] for i in self.variables}
        return Monomial(temp_variables, Monomial._rationalize_if_possible(self.coeff)).clean()

    # def clean(self) -> Monomial:
    def clean(self):
        """
        Clean the monomial by dropping any variables that have power 0.
        """
        temp_variables = {i: self.variables[i] for i in self.variables if self.variables[i] != 0}
        return Monomial(temp_variables, Monomial._rationalize_if_possible(self.coeff))

    # def __sub__(self, other: Union[int, float, Fraction, Monomial]) -> Monomial:
    def __sub__(self, other: Union[int, float, Fraction]):
        """
        Compute the subtraction
        of a monomial and a datatype
        such as int, float, Fraction, or Monomial.
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            mono = {i: self.variables[i] for i in self.variables if self.variables[i] != 0}
            if len(mono) != 0:
                raise ValueError('Can only subtract like monomials.')
            other_term = Monomial(mono, Monomial._rationalize_if_possible(other))
            return self.__sub__(other_term)
        if not isinstance(other, Monomial):
            raise ValueError('Can only subtract monomials')
        return self.__add__(other.__mul__(Fraction(-1, 1)))

    def __hash__(self) -> int:
        """
        Define the hash of a monomial
        by the underlying variables.

        If hashing is implemented in O(v*log(v))
        where v represents the number of
        variables in the monomial,
        then search queries for the
        purposes of simplification of a
        polynomial can be performed in
        O(v*log(v)) as well; much better than
        the length of the polynomial.
        """
        arr = []
        for i in sorted(self.variables):
            if self.variables[i] > 0:
                for _ in range(self.variables[i]):
                    arr.append(i)
        return hash(tuple(arr))

    def all_variables(self) -> Set:
        """
        Get the set of all variables
        present in the monomial.
        """
        return set(sorted(self.variables.keys()))

    def substitute(self, substitutions: Union[int, float, Fraction, Dict[int, Union[int, float, Fraction]]]) -> Fraction:
        """
        Substitute the variables in the
        monomial for values defined by
        the substitutions dictionary.
        """
        if isinstance(substitutions, int) or isinstance(substitutions, float) or isinstance(substitutions, Fraction):
            substitutions = {v: Monomial._rationalize_if_possible(substitutions) for v in self.all_variables()}
        else:
            if not self.all_variables().issubset(set(substitutions.keys())):
                raise ValueError('Some variables didn\'t receive their values.')
        if self.coeff == 0:
            return Fraction(0, 1)
        ans = Monomial._rationalize_if_possible(self.coeff)
        for k in self.variables:
            ans *= Monomial._rationalize_if_possible(substitutions[k]**self.variables[k])
        return Monomial._rationalize_if_possible(ans)

    def __str__(self) -> str:
        """
        Get a string representation of
        the monomial.
        """
        if len(self.variables) == 0:
            return str(self.coeff)

        result = str(self.coeff)
        result += '('
        for i in self.variables:
            temp = 'a_{}'.format(str(i))
            if self.variables[i] > 1:
                temp = '(' + temp + ')**{}'.format(self.variables[i])
            elif self.variables[i] < 0:
                temp = '(' + temp + ')**(-{})'.format(-self.variables[i])
            elif self.variables[i] == 0:
                continue
            else:
                temp = '(' + temp + ')'
            result += temp
        return result + ')'


class Polynomial:
    """
    A simple implementation
    of a polynomial class that
    records the details about two polynomials
    that are potentially comprised of multiple
    variables.
    """
    def __init__(self, monomials: Iterable[Union[int, float, Fraction, Monomial]]) -> None:
        '''
        Create a polynomial in the given variables:
        Examples:

            Polynomial([
                Monomial({1:1}, 2),
                Monomial({2:3, 1:-1}, -1),
                math.pi,
                Fraction(-1, 2)
            ]) = (a_1)^2 + (-1)(a_2)^3(a_1)^(-1) + 2.6415926536

            Polynomial([]) = 0

        '''
        self.monomials = set()
        for m in monomials:
            if any(map(lambda x: isinstance(m, x), [int, float, Fraction])):
                self.monomials |= {Monomial({}, m)}
            elif isinstance(m, Monomial):
                self.monomials |= {m}
            else:
                raise ValueError('Iterable should have monomials, int, float, or Fraction.')
        self.monomials -= {Monomial({}, 0)}

    @staticmethod
    def _rationalize_if_possible(num):
        '''
        A helper for converting numbers
        to Fraction only when possible.
        '''
        if isinstance(num, Rational):
            res = Fraction(num, 1)
            return Fraction(res.numerator, res.denominator)
        else:
            return num


    # def __add__(self, other: Union[int, float, Fraction, Monomial, Polynomial]) -> Polynomial:
    def __add__(self, other: Union[int, float, Fraction, Monomial]):
        """
        Add a given poylnomial to a copy of self.

        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            return self.__add__(Monomial({}, Polynomial._rationalize_if_possible(other)))
        elif isinstance(other, Monomial):
            monos = {m.clone() for m in self.monomials}

            for _own_monos in monos:
                if _own_monos.equal_upto_scalar(other):
                    scalar = _own_monos.coeff
                    monos -= {_own_monos}
                    temp_variables = {i: other.variables[i] for i in other.variables}
                    monos |= {Monomial(temp_variables, Polynomial._rationalize_if_possible(scalar + other.coeff))}
                    return Polynomial([z for z in monos])

            monos |= {other.clone()}
            return Polynomial([z for z in monos])
        elif isinstance(other, Polynomial):
            temp = list(z for z in {m.clone() for m in self.all_monomials()})
        
            p = Polynomial(temp)
            for o in other.all_monomials():
                p = p.__add__(o.clone())
            return p
        else:
            raise ValueError('Can only add int, float, Fraction, Monomials, or Polynomials to Polynomials.')

    # def __sub__(self, other: Union[int, float, Fraction, Monomial, Polynomial]) -> Polynomial:
    def __sub__(self, other: Union[int, float, Fraction, Monomial]):
        """
        Subtract the given polynomial
        from a copy of self.

        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            return self.__sub__(Monomial({}, Polynomial._rationalize_if_possible(other)))
        elif isinstance(other, Monomial):
            monos = {m.clone() for m in self.all_monomials()}
            for _own_monos in monos:
                if _own_monos.equal_upto_scalar(other):
                    scalar = _own_monos.coeff
                    monos -= {_own_monos}
                    temp_variables = {i: other.variables[i] for i in other.variables}
                    monos |= {Monomial(temp_variables, Polynomial._rationalize_if_possible(scalar - other.coeff))}
                    return Polynomial([z for z in monos])

            to_insert = other.clone()
            to_insert.coeff *= -1

            monos |= {to_insert}
            return Polynomial([z for z in monos])

        elif isinstance(other, Polynomial):
            p = Polynomial(list(z for z in {m.clone() for m in self.all_monomials()}))
            for o in other.all_monomials():
                p = p.__sub__(o.clone())
            return p
        
        else:
            raise ValueError('Can only subtract int, float, Fraction, Monomials, or Polynomials from Polynomials.')
            return

    # def __mul__(self, other: Union[int, float, Fraction, Monomial, Polynomial]) -> Polynomial:
    def __mul__(self, other: Union[int, float, Fraction, Monomial]):
        """
        Multiply a given polynomial
        to a copy of self.
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            result = Polynomial([])
            monos = {m.clone() for m in self.all_monomials()}
            for m in monos:
                result = result.__add__(m.clone()*other)
            return result
        elif isinstance(other, Monomial):
            result = Polynomial([])
            monos = {m.clone() for m in self.all_monomials()}
            for m in monos:
                result = result.__add__(m.clone() * other)
            return result
        elif isinstance(other, Polynomial):
            temp_self = {m.clone() for m in self.all_monomials()}
            temp_other = {m.clone() for m in other.all_monomials()}

            result = Polynomial([])

            for i in temp_self:
                for j in temp_other:
                    result = result.__add__(i * j)

            return result
        else:
            raise ValueError('Can only multiple int, float, Fraction, Monomials, or Polynomials with Polynomials.')

    # def __floordiv__(self, other: Union[int, float, Fraction, Monomial, Polynomial]) -> Polynomial:
    def __floordiv__(self, other: Union[int, float, Fraction, Monomial]):
        """
        For Polynomials, floordiv is the same
        as truediv.
        """
        return self.__truediv__(other)

    # def __truediv__(self, other: Union[int, float, Fraction, Monomial, Polynomial]) -> Polynomial:
    def __truediv__(self, other: Union[int, float, Fraction, Monomial]):
        """
        For Polynomials, only division by a monomial
        is defined.

        TODO: Implement polynomial / polynomial.
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            return self.__truediv__( Monomial({}, other) )
        elif isinstance(other, Monomial):
            poly_temp = reduce(lambda acc, val: acc + val, map(lambda x: x / other, [z for z in self.all_monomials()]), Polynomial([Monomial({}, 0)]))
            return poly_temp
        elif isinstance(other, Polynomial):
            if Monomial({}, 0) in other.all_monomials():
                if len(other.all_monomials()) == 2:
                    temp_set = {x for x in other.all_monomials() if x != Monomial({}, 0)}
                    only = temp_set.pop()
                    return self.__truediv__(only)
            elif len(other.all_monomials()) == 1:
                temp_set = {x for x in other.all_monomials()}
                only = temp_set.pop()
                return self.__truediv__(only)

        raise ValueError('Can only divide a polynomial by an int, float, Fraction, or a Monomial.')

        return

    # def clone(self) -> Polynomial:
    def clone(self):
        """
        Clone the polynomial.
        """
        return Polynomial(list({m.clone() for m in self.all_monomials()}))

    def variables(self) -> Set:
        """
        Get all the variables present
        in this polynomials.
        """
        res = set()
        for i in self.all_monomials():
            res |= {j for j in i.variables}
        res = list(res)
        # res.sort()
        return set(res)

    def all_monomials(self) -> Iterable[Monomial]:
        """
        Get the monomials of this polynomial.
        """
        return {m for m in self.monomials if m != Monomial({}, 0)}


    def __eq__(self, other) -> bool:
        """
        Return True if the other polynomial is the same as
        this.
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            other_poly = Polynomial([Monomial({}, other)])
            return self.__eq__(other_poly)
        elif isinstance(other, Monomial):
            return self.__eq__(Polynomial([other]))
        elif isinstance(other, Polynomial):
            return self.all_monomials() == other.all_monomials()
        else:
            raise ValueError('Can only compare a polynomial with an int, float, Fraction, Monomial, or another Polynomial.')


    def subs(self, substitutions: Union[int, float, Fraction, Dict[int, Union[int, float, Fraction]]]) -> Union[int, float, Fraction]:
        """
        Get the value after substituting
        certain values for the variables
        defined in substitutions.
        """
        if isinstance(substitutions, int) or isinstance(substitutions, float) or isinstance(substitutions, Fraction):
            substitutions = {i: Polynomial._rationalize_if_possible(substitutions) for i in set(self.variables())}
            return self.subs(substitutions)
        elif not isinstance(substitutions, dict):
            raise ValueError('The substitutions should be a dictionary.')
        if not self.variables().issubset(set(substitutions.keys())):
            raise ValueError('Some variables didn\'t receive their values.')

        ans = 0
        for m in self.all_monomials():
            ans += Polynomial._rationalize_if_possible(m.substitute(substitutions))
        return Polynomial._rationalize_if_possible(ans)

    def __str__(self) -> str:
        """
        Get a string representation of
        the polynomial.
        """
        return ' + '.join(str(m) for m in self.all_monomials() if m.coeff != Fraction(0, 1))

