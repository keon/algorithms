def matrix_multiplaction(matrixA,matrixB):
    matrixC=[]
    
    for m in range(len(matrixA)):
        matrixC.append([0]*len(matrixB[0]))
    for i in range(len(matrixA)):
        for j in range(len(matrixC[0])):
            result=0
            for k in range(len(matrixB)):
                matrixC[i][j]+=matrixA[i][k]*matrixB[k][j]
    return matrixC
def matrix_exponentiation(matrix,power):
    import cp
    identity=[]
    for m in range(len(matrix)):
        identity.append([0]*len(matrix[0]))
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row==column:
                identity[row][column]=1
    while power>0:
        if power%2!=0:
            identity=cp.matrix_multiplaction(identity, matrix)
        matrix=cp.matrix_multiplaction(matrix, matrix)
        power=power//2
    return identity
