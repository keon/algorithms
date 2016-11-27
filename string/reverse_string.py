def recursive(s):
    l = len(s)
    if l < 2:
        return s
    return recursive(s[l//2:]) + recursive(s[:l//2])

s = "hello there"
print(recursive(s))

def iterative(s):
    r = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1
    return "".join(r)

print(iterative(s))

def pythonic(s):
    r = list(reversed(s))
    return "".join(r)

print(pythonic(s))
