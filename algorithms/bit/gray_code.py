"""
Gray Code Generator

Gray code is a binary numeral system where two successive values differ by only one bit. This function generates a sequence of n-bit Gray codes, where n is the number of bits.
"""


def gray_code(n):
    """
    Generate the sequence of n-bit Gray code.

    :param n: Number of bits for the Gray code
    :return: List of Gray code sequence in decimal representation
    """
    if n == 0:
        return [0]

    # Recursive step: generate (n-1)-bit Gray code
    previous_gray = gray_code(n - 1)

    # Mirror the previous Gray code
    new_gray = [(1 << (n - 1)) | i for i in reversed(previous_gray)]

    # Concatenate the old and new mirrored Gray code
    return previous_gray + new_gray
