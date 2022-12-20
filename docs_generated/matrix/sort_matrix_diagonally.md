
# Sort Diagonally

Given a m * n matrix `mat` of integers, you are tasked with sorting it diagonally in ascending order from the top-left to the bottom-right and then returning the sorted array. 

For example, given the following matrix:

```
mat = [
    [3,3,1,1],
    [2,2,1,2],
    [1,1,1,2]
]
```

The expected output is:

```
[
    [1,1,1,1],
    [1,2,2,2],
    [1,2,3,3]
]
```

## Solution

We can use a heap to sort each diagonal of the matrix. To do this, we can iterate through each row and column and add each element to the heap. Then, we can sort the heap and update each element in the matrix. 

We can represent this algorithm in Python as follows:

```python
from heapq import heappush, heappop
from typing import List

def sort_diagonally(mat: List[List[int]]) -> List[List[int]]:
    # If the input is a vector, return the vector
    if len(mat) == 1 or len(mat[0]) == 1:
        return mat

    # Rows + columns - 1
    # The -1 helps you to not repeat a column
    for i in range(len(mat)+len(mat[0])-1):
        # Process the rows
        if i+1 < len(mat):
            # Initialize heap, set row and column
            h = []
            row = len(mat)-(i+1)
            col = 0

            # Traverse diagonally, and add the values to the heap
            while row < len(mat):
                heappush(h, (mat[row][col]))
                row += 1
                col += 1

            # Sort the diagonal
            row = len(mat)-(i+1)
            col = 0
            while h:
                ele = heappop(h)
                mat[row][col] = ele
                row += 1
                col += 1
        else:
            # Process the columns
            # Initialize heap, row and column
            h = []
            row = 0
            col = i - (len(mat)-1)

            # Traverse Diagonally
            while col < len(mat[0]) and row < len(mat):
                heappush(h, (mat[row][col]))
                row += 1
                col += 1

            # Sort the diagonal
            row = 0
            col = i - (len(mat)-1)
            while h:
                ele = heappop(h)
                mat[row][col] = ele
                row += 1
                col += 1

    # Return the updated matrix
    return mat
```

We start by checking if the input is a vector. If it is, we simply return the vector. Otherwise, we iterate through each row and column, adding each element to the heap. We then sort the heap and update each element in the matrix. 

Finally, we return the updated matrix.

## Complexity

The time complexity of this algorithm is O(m<sup>2</sup>n<sup>2</sup>) as we need to iterate through each row and column and add each element to the heap. The space complexity is O(m+n) as we need to store the elements in the heap.