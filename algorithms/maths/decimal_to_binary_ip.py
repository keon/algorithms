"""
Decimal to Binary IP Conversion

Convert an IP address from dotted-decimal notation to its binary
representation.

Reference: https://en.wikipedia.org/wiki/IP_address

Complexity:
    Time:  O(1) (fixed 4 octets, 8 bits each)
    Space: O(1)
"""

from __future__ import annotations


def decimal_to_binary_util(val: str) -> str:
    """Convert a single decimal octet (0-255) to an 8-bit binary string.

    Args:
        val: String representation of an octet value.

    Returns:
        8-character binary string.

    Examples:
        >>> decimal_to_binary_util('192')
        '11000000'
    """
    bits = [128, 64, 32, 16, 8, 4, 2, 1]
    val_int = int(val)
    binary_rep = ''
    for bit in bits:
        if val_int >= bit:
            binary_rep += str(1)
            val_int -= bit
        else:
            binary_rep += str(0)

    return binary_rep


def decimal_to_binary_ip(ip: str) -> str:
    """Convert a dotted-decimal IP address to binary representation.

    Args:
        ip: IP address in dotted-decimal format (e.g., '192.168.0.1').

    Returns:
        Binary representation with dot-separated octets.

    Examples:
        >>> decimal_to_binary_ip('192.168.0.1')
        '11000000.10101000.00000000.00000001'
    """
    values = ip.split('.')
    binary_list = []
    for val in values:
        binary_list.append(decimal_to_binary_util(val))
    return '.'.join(binary_list)
