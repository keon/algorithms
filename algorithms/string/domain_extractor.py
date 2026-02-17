"""
Domain Name Extractor

Given a URL as a string, parse out just the domain name and return it.
Uses only the .split() built-in function without regex or urlparse.

Reference: https://en.wikipedia.org/wiki/Domain_name

Complexity:
    Time:  O(n) where n is the length of the URL
    Space: O(n)
"""

from __future__ import annotations


def domain_name_1(url: str) -> str:
    """Extract the domain name from a URL by splitting on protocol and dots.

    Args:
        url: The full URL string.

    Returns:
        The domain name extracted from the URL.

    Examples:
        >>> domain_name_1("https://github.com/SaadBenn")
        'github'
    """
    full_domain_name = url.split("//")[-1]
    actual_domain = full_domain_name.split(".")
    if len(actual_domain) > 2:
        return actual_domain[1]
    return actual_domain[0]


def domain_name_2(url: str) -> str:
    """Extract the domain name from a URL using chained splits.

    Args:
        url: The full URL string.

    Returns:
        The domain name extracted from the URL.

    Examples:
        >>> domain_name_2("http://google.com")
        'google'
    """
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
