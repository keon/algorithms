"""
Given a array/list , return a randomly shuffle array/list
this is implementation of "Fisher–Yates shuffle Algorithm",time complexity of this algorithm
is O(n) assumption here is, function rand() that generates random number in O(1) time.

Examples:
Given [1,2,3,4,5,6,7], [5, 2, 3, 4, 1]
Given [1,2,3,4,5,6,7], [1,2,3,4,5,6,7]
Given [1,2,3,4,5,6,7], [1, 2, 3, 5, 4]

"""


import random

def randomize_array(arr):

    for i in range(len(arr)-1,0,-1):

        # To generate a random nummber within it's index
        j = random.randint(0,i)

        # Swap arr[i] with the element at random index
        arr[i],arr[j] = arr[j],arr[i]
        return arr
