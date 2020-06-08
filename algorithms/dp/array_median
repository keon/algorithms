import sys

# Part of Cosmos by OpenGenus Foundation


def median(nums):
    """
        Calculates the median of a list of numbers.
        import median from statistics in python 3.4 and above.
    """
    sorted_nums = sorted(nums)
    len_nums = len(nums)
    odd = len_nums % 2

    # If the length is odd, the median is the middle value of the sorted list.
    if odd:
        return sorted_nums[(len_nums - 1) // 2]

    # Otherwise it's the average of the middle two.
    return (nums[len_nums // 2] + nums[(len_nums // 2) - 1]) / 2


def main():
    """Calculates median of numbers in stdin."""
    # Read stdin until EOF
    nums_string = sys.stdin.read()

    # Split on whitespace
    num_strings = nums_string.split()

    # Make a new list of floats of all the non-whitespace values.
    nums = [float(i) for i in num_strings if i]

    # Print median
    if not nums:
        print("You didn't enter any numbers.")
    else:
        print(median(nums))


def test_median():
    """Test the median function for correctness."""
    assert median([1, 2, 3]) == 2
    assert median([1, 2.9, 3]) == 2.9
    assert median([1, 2, 3, 4]) == 2.5
    assert median([2, 1, 4, 3]) == 2.5
    assert median([1, 3, 3, 4, 5, 6, 8, 9]) == 4.5


def test_main():
    """Test the main function for correctness."""
    # Backup stdin.read
    _stdin_read = sys.stdin.read

    # patch main's print
    def print_patch(arg):
        assert arg == 5.5

    main.__globals__["print"] = print_patch

    # patch main's stdin
    class stdin_patch:
        def read(self):
            return "1 2 3 4 5.5 6 7 8 9\n"

    main.__globals__["sys"].stdin = stdin_patch()

    # invoke main with mocks
    main()

    # undo patches
    main.__globals__["sys"].stdin.read = _stdin_read
    del main.__globals__["print"]


if __name__ == "__main__":
    test_median()
    #    test_main()
    main()
