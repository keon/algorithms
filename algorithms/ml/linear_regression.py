# Algorithm to implement Linear Regression

import numpy as np
import matplotlib.pyplot as plt

def find_coeff(x,y):
    #number of points
    n=np.size(x)

    #mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    #find cross-deviation and deviation about x
    cross_dev = np.sum(y*x) - n*m_y*m_x
    dev_x = np.sum(x*x) - n*m_x*m_x

    #calculating the regression coefficients
    b1 = cross_dev/dev_x
    b0 = m_y - b1*m_x

    return (b0,b1)

def plot_line(x,y,b):
    #plot the actual points as a scatter plot
    plt.scatter(x,y, c='m', marker='o', s=30)

    #predicted vector
    y_pred = b[0] +b[1]*x

    #plotting regression line
    plt.plot(x,y_pred, color='b')

    #labels
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

#example observations
x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])

#finding coefficients
b = find_coeff(x,y)
print("Estimated Coefficients: \n b0 = {} \n b1 = {}".format(b[0],b[1]))

#plotting the regression line
plot_line(x,y,b)



