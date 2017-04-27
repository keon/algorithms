
def reverse(array, i, j):
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

def reverse_words(string):
    arr = list(string)
    n = len(arr)
    reverse(arr, 0, n-1)

    start = None
    for i in range(n):
        if arr[i] == " ":
           if start is not None:
                reverse(arr, start, i-1)
                start = None
        elif i == n-1:
            if start is not None:
                reverse(arr, start, i)
        else:
            if start is None:
                start = i
    return "".join(arr)


if __name__ == "__main__":
    test = "I am keon kim and I like pizza"
    print(test)
    print(reverse_words(test))
