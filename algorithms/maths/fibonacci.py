""" Fibonacci sequence
Generates a list consisting of fibonacci numbers from F(0)
to F(n) for the input n

Arguments:
n -- The nth fibonacci number to generate to.
simulation -- whether or not the script should return info
about an estimation of phi
"""
def fibonacci(n, simulation=False):
    f_nums = [1,1]
    for x in range(1,n):
        f_nums.append(f_nums[x-1] + f_nums[x])
    if (simulation):
        phi = (1 + 5**0.5)/2
        print(f_nums)
        print("F({}) - F({}) = {}".format(n, n-1, f_nums[-1]/f_nums[-2]))
        print("The true value of phi is {}".format(phi))
    return f_nums
