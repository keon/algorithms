# Fills Z array for given string str[]
def create_Zarr(string, z):
    n = len(string)
 
    # [L,R] make a window which matches
    # with prefix of s
    left, right, k = 0, 0, 0
    for i in range(1, n):
 
        # if i>R nothing matches so we will calculate.
        # Z[i] using naive way.
        if i > right:
            left, right = i, i
 
            # R-L = 0 in starting, so it will start
            # checking from 0'th index.
            while right < n and string[right - left] == string[right]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
 
            # k = i-L so k corresponds to number which
            # matches in [L,R] interval.
            k = i - left
 
            # if Z[k] is less than remaining interval
            # then Z[i] will be equal to Z[k].
            
            if z[k] < right - i + 1:
                z[i] = z[k]
 
           
            else:
 
                # else start from R and check manually
                left = i
                while right < n and string[right - left] == string[right]:
                    right += 1
                z[i] = right - left
                right -= 1
 
# prints all occurrences of pattern
# in text using Z algo
def find(text, pattern):
 
    # Create concatenated string "P$T"
    concat = pattern + "$" + text
    left = len(concat)
 
    # Construct Z array
    z = [0] * left
    create_Zarr(concat, z)
 
    # now looping through Z array for matching condition
    for i in range(left):
 
        # if Z[i] (matched region) is equal to pattern
        # length we got the pattern
        if z[i] == len(pattern):
            print("Pattern found at index",
                      i - len(pattern) - 1)
 
# Driver Code
if __name__ == "__main__":
    text = "faabbcdeffghiaaabbcdfgaabf"
    pattern = "aabb"
    find(text, pattern)
