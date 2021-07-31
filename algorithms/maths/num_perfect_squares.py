"""
Some examples:
10 = 1^2 + 3^2
Answer = 2
12 = 2^2 + 2^2 + 2^2
Answer = 3
13 = 2^2 + 3^2
Answer = 2
"""
import math



def num_perfect_square(number) -> int:
    if(math.sqrt(number) ** 2 == number):    # if its a perfect squre check
        return 1
    while( number % 4 ==0):  #Check if number is of the form 4^a(8b + 7) 
        number /= 4
           
    if(number %8 ==7): # check the 7 now
        return 4
    
    i=1

    #Now just chekc for 2 if not 2 return 3
    # now will find a break point which square is n- i*i
    while(i*i <=number):   
        b = int(math.sqrt(number - i*i))
        if(b*b == (number - i*i)):
            return 2
        i += 1

    return 3
    
# for more info please check https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem


