"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections.abc import Iterable


# return list
def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            flatten(ele, output_arr)    #tail-recursion
        else:
            output_arr.append(ele)      #produce the result
    return output_arr


# retrun list
# not use recursive functions for python recursion limit
def flatten_v2(input_arr) -> list:
    idx = 0
    while idx < len(input_arr):
        print(input_arr)
        ele = input_arr[idx]
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            input_arr = input_arr[:idx] + ele + input_arr[idx+1:]
        else:
            idx += 1
    return input_arr


# returns iterator
def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if not isinstance(element, str) and isinstance(element, Iterable):
            yield from flatten_iter(element)    
        else:
            yield element
