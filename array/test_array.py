from delete_nth import delete_nth, delete_nth_naive
from flatten import flatten, flatten_iter
from garage import garage
from josephus_problem import josephus

import unittest


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


class TestDeleteNth(unittest.TestCase):

    def test_delete_nth_naive(self):

        self.assertListEqual(delete_nth_naive([20, 37, 20, 21, 37, 21, 21], n=1),
                             [20, 37, 21])
        self.assertListEqual(delete_nth_naive([1, 1, 3, 3, 7, 2, 2, 2, 2], n=3),
                             [1, 1, 3, 3, 7, 2, 2, 2])
        self.assertListEqual(delete_nth_naive([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=3),
                             [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])
        self.assertListEqual(delete_nth_naive([], n=5),
                             [])
        self.assertListEqual(delete_nth_naive([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=0),
                             [])

    def test_delete_nth(self):

        self.assertListEqual(delete_nth([20, 37, 20, 21, 37, 21, 21], n=1),
                             [20, 37, 21])
        self.assertListEqual(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], n=3),
                             [1, 1, 3, 3, 7, 2, 2, 2])
        self.assertListEqual(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=3),
                             [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])
        self.assertListEqual(delete_nth([], n=5),
                             [])
        self.assertListEqual(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=0),
                             [])


class TestFlatten(unittest.TestCase):

    def test_flatten(self):

        nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [2, 1, 3, 4, 5, 6, 7, 8])

        nested_list = [[3, [4, 5], 6], 7, [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [3, 4, 5, 6, 7, 8])

        nested_list = [[], [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [8])

    def test_flatten_iter(self):

        nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
        flattened = flatten_iter(nested_list)
        self.assertEqual(next(flattened), 2)
        self.assertEqual(next(flattened), 1)
        self.assertEqual(next(flattened), 3)
        self.assertEqual(next(flattened), 4)
        self.assertEqual(next(flattened), 5)
        self.assertEqual(next(flattened), 6)
        self.assertEqual(next(flattened), 7)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)

        nested_list = [[3, [4, 5], 6], 7, [8]]
        flattened = flatten_iter(nested_list)
        self.assertEqual(next(flattened), 3)
        self.assertEqual(next(flattened), 4)
        self.assertEqual(next(flattened), 5)
        self.assertEqual(next(flattened), 6)
        self.assertEqual(next(flattened), 7)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)

        nested_list = [[], [8]]
        flattened = flatten_iter(nested_list)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)


if __name__ == '__main__':
    unittest.main()
