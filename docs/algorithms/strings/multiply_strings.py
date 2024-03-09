"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert
the inputs to integer directly.
"""


def multiply(num1: "str", num2: "str") -> "str":
    interm = []
    zero = ord('0')
    i_pos = 1
    for i in reversed(num1):
        j_pos = 1
        add = 0
        for j in reversed(num2):
            mult = (ord(i)-zero) * (ord(j)-zero) * j_pos * i_pos
            j_pos *= 10
            add += mult
        i_pos *= 10
        interm.append(add)
    return str(sum(interm))


if __name__ == "__main__":
    print(multiply("1", "23"))
    print(multiply("23", "23"))
    print(multiply("100", "23"))
    print(multiply("100", "10000"))
