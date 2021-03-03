
"""
1-sparse recovery problem. This algorithm assumes we have a non negative dynamic stream.
Given a stream of tuples, where each tuple contains a number and a sign (+/-), it check if the stream is 1-sparse, meaning if the elements
in the stream cancel eacheother out in such a way that ther is only a unique number at the end. 

Examples:
if the stream consists of [(4,'+'), (2,'+'),(2,'-'),(4,'+'),(3,'+'),(3,'-')], the algorithm will return 4, since the 2s and 3s will cancel eachother out
and there will only be 4s left

if the stream consists of [(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+')], the algorithm returns 2, since the stream only consists of the same number and sign

if the stream consists of [(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(1,'+')], the algorithm returns None, since there will be 2 different number remaining

"""

def one_sparse(array):
  sum_signs = 0
  bitsum = [0]*32
  sum_values = 0
  for element in array:
    val,sign = element
    if sign == "+":
      sum_signs += 1
      sum_values += val
    else:
      sum_signs -= 1
      sum_values -= val

    bitsum = _get_bit_sum(bitsum,val,sign)
  
  if sum_signs > 0 and _check_every_number_in_bitsum(bitsum,sum_signs):
    return int(sum_values/sum_signs)
  else:
    return None
 
   
#Helper function to check that every entry in the list is either 0 or  the same as the
#sum of signs
def _check_every_number_in_bitsum(bitsum,sum_signs):
  for val in bitsum:
    if val == sum_signs or val == 0:
      continue
    else:
      return False
  return True


#Given 2 lists, representing 2 binary numbers, return either the sum or difference at each entry in the list
def _get_bit_sum(sum_bits,new_value,sign):
  bit_repr = [int(x) for x in bin(new_value)[2:]]
  while len(bit_repr) < 32:
    bit_repr.insert(0,0)
  assert len(bit_repr) == len(sum_bits)
  if sign == "+":
    for i in range(len(bit_repr)-1,-1,-1):
      sum_bits[i] += bit_repr[i] 

  if sign == "-":
    for i in range(len(bit_repr)-1,-1,-1):
      sum_bits[i] -= bit_repr[i] 

  return sum_bits
  
