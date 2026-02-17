"""
FizzBuzz

Return an array of numbers from 1 to N, replacing multiples of 3 with 'Fizz',
multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'.

Reference: https://en.wikipedia.org/wiki/Fizz_buzz

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from typing import Union


def fizzbuzz(number: int) -> list[Union[int, str]]:
    """Generate FizzBuzz sequence from 1 to number.

    Args:
        number: The upper bound of the sequence (inclusive).

    Returns:
        A list where multiples of 3 are 'Fizz', multiples of 5 are 'Buzz',
        multiples of both are 'FizzBuzz', and all others are the integer value.

    Raises:
        ValueError: If number is less than 1.
        TypeError: If number is None.

    Examples:
        >>> fizzbuzz(5)
        [1, 2, 'Fizz', 4, 'Buzz']
    """
    if number < 1:
        raise ValueError('n cannot be less than one')
    if number is None:
        raise TypeError('n cannot be None')

    result: list[Union[int, str]] = []
    for value in range(1, number + 1):
        if value % 3 == 0 and value % 5 == 0:
            result.append('FizzBuzz')
        elif value % 3 == 0:
            result.append('Fizz')
        elif value % 5 == 0:
            result.append('Buzz')
        else:
            result.append(value)
    return result


def fizzbuzz_with_helper_func(number: int) -> list[Union[int, str]]:
    """Generate FizzBuzz sequence using a helper function.

    Args:
        number: The upper bound of the sequence (inclusive).

    Returns:
        A list of FizzBuzz values from 1 to number.

    Examples:
        >>> fizzbuzz_with_helper_func(3)
        [1, 2, 'Fizz']
    """
    return [_fb(value) for value in range(1, number + 1)]


def _fb(value: int) -> Union[int, str]:
    """Return the FizzBuzz value for a single number.

    Args:
        value: The number to evaluate.

    Returns:
        'Fizz', 'Buzz', 'FizzBuzz', or the number itself.
    """
    result = (value % 3 == 0) * "Fizz" + (value % 5 == 0) * "Buzz"
    return result if result != "" else value
