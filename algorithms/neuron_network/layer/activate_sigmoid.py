import numpy as np

from .layer import Layer

class Sigmoid(Layer):

	def active_function(self, x, debug=False):
		return 1 / (1 + np.exp(-x))

	def forward(self, input, debug=False):
		input = np.array(input)
		self.input = input
		self.output = self.active_function(input)
		return self.output

	def backward(self, gradient, debug=False):
		gradient = np.array(gradient)
		return self.output*(1-self.output)*gradient