# Math Algorithm
# Armstrong Number of n digits
# To find if the s of its digits raised to the third power is equal to the number.


def function(num, order):
    s = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        s += digit ** order
        temp //= 10
    if num == s:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


num = int(input("Enter the number: "))
order = len(str(num))
function(num, order)