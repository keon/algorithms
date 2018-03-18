"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
give a single resultant array.

function flatten(input){
}

Example:

Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""
import collections


def flatten(inputArr, outputArr=None):
    if not outputArr:
        outputArr = []
    for ele in inputArr:
        if isinstance(ele, collections.Iterable):
            flatten(ele, outputArr)
        else:
            outputArr.append(ele)
    return outputArr
