# Sparse Arrays 

# There is a collection of input strings and a collections of query strings . For each query strings , determine how many times it occurs in the list of input strings.
# For example given input strings =[ab,ab,abc] and queries=[ab,abc,bc], we find 2 instances of ab, 1 instance of abc and 0 instance of bc .For ech query, we add an element to our return array, results =[2,1,0].

# Function Description
# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurence of each query string in strings.
# matchingStrings has the following parameters 

# strings- an array of strings to search
# queries an array of query strings 

# Input Format
# the first line contains and integer n, the size of strings. Each of the next n lines contains a string strings[i]. The next line line contains q, the size of queries. Each of the next q lines contains a string queries[i].

#Constraints

#1<=n,q<=1000
#1<=|strings[i]|,|queries[i]|<=20.

#Output Format

# Return an internal array of the results of all queries in order. 


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    #result = []
    count_dict = Counter(strings)
    #for k in queries:
        #if k in count_dict:
            #result.append(count_dict[k])
        #else:
            #result.append(0)
    result = [count_dict[x] if x in count_dict else 0 for x in queries ]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
