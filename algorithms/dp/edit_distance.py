"""The edit distance between two words is the minimum number of letter insertions,
letter deletions, and letter substitutions required to transform one word into another.

For example, the edit distance between FOOD and MONEY is at most four:

FOOD -> MOOD -> MOND -> MONED -> MONEY

Given two words A and B, find the minimum number of operations required to transform one string into the other.
In other words, find the edit distance between A and B.

Thought process:

Let edit(i, j) denote the edit distance between the prefixes A[1..i] and B[1..j].

Then, the function satifies the following recurrence:

edit(i, j) = i if j = 0
             j if i = 0
             min(edit(i-1, j) + 1, 
                 edit(i, j-1), + 1,
                 edit(i-1, j-1) + cost) otherwise

There are two base cases, both of which occur when one string is empty and the other is not.
1. To convert an empty string A into a string B of length n, perform n insertions.
2. To convert a string A of length m into an empty string B, perform m deletions.

Here, the cost is 1 if a substitution is required,
or 0 if both chars in words A and B are the same at indexes i and j, respectively.

To find the edit distance between two words A and B,
we need to find edit(m, n), where m is the length of A and n is the length of B.
"""


def edit_distance(A, B):
    # Time: O(m*n)
    # Space: O(m*n)

    m, n = len(A) + 1, len(B) + 1

    edit = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        edit[i][0] = i

    for j in range(1, n):
        edit[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if A[i - 1] == B[j - 1] else 1
            edit[i][j] = min(edit[i - 1][j] + 1, edit[i][j - 1] + 1, edit[i - 1][j - 1] + cost)

    return edit[-1][-1]  # this is the same as edit[m][n]
