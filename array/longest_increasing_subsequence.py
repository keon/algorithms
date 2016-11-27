

def longest_increasing_subsequence(sequence):
    """
    Dynamic Programming Algorithm for
    counting the length of longest increasing subsequence
    type sequence: List[int]
    """
    length = len(sequence)
    counts = [1 for _ in range(length)]
    for i in range(1, length):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                counts[i] = max(counts[i], counts[j] + 1)
                print(counts)
    return max(counts)


sequence = [1, 101, 10, 2, 3, 100, 4, 6, 2]
print("sequence: ", sequence)
print("output: ", longest_increasing_subsequence(sequence))
print("answer: ", 5)

