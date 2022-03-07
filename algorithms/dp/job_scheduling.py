"""
Python program for weighted job scheduling using Dynamic
Programming and Binary Search
"""

class Job:
    """
    Class to represent a job
    """
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit  = profit

def binary_search(job, start_index):
    """
    A Binary Search based function to find the latest job
    (before current job) that doesn't conflict with current
    job.  "index" is index of the current job.  This function
    returns -1 if all jobs before index conflict with it.
    The array jobs[] is sorted in increasing order of finish
    time.
    """

    left = 0
    right = start_index - 1

    # Perform binary Search iteratively
    while left <= right:
        mid = (left + right) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                left = mid + 1
            else:
                return mid
        else:
            right = mid - 1
    return -1

def schedule(job):
    """
    The main function that returns the maximum possible
    profit from given array of jobs
    """

    # Sort jobs according to finish time
    job = sorted(job, key = lambda j: j.finish)

    # Create an array to store solutions of subproblems.  table[i]
    # stores the profit for jobs till arr[i] (including arr[i])
    length = len(job)
    table = [0 for _ in range(length)]

    table[0] = job[0].profit

    # Fill entries in table[] using recursive property
    for i in range(1, length):

        # Find profit including the current job
        incl_prof = job[i].profit
        pos = binary_search(job, i)
        if pos != -1:
            incl_prof += table[pos]

        # Store maximum of including and excluding
        table[i] = max(incl_prof, table[i - 1])

    return table[length-1]
