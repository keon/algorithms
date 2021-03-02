def solve_chinese_remainder(num : list[int], rem : list[int]):
    """
    Computes the smallest x that satisfies the chinese remainder theorem
    """
    k = len(num)
    if not len(num) == len(rem):
        raise Exception("num and rem should have equal length")
    x = 1
    while True:
        i = 0
        while i < k:
            if x % num[i] != rem[i]:
                break
            i += 1
        if i == k:
            return x
        else:
            x += 1