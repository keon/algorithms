"""
Given an integer num_perfect_squares will return the amount of perfect squares that are required to sum to the specified number.

Some examples:

10 = 1^2 + 3^2
Answer = 2

12 = 2^2 + 2^2 + 2^2
Answer = 3

13 = 2^2 + 3^2
Answer = 2
"""
import math


def num_perfect_squares(number):
    # If the number is a perfect square then we only need 1 number.
    if int(math.sqrt(number))**2 == number:
        return 1

    # We check if https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem holds.
    while number > 0 and number % 4 == 0:
        number /= 4

    # If it cannot be expressed as three squares it has to be made of four squares
    # in accordance with https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
    if number % 8 == 7:
        return 4

    # Check if there is any number `i` from 1 to sqrt(number) that will result in two perfect squares.
    if any([int(math.sqrt(number - i*i))**2 == number-i*i for i in range(1, int(math.sqrt(number))+1)]):
        return 2

    return 3
