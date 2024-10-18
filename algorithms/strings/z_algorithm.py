"""
Algorithm that computes the Z-array for a given string using the Z Algorithm.

The Z-array stores the length of the longest substring starting from index i which is also a prefix of the string.

Time Complexity: O(n), where n is the length of the input string.
"""

def compute_z_array(input_string):
    n = len(input_string)
    z_array = [0] * n
    left, right, k = 0, 0, 0

    for i in range(1, n):
        # Case 1: i is outside the current Z-box
        if i > right:
            left, right = i, i
            # Expand the Z-box by matching with the prefix
            while right < n and input_string[right] == input_string[right - left]:
                right += 1
            z_array[i] = right - left
            right -= 1
        else:
            # Case 2: i is within the current Z-box
            k = i - left
            # If the Z[k] value is less than the remaining length of Z-box
            if z_array[k] < right - i + 1:
                z_array[i] = z_array[k]
            else:
                # Start from the right boundary and try to extend
                left = i
                while right < n and input_string[right] == input_string[right - left]:
                    right += 1
                z_array[i] = right - left
                right -= 1
    return z_array
