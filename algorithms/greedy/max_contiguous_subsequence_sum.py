'''
Algorithm used => Kadane's Algorithm

kadane's algorithm is used for finding the maximum sum of contiguous subsequence in a sequence.
It is considered a greedy/dp algorithm but I think they more greedy than dp
here are some of the examples to understand the use case more clearly
Example1 => [-2, 3, 8, -1, 4]
result =>  {3, 8, -1, 4} => 14
Example2 => [-1, 1, 0]
result => {1} => 1
Example3 => [-1, -3, -4]
result => -1
Example1 => [-2, 3, 8, -12, 8, 4]
result =>  {8, 4} => 12
Basic Algorithm Idea
    If the sum of the current contiguous subsequence after adding the value at the current position is less than the value
    at the current position then we know that it will be better if we start the current contiguous subsequence from this position.
    Else we add the value at the current position to the current contiguous subsequence.
Note
    In the implementation, the contiguous subsequence has at least one element.
    If it can have 0 elements then the result will be max(max_till_now, 0)
'''


def max_contiguous_subsequence_sum(arr) -> int:
    arr_size = len(arr)

    if arr_size == 0:
        return 0

    max_till_now = arr[0]
    curr_sub_sum = 0

    for i in range(0, arr_size):
        if curr_sub_sum + arr[i] < arr[i]:
            curr_sub_sum = arr[i]
        else:
            curr_sub_sum += arr[i]

        max_till_now = max(max_till_now, curr_sub_sum)

    return max_till_now
