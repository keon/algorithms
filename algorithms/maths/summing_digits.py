"""
Recently, I encountered an interview question whose description was as below:

The number 89 is the first integer with more than one digit whose digits when raised up to
consecutive powers give the same number. For example, 89 = 8**1 + 9**2 gives the number 89.

The next number after 89 with this property is 135 = 1**1 + 3**2 + 5**3 = 135.

Write a function that returns a list of numbers with the above property. The function will
receive range as parameter.
"""

def sum_dig_pow(low, high):
    result = []

    for number in range(low, high + 1):
        exponent = 1  # set to 1
        summation = 0    # set to 1
        number_as_string = str(number)

        tokens = list(map(int, number_as_string))  # parse the string into individual digits

        for k in tokens:
            summation = summation + (k ** exponent)
            exponent += 1

        if summation == number:
            result.append(number)
    return result


# Some test cases:
assert sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
