def longest_palindromic_subsequence(str):
    n = len(str)
  
    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]
  
    for i in range(n):
        L[i][i] = 1
  
    
    for cl in range(2, n + 1):
        for i in range(n-cl + 1):
            j = i + cl-1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i + 1][j]);
  
    return L[0][n-1]

