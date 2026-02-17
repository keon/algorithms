"""Collection of search algorithms: finding the needle in a haystack."""

from algorithms.search.binary_search import binary_search, binary_search_recur
from algorithms.search.find_min_rotate import find_min_rotate, find_min_rotate_recur
from algorithms.search.first_occurrence import first_occurrence
from algorithms.search.generalized_binary_search import binary_search_first_true
from algorithms.search.interpolation_search import interpolation_search
from algorithms.search.jump_search import jump_search
from algorithms.search.last_occurrence import last_occurrence
from algorithms.search.linear_search import linear_search
from algorithms.search.next_greatest_letter import (
    next_greatest_letter,
    next_greatest_letter_v1,
    next_greatest_letter_v2,
)
from algorithms.search.search_insert import search_insert
from algorithms.search.search_range import search_range
from algorithms.search.search_rotate import search_rotate, search_rotate_recur
from algorithms.search.ternary_search import ternary_search
from algorithms.search.two_sum import two_sum, two_sum1, two_sum2

__all__ = [
    "binary_search",
    "binary_search_first_true",
    "binary_search_recur",
    "find_min_rotate",
    "find_min_rotate_recur",
    "first_occurrence",
    "interpolation_search",
    "jump_search",
    "last_occurrence",
    "linear_search",
    "next_greatest_letter",
    "next_greatest_letter_v1",
    "next_greatest_letter_v2",
    "search_insert",
    "search_range",
    "search_rotate",
    "search_rotate_recur",
    "ternary_search",
    "two_sum",
    "two_sum1",
    "two_sum2",
]
