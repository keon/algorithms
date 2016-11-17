


def reverse(array):
    i, j = 0, len(array)
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

def reverseWords(array):
    reverse(array)

