"""
Euler's totient function, also known as phi-function ϕ(n),
counts the number of integers between 1 and n inclusive,
which are coprime to n.
(Two numbers are coprime if their greatest common divisor (GCD) equals 1).
"""
branch_coverage = {
    "check_1": False,  # if branch for x > 0
    "check_2": False,   # else branch
    "check_2": False,
    "check_2": False,
}
def euler_totient(n):
    """Euler's totient function or Phi function.
    Time Complexity: O(sqrt(n))."""
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        branch_coverage["check_1"] = True
        if n % i == 0:
            branch_coverage["check_2"] = True
            while n % i == 0:
                branch_coverage["check_3"] = True
                n //= i
            result -= result // i
    if n > 1:
        branch_coverage["check_4"] = True
        result -= result // n
    return result

def print_coverage():
    total = len(branch_coverage)
    reached = sum(branch_coverage.values())
    coverage_percentage = (reached / total) * 100 
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
    print(f"coverage_percentage: {coverage_percentage}%")


result = euler_totient(21)
print_coverage()