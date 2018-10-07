import numpy as np

def fibonacci(n):
    """ fibonacci
    Author-- makeroflight


    Generates a list consisting of fibonacci numbers from F(0)
    to F(n) for the input n, and then estimates phi from F(n) /
    F(n-1) and compares the result to ( 1 + sqrt(5) ) / 2.

    For example
    fibonacci(5) generates the list [1, 1, 2, 3, 5, 8], and then
    estimates phi as 8/5.

    Arguments:
    n -- The nth fibonacci number to generate to.
    """
    f_nums = [1,1]
    for x in range(1,n):
        f_nums.append(f_nums[x-1] + f_nums[x])

    phi = 2 * np.cos(np.pi/5)
    err = np.round(((f_nums[-1]/f_nums[-2] - phi)/phi * 100), decimals=2)

    print(f_nums)
    print("F({}) - F({}) = {}".format(n, n-1, f_nums[-1]/f_nums[-2]))
    print("{}% error.".format(np.round(abs(err))))

# uncomment these to get the script to prompt for input

# number = input("Enter a number n to generate up to the nth fibonacci number: ")
# fibonacci(int(number))
