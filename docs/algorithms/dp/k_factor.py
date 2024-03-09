'''
The K factor of a string is defined as the number of times 'abba' appears as a
substring. Given two numbers `length` and `k_factor`, find the number of
strings of length `length` with 'K factor' = `k_factor`.

The algorithms is as follows:

dp[length][k_factor] will be a 4 element array, wherein each element can be the
number of strings of length `length` and 'K factor' = `k_factor` which belong
to the criteria represented by that index:

    - dp[length][k_factor][0] can be the number of strings of length `length`
      and K-factor = `k_factor` which end with substring 'a'

    - dp[length][k_factor][1] can be the number of strings of length `length`
      and K-factor = `k_factor` which end with substring 'ab'

    - dp[length][k_factor][2] can be the number of strings of length `length`
      and K-factor = `k_factor` which end with substring 'abb'

    - dp[length][k_factor][3] can be the number of strings of `length` and
      K-factor = `k_factor` which end with anything other than the above
      substrings (anything other than 'a' 'ab' 'abb')

Example inputs

length=4 k_factor=1  no of strings = 1
length=7 k_factor=1 no of strings = 70302
length=10 k_factor=2 no of strings = 74357

'''

def find_k_factor(length, k_factor):
    """Find the number of strings of length `length` with K factor = `k_factor`.

    Keyword arguments:
    length -- integer
    k_factor -- integer
    """
    mat=[[[0 for i in range(4)]for j in range((length-1)//3+2)]for k in range(length+1)]
    if 3*k_factor+1>length:
        return 0
    #base cases
    mat[1][0][0]=1
    mat[1][0][1]=0
    mat[1][0][2]=0
    mat[1][0][3]=25

    for i in range(2,length+1):
        for j in range((length-1)//3+2):
            if j==0:
                #adding a at the end
                mat[i][j][0]=mat[i-1][j][0]+mat[i-1][j][1]+mat[i-1][j][3]

                #adding b at the end
                mat[i][j][1]=mat[i-1][j][0]
                mat[i][j][2]=mat[i-1][j][1]

                #adding any other lowercase character
                mat[i][j][3]=mat[i-1][j][0]*24+mat[i-1][j][1]*24+mat[i-1][j][2]*25+mat[i-1][j][3]*25

            elif 3*j+1<i:
                #adding a at the end
                mat[i][j][0]=mat[i-1][j][0]+mat[i-1][j][1]+mat[i-1][j][3]+mat[i-1][j-1][2]

                #adding b at the end
                mat[i][j][1]=mat[i-1][j][0]
                mat[i][j][2]=mat[i-1][j][1]

                #adding any other lowercase character
                mat[i][j][3]=mat[i-1][j][0]*24+mat[i-1][j][1]*24+mat[i-1][j][2]*25+mat[i-1][j][3]*25

            elif 3*j+1==i:
                mat[i][j][0]=1
                mat[i][j][1]=0
                mat[i][j][2]=0
                mat[i][j][3]=0

            else:
                mat[i][j][0]=0
                mat[i][j][1]=0
                mat[i][j][2]=0
                mat[i][j][3]=0

    return sum(mat[length][k_factor])
