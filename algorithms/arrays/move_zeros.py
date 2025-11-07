"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]

The time complexity of the below algorithm is O(n).
"""

def move_zeros(array):
    result = []
    zeros = 0

    for i in array:
            # Check for numeric zeros but exclude boolean False
            # False and other falsy values (like [], '') are NOT treated as zeros.
            if i == 0 and not isinstance(i, bool):  
                zeros += 1
            else:
                result.append(i)

    # Append zeros to the end without allocating another temporary list
    for _ in range(zeros):
         result.append(0)
    
    return result
