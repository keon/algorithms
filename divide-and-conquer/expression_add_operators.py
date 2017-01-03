"""
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they prevuate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""

def add_operator(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    res = []
    if not num: return res
    helper(res, "", num, target, 0, 0, 0)
    return res

def helper(res, path, num, target, pos, prev, multed):
    if pos == len(num):
        if (target == prev):
            res.append(path)
        return
    for i in range(pos, len(num)):
        if i != pos and num[pos] == '0': # all digits have to be used
            break
        cur = int(num[pos:i+1])
        if pos == 0:
            helper(res, path + str(cur), num, target, i+1, cur, cur)
        else:
            helper(res, path + "+" + str(cur), num, target, i+1, prev + cur, cur)
            helper(res, path + "-" + str(cur), num, target, i+1, prev - cur, -cur)
            helper(res, path + "*" + str(cur), num, target, i+1, prev - multed + multed * cur, multed * cur)


# "123", 6 -> ["1+2+3", "1*2*3"]
s = "123"
target = 6
print(add_operator(s, target))
# "232", 8 -> ["2*3+2", "2+3*2"]
s = "232"
target = 8
print(add_operator(s, target))

s = "123045"
target = 3
print(add_operator(s, target))
