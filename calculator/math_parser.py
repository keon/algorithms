"""
Contributed by izanbf1803.

Example:
-------------------------------------------------------------------------------------------------
	Code:
		|	exp = "2452 * (3 * 6 + 1) * 6 / 235"
		|	print("Expression:", exp)
		|	print("Parsed expression:", mp.parse(exp))
		|	print("Evaluation result:", mp.evaluate(exp))

	Output:
		|	Expression: 2452 * (3 * 6 + 1) * 6 / 235
		|	Parsed expression: ['2452', '*', '(', '3', '*', '6', '+', '1', ')', '*', '6', '/', '235']
		|	Evaluation result: 1189.4808510638297
-------------------------------------------------------------------------------------------------
"""

from collections import deque

__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
	'+': 0,
	'-': 0,
	'*': 1,
	'/': 1,
}

def isOperator(token):
	"""
	Check if token it's a operator

	token Char: Token
	"""
	return token in __operators__

def higherPriority(op1, op2):
	"""
	Check if op1 have higher priority than op2

	op1 Char: Operation Token 1
	op2 Char: Operation Token 2
	"""
	return __priority__[op1] >= __priority__[op2]

def calc(n2, n1, operator):
	"""
	Calculate operation result

	n2 Number: Number 2
	n1 Number: Number 1
	operator Char: Operation to calculate
	"""
	if operator == '-': return n1 - n2
	elif operator == '+': return n1 + n2
	elif operator == '*': return n1 * n2
	elif operator == '/': return n1 / n2
	return 0

def applyOperation(opStack, outStack):
	"""
	Apply operation to the first 2 items of the output queue

	opStack Deque (reference)
	outStack Deque (reference)
	"""
	outStack.append(calc(outStack.pop(), outStack.pop(), opStack.pop()))

def parse(expression):
	"""
	Return array of parsed tokens in the expression

	expression String: Math expression to parse in infix notation
	"""
	result = []
	current = ""
	for i in expression:
		if i.isdigit():
			current += i
		else:
			if len(current) > 0:
				result.append(current)
				current = ""
			if i != ' ':
				result.append(i)
	if len(current) > 0:
		result.append(current)
	return result

def evaluate(expression):
	"""
	Calculate result of expression

	expression String: The expression
	type Type (optional): Number type [int, float]
	"""
	opStack  = deque() # operator stack
	outStack = deque() # output stack (values)
	for token in parse(expression):
		if token.isdigit():
			outStack.append(float(token))
		elif token == '(':
			opStack.append(token)
		elif token == ')':
			while len(opStack) > 0 and opStack[-1] != '(':
				applyOperation(opStack, outStack)
			opStack.pop() # Remove remaining '('
		else: # isOperator(token)
			while len(opStack) > 0 and isOperator(opStack[-1]) and higherPriority(opStack[-1], token):
				applyOperation(opStack, outStack)
			opStack.append(token)

	while len(opStack) > 0:
		applyOperation(opStack, outStack)

	return outStack[-1]