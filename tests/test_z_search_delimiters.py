"""Check pattern matching when text contains the Z-search separator."""

from itertools import product

import pytest

from algorithms.string.z_algorithm import z_search


@pytest.mark.parametrize(
    "text,pattern,expected",
    [
        ("$$$", "$", [0, 1, 2]),
        ("$$$$", "$$", [0, 1, 2]),
        ("a$a$a", "a", [0, 2, 4]),
        ("$a$a$", "$a", [0, 2]),
        ("a$$a$$", "a$", [0, 3]),
        ("a$a", "$$", []),
        ("$", "$$", []),
        ("λ$λ$", "λ$", [0, 2]),
    ],
)
def test_literal_dollars(text, pattern, expected):
    """Dollar signs in either argument are ordinary matching characters."""
    assert z_search(text, pattern) == expected


def test_short_strings_match_startswith_oracle():
    """Exhaustively compare overlapping matches with Python's string API."""
    texts = [
        "".join(chars)
        for length in range(6)
        for chars in product("a$", repeat=length)
    ]
    patterns = [
        "".join(chars)
        for length in range(1, 4)
        for chars in product("a$", repeat=length)
    ]
    for text in texts:
        for pattern in patterns:
            expected = [
                index
                for index in range(len(text))
                if text.startswith(pattern, index)
            ]
            assert z_search(text, pattern) == expected, (text, pattern)


@pytest.mark.parametrize("text,pattern", [("", "$"), ("$", ""), ("", "")])
def test_empty_input_contract(text, pattern):
    """Preserve the existing no-match convention for empty arguments."""
    assert z_search(text, pattern) == []
