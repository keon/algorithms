"""
When make reliable means, we need to neglect best and worst value. For example, when making average score on athletes we need this option.
So, this algorithms, fix some percentage to neglect when making mean. For example, if you suggest 20%, it will neglect best 10% value, and
worst 10% value.
"""
def trimmean(arr, per):
    ratio = per/200
    # /100 for easy calculation by *, and /2 for easy adaption to best and worst parts.
    cal_sum = 0
    # sum value to be calculated to trimmean.
    arr.sort()
    count = 0
    # count how many values added.
    for i in range(len(arr)):
        if i>(len(arr)*ratio-1) and i<(len(arr)-len(arr)*ratio):
            cal_sum += arr[i]
            count += 1
    #print(cal_sum, count)
    return cal_sum/count
