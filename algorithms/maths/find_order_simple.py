"""
For positive integer n and given integer a that satisfies gcd(a, n) = 1,
the order of a modulo n is the smallest positive integer k that satisfies
pow (a, k) % n = 1. In other words, (a^k) ≡ 1 (mod n).
Order of a certain number may or may not be exist. If not, return -1.

Total time complexity O(nlog(n)):
O(n) for iteration loop, 
O(log(n)) for built-in power function
"""

import math

branch_coverage = {
    "branch_6": False,
    "branch_7": False,
    "branch_8": False,
    "branch_9": False,
    "branch_10": False   
}

def find_order(a, n):
    """
    Find order for positive integer n and given integer a that satisfies gcd(a, n) = 1.
    """
    
    if (a == 1) & (n == 1):
        # Exception Handeling : 1 is the order of of 1
        branch_coverage["branch_6"] = True
        print("branch_6")
        return 1
    if math.gcd(a, n) != 1:
        branch_coverage["branch_7"] = True
        print("branch_7")
        print ("a and n should be relative prime!")
        return -1
    for i in range(1, n):
        branch_coverage["branch_8"] = True
        print("branch_8")
        if pow(a, i) % n == 1:
            branch_coverage["branch_9"] = True
            print("branch_9")
            return i
    branch_coverage["branch_10"] = True
    print("branch_10")
    return -1

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
        
print_coverage()