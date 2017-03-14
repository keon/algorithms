"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""


# Python solution without table (~156ms):
def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if A is None or B is None: return None
    m, n, l = len(A), len(A[0]), len(B[0])
    if len(B) != n:
        raise Exception("A's column number must be equal to B's row number.")
    C = [[0 for _ in range(l)] for _ in range(m)]
    for i, row in enumerate(A):
        for k, eleA in enumerate(row):
            if eleA:
                for j, eleB in enumerate(B[k]):
                    if eleB: C[i][j] += eleA * eleB
    return C


# Python solution with only one table for B (~196ms):
def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if A is None or B is None: return None
    m, n, l = len(A), len(A[0]), len(B[0])
    if len(B) != n:
        raise Exception("A's column number must be equal to B's row number.")
    C = [[0 for _ in range(l)] for _ in range(m)]
    tableB = {}
    for k, row in enumerate(B):
        tableB[k] = {}
        for j, eleB in enumerate(row):
            if eleB: tableB[k][j] = eleB
    for i, row in enumerate(A):
        for k, eleA in enumerate(row):
            if eleA:
                for j, eleB in tableB[k].iteritems():
                    C[i][j] += eleA * eleB
    return C

# Python solution with two tables (~196ms):
def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if A is None or B is None: return None
    m, n = len(A), len(A[0])
    if len(B) != n:
        raise Exception("A's column number must be equal to B's row number.")
    l = len(B[0])
    table_A, table_B = {}, {}
    for i, row in enumerate(A):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_A: table_A[i] = {}
                table_A[i][j] = ele
    for i, row in enumerate(B):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_B: table_B[i] = {}
                table_B[i][j] = ele
    C = [[0 for j in range(l)] for i in range(m)]
    for i in table_A:
        for k in table_A[i]:
            if k not in table_B: continue
            for j in table_B[k]:
                C[i][j] += table_A[i][k] * table_B[k][j]
    return C
