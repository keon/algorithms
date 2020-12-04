'''The K factor of a string is defined as the number of times 'abba' appears as a substring.
Given two numbers N and k,​ find the number of strings of length N with 'K factor' = k.

The algorithms is as follows:

dp[n][k] will be a 4 element array, wherein each element can be the number of strings of length n and 'K factor' = k which belong to the criteria represented by that index:

    dp[n][k][0] can be the number of strings of length n and K-factor = k which end with substring 'a'
    dp[n][k][1] can be the number of strings of length n and K-factor = k which end with substring 'ab'
    dp[n][k][2] can be the number of strings of length n and K-factor = k which end with substring 'abb'
    dp[n][k][3] can be the number of strings of length n and K-factor = k which end with anything other than the above substrings (anything other than 'a' 'ab' 'abb')

Example inputs

n=4 k=1  no of strings = 1
n=7 k=1 no of strings = 70302
n=10 k=2 no of strings = 74357

'''

def find_k_factor(n,k):
    dp=[[[0 for i in range(4)]for j in range((n-1)//3+2)]for k in range(n+1)]
    if(3*k+1>n):
        return 0
    #base cases
    dp[1][0][0]=1;
    dp[1][0][1]=0;
    dp[1][0][2]=0;
    dp[1][0][3]=25;

    for i in range(2,n+1):
        for j in range((n-1)//3+2):
            if(j==0):
                #adding a at the end
                dp[i][j][0]=dp[i-1][j][0]+dp[i-1][j][1]+dp[i-1][j][3]

                #adding b at the end
                dp[i][j][1]=dp[i-1][j][0]
                dp[i][j][2]=dp[i-1][j][1]

                #adding any other lowercase character
                dp[i][j][3]=dp[i-1][j][0]*24+dp[i-1][j][1]*24+dp[i-1][j][2]*25+dp[i-1][j][3]*25

            elif(3*j+1<i):
                #adding a at the end
                dp[i][j][0]=dp[i-1][j][0]+dp[i-1][j][1]+dp[i-1][j][3]+dp[i-1][j-1][2]

                #adding b at the end
                dp[i][j][1]=dp[i-1][j][0]
                dp[i][j][2]=dp[i-1][j][1]

                #adding any other lowercase character
                dp[i][j][3]=dp[i-1][j][0]*24+dp[i-1][j][1]*24+dp[i-1][j][2]*25+dp[i-1][j][3]*25

            elif(3*j+1==i):
                dp[i][j][0]=1
                dp[i][j][1]=0
                dp[i][j][2]=0
                dp[i][j][3]=0
            
            else:
                dp[i][j][0]=0
                dp[i][j][1]=0
                dp[i][j][2]=0
                dp[i][j][3]=0

    return sum(dp[n][k])

