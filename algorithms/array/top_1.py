"""
this algorithms receive array and check most_frequent_value(a.k.a mode). Also, sometimes it can be have numerous most_frequent_value,
so this funtion returns list. This result can be used as finding representative value on array.

This algorithms get array, and make dictionary of it, find most frequent count, and make result list.

For example) top_1([1, 1, 2, 2, 3, 4]) will return [1, 2]

Complexity: O(n)
"""
def top_1(arr):
    values = {}
    #reserve each value which first appears on keys
    #reserve how many time each value appears by index number on values
    result = []
    f_val = 0

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    a = list(values.values())

    a.sort()

    f_val = a[len(a)-1]
        
    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue
    
    return result
