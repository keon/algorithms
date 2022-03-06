import math
import statistics
import random


def simple_linear_regression(data):
    """ Simple linear regression model of type y = b_0 + b_1*x
    Cost function to minimize is RSS with data segmentation according to
    k fold cross validation
    """

    # Initializing parameters using random normal distribution
    param_0 = random.random
    param_1 = random.random

    mean_x = statistics.mean(data[0])
    mean_y = statistics.mean(data[1])

    numerator = 0  # ((data[0]-mean_x)*(data[1]-mean_y))
    denominator = 0
    for index in range(len(data[0])):
        numerator += (data[0][index]-mean_x)*(data[1][index]-mean_y)
        denominator += (data[0][index]-mean_x)**2

    param_1 = numerator / denominator
    param_0 = mean_y - param_1*mean_x
    rss = RSS_calculator([param_0, param_1], data)
    rse = RSE_calculator(rss, len(data[0]))
    r_2 = R_2(rss, mean_y, data)

    return (param_0, param_1, rse, r_2)


def RSS_calculator(params, data):
    rss = 0
    for index in range(len(data[0])):
        rss += (data[1][index] - (params[0] + params[1]*data[0][index]))**2
    return rss


def RSE_calculator(rss, n):
    return math.sqrt(rss / (n - 2))


def R_2(rss, mean_y, data):
    tss = 0
    for val in data[1]:
        tss += (val-mean_y) ** 2
    r_2 = 1 - (rss/tss)
    return r_2
