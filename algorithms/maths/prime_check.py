branch_coverage = {
    "branch_1": False,  # n <= 1
    "branch_2": False,  # n == 2 or n == 3
    "branch_3": False,  # n % 2 == 0 or n % 3 == 0
    "branch_4": False,  # while j * j <= n
    "branch_5": False   # n % j == 0 or n % (j + 2) == 0
}
def prime_check(n):
    """Return True if n is a prime number
    Else return False.
    """
    print(f"Checking {n}")  # Debugging statement

    if n <= 1:
        branch_coverage["branch_1"] = True
        print("branch_1")
        return False

    if n == 2 or n == 3:
        branch_coverage["branch_2"] = True
        print("branch_2")
        return True
    if n % 2 == 0 or n % 3 == 0:
        branch_coverage["branch_3"] = True
        print("branch_3")
        return False
    j = 5
    while j * j <= n:
        branch_coverage["branch_4"] = True
        print("branch_4")
        if n % j == 0 or n % (j + 2) == 0:
            branch_coverage["branch_5"] = True
            print("branch_5")
            return False
        j += 6
    return True

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
        
print_coverage()
