# Class about simple matrix characteristics
class Matrix(object):
    def __init__(self, matrix):
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.matrix = matrix

    def isLowertriangular(self):
        matrix = self.matrix 
        for i in range(0, len(matrix)): 
            for j in range(i + 1, len(matrix)): 
                if(matrix[i][j] != 0):  
                        return False
        return True

    def isUppertriangular(self): 
        matrix = self.matrix 
        for i in range(1, len(matrix)): 
            for j in range(0, i): 
                if(matrix[i][j] != 0):  
                        return False
        return True

    def isIdentity(self):
        matrix = self.matrix 
        for i in range(self.rows): 
            if (matrix[i][i] == 1):
                continue
            else: 
                return False
    
        return True

    # Function to implement matrix 
    # for swapping the upper diagonal 
    # elements with lower diagonal  
    # elements of matrix. 
    
    # Function to swap the diagonal  
    # elements in a matrix. 
    def swapUpperToLower(self): 
        matrix = self.matrix
        newRows = self.columns
        newColumns = self.rows 

        transposedMatrix = [[0 for i in range(newRows)] for j in range(newColumns)]
        
        # Loop for swap the elements 
        # of matrix. 
        for i in range(newRows):  
            for j in range(newColumns): 
                transposedMatrix[i][j] = matrix[j][i] 
        
        return transposedMatrix

