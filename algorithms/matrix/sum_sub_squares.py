# Function to find sum of all  
# sub-squares of size k x k in a given 
# square matrix of size n x n 
def sum_sub_squares(matrix, k):
    n = len(matrix)
    result = [[0 for i in range(k)] for j in range(k)]

    if k > n:
        return
    for i in range(n - k + 1):
        l = 0 
        for j in range(n - k + 1):
            sum = 0
            
            # Calculate and print sum of current sub-square 
            for p in range(i, k + i):
                for q in range(j, k + j):
                    sum += matrix[p][q]
            
            result[i][l] = sum
            l += 1 
         
    return result

