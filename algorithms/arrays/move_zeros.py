"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]

The time complexity of the below algorithm is O(n).
"""



# False == 0 is True
def move_zeros(array):
    result = [x for x in array if (x != 0 and type(x)!=bool)]
    return result + [0]*(len(array)- len(result))

print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
