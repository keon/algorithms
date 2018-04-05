"""
I just bombed an interview and made pretty much zero 
progress on my interview question. 

Given a number, find the next higher number which has the 
exact same set of digits as the original number. 
For example: given 38276 return 38627.

"""

"""
Condensed mathematical description:

Find largest index i such that array[i − 1] < array[i].
(If no such i exists, then this is already the last permutation.)

Find largest index j such that j ≥ i and array[j] > array[i − 1].

Swap array[j] and array[i − 1].

Reverse the suffix starting at array[i].

"""

def next_bigger(num):
    digits = [int(i) for i in str(num)]
    idx = len(digits) - 1
    while idx >= 1 and digits[idx-1] >= digits[idx]:
        idx -= 1
    if idx == 0:
        return -1
    pivot = digits[idx-1]
    swap_idx = len(digits) - 1
    while pivot >= digits[swap_idx]:
        swap_idx -= 1
    digits[swap_idx], digits[idx-1] = digits[idx-1], digits[swap_idx]
    digits[idx:] = digits[:idx-1:-1] # prefer slicing instead of reversed(digits[idx:])
    return int(''.join(str(x) for x in digits))