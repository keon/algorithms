"""
Given the lengths of two of the three sides of a right angled triangle, this function returns the
length of the third side.
"""
branch_coverage = {
    "branch_1": False,
    "branch_2": False,
    "branch_3": False,
    "branch_4": False,
    #"branch_5": False 
}

def pythagoras(opposite, adjacent, hypotenuse):
    """
    Returns length of a third side of a right angled triangle.
    Passing "?" will indicate the unknown side.
    """
    try:
        if opposite == str("?"):
            branch_coverage["branch_1"] = True
            print("branch_1")
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent**2))**0.5))
        if adjacent == str("?"):
            branch_coverage["branch_2"] = True
            print("branch_2")
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite**2))**0.5))
        if hypotenuse == str("?"):
            branch_coverage["branch_3"] = True
            print("branch_3")
            return ("Hypotenuse = " + str(((opposite**2) + (adjacent**2))**0.5))
        branch_coverage["branch_4"] = True
        print("branch_4")
        return "You already know the answer!"
    except:
        # branch_coverage["branch_5"] = True
        # print("branch_5")
        raise ValueError("invalid argument(s) were given.")
    
def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
        
print_coverage()

# total = len(branch_coverage)
#     reached_branches = sum(branch_coverage.values())
#     percentage = (reached_branches/total)*100
# print_coverage()
