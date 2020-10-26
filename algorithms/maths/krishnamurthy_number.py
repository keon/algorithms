"""
A Krishnamurthy number is a number whose sum total of the factorials of each digit is equal to the number itself.

Here's what I mean by that:

"145" is a Krishnamurthy Number because,
1! + 4! + 5! = 1 + 24 + 120 = 145

"40585" is also a Krishnamurthy Number.
4! + 0! + 5! + 8! + 5! = 40585

"357" or "25965" is NOT a Krishnamurthy Number
3! + 5! + 7! = 6 + 120 + 5040 != 357

The following function will check if a number is a Krishnamurthy Number or not and return a boolean value.
"""


def find_factorial(n):
    fact = 1
    while n != 0:
        fact *= n
        n -= 1
    return fact


def krishnamurthy_number(n):
    if n == 0:
        return False
    sum_of_digits = 0   # will hold sum of FACTORIAL of digits
    temp = n

    while temp != 0:

        # get the factorial of of the last digit of n and add it to sum_of_digits
        sum_of_digits += find_factorial(temp % 10)

        # replace value of temp by temp/10
        # i.e. will remove the last digit from temp
        temp //= 10

    # returns True if number is krishnamurthy
    return (sum_of_digits == n)
