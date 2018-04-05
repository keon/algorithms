"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

import unittest


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(left: Node, right: Node) -> Node:
    head = Node(0)
    current = head
    sum = 0
    while left or right:
        print("adding: ", left.val, right.val)
        sum //= 10
        if left:
            sum += left.val
            left = left.next
        if right:
            sum += right.val
            right = right.next
        current.next = Node(sum % 10)
        current = current.next
    if sum // 10 == 1:
        current.next = Node(1)
    return head.next


def convert_to_list(number: int) -> Node:
    """
        converts a positive integer into a (reversed) linked list.
        for example: give 112
        result 2 -> 1 -> 1
    """
    if number >= 0:
        head = Node(0)
        current = head
        remainder = number % 10
        quotient = number // 10

        while quotient != 0:
            current.next = Node(remainder)
            current = current.next
            remainder = quotient % 10
            quotient //= 10
        current.next = Node(remainder)
        return head.next
    else:
        print("number must be positive!")


def convert_to_str(l: Node) -> str:
    """
        converts the non-negative number list into a string.
    """
    result = ""
    while l:
        result += str(l.val)
        l = l.next
    return result


class TestSuite(unittest.TestCase):
    """
        testsuite for the linked list structure and
        the adding function, above.
    """

    def test_convert_to_str(self):
        number1 = Node(2)
        number1.next = Node(4)
        number1.next.next = Node(3)
        self.assertEqual("243", convert_to_str(number1))

    def test_add_two_numbers(self):
        # 1. test case
        number1 = Node(2)
        number1.next = Node(4)
        number1.next.next = Node(3)
        number2 = Node(5)
        number2.next = Node(6)
        number2.next.next = Node(4)
        result = convert_to_str(add_two_numbers(number1, number2))
        self.assertEqual("708", result)

        # 2. test case
        number3 = Node(1)
        number3.next = Node(1)
        number3.next.next = Node(9)
        number4 = Node(1)
        number4.next = Node(0)
        number4.next.next = Node(1)
        result = convert_to_str(add_two_numbers(number3, number4))
        self.assertEqual("2101", result)

        # 3. test case
        number5 = Node(1)
        number6 = Node(0)
        result = convert_to_str(add_two_numbers(number5, number6))
        self.assertEqual("1", result)

        # 4. test case
        number7 = Node(9)
        number7.next = Node(1)
        number7.next.next = Node(1)
        number8 = Node(1)
        number8.next = Node(0)
        number8.next.next = Node(1)
        result = convert_to_str(add_two_numbers(number7, number8))
        self.assertEqual("022", result)

    def test_convert_to_list(self):
        result = convert_to_str(convert_to_list(112))
        self.assertEqual("211", result)


if __name__ == "__main__":
    unittest.main()
