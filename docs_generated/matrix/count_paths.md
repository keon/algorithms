
# Count the Number of Unique Paths from a[0][0] to a[m-1][n-1]

Finding the number of unique paths from the starting point of a matrix to the end point can be a challenging problem. We are allowed to move either right or down from a cell in the matrix. There are two approaches to solve this problem:

## Recursion

This approach recursively calls the same function starting from the end point of the matrix, a[m-1][n-1], and moving upwards and leftwards. At each recursive call, the path count of both recursions is added and then returned.

Time Complexity: O(mn)  
Space Complexity: O(mn)

## Dynamic Programming

This approach starts from the starting point of the matrix, a[0][0], and stores the count in a count matrix. The number of ways to reach a[i][j] is calculated by taking the sum of the number of ways to reach a[i-1][j] and a[i][j-1]. The final answer is returned from count[m-1][n-1].

Time Complexity: O(mn)  
Space Complexity: O(mn)

Below is the Python code for the Dynamic Programming approach:

```python
def count_paths(m, n):
    if m < 1 or n < 1:
        return -1
    count = [[None for j in range(n)] for i in range(m)]

    # Taking care of the edge cases- matrix of size 1xn or mx1
    for i in range(n):
        count[0][i] = 1
    for j in range(m):
        count[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            # Number of ways to reach a[i][j] = number of ways to reach
            #                                   a[i-1][j] + a[i][j-1]
            count[i][j] = count[i - 1][j] + count[i][j - 1]

    print(count[m - 1][n - 1])


def main():
    m, n = map(int, input('Enter two positive integers: ').split())
    count_paths(m, n)


if __name__ == '__main__':
    main()
```