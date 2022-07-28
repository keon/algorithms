import random


def quick_sort(arr, simulation=False, randomized=False):
    """ Quick sort
        Complexity: best O(n log(n)) avg O(n log(n)), worst O(N^2)
    """

    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)
    arr, _ = quick_sort_recur(
        arr, 0, len(arr) - 1,
        iteration, simulation, randomized,
    )
    return arr


def quick_sort_recur(arr, first, last, iteration, simulation, randomized):
    if first < last:
        if randomized:
            pos = randomized_partition(arr, first, last)
        else:
            pos = partition(arr, first, last)
        # Start our two recursive calls
        if simulation:
            iteration = iteration + 1
            print("iteration", iteration, ":", *arr)

        _, iteration = quick_sort_recur(
            arr, first, pos - 1,
            iteration, simulation, randomized,
        )
        _, iteration = quick_sort_recur(
            arr, pos + 1, last,
            iteration, simulation, randomized,
        )

    return arr, iteration


def randomized_partition(arr, first, last):
    index = random.randint(first, last)
    arr[last], arr[index] = arr[index], arr[last]
    return partition(arr, first, last)


def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]:  # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    return wall


if __name__ == "__main__":
    quick_sort([1, 3, 4, 2, 5, 6, 3, 1], simulation=True, randomized=True)
