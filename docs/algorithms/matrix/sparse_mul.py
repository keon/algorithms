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
def multiply(self, a, b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if a is None or b is None:
        return None
    m, n, l = len(a), len(b[0]), len(b[0])
    if len(b) != n:
        raise Exception("A's column number must be equal to B's row number.")
    c = [[0 for _ in range(l)] for _ in range(m)]
    for i, row in enumerate(a):
        for k, eleA in enumerate(row):
            if eleA:
                for j, eleB in enumerate(b[k]):
                    if eleB:
                        c[i][j] += eleA * eleB
    return c


# Python solution with only one table for B (~196ms):
def multiply(self, a, b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if a is None or b is None:
        return None
    m, n, l = len(a), len(a[0]), len(b[0])
    if len(b) != n:
        raise Exception("A's column number must be equal to B's row number.")
    c = [[0 for _ in range(l)] for _ in range(m)]
    table_b = {}
    for k, row in enumerate(b):
        table_b[k] = {}
        for j, eleB in enumerate(row):
            if eleB:
                table_b[k][j] = eleB
    for i, row in enumerate(a):
        for k, eleA in enumerate(row):
            if eleA:
                for j, eleB in table_b[k].iteritems():
                    c[i][j] += eleA * eleB
    return c


# Python solution with two tables (~196ms):
def multiply(self, a, b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if a is None or b is None:
        return None
    m, n = len(a), len(b[0])
    if len(b) != n:
        raise Exception("A's column number must be equal to B's row number.")
    l = len(b[0])
    table_a, table_b = {}, {}
    for i, row in enumerate(a):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_a:
                    table_a[i] = {}
                table_a[i][j] = ele
    for i, row in enumerate(b):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_b:
                    table_b[i] = {}
                table_b[i][j] = ele
    c = [[0 for j in range(l)] for i in range(m)]
    for i in table_a:
        for k in table_a[i]:
            if k not in table_b:
                continue
            for j in table_b[k]:
                c[i][j] += table_a[i][k] * table_b[k][j]
    return c
