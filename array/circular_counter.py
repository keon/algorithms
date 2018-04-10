"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""
import unittest


def josephus(int_list, skip):
    skip = skip - 1  # list starts with 0 index
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (skip+idx) % len_list  # hash index to every 3rd
        yield int_list.pop(idx)
        len_list -= 1


class TestJosephus(unittest.TestCase):

    def test_josephus(self):
        a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        josephus_generator = josephus(a, 3)
        self.assertEqual(next(josephus_generator), '3')
        self.assertEqual(next(josephus_generator), '6')
        self.assertEqual(next(josephus_generator), '9')
        self.assertEqual(next(josephus_generator), '4')
        self.assertEqual(next(josephus_generator), '8')
        self.assertEqual(next(josephus_generator), '5')
        self.assertEqual(next(josephus_generator), '2')
        self.assertEqual(next(josephus_generator), '7')
        self.assertEqual(next(josephus_generator), '1')
        self.assertRaises(StopIteration, next, josephus_generator)


if __name__ == "__main__":
    
    unittest.main()
