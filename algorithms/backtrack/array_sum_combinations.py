"""
WAP to take one element from each of the array add it to the target sum.
Print all those three-element combinations.

/*
A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [2, 3, 3, 4]
target = 7
*/

Result:
[[1, 2, 4], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 4, 2],
 [2, 2, 3], [2, 2, 3], [2, 3, 2], [2, 3, 2], [3, 2, 2], [3, 2, 2]]
"""
import itertools
from functools import partial


def array_sum_combinations(A, B, C, target):

    def over(constructed_sofar):
        sum = 0
        to_stop, reached_target = False, False
        for elem in constructed_sofar:
            sum += elem
        if sum >= target or len(constructed_sofar) >= 3:
            to_stop = True
            if sum == target and 3 == len(constructed_sofar):
                reached_target = True
        return to_stop, reached_target

    def construct_candidates(constructed_sofar):
        array = A
        if 1 == len(constructed_sofar):
            array = B
        elif 2 == len(constructed_sofar):
            array = C
        return array

    def backtrack(constructed_sofar=[], res=[]):
        to_stop, reached_target = over(constructed_sofar)
        if to_stop:
            if reached_target:
                res.append(constructed_sofar)
            return
        candidates = construct_candidates(constructed_sofar)

        for candidate in candidates:
            constructed_sofar.append(candidate)
            backtrack(constructed_sofar[:], res)
            constructed_sofar.pop()

    res = []
    backtrack([], res)
    return res


def unique_array_sum_combinations(A, B, C, target):
    """
    1. Sort all the arrays - a,b,c. - This improves average time complexity.
    2. If c[i] < Sum, then look for Sum - c[i] in array a and b.
       When pair found, insert c[i], a[j] & b[k] into the result list.
       This can be done in O(n).
    3. Keep on doing the above procedure while going through complete c array.

    Complexity: O(n(m+p))
    """
    def check_sum(n, *nums):
        if sum(x for x in nums) == n:
            return (True, nums)
        else:
            return (False, nums)

    pro = itertools.product(A, B, C)
    func = partial(check_sum, target)
    sums = list(itertools.starmap(func, pro))

    res = set()
    for s in sums:
        if s[0] is True and s[1] not in res:
            res.add(s[1])

    return list(res)
