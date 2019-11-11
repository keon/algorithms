"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

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
    mx = max(sequence)
    tree = [0] * (mx<<2)

    def update(p, l, r, i, v):
        if l == r:
            tree[p] = v
            return
        mid = (l+r)>>1
        if i <= mid:
            update(p<<1, l, mid, i, v)
        else:
            update((p<<1)|1, mid+1, r, i, v)
        tree[p] = max(tree[p<<1], tree[(p<<1)|1])

    def get_max(p, l, r, s, e):
        if l > e or r < s:
            return 0
        if l >= s and r <= e:
            return tree[p]
        mid = (l+r)>>1
        return max(get_max(p<<1, l, mid, s, e), get_max((p<<1)|1, mid+1, r, s, e))
    ans = 0
    for x in sequence:
       cur = get_max(1, 0, mx, 0, x-1)+1
       ans = max(ans, cur)
       update(1, 0, mx, x, cur)
    return ans

def longest_increasing_subsequence_optimized2(sequence):
    """
    Optimized dynamic programming algorithm for
    counting the length of the longest increasing subsequence
    using segment tree data structure to achieve better complexity
    type sequence: list[int]
    rtype: int
    """
    n = len(sequence)
    tree = [0] * (n<<2)
    sorted_seq = sorted((x, -i) for i, x in enumerate(sequence))
    def update(p, l, r, i, v):
        if l ==r:
            tree[p] = v
            return
        mid = (l+r)>>1
        if i <= mid:
            update(p<<1, l, mid, i, v)
        else:
            update((p<<1)|1, mid+1, r, i, v)
        tree[p] = max(tree[p<<1], tree[(p<<1)|1])

    def get_max(p, l, r, s, e):
        if l > e or r < s:
            return 0
        if l >= s and r <= e:
            return tree[p]
        mid = (l+r)>>1
        return max(get_max(p<<1, l, mid, s, e), get_max((p<<1)|1, mid+1, r, s, e))
    ans = 0
    for x, j in sorted_seq:
        i = -j
        cur = get_max(1, 0, n-1, 0, i-1)+1
        ans = max(ans, cur)
        update(1, 0, n-1, i, cur)
    return ans 

