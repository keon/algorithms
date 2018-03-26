"""
https://en.wikipedia.org/wiki/Josephus_problem

There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271


>>> a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> josepheus_generator = josepheus(a, 3)
>>> assert next(josepheus_generator) == '3'
>>> assert next(josepheus_generator) == '6'
>>> assert next(josepheus_generator) == '9'
>>> assert next(josepheus_generator) == '4'
>>> assert next(josepheus_generator) == '8'
>>> assert next(josepheus_generator) == '5'
>>> assert next(josepheus_generator) == '2'
>>> assert next(josepheus_generator) == '7'
>>> assert next(josepheus_generator) == '1'
"""


def josepheus(int_list, skip):
    skip = skip - 1  # list starts with 0 index
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (skip+idx) % len_list  # hash index to every 3rd
        yield int_list.pop(idx)
        len_list -= 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
