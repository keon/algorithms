'''
radix sort
complexity: O(nk) . n is the size of input list and k is the digit length of the number
'''
def radix_sort(arr):
    is_done = False
    position = 1

    while not is_done:
        queue_list = [list() for _ in range(10)]
        is_done = True

        for num in arr:
            digit_number = (int)(num/position)%10
            queue_list[digit_number].append(num)
            if is_done and digit_number > 0:
                is_done = False

        index = 0
        for numbers in queue_list:
            for num in numbers:
                arr[index] = num
                index += 1

        position *= 10
