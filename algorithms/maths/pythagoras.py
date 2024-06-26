"""
Given the lengths of two of the three sides of a right angled triangle, this function returns the
length of the third side.
"""
branch_coverage = {
    "branch_31": False,
    "branch_32": False,
    "branch_33": False,
    "branch_34": False,
    "branch_35": False 
}

def pythagoras(opposite, adjacent, hypotenuse):
    """
    Returns length of a third side of a right angled triangle.
    Passing "?" will indicate the unknown side.
    """
    try:
        if opposite == str("?"):
            branch_coverage["branch_31"] = True
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent**2))**0.5))
        if adjacent == str("?"):
            branch_coverage["branch_32"] = True
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite**2))**0.5))
        if hypotenuse == str("?"):
            branch_coverage["branch_33"] = True
            return ("Hypotenuse = " + str(((opposite**2) + (adjacent**2))**0.5))
        branch_coverage["branch_34"] = True
        return "You already know the answer!"
    except:
        branch_coverage["branch_35"] = True
        raise ValueError("invalid argument(s) were given.")
    
def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
        
pythagoras(3, 2, "?")

print_coverage()

