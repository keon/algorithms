
import numpy as np
import pandas as pd 


class Linear_Regression():
    def __init__(self, X, y, alpha, epochs):
        self.X = X
        self.y = y
        self.alpha = alpha
        self.epochs = epochs
        self.theta =  np.array([0.0] * len(self.X.columns))
        self.m = len(self.X)
    def hypothesis(self):
        return self.theta*self.X
    
    def computeCost(self):
        h = self.hypothesis()
        h = np.sum(h, axis=1)
        return sum(np.sqrt((h-self.y)**2))/(2*self.m)
    
    
    def gradientDescent(self):
        losses = []
        for epoch in range(self.epochs):        
            h = self.hypothesis()
            h = np.sum(h, axis=1)
            for c in range(0, len(self.X.columns)):
                self.theta[c] = self.theta[c] - self.alpha * (sum((h-self.y)*self.X.iloc[:,c])/len(self.X))
            j = self.computeCost()
            print("Loss at iteration {} : {}".format(epoch,j))
            losses.append(j)
        return losses, self.theta


#l = Linear_Regression(X_train,y_train,0.001,50)
#losses, theta = l.gradientDescent()

