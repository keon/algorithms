"""Magic Number
A number is said to be a magic number,
if the sum of its digits are calculated till a single digit recursively
by adding the sum of the digits after every addition.
If the single digit comes out to be 1,then the number is a magic number.

Example:
    Number = 50113 => 5+0+1+1+3=10 => 1+0=1 [This is a Magic Number]
    Number = 1234 => 1+2+3+4=10 => 1+0=1 [This is a Magic Number]
    Number = 199 => 1+9+9=19 => 1+9=10 => 1+0=1 [This is a Magic Number]
    Number = 111 => 1+1+1=3 [This is NOT a Magic Number]

The following function checks for Magic numbers and returns a Boolean accordingly.
"""


def magic_number(n):
    sum_total = 0

    # will end when n becomes 0
    # AND
    # sum becomes single digit.
    while n > 0 or sum_total > 9:

        if not n:
            n = sum_total  # only when sum of digits isn't single digit
            sum_total = 0
        sum_total += n % 10
        n //= 10

    # Return true if sum becomes 1
    return sum_total == 1


