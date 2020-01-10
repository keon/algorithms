"""
Given the Number of Nodes of Binary Tree.
Return the Number of Unique Binary Tree.

Algo:
1. Find the Factorial of n(i.e Number of Nodes).
2. Find the Catalan Number of n.
More About Catalan Number: https://en.wikipedia.org/wiki/Catalan_number#First_proof
3. Multiply Both of Them to calculate the Number of Unique Number of Binary Tree.
"""
def factorial(n):
    '''
    Function to find the Factorial.
    :param n: Number of Nodes.
    :return: Factorial of Number.
    '''
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
def binomial_coefficient(n, k):
    """
    Since Here we Find the Binomial Coefficient:
    https://en.wikipedia.org/wiki/Binomial_coefficient
    C(n,k) = n! / k!(n-k)!
    :param n: 2 times of Number of nodes
    :param k: Number of nodes
    :return:  Integer Value
    """
    result = 1  # To kept the Calculated Value
    # Since C(n, k) = C(n, n-k)
    if k > (n - k):
        k = n - k
    # Calculate C(n,k)
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result
def catalan_number(node_count):
    """
    We can find Catalan number many ways but here we use Binomial Coefficent because it
    does the job in O(n)
    return the Catalan number of n using 2nCn/(n+1).
    :param n: number of nodes
    :return: Catalan number of n nodes
    """
    return binomial_coefficient(2 * node_count, node_count) // (node_count + 1)
def unique_binary_tree(n):
    '''
    Function to find Number of Unique Number of Binary Tree.
    :param n: Number of Nodes
    :return: Number of Unique Binary Tree.
    '''
    return factorial(n) * catalan_number(n)

if __name__ == "__main__":
    print(unique_binary_tree(5))