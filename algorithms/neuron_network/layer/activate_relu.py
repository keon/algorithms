import numpy as np

from .layer import Layer
import sys
sys.path.insert(1, "./../")
from debug import Debug

class ReLU(Layer):

	def __init__(self, name="", debug=False):
		self.parameter = 0
		self.name = name
		self.debug = Debug(self.name)

	def active_function(self, x, debug=False):
		return np.where(x >= 0, x, self.parameter*x)

	def forward(self, input, debug=False):
		input = np.array(input)
		self.input = input
		self.output = self.active_function(input)
		if debug:
			self.debug.buff("input"+str(input))
			self.debug.buff("output"+str(self.output))
			self.debug.log()
		return self.output

	def backward(self, gradient, debug=False):
		gradient = np.array(gradient)
		output = np.where(self.input >= 0, gradient, self.parameter*gradient)
		if debug:
			self.debug.buff("gradient"+str(gradient))
			self.debug.buff("backward"+str(output))
			self.debug.log()
		return output

class PReLU(ReLU):
	def __init__(self, parameter=0.01, name="", debug=False):
		super().__init__(name, debug)
		self.parameter = parameter