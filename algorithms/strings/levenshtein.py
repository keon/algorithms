"""Levenshtein Distance.

In information theory, linguistics and computer science,
the Levenshtein distance is a string metric for measuring the difference
between two sequences. Informally, the Levenshtein distance between two words
is the minimum number of single-character edits (insertions, deletions or
substitutions) required to change one word into the other.
It is named after the Soviet mathematician Vladimir Levenshtein, who considered
this distance in 1965.[1]

Levenshtein distance may also be referred to as edit distance, although that
term may also denote a larger family of distance metrics.[2]:32 It is closely
related to pairwise string alignments.

https://en.wikipedia.org/wiki/Levenshtein_distance (27/09/2018)
"""


def levenshtein(A, B):
    """
    Return the edit distance between two strings.

    Example:
    >>> from levenshtein import levenshtein
    >>> levenshtein("Star Wars", "Star Trek")
    >>> 4
    """
    m = len(A)
    n = len(B)
    M = []

    for x in range(m+1):
        M.append([])
        for y in range(n+1):
            M[x].append((0))

    for i in range(0, m+1):
        M[i][0] = i

    for j in range(0, n+1):
        M[0][j] = j

    for x in range(1, m+1):
        for y in range(1, n+1):
            if A[x-1] == B[y-1]:
                cost = 0
            else:
                cost = 1

            M[x][y] = min((M[x-1][y-1] + cost,
                           M[x-1][y] + 1,
                           M[x][y-1] + 1,))

    return(M[m][n])
