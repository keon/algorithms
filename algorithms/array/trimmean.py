"""
When make reliable means, we need to neglect best and worst value. For example, when making average score on athletes we need this option.
So, this algorithms, fix some percentage to neglect when making mean. For example, if you suggest 20%, it will neglect best 10% value, and
worst 10% value.

This algorithm gets array and percentage to neglect. After sorted, if index of array is larger or smaller or wanted ratio, we don't
compute it.

Compleity: O(n)
"""
def trimmean(arr, per):
    ratio = per/200
    # /100 for easy calculation by *, and /2 for easy adaption to best and worst parts.
    cal_sum = 0
    # sum value to be calculated to trimmean.
    arr.sort()
    neg_val = int(len(arr)*ratio)
    arr = arr[neg_val:len(arr)-neg_val]
    for i in arr:
        cal_sum += i
    #print(cal_sum, len(arr))
    return cal_sum/len(arr)
