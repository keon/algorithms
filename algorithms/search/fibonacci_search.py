"""
https://en.wikipedia.org/wiki/Fibonacci_search_technique


Let k be defined as an element in F, the array of Fibonacci numbers. n = Fm is the array size. If n is not a Fibonacci number, let Fm be the smallest number in F that is greater than n.

The array of Fibonacci numbers is defined where Fk+2 = Fk+1 + Fk, when k ≥ 0, F1 = 1, and F0 = 0.

To test whether an item is in the list of ordered numbers, follow these steps:

    1. Set k = m.
    2. If k = 0, stop. There is no match; the item is not in the array.
    3. Compare the item against element in Fk−1.
    4. If the item matches, stop.
    5. If the item is less than entry Fk−1, discard the elements from positions Fk−1 + 1 to n. Set k = k − 1 and return to step 2.
    6. If the item is greater than entry Fk−1, discard the elements from positions 1 to Fk−1. Renumber the remaining elements from 1 to Fk−2, set k = k − 2, and return to step 2.

"""

from bisect import bisect_left 

def fibonacci_search(arr, x): 
      
    fib2 = 0 
    fib1 = 1 
    fib3 = fib2 + fib1
  
    n = len(arr)
    while (fib3 < n): 
        fib2 = fib1 
        fib1 = fib3 
        fib3 = fib2 + fib1 
  
    offset = -1; 
  
    while (fib3 > 1): 
          
        i = min(offset+fib2, n-1) 
  
        if (arr[i] < x): 
            fib3 = fib1 
            fib1 = fib2 
            fib2 = fib3 - fib1 
            offset = i 
  
        elif (arr[i] > x): 
            fib3 = fib2 
            fib1 = fib1 - fib2 
            fib2 = fib3 - fib1 
  
        else : 
            return i 
  
    if(fib1 == 1 and offset < n - 1  and arr[offset+1] == x): 
        return offset+1; 
  
    return None
