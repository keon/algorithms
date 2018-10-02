def lcs(X , Y): 
    
    l1 = len(X) 
    l2 = len(Y) 
  
    dp = [[0]*(l2+1) for i in xrange(l1+1)] 
  
    for i in range(l1+1): 
        for j in range(l2+1): 
            if i == 0 or j == 0 : 
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                dp[i][j] = dp[i-1][j-1]+1
            else: 
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1]) 
  
    return dp[l1][l2]  


X = "YRHHYDKP"
Y = "AYARHADP"
print "Length of LCS is ", lcs(X, Y) 