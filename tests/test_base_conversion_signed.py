"""Check that signed encodings can be decoded in every supported base."""

import pytest

from algorithms.math.base_conversion import base_to_int, int_to_base


@pytest.mark.parametrize("base", range(2, 37))
def test_signed_conversion_matches_builtin(base):
    """Use int as an independent oracle for positive and negative outputs."""
    for number in [-2**128, -255, -31, -1, 0, 1, 31, 255, 2**128]:
        encoded = int_to_base(number, base)
        assert int(encoded, base) == number
        assert base_to_int(encoded, base) == number


@pytest.mark.parametrize(
    "encoded,base,expected",
    [("-101", 2, -5), ("-FF", 16, -255), ("-Z", 36, -35), ("-0", 10, 0)],
)
def test_decode_negative_literal(encoded, base, expected):
    """Decoding also works on literals not produced by the encoder."""
    assert base_to_int(encoded, base) == expected


@pytest.mark.parametrize("encoded", ["", "-"])
def test_missing_digits_are_rejected(encoded):
    """Neither an empty string nor a sign alone represents zero."""
    with pytest.raises(ValueError, match="at least one digit"):
        base_to_int(encoded, 16)
