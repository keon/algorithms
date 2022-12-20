
# Matrix Multiplication Algorithm
This algorithm takes two compatible two dimensional matrices and returns their product. The space complexity of this algorithm is **O(n<sup>2</sup>)**. 

The possible edge case for this algorithm is when the number of columns of the multiplicand is not consistent with the number of rows of the multiplier. This will raise an exception.

## Code Snippet
```python
def multiply(multiplicand: list, multiplier: list) -> list:
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    multiplicand_row, multiplicand_col = len(
        multiplicand), len(multiplicand[0])
    multiplier_row, multiplier_col = len(multiplier), len(multiplier[0])
    if(multiplicand_col != multiplier_row):
        raise Exception(
            "Multiplicand matrix not compatible with Multiplier matrix.")
    # create a result matrix
    result = [[0] * multiplier_col for i in range(multiplicand_row)]
    for i in range(multiplicand_row):
        for j in range(multiplier_col):
            for k in range(len(multiplier)):
                result[i][j] += multiplicand[i][k] * multiplier[k][j]
    return result
```