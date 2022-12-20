
# Rotating an Image by 90 Degrees

Rotating an image by 90 degrees is a common task in computer vision and image processing. In this article, we will discuss how to rotate an image by 90 degrees (clockwise) using the Python language.

## Problem Description

Given an n x n 2D matrix representing an image, we wish to rotate the image by 90 degrees (clockwise).

## Solution

We can solve this problem in-place by first reversing the matrix up to down, then swapping the symmetry of the elements.

### Algorithm

1. Reverse the matrix up to down
2. Swap the symmetry of the elements

### Code Snippet

```python
def rotate(mat):
    if not mat:
        return mat
    mat.reverse()
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat
```

### Example

Let's consider the following example:

```
1 2 3
4 5 6
7 8 9
```

Applying the above algorithm, we get the following result:

```
7 4 1
8 5 2
9 6 3
```

## Conclusion

In this article, we discussed how to rotate an image by 90 degrees (clockwise) using the Python language. We used an algorithm that reversed the matrix up to down, then swapped the symmetry of the elements.