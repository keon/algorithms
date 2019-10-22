"""
Histogram function.

Histogram is an accurate representation of the distribution of numerical data.
It is an estimate of the probability distribution of a continuous variable.
https://en.wikipedia.org/wiki/Histogram

Example:
    list_1 = [3, 3, 2, 1]
    :return {1: 1, 2: 1, 3: 2}

    list_2 = [2, 3, 5, 5, 5, 6, 4, 3, 7]
    :return {2: 1, 3: 2, 4: 1, 5: 3, 6: 1, 7: 1}
"""


def get_histogram(input_list: list) -> dict:
    """
    Get histogram representation
    :param input_list: list with different and unordered values
    :return histogram: dict with histogram of input_list
    """
    # Create dict to store histogram
    histogram = {}
    # For each list value, add one to the respective histogram dict position
    for i in input_list:
        histogram[i] = histogram.get(i, 0) + 1
    return histogram
