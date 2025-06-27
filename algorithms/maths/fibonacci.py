n=int(input("enter the no of terms "))#input from the user
a=int(input("enter the first number "))#input from the user
b= int(input("enter the second number "))#input from the user
i=2                   #i is initialised from 2 because we have taken two elements of the fibonacci already 
print(a)
print(b)
while(i<n):
    fibbonacci=a+b    #adding last two numbers
    print(fibbonacci) 
    a=b               #storing the value of b in a  
    b=fibbonacci      #storing the value of fibbonacci in b 
    i=i+1             #increasing the value  of i 
