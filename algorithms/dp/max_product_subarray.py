"""
Maximum Product Subarray

Find the contiguous subarray within an array that has the largest product.

Reference: https://leetcode.com/problems/maximum-product-subarray/

Complexity:
    max_product:
        Time:  O(n)
        Space: O(1)
    subarray_with_max_product:
        Time:  O(n)
        Space: O(1)
"""

from __future__ import annotations

from functools import reduce


def max_product(nums: list[int]) -> int:
    """Find the maximum product of a contiguous subarray.

    Args:
        nums: List of integers (containing at least one number).

    Returns:
        Largest product among all contiguous subarrays.

    Examples:
        >>> max_product([2, 3, -2, 4])
        6
    """
    lmin = lmax = gmax = nums[0]
    for num in nums[1:]:
        t_1 = num * lmax
        t_2 = num * lmin
        lmax = max(max(t_1, t_2), num)
        lmin = min(min(t_1, t_2), num)
        gmax = max(gmax, lmax)
    return gmax


def subarray_with_max_product(arr: list[int]) -> tuple[int, list[int]]:
    """Find the maximum product subarray and return the product and subarray.

    Args:
        arr: List of positive or negative integers.

    Returns:
        A tuple of (max_product, subarray) where subarray is the contiguous
        slice that achieves the maximum product.

    Examples:
        >>> subarray_with_max_product([-2, -3, 6, 0, -7, -5])
        (36, [-2, -3, 6])
    """
    length = len(arr)
    product_so_far = max_product_end = 1
    max_start_i = 0
    so_far_start_i = so_far_end_i = 0
    all_negative_flag = True

    for i in range(length):
        max_product_end *= arr[i]
        if arr[i] > 0:
            all_negative_flag = False

        if max_product_end <= 0:
            max_product_end = arr[i]
            max_start_i = i

        if product_so_far <= max_product_end:
            product_so_far = max_product_end
            so_far_end_i = i
            so_far_start_i = max_start_i

    if all_negative_flag:
        product = reduce(lambda x, y: x * y, arr)
        return product, arr

    return product_so_far, arr[so_far_start_i:so_far_end_i + 1]
