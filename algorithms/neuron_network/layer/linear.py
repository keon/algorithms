import numpy as np

from .layer import Layer
import sys
sys.path.insert(1, "./../")
from debug import Debug

class Linear(Layer):

	def __init__(self, input_dim, output_dim, name, debug=False):
		self.weights = np.random.random((input_dim, output_dim))
		self.bias = np.random.random((output_dim, 1))
		# if debug:
		# 	print("bias", self.bias)
		self.name = name
		self.debug = Debug(self.name)

	def forward(self, input, debug=False):
		input = np.array(input)
		self.input = input
		output = np.dot(self.weights.T, input) + self.bias
		if debug:
			print(self.bias)
			self.debug.buff("input"+str(input))
			self.debug.buff("pre weight"+str(self.weights))
			self.debug.buff("pre bias"+str(self.bias))
			self.debug.buff("output"+str(output))
			self.debug.log()
		return output

	def backward(self, gradient, debug=False):
		gradient = np.array(gradient)
		self.bias_gradient = gradient
		self.weight_gradient = self.input * gradient.reshape(-1)
		result = np.dot(self.weights, gradient)
		if debug:
			self.debug.buff("gradient"+str(gradient))
			self.debug.buff("input"+str(self.input))
			self.debug.buff("weight gradient"+str(self.weight_gradient))
			self.debug.buff("backward"+str(result))
			self.debug.log()
		return result

	def get_params(self, debug=False):
		return self.weights, self.bias

	def get_grads(self, debug=False):
		return self.weight_gradient, self.bias_gradient

	def update(self, new_weights, new_bias, debug=False):
		self.weights =  np.array(new_weights)
		self.bias = np.array(new_bias)