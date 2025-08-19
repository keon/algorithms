"""
Given a postfix expression, a function eval_postfix 
takes a string of postfix expression and evaluates it.
Note that numbers and operators are seperated by whitespace.

For example:
eval_postfix('5 14 - 3 /') should return -3.0.
eval_postfix('-1.3 3 + 2 *') should return 3.4.

"""

def eval_postfix(expression):
    stack = []
    split_exp = expression.split()
    for item in split_exp:
        try:
            stack.append(float(item))
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            if item == '+':
                stack.append(val2 + val1)
            elif item == '-':
                stack.append(val2 - val1)
            elif item == '*':
                stack.append(val2 * val1)
            elif item == '/':
                stack.append(val2 / val1)
    return stack.pop()

print(eval_postfix('5 14 - 3 /'))
print(eval_postfix('-1.3 3 + 2 *'))