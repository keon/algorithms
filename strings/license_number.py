
def license_number(key, k):
    res, alnum = [], []
    for char in key:
        if char != "-":
            alnum.append(char)
    for i, char in enumerate(reversed(alnum)):
        res.append(char)
        if (i+1) % k == 0 and i != len(alnum)-1:
            res.append("-")
    return "".join(res[::-1])
