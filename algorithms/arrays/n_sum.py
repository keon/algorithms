"""
Given an array of n integers, are there elements a, b, .. , n in nums
such that a + b + .. + n = target?

Find all unique triplets in the array which gives the sum of target.

Example:
    basic:
        Given:
            n = 4, nums = [1, 0, -1, 0, -2, 2], target = 0,
        return [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    advanced:
        Given:
            n = 2
            nums = [[-3, 0], [-2, 1], [2, 2], [3, 3], [8, 4], [-9, 5]]
            taget = -5
            def sum(a, b):
                return [a[0] + b[1], a[1] + b[0]]
            def compare(num, taget):
                if num[0] < taget:
                    return -1
                elif if num[0] > taget:
                    return 1
                else:
                    return 0
        return [[-9, 5], [8, 4]]
        because -9 + 4 = -5
"""


def n_sum(n, nums, target, **kv):

    def __sum_closure_default(a, b):
        return a + b

    def __compare_closure_default(num, taget):
        if num < taget:
            return -1
        elif num > taget:
            return 1
        else:
            return 0

    def __same_closure_default(a, b):
        return a == b

    def __n_sum(n, nums, target):
        if n == 2:
            results = __two_sum(nums, target)
        else:
            results = set()
            prev_num = None
            for index, num in enumerate(nums):
                if prev_num is not None and \
                    __same_closure(prev_num, num):
                    continue
                prev_num = num
                n_minus1_results = __n_sum(n - 1,
                                           nums[index + 1:],
                                           target - num)
                n_minus1_results = __append_num_to_each_tuple(num,
                                                              n_minus1_results)
                results = results.union(n_minus1_results)
        return __convert_type(results)


    def __two_sum(nums, target):
        nums.sort()
        lt = 0
        rt = len(nums) - 1
        results = set()
        while lt < rt:
            sum_ = __sum_closure(nums[lt], nums[rt])
            flag = __compare_closure(sum_, target)
            if flag == -1:
                lt += 1
            elif flag == 1:
                rt -= 1
            else:
                results.add((nums[lt], nums[rt], ))
                lt += 1
                rt -= 1
                while (lt < len(nums) and
                       __same_closure(nums[lt - 1], nums[lt])):
                    lt += 1
                while (0 <= rt and
                       __same_closure(nums[rt], nums[rt + 1])):
                    rt -= 1
        return results


    def __append_num_to_each_tuple(num, tps):
        results = set()
        for tp in tps:
            tp += (num, )
            tp = tuple(sorted(list(tp)))
            results.add(tp)
        return results


    def __convert_type(results_set):
        results = []
        for result in results_set:
            results.append(sorted(list(result)))
        return sorted(results)

    __sum_closure = kv.get('sum_closure', __sum_closure_default)
    __same_closure = kv.get('same_closure', __same_closure_default)
    __compare_closure = kv.get('compare_closure', __compare_closure_default)
    nums.sort()
    return __n_sum(n, nums, target)
