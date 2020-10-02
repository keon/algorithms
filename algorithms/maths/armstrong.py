#Check Armstrong number of n digits

num = input("Enter the number: ")
order = len(str(num))

s = 0

temp = num
while temp > 0:
   digit = temp % 10
   s = s + (digit ** order)
   temp //= 10


if num == s:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")