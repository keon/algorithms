"""
this algorithms receive array and check most_frequent_value(a.k.a mode). Also, sometimes it can be have numerous most_frequent_value,
so this funtion returns list. This result can be used as finding representative value on array.
"""
def most_frequent_value(arr):
    values = []
    #reserve each value which first appears
    times = []
    #reserve how many time each value appears by index number
    result = []
    f_val = 0
    check = 0
    for i in arr:
        for a in range(len(values)):
            if values[a] == i:
                times[a] += 1
                check = 1
        if check == 0:
            values.append(i)
            times.append(1)
        check = 0
    for i in range(len(times)):
        if times[i] > f_val:
            result = []
            result.append(values[i])
            f_val = times[i]
        elif times[i] == f_val:
            result.append(values[i])
        else:
            continue
    return result
