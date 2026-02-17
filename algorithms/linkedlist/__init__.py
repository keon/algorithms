"""Linked list algorithm implementations."""

from algorithms.linkedlist.add_two_numbers import (
    add_two_numbers,
    convert_to_list,
    convert_to_str,
)
from algorithms.linkedlist.copy_random_pointer import (
    RandomListNode,
    copy_random_pointer_v1,
    copy_random_pointer_v2,
)
from algorithms.linkedlist.delete_node import delete_node
from algorithms.linkedlist.first_cyclic_node import first_cyclic_node
from algorithms.linkedlist.intersection import intersection
from algorithms.linkedlist.is_cyclic import is_cyclic
from algorithms.linkedlist.is_palindrome import (
    is_palindrome,
    is_palindrome_dict,
    is_palindrome_stack,
)
from algorithms.linkedlist.is_sorted import is_sorted
from algorithms.linkedlist.kth_to_last import (
    kth_to_last,
    kth_to_last_dict,
    kth_to_last_eval,
)
from algorithms.data_structures.linked_list import (
    DoublyLinkedListNode,
    SinglyLinkedListNode,
)
from algorithms.linkedlist.merge_two_list import (
    merge_two_list,
    merge_two_list_recur,
)
from algorithms.linkedlist.partition import partition
from algorithms.linkedlist.remove_duplicates import (
    remove_dups,
    remove_dups_wothout_set,
)
from algorithms.linkedlist.remove_range import remove_range
from algorithms.linkedlist.reverse import (
    reverse_list,
    reverse_list_recursive,
)
from algorithms.linkedlist.rotate_list import rotate_right
from algorithms.linkedlist.swap_in_pairs import swap_pairs

__all__ = [
    "add_two_numbers",
    "convert_to_list",
    "convert_to_str",
    "RandomListNode",
    "copy_random_pointer_v1",
    "copy_random_pointer_v2",
    "delete_node",
    "first_cyclic_node",
    "intersection",
    "is_cyclic",
    "is_palindrome",
    "is_palindrome_dict",
    "is_palindrome_stack",
    "is_sorted",
    "kth_to_last",
    "kth_to_last_dict",
    "kth_to_last_eval",
    "DoublyLinkedListNode",
    "SinglyLinkedListNode",
    "merge_two_list",
    "merge_two_list_recur",
    "partition",
    "remove_dups",
    "remove_dups_wothout_set",
    "remove_range",
    "reverse_list",
    "reverse_list_recursive",
    "rotate_right",
    "swap_pairs",
]
