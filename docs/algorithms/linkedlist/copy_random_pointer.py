"""
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
from collections import defaultdict


class RandomListNode(object):
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None


def copy_random_pointer_v1(head):
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


# O(n)
def copy_random_pointer_v2(head):
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
