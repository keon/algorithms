# This code converts roman_number into arabic_number

# There are a few rules for writing Roman numerals:
# Roman numerals are always read from left to right, not a problem for us since our writing and reading systems read in the same order.
#     1) The Roman numerals I, X, C and M may be repeated up to three times when writing a compound Roman numeral.
#     2) The Roman numerals V, L and D may never be repeated.
#     3) If a compound Roman numeral has a number on the right that is smaller than the number on the left, both numbers are added.
#       Example: XI: the number on the right (I = 1) is smaller than the number on the left (X = 10), then they are added, so XI = 11
#     4) If a composite Roman numeral has a number on the right greater than the number on the left, and it is I, X or C,
#       then the number on the left is subtracted from the number on the right.
#       Example: IX: The number on the right (X = 10) is greater than the number on the left (I = 1), and it is also I, then the number on the left is subtracted from the number on the right, so IX = 9

def roman_to_arabic(roman_num):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(roman_num) - 1):
        if romans[roman_num[i]] >= romans[roman_num[i + 1]]:
            result += int(romans[roman_num[i]])
        else:
            result -= int((romans[roman_num[i]]))
    result += romans[roman_num[-1]]


roman_to_arabic("MM")  # 2000
roman_to_arabic("XXI")  # 21
roman_to_arabic("MCMXC")  # 1990
roman_to_arabic("MDCLXVI")  # 1666
roman_to_arabic("MMVIII")  # 2008
