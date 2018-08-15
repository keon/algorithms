"""
Contributed by izanbf1803.

Example:
-------------------------------------------------------------------------------------------------
    Code:
        |   exp = "2452 * (3 * 6.5 + 1) * 6 / 235"
        |   print("Expression:", exp)
        |   print("Parsed expression:", mp.parse(exp))
        |   print("Evaluation result:", mp.evaluate(exp))

    Output:
        |   Expression: 2452 * (3 * 6 + 1) * 6 / 235
        |   Parsed expression: ['2452', '*', '(', '3', '*', '6', '+', '1', ')', '*', '6', '/', '235']
        |   Evaluation result: 1189.4808510638297
-------------------------------------------------------------------------------------------------

Now added '^' operator for exponents. (by @goswami-rahul)
"""

from collections import deque
import re

numeric_value = re.compile('\d+(\.\d+)?')

__operators__ = "+-/*^"
__parenthesis__ = "()"
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
    '^': 2
}

def is_operator(token):
    """
    Check if token it's a operator

    token Char: Token
    """
    return token in __operators__

def higher_priority(op1, op2):
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
    elif operator == '^': return n1 ** n2
    return 0

def apply_operation(op_stack, out_stack):
    """
    Apply operation to the first 2 items of the output queue

    op_stack Deque (reference)
    out_stack Deque (reference)
    """
    out_stack.append(calc(out_stack.pop(), out_stack.pop(), op_stack.pop()))

def parse(expression):
    """
    Return array of parsed tokens in the expression

    expression String: Math expression to parse in infix notation
    """
    result = []
    current = ""
    for i in expression:
        if i.isdigit() or i == '.':
            current += i
        else:
            if len(current) > 0:
                result.append(current)
                current = ""
            if i in __operators__ or i in __parenthesis__:
                result.append(i)
            else:
                raise Exception("invalid syntax " + i)
                
    if len(current) > 0:
        result.append(current)
    return result

def evaluate(expression):
    """
    Calculate result of expression

    expression String: The expression
    type Type (optional): Number type [int, float]
    """
    op_stack  = deque() # operator stack
    out_stack = deque() # output stack (values)
    tokens = parse(expression) # calls the function only once!
    for token in tokens:
        if numeric_value.match(token):
            out_stack.append(float(token))
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            while len(op_stack) > 0 and op_stack[-1] != '(':
                apply_operation(op_stack, out_stack)
            op_stack.pop() # Remove remaining '('
        else: # is_operator(token)
            while len(op_stack) > 0 and is_operator(op_stack[-1]) and higher_priority(op_stack[-1], token):
                apply_operation(op_stack, out_stack)
            op_stack.append(token)

    while len(op_stack) > 0:
        apply_operation(op_stack, out_stack)

    return out_stack[-1]


def main():
    """
        simple user-interface
    """
    print("\t\tCalculator\n\n")
    user_input = input("expression or exit: ")
    while user_input != "exit":
        try:
            print("The result is {0}".format(evaluate(user_input)))
        except Exception:
            print("invalid syntax!")
            user_input = input("expression or exit: ")
    print("program end")
        

if __name__ == "__main__":
    main()
