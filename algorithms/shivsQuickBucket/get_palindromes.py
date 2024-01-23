'''Generate palindromes from 1 to 10 ** 9'''

l = []
for i in range(1, 100000):
    s = str(i)
    l.append(int(s + s[::-1]))
    l.append(int(s + s[::-1][1:]))
l.sort()