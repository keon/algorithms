"""
input two of the three side in right angled triangle and return the third. use "?" to indicate the unknown side. 
"""

def pythagoras(opposite,adjacent,hypotenuse):
    if opposite == str("?"):
        print ("Solving for opposite")
        return ((hypotenuse**2) - (adjacent**2))**0.5
    elif adjacent == str("?"):
        print ("Solving for adjacent")
        return ((hypotenuse**2) - (opposite**2))**0.5
    elif hypotenuse == str("?"):
        print ("Solving for hypotenuse")
        return ((opposite**2)+(adjacent**2))**0.5
    else:
        return "you already know the answer!"
