"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n
and return all possible combinations of its factors.

Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples:
input: 1
output:
[]
input: 37
output:
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""


# Iterative:
def get_factors(n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis.append(combi + [i, n//i])
                todo.append((n//i, i, combi+[i]))
            i += 1
    return combis


# Recursive:
def recursive_get_factors(n):

    def factor(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis.append(combi + [i, n//i]),
                factor(n//i, i, combi+[i], combis)
            i += 1
        return combis

    return factor(n, 2, [], [])
