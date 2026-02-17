"""Stack-based algorithm implementations."""

from __future__ import annotations

from algorithms.data_structures.stack import AbstractStack, ArrayStack, LinkedListStack, StackNode

from .is_consecutive import first_is_consecutive, second_is_consecutive
from .is_sorted import is_sorted
from .longest_abs_path import length_longest_path
from .ordered_stack import OrderedStack
from .remove_min import remove_min
from .simplify_path import simplify_path
from .stutter import first_stutter, second_stutter
from .switch_pairs import first_switch_pairs, second_switch_pairs
from .valid_parenthesis import is_valid

__all__ = [
    "AbstractStack",
    "ArrayStack",
    "LinkedListStack",
    "OrderedStack",
    "StackNode",
    "first_is_consecutive",
    "first_stutter",
    "first_switch_pairs",
    "is_sorted",
    "is_valid",
    "length_longest_path",
    "remove_min",
    "second_is_consecutive",
    "second_stutter",
    "second_switch_pairs",
    "simplify_path",
]
