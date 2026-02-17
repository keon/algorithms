"""
Fast Fourier Transform (Cooley-Tukey)

Compute the Discrete Fourier Transform of a sequence using the Cooley-Tukey
radix-2 decimation-in-time algorithm. Input length must be a power of 2.

Reference: https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm

Complexity:
    Time:  O(n log n)
    Space: O(n log n)
"""

from __future__ import annotations

from cmath import exp, pi


def fft(x: list[complex]) -> list[complex]:
    """Compute the FFT of a sequence using the Cooley-Tukey algorithm.

    Args:
        x: Input array of complex values. Length must be a power of 2.

    Returns:
        The Discrete Fourier Transform of x.

    Examples:
        >>> fft([1.0, 1.0, 1.0, 1.0])
        [(4+0j), 0j, 0j, 0j]
    """
    n = len(x)
    if n == 1:
        return x

    even = fft(x[0::2])
    odd = fft(x[1::2])

    y = [0 for _ in range(n)]
    for k in range(n // 2):
        q = exp(-2j * pi * k / n) * odd[k]
        y[k] = even[k] + q
        y[k + n // 2] = even[k] - q

    return y
