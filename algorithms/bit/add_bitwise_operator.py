"""
The following code adds two positive integers without using the '+' operator.
The code uses bitwise operations to add two numbers.

Input: 2 3
Output: 5
"""
def add_bitwise_operator(x, y):

    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x
