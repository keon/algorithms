def getZarr(str, Z):
    n = len(str)
    Left = 0
    Right = 0

    for i in range(1, n):
        if i > Right:
            Left = i
            Right = i

            while Right < n and str[Right - Left] == str[Right]:
                Right += 1

            Z[i] = Right - Left
            Right -= 1
        else:
            k = i - Left

            if Z[k] < Right - i + 1:
                Z[i] = Z[k]
            else:
                Left = i

                while Right < n and str[Right - Left] == str[Right]:
                    Right += 1

                Z[i] = Right - Left
                Right -= 1


def search(text, pattern):
    concat = pattern + "$" + text
    size = len(concat)
    Z = [0] * size

    getZarr(concat, Z)

    for i in range(0, size):
        if Z[i] == len(pattern):
            print("Pattern found at " + str(i - len(pattern)))


text = "namanchamanbomanamansanam"
pattern = "aman"

search(text, pattern)

""" Output
Pattern found at 2
Pattern found at 8
Pattern found at 17
"""
