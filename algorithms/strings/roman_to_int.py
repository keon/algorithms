"""
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""


def roman_to_int(s:"str")->"int":
    number = 0
    roman = {'M':1000, 'D':500, 'C': 100, 'L':50, 'X':10, 'V':5, 'I':1}
    for i in range(len(s)-1):
        if roman[s[i]] < roman[s[i+1]]:
            number -= roman[s[i]]
        else:
            number += roman[s[i]]
    return number + roman[s[-1]]


if __name__ == "__main__":
    roman = "DCXXI"
    print(roman_to_int(roman))
