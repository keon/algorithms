
def interpolation_search(arr, x):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        m = lo + int(float(hi - lo) / (arr[hi] - arr[lo] + 1) * (x - arr[lo]))

        if arr[m] == x:
            return m

        if arr[m] < x:
            lo = m + 1

        else:
            hi = m - 1

    return -1
