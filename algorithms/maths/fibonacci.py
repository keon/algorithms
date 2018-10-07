import numpy as np

def fibonacci(n):
    f_nums = [1,1]

    for x in range(1,n):
        f_nums.append(f_nums[x-1] + f_nums[x])

    phi = 2 * np.cos(np.pi/5)
    err = np.round(((f_nums[-1]/f_nums[-2] - phi)/phi * 100), decimals=2)

    print(f_nums)
    print("F({}) - F({}) = {}".format(n, n-1, f_nums[-1]/f_nums[-2]))
    print('{}% error.'.format(np.round(abs(err))))

number = input("Enter a number n to generate up to the nth fibonacci number: ")
fibonacci(int(number))
