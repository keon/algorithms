"""
Non-negative 1-sparse recovery problem.
This algorithm assumes we have a non negative dynamic stream.

Given a stream of tuples, where each tuple contains a number and a sign (+/-), it check if the
stream is 1-sparse, meaning if the elements in the stream cancel eacheother out in such
a way that ther is only a unique number at the end.

Examples:
#1
Input:  [(4,'+'), (2,'+'),(2,'-'),(4,'+'),(3,'+'),(3,'-')],
Output: 4
Comment: Since 2 and 3 gets removed.
#2
Input:  [(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+')]
Output: 2
Comment: No other numbers present
#3
Input:  [(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(1,'+')]
Output: None
Comment: Not 1-sparse
"""

def one_sparse(array):
    """1-sparse algorithm

    Keyword arguments:
    array -- stream of tuples
    """
    sum_signs = 0
    bitsum = [0]*32
    sum_values = 0
    for val,sign in array:
        if sign == "+":
            sum_signs += 1
            sum_values += val
        else:
            sum_signs -= 1
            sum_values -= val

        _get_bit_sum(bitsum,val,sign)

    if sum_signs > 0 and _check_every_number_in_bitsum(bitsum,sum_signs):
        return int(sum_values/sum_signs)
    else:
        return None

#Helper function to check that every entry in the list is either 0 or  the same as the
#sum of signs
def _check_every_number_in_bitsum(bitsum,sum_signs):
    for val in bitsum:
        if val != 0 and val != sum_signs :
            return False
    return True

# Adds bit representation value to bitsum array
def _get_bit_sum(bitsum,val,sign):
    i = 0
    if sign == "+":
        while val:
            bitsum[i] += val & 1
            i +=1
            val >>=1
    else :
        while val:
            bitsum[i] -= val & 1
            i +=1
            val >>=1
