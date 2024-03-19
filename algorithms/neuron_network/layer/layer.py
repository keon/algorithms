import numpy as np

class Layer: 
	def forward(self, input):
		raise NotImplementedError
	def backward(self, gradient):
		raise NotImplementedError
	def get_params(self):
		return None, None
	def get_grads(self):
		return None, None
	def update(self, new_weights, new_bias):
		raise NotImplementedError