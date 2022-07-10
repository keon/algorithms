
"""
Implementing linear regression in python from scratch. 
Linear Regression is a machine learning algorithm based 
on supervised learning, and it's commonly used for predictive 
analysis.

"""

# importing all the required libraries

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import numpy as np


class LinearRegression() :

    def __init__(self,learning_rate=0.0001,epochs=100000):
        self.epochs = epochs
        self.lr = learning_rate
        self.w = None
        self.b = None
        self.cost_list = []
        
    def __initial_params(self,shape):
        #initialize weigth and bias as zero
        self.w = np.zeros(shape)
        self.b = 0
        return True
        
    def __predictions(self,X):
        return np.dot(X, self.w) + self.b

    def __calculate_cost(self,error):
        return (1/(2*error.size)) * np.dot(error.T,error)

    def __gradient_descent(self,X,y,y_pred):
        #difference between prediction and actual
        error = y_pred - y
        #calculate cost and append them to list
        cost = self.__calculate_cost(error)
        self.cost_list.append(cost)
        #gradients
        dw = (1 / X.shape[0]) * np.dot(X.T,error)
        db = (1 / X.shape[0]) * np.sum(error)
        return dw, db

    def __update_parameters(self,dw,db):
        #update weight and bias with gradients
        self.w -= self.lr * dw
        self.b -= self.lr * db
        return True

    def fit(self,X,y):
        """fits the model"""
        self.__initial_params(X.shape[1])
        for _ in range(self.epochs):
            y_pred = self.__predictions(X)
            dw, db,  = self.__gradient_descent(X, y, y_pred)
            self.__update_parameters(dw, db)
        return True

    def predict(self,X):
        return self.__predictions(X)

    def rmse(self,y_real,y_pred):
        """returns root mean square error"""
        return np.sqrt(np.mean((y_pred-y_real)**2))
        
    def r2(self,X,y):
        """returns r2"""
        sum_squares = 0
        sum_residuals = 0
        y_mean = np.mean(y)
        for i in range(X.shape[0]):
            y_pred = self.__predictions(X[i])
            sum_squares += (y[i] - y_mean) ** 2
            sum_residuals += (y[i] - y_pred) ** 2
        score = 1- (sum_residuals / sum_squares)
        return score


def create_dataset(n_samples=100000,n_features=1,noise=0.4):
    """generates dataset"""
    X,y = make_regression(n_samples=n_samples,n_features=n_features,noise=noise)
    return X,y



if __name__ == "__main__":

    # get dataset
    X,y = create_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # instantiate regressor and fit
    linreg = LinearRegression(learning_rate=0.01, epochs=10000)
    linreg.fit(X_train, y_train)

    # make prediction
    y_pred = linreg.predict(X_test)

    # metrics 

    rms = linreg.rmse(y_test, y_pred)
    print("RMSE: ",round(rms,2))

    r2 = linreg.r2(X_test,y_test)
    print("R2: ",round(r2,3))