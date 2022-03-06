"""
Given an integer num_perfect_squares will return the minimum amount of perfect squares are required
to sum to the specified number. Lagrange's four-square theorem gives us that the answer will always
be between 1 and 4 (https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem).

Some examples:
Number | Perfect Squares representation | Answer
-------|--------------------------------|--------
9      | 3^2                            | 1
10     | 3^2 + 1^2                      | 2
12     | 2^2 + 2^2 + 2^2                | 3
31     | 5^2 + 2^2 + 1^2 + 1^2          | 4
"""

import math

def num_perfect_squares(number):
    """
    Returns the smallest number of perfect squares that sum to the specified number.
    :return: int between 1 - 4
    """
    # If the number is a perfect square then we only need 1 number.
    if int(math.sqrt(number))**2 == number:
        return 1

    # We check if https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem holds and divide
    # the number accordingly. Ie. if the number can be written as a sum of 3 squares (where the
    # 0^2 is allowed), which is possible for all numbers except those of the form: 4^a(8b + 7).
    while number > 0 and number % 4 == 0:
        number /= 4

    # If the number is of the form: 4^a(8b + 7) it can't be expressed as a sum of three (or less
    # excluding the 0^2) perfect squares. If the number was of that form, the previous while loop
    # divided away the 4^a, so by now it would be of the form: 8b + 7. So check if this is the case
    # and return 4 since it neccessarily must be a sum of 4 perfect squares, in accordance 
    # with https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem.
    if number % 8 == 7:
        return 4

    # By now we know that the number wasn't of the form 4^a(8b + 7) so it can be expressed as a sum
    # of 3 or less perfect squares. Try first to express it as a sum of 2 perfect squares, and if
    # that fails, we know finally that it can be expressed as a sum of 3 perfect squares.
    for i in range(1, int(math.sqrt(number)) + 1):
        if int(math.sqrt(number - i**2))**2 == number - i**2:
            return 2

    return 3
