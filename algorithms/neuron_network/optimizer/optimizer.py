import numpy as np

class Optimizer:
	def step(self, network):
		raise NotImplementedError

class GradientDescent(Optimizer):
	def __init__(self, learning_rate = 0.1, debug=False):
		self.learning_rate = learning_rate

	def step(self, network, debug=False):
		for layer in network.get_layers():
			weights, bias = layer.get_params()
			weight_gradient, bias_gradient = layer.get_grads()
			if weights is not None:
				weights = weights - self.learning_rate*weight_gradient
				bias = bias - self.learning_rate*bias_gradient
				layer.update(weights, bias) 