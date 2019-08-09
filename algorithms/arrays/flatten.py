
from collections import Iterable


# return list
def flatten(input_arr, output_arr=None):
    if not input_arr:
      return output_arr 
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
     try:
        iter(ele)
        if ele:
            output_arr.append(ele[0])
            flatten(ele[1:], output_arr)
     except TypeError:
        output_arr.append(ele)
          
          
    return output_arr


# returns iterator
def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten_iter(element)    
        else:
            yield element
