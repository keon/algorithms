"""
Given the lengths of two of the three sides of a right angled triangle, this function returns the
length of the third side.
"""

def pythagoras(opposite, adjacent, hypotenuse):
    """
    Returns length of a third side of a right angled triangle.
    Passing "?" will indicate the unknown side.
    """
    try:
        if opposite == str("?"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent**2))**0.5))
        if adjacent == str("?"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite**2))**0.5))
        if hypotenuse == str("?"):
            return ("Hypotenuse = " + str(((opposite**2) + (adjacent**2))**0.5))
        return "You already know the answer!"
    except:
        raise ValueError("invalid argument(s) were given.")
