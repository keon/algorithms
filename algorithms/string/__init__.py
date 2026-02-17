"""String algorithms package."""

from __future__ import annotations

from algorithms.string.add_binary import add_binary
from algorithms.string.atbash_cipher import atbash
from algorithms.string.breaking_bad import bracket, match_symbol, match_symbol_1
from algorithms.string.caesar_cipher import caesar_cipher
from algorithms.string.check_pangram import check_pangram
from algorithms.string.contain_string import contain_string
from algorithms.string.count_binary_substring import count_binary_substring
from algorithms.string.decode_string import decode_string
from algorithms.string.delete_reoccurring import delete_reoccurring_characters
from algorithms.string.domain_extractor import domain_name_1, domain_name_2
from algorithms.string.encode_decode import decode, encode
from algorithms.string.first_unique_char import first_unique_char
from algorithms.string import fizzbuzz
from algorithms.string.fizzbuzz import fizzbuzz_with_helper_func
from algorithms.string.group_anagrams import group_anagrams
from algorithms.string.int_to_roman import int_to_roman
from algorithms.string.is_palindrome import (
    is_palindrome,
    is_palindrome_deque,
    is_palindrome_reverse,
    is_palindrome_stack,
    is_palindrome_two_pointer,
)
from algorithms.string.is_rotated import is_rotated, is_rotated_v1
from algorithms.string.judge_circle import judge_circle
from algorithms.string.knuth_morris_pratt import knuth_morris_pratt
from algorithms.string.license_number import license_number
from algorithms.string.longest_common_prefix import (
    longest_common_prefix_v1,
    longest_common_prefix_v2,
    longest_common_prefix_v3,
)
from algorithms.string.longest_palindromic_substring import longest_palindrome
from algorithms.string.make_sentence import make_sentence
from algorithms.string.merge_string_checker import (
    is_merge_iterative,
    is_merge_recursive,
)
from algorithms.string.min_distance import min_distance, min_distance_dp
from algorithms.string.multiply_strings import multiply
from algorithms.string.one_edit_distance import is_one_edit, is_one_edit2
from algorithms.string.panagram import panagram
from algorithms.string.rabin_karp import rabin_karp, RollingHash
from algorithms.string.repeat_string import repeat_string
from algorithms.string.repeat_substring import repeat_substring
from algorithms.string.reverse_string import (
    iterative,
    pythonic,
    recursive,
    ultra_pythonic,
)
from algorithms.string.reverse_vowel import reverse_vowel
from algorithms.string.reverse_words import reverse_words
from algorithms.string.roman_to_int import roman_to_int
from algorithms.string.rotate import rotate, rotate_alt
from algorithms.string.strong_password import strong_password
from algorithms.string.strip_url_params import (
    strip_url_params1,
    strip_url_params2,
    strip_url_params3,
)
from algorithms.string.text_justification import text_justification
from algorithms.string.unique_morse import convert_morse_word, unique_morse
from algorithms.string.validate_coordinates import (
    is_valid_coordinates_0,
    is_valid_coordinates_1,
    is_valid_coordinates_regular_expression,
)
from algorithms.string.word_squares import word_squares

__all__ = [
    "add_binary",
    "atbash",
    "bracket",
    "caesar_cipher",
    "check_pangram",
    "contain_string",
    "convert_morse_word",
    "count_binary_substring",
    "decode",
    "decode_string",
    "delete_reoccurring_characters",
    "domain_name_1",
    "domain_name_2",
    "encode",
    "first_unique_char",
    "fizzbuzz",
    "fizzbuzz_with_helper_func",
    "group_anagrams",
    "int_to_roman",
    "is_merge_iterative",
    "is_merge_recursive",
    "is_one_edit",
    "is_one_edit2",
    "is_palindrome",
    "is_palindrome_deque",
    "is_palindrome_reverse",
    "is_palindrome_stack",
    "is_palindrome_two_pointer",
    "is_rotated",
    "is_rotated_v1",
    "is_valid_coordinates_0",
    "is_valid_coordinates_1",
    "is_valid_coordinates_regular_expression",
    "iterative",
    "judge_circle",
    "knuth_morris_pratt",
    "license_number",
    "longest_common_prefix_v1",
    "longest_common_prefix_v2",
    "longest_common_prefix_v3",
    "longest_palindrome",
    "make_sentence",
    "match_symbol",
    "match_symbol_1",
    "min_distance",
    "min_distance_dp",
    "multiply",
    "panagram",
    "pythonic",
    "rabin_karp",
    "recursive",
    "repeat_string",
    "repeat_substring",
    "reverse_vowel",
    "reverse_words",
    "RollingHash",
    "roman_to_int",
    "rotate",
    "rotate_alt",
    "strong_password",
    "strip_url_params1",
    "strip_url_params2",
    "strip_url_params3",
    "text_justification",
    "ultra_pythonic",
    "unique_morse",
    "word_squares",
]
