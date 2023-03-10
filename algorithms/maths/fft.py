"""
Implementation of the Cooley-Tukey, which is the most common FFT algorithm.

Input: an array of complex values which has a size of N, where N is an integer power of 2
Output: an array of complex values which is the discrete fourier transform of the input

Example 1
Input: [2.0+2j, 1.0+3j, 3.0+1j, 2.0+2j]
Output: [8+8j, 2j, 2-2j, -2+0j]


Pseudocode: https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm
"""
from cmath import exp, pi

def fft(x):
    """ Recursive implementation of the Cooley-Tukey"""
    N = len(x)
    if N == 1:
        return x

    # get the elements at even/odd indices
    even = fft(x[0::2])
    odd = fft(x[1::2])

    y = [0 for i in range(N)]
    for k in range(N//2):
        q = exp(-2j*pi*k/N)*odd[k]
        y[k] = even[k] + q
        y[k + N//2] = even[k] - q

    return y
