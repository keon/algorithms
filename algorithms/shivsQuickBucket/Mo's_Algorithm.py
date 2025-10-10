import math
 
# Function that accepts array and list of queries and print sum of each query
def queryResults(arr,Q):
     
    #Q.sort(): # Sort by L
    #sort all queries so that all queries in the increasing order of R values .  
    Q.sort(key=lambda x: x[1])
     
    # Initialize current L, current R and current sum
    currL,currR,currSum = 0,0,0
     
    # Traverse through all queries
    for i in range(len(Q)):
        L,R = Q[i] # L and R values of current range
         
        # Remove extra elements from previous range
        # if previous range is [0, 3] and current  
        # range is [2, 5], then a[0] and a[1] are subtracted  
        while currL<L:
            currSum-=arr[currL]
            currL+=1
             
        # Add elements of current range
        while currL>L:
            currSum+=arr[currL-1]
            currL-=1
        while currR<=R:
            currSum+=arr[currR]
            currR+=1
             
        # Remove elements of previous range
        # when previous range is [0, 10] and current range  
        # is [3, 8], then a[9] and a[10] are subtracted  
        while currR>R+1:
            currSum-=arr[currR-1]
            currR-=1
         
        # Print the sum of current range
        print("Sum of",Q[i],"is",currSum)
 
arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
Q = [[0, 4], [1, 3], [2, 4]]
queryResults(arr,Q)