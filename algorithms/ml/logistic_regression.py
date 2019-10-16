'''
Learn about the algorithm
https://www.geeksforgeeks.org/understanding-logistic-regression/
'''

import csv
import numpy as np 
import matplotlib.pyplot as plt 

# Load dataset
def loadCSV(filename):
	with open(filename,"r") as csvfile: 
		lines = csv.reader(csvfile) 
		dataset = list(lines) 
		for i in range(len(dataset)): 
			dataset[i] = [float(x) for x in dataset[i]]	 
	return np.array(dataset)

# Normalizing feature matrix X
def normalize(X):
	rng = np.max(X, axis = 0) - np.min(X, axis = 0)
	norm_X = 1 - ((np.max(X, axis = 0) - X)/rng)
	return norm_X

#Logistic(sigmoid) function
def logistic_func(beta, X): 
	return 1.0/(1 + np.exp(-np.dot(X, beta.T)))

#logistic gradient function
def log_gradient(beta, X, y): 
	first_calc = logistic_func(beta, X) - y.reshape(X.shape[0], -1)
	final_calc = np.dot(first_calc.T, X) 
	return final_calc 

#The cost function
def cost_func(beta, X, y): 
	log_func_v = logistic_func(beta, X)
	y = np.squeeze(y) 
	step1 = y * np.log(log_func_v) 
	step2 = (1 - y) * np.log(1 - log_func_v) 
	final = -step1 - step2 
	return np.mean(final) 

#Calculating gradient descent
def grad_desc(X, y, beta, lr=.01, converge_change=.001): 

	cost = cost_func(beta, X, y)
	change_cost = 1
	num_iter = 1
	
	while(change_cost > converge_change): 
		old_cost = cost 
		beta = beta - (lr * log_gradient(beta, X, y)) 
		cost = cost_func(beta, X, y) 
		change_cost = old_cost - cost 
		num_iter += 1
	
	return beta, num_iter 

#Predicting labels
def pred_values(beta, X): 
	pred_prob = logistic_func(beta, X)
	pred_value = np.where(pred_prob >= .5, 1, 0) 
	return np.squeeze(pred_value) 

#Plot regression
def plot_reg(X, y, beta):
	# labelled observations 
	x_0 = X[np.where(y == 0.0)] 
	x_1 = X[np.where(y == 1.0)] 
	
	# plotting points with diff color for diff label 
	plt.scatter([x_0[:, 1]], [x_0[:, 2]], c='b', label='y = 0') 
	plt.scatter([x_1[:, 1]], [x_1[:, 2]], c='r', label='y = 1') 
	
	# plotting decision boundary 
	x1 = np.arange(0, 1, 0.1) 
	x2 = -(beta[0,0] + beta[0,1]*x1)/beta[0,2] 
	plt.plot(x1, x2, c='k', label='reg line') 

	plt.xlabel('x1') 
	plt.ylabel('x2') 
	plt.legend() 
	plt.show() 
	

	
if __name__ == "__main__": 
	# load the dataset 
	dataset = loadCSV('dataset1.csv') 
	
	# normalizing feature matrix 
	X = normalize(dataset[:, :-1]) 
	
	# stacking columns wth all ones in feature matrix 
	X = np.hstack((np.matrix(np.ones(X.shape[0])).T, X)) 

	# response vector 
	y = dataset[:, -1] 

	# initial beta values 
	beta = np.matrix(np.zeros(X.shape[1])) 

	# beta values after running gradient descent 
	beta, num_iter = grad_desc(X, y, beta) 

	# estimated beta values and number of iterations 
	print("Estimated regression coefficients:", beta) 
	print("No. of iterations:", num_iter) 

	# predicted labels 
	y_pred = pred_values(beta, X) 
	
	# number of correctly predicted labels 
	print("Correctly predicted labels:", np.sum(y == y_pred)) 
	
	# plotting regression line 
	plot_reg(X, y, beta) 
