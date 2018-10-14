"""
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
from collections import defaultdict
from unittest import TestCase


class RandomListNode(object):
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None


class Solution0:
    def copy_random_list(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = dict()
        m = n = head
        while m:
            dic[m] = RandomListNode(m.label)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)


#
#
class Solution1:  # O(n)
    def copy_random_list(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        copy = defaultdict(lambda: RandomListNode(0))
        copy[None] = None
        node = head
        while node:
            copy[node].label = node.label
            copy[node].next = copy[node.next]
            copy[node].random = copy[node.random]
            node = node.next
        return copy[head]


class TestSuite(TestCase):
    """
        The test creates a simple structure and navigates through the elements to
        verify the copy is valid.
    """
    def setUp(self):
        self.node1 = RandomListNode(1)
        node2 = RandomListNode(2)
        node3 = RandomListNode(3)
        node4 = RandomListNode(4)
        node5 = RandomListNode(5)

        self.node1.next, self.node1.random = node2, node4
        node2.next, node2.random = node3, node5
        node3.next, node3.random = node4, node2
        node4.next = node5
        node5.random = node3

    def test_solution_0(self):
        s0 = Solution0()
        result = s0.copy_random_list(self.node1)
        self._assert_is_a_copy(result)

    def test_solution_1(self):
        s1 = Solution1()
        result = s1.copy_random_list(self.node1)
        self._assert_is_a_copy(result)

    def _assert_is_a_copy(self, result):
        self.assertEqual(5, result.next.next.next.next.label)
        self.assertEqual(4, result.next.next.next.label)
        self.assertEqual(3, result.next.next.label)
        self.assertEqual(2, result.next.label)
        self.assertEqual(1, result.label)
        self.assertEqual(3, result.next.next.next.next.random.label)
        self.assertIsNone(result.next.next.next.random)
        self.assertEqual(2, result.next.next.random.label)
        self.assertEqual(5, result.next.random.label)
        self.assertEqual(4, result.random.label)
