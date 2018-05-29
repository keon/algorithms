"""
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
# from collections import defaultdict

# TODO: This requires to be rewritten -- commenting it out for now
# class Solution0:
  # @param head, a RandomListNode
  # @return a RandomListNode
  # def copyRandomList(self, head):
  #   dic = dict()
  #   m = n = head
  #   while m:
  #       dic[m] = RandomListNode(m.label)
  #       m = m.next
  #   while n:
  #       dic[n].next = dic.get(n.next)
  #       dic[n].random = dic.get(n.random)
  #       n = n.next
  #   return dic.get(head)
#
#
# class Solution1:  # O(n)
#   @param head, a RandomListNode
#   @return a RandomListNode
  # def copyRandomList(self, head):
  #   copy = defaultdict(lambda: RandomListNode(0))
  #   copy[None] = None
  #   node = head
  #   while node:
  #       copy[node].label = node.label
  #       copy[node].next = copy[node.next]
  #       copy[node].random = copy[node.random]
  #       node = node.next
  #   return copy[head]
