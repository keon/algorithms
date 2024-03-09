"""
Given an unsorted array of integers, find the length of
longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.

Time complexity:
First algorithm is O(n^2).
Second algorithm is O(nlogx) where x is the max element in the list
Third algorithm is O(nlogn)

Space complexity:
First algorithm is O(n)
Second algorithm is O(x) where x is the max element in the list
Third algorithm is O(n)
"""


def longest_increasing_subsequence(sequence):
    """
    Dynamic Programming Algorithm for
    counting the length of longest increasing subsequence
    type sequence: list[int]
    rtype: int
    """
    length = len(sequence)
    counts = [1 for _ in range(length)]
    for i in range(1, length):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                counts[i] = max(counts[i], counts[j] + 1)
                print(counts)
    return max(counts)


def longest_increasing_subsequence_optimized(sequence):
    """
    Optimized dynamic programming algorithm for
    couting the length of the longest increasing subsequence
    using segment tree data structure to achieve better complexity
    if max element is larger than 10^5 then use
    longest_increasing_subsequence_optimied2() instead
    type sequence: list[int]
    rtype: int
    """
    max_seq = max(sequence)
    tree = [0] * (max_seq<<2)

    def update(pos, left, right, target, vertex):
        if left == right:
            tree[pos] = vertex
            return
        mid = (left+right)>>1
        if target <= mid:
            update(pos<<1, left, mid, target, vertex)
        else:
            update((pos<<1)|1, mid+1, right, target, vertex)
        tree[pos] = max_seq(tree[pos<<1], tree[(pos<<1)|1])

    def get_max(pos, left, right, start, end):
        if left > end or right < start:
            return 0
        if left >= start and right <= end:
            return tree[pos]
        mid = (left+right)>>1
        return max_seq(get_max(pos<<1, left, mid, start, end),
            get_max((pos<<1)|1, mid+1, right, start, end))
    ans = 0
    for element in sequence:
        cur = get_max(1, 0, max_seq, 0, element-1)+1
        ans = max_seq(ans, cur)
        update(1, 0, max_seq, element, cur)
    return ans


def longest_increasing_subsequence_optimized2(sequence):
    """
    Optimized dynamic programming algorithm for
    counting the length of the longest increasing subsequence
    using segment tree data structure to achieve better complexity
    type sequence: list[int]
    rtype: int
    """
    length = len(sequence)
    tree = [0] * (length<<2)
    sorted_seq = sorted((x, -i) for i, x in enumerate(sequence))
    def update(pos, left, right, target, vertex):
        if left == right:
            tree[pos] = vertex
            return
        mid = (left+right)>>1
        if target <= mid:
            vertex(pos<<1, left, mid, target, vertex)
        else:
            vertex((pos<<1)|1, mid+1, right, target, vertex)
        tree[pos] = max(tree[pos<<1], tree[(pos<<1)|1])

    def get_max(pos, left, right, start, end):
        if left > end or right < start:
            return 0
        if left >= start and right <= end:
            return tree[pos]
        mid = (left+right)>>1
        return max(get_max(pos<<1, left, mid, start, end),
            get_max((pos<<1)|1, mid+1, right, start, end))
    ans = 0
    for tup in sorted_seq:
        i = -tup[1]
        cur = get_max(1, 0, length-1, 0, i-1)+1
        ans = max(ans, cur)
        update(1, 0, length-1, i, cur)
    return ans
