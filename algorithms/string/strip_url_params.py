"""
Strip URL Parameters

Remove duplicate query string parameters from a URL and optionally remove
specified parameters. Three approaches of increasing Pythonic style.

Reference: https://en.wikipedia.org/wiki/Query_string

Complexity:
    Time:  O(n) where n is the length of the URL
    Space: O(n)
"""

from __future__ import annotations

import urllib
import urllib.parse
from collections import defaultdict


def strip_url_params1(
    url: str, params_to_strip: list[str] | None = None
) -> str:
    """Remove duplicate and specified URL parameters using manual parsing.

    Args:
        url: The URL string to process.
        params_to_strip: Optional list of parameter names to remove.

    Returns:
        The URL with duplicate and specified parameters removed.

    Examples:
        >>> strip_url_params1("www.saadbenn.com?a=1&b=2&a=2")
        'www.saadbenn.com?a=1&b=2'
    """
    if not params_to_strip:
        params_to_strip = []
    if url:
        result = ''
        tokens = url.split('?')
        domain = tokens[0]
        query_string = tokens[-1]
        result += domain
        if len(tokens) > 1:
            result += '?'
        if not query_string:
            return url
        else:
            key_value_pairs: list[str] = []
            fragment = ''
            for char in query_string:
                if char.isdigit():
                    key_value_pairs.append(fragment + char)
                    fragment = ''
                else:
                    fragment += char
            seen: dict[str, int] = defaultdict(int)
            for pair in key_value_pairs:
                token_parts = pair.split('=')
                if token_parts[0]:
                    length = len(token_parts[0])
                    if length == 1:
                        if token_parts and (token_parts[0] not in seen):
                            if params_to_strip:
                                if token_parts[0] != params_to_strip[0]:
                                    seen[token_parts[0]] = token_parts[1]
                                    result = (
                                        result + token_parts[0]
                                        + '=' + token_parts[1]
                                    )
                            else:
                                if token_parts[0] not in seen:
                                    seen[token_parts[0]] = token_parts[1]
                                    result = (
                                        result + token_parts[0]
                                        + '=' + token_parts[1]
                                    )
                    else:
                        check = token_parts[0]
                        letter = check[1]
                        if token_parts and (letter not in seen):
                            if params_to_strip:
                                if letter != params_to_strip[0]:
                                    seen[letter] = token_parts[1]
                                    result = (
                                        result + token_parts[0]
                                        + '=' + token_parts[1]
                                    )
                            else:
                                if letter not in seen:
                                    seen[letter] = token_parts[1]
                                    result = (
                                        result + token_parts[0]
                                        + '=' + token_parts[1]
                                    )
    return result


def strip_url_params2(
    url: str, param_to_strip: list[str] | None = None
) -> str:
    """Remove duplicate and specified URL parameters using list operations.

    Args:
        url: The URL string to process.
        param_to_strip: Optional list of parameter names to remove.

    Returns:
        The URL with duplicate and specified parameters removed.

    Examples:
        >>> strip_url_params2("www.saadbenn.com?a=1&b=2&a=2")
        'www.saadbenn.com?a=1&b=2'
    """
    if param_to_strip is None:
        param_to_strip = []
    if '?' not in url:
        return url

    queries = (url.split('?')[1]).split('&')
    query_keys = [query[0] for query in queries]
    for index in range(len(query_keys) - 1, 0, -1):
        if (
            query_keys[index] in param_to_strip
            or query_keys[index] in query_keys[0:index]
        ):
            queries.pop(index)

    return url.split('?')[0] + '?' + '&'.join(queries)


def strip_url_params3(
    url: str, strip: list[str] | None = None
) -> str:
    """Remove duplicate and specified URL parameters using urllib.

    Args:
        url: The URL string to process.
        strip: Optional list of parameter names to remove.

    Returns:
        The URL with duplicate and specified parameters removed.

    Examples:
        >>> strip_url_params3("www.saadbenn.com?a=1&b=2&a=2")
        'www.saadbenn.com?a=1&b=2'
    """
    if not strip:
        strip = []

    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)

    query = {key: values[0] for key, values in query.items() if key not in strip}
    query_string = urllib.parse.urlencode(query)
    new_parsed = parsed._replace(query=query_string)

    return new_parsed.geturl()
