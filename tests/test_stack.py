from algorithms.stack import (
    first_is_consecutive, second_is_consecutive,
    is_sorted,
    remove_min,
    first_stutter, second_stutter,
    first_switch_pairs, second_switch_pairs,
    is_valid,
    simplify_path,
    ArrayStack, LinkedListStack,
    OrderedStack
)

import unittest
class TestSuite(unittest.TestCase):
    def test_is_consecutive(self):
        self.assertTrue(first_is_consecutive([3, 4, 5, 6, 7]))
        self.assertFalse(first_is_consecutive([3, 4, 6, 7]))
        self.assertFalse(first_is_consecutive([3, 2, 1]))

        self.assertTrue(second_is_consecutive([3, 4, 5, 6, 7]))
        self.assertFalse(second_is_consecutive([3, 4, 6, 7]))
        self.assertFalse(second_is_consecutive([3, 2, 1]))

    def test_is_sorted(self):
        # Test case: bottom [6, 3, 5, 1, 2, 4] top
        self.assertFalse(is_sorted([6, 3, 5, 1, 2, 4]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertFalse(is_sorted([3, 4, 7, 8, 5, 6]))

    def test_remove_min(self):
        # Test case: bottom [2, 8, 3, -6, 7, 3] top
        self.assertEqual([2, 8, 3, 7, 3], remove_min([2, 8, 3, -6, 7, 3]))
        # Test case: 2 smallest value [2, 8, 3, 7, 3]
        self.assertEqual([4, 8, 7], remove_min([4, 8, 3, 7, 3]))

    def test_stutter(self):
        # Test case: bottom [3, 7, 1, 14, 9] top
        self.assertEqual([3, 3, 7, 7, 1, 1, 14, 14, 9, 9],
                         first_stutter([3, 7, 1, 14, 9]))
        self.assertEqual([3, 3, 7, 7, 1, 1, 14, 14, 9, 9],
                         second_stutter([3, 7, 1, 14, 9]))

    def test_switch_pairs(self):
        # Test case: even number of values in stack
        # bottom [3, 8, 17, 9, 1, 10] top
        self.assertEqual([8, 3, 9, 17, 10, 1],
                         first_switch_pairs([3, 8, 17, 9, 1, 10]))
        self.assertEqual([8, 3, 9, 17, 10, 1],
                         second_switch_pairs([3, 8, 17, 9, 1, 10]))
        # Test case: odd number of values in stack
        # bottom [3, 8, 17, 9, 1] top
        self.assertEqual([8, 3, 9, 17, 1],
                         first_switch_pairs([3, 8, 17, 9, 1]))
        self.assertEqual([8, 3, 9, 17, 1],
                         second_switch_pairs([3, 8, 17, 9, 1]))

    def test_is_valid_parenthesis(self):

        self.assertTrue(is_valid("[]"))
        self.assertTrue(is_valid("[]()[]"))
        self.assertFalse(is_valid("[[[]]"))
        self.assertTrue(is_valid("{([])}"))
        self.assertFalse(is_valid("(}"))

    def test_simplify_path(self):
        p = '/my/name/is/..//keon'
        self.assertEqual('/my/name/keon', simplify_path(p))


class TestStack(unittest.TestCase):
    def test_ArrayStack(self):
        stack = ArrayStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        # test __iter__()
        it = iter(stack)
        self.assertEqual(3, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(1, next(it))
        self.assertRaises(StopIteration, next, it)

        # test __len__()
        self.assertEqual(3, len(stack))

        # test __str__()
        self.assertEqual(str(stack), "Top-> 3 2 1")

        # test is_empty()
        self.assertFalse(stack.is_empty())

        # test peek()
        self.assertEqual(3, stack.peek())

        # test pop()
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())

        self.assertTrue(stack.is_empty())

    def test_LinkedListStack(self):
        stack = LinkedListStack()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        # test __iter__()
        it = iter(stack)
        self.assertEqual(3, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(1, next(it))
        self.assertRaises(StopIteration, next, it)

        # test __len__()
        self.assertEqual(3, len(stack))

        # test __str__()
        self.assertEqual(str(stack), "Top-> 3 2 1")

        # test is_empty()
        self.assertFalse(stack.is_empty())

        # test peek()
        self.assertEqual(3, stack.peek())

        # test pop()
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())

        self.assertTrue(stack.is_empty())

class TestOrderedStack(unittest.TestCase):
    def test_OrderedStack(self):
        stack = OrderedStack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        stack.push(4)
        stack.push(3)
        stack.push(6)
        "bottom - > 1 3 4 6 "
        self.assertEqual(6, stack.pop())
        self.assertEqual(4, stack.peek())
        self.assertEqual(3, stack.size())


if __name__ == "__main__":
    unittest.main()
