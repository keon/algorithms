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


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(left:"Node", right:"Node")->"Node":
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


if __name__ == "__main__":
    left = Node(2)
    left.next = Node(4)
    left.next.next = Node(3)

    right = Node(5)
    right.next = Node(6)
    right.next.next = Node(4)

    res = add_two_numbers(left, right)
    while res:
        print(res.val)
        res = res.next
