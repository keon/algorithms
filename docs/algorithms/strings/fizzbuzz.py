"""
Write a function that returns an array containing the numbers from 1 to N, 
where N is the parametered value. N will never be less than 1.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value 'Fizz' instead
If the value is a multiple of 5: use the value 'Buzz' instead
If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead
"""

"""
There is no fancy algorithm to solve fizz buzz.

Iterate from 1 through n
Use the mod operator to determine if the current iteration is divisible by:
3 and 5 -> 'FizzBuzz'
3 -> 'Fizz'
5 -> 'Buzz'
else -> string of current iteration
return the results
Complexity:

Time: O(n)
Space: O(n)
"""

def fizzbuzz(n):
    
    # Validate the input
    if n < 1:
        raise ValueError('n cannot be less than one')
    if n is None:
        raise TypeError('n cannot be None')
    
    result = []
    
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            result.append('FizzBuzz')
        elif i%3 == 0:
            result.append('Fizz')
        elif i%5 == 0:
            result.append('Buzz')
        else:
            result.append(i)
    return result

# Alternative solution
def fizzbuzz_with_helper_func(n):
    return [fb(m) for m in range(1,n+1)]
    
def fb(m):
    r = (m % 3 == 0) * "Fizz" + (m % 5 == 0) * "Buzz"
    return r if r != "" else m
