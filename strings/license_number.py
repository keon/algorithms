
def license_number(key, K):
    res, alnum = [], []
    for char in key:
        if char != "-":
            alnum.append(char)
    for i, char in enumerate(reversed(alnum)):
        res.append(char)
        if (i+1) % K == 0 and i != len(alnum)-1:
            res.append("-")
    return "".join(res[::-1])


print(license_number("a-bc-dfd-df", 1), 1)
print(license_number("a-bc-dfd-df", 2), 2)
print(license_number("a-bc-dfd-df", 3), 3)
print(license_number("a-bc-dfd-df", 4), 4)
print(license_number("a-bc-dfd-df", 5), 5)

