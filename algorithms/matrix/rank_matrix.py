# Class about the calculation of the rank of a given matrix
class RankMatrix(object): 
    def __init__(self, Matrix): 
        self.rows = len(Matrix) 
        self.columns = len(Matrix[0])
        self.matrix = Matrix 
          
    # Function for exchanging two rows of a matrix 
    def swap(self, row1, row2, col): 
        for i in range(col): 
            temp = self.matrix[row1][i] 
            self.matrix[row1][i] = self.matrix[row2][i] 
            self.matrix[row2][i] = temp 
              
    # Function to Display a matrix 
    def Display(self): 
        for i in range(self.rows): 
            for j in range(self.columns): 
                print (" " + str(self.matrix[i][j])) 
            print ('\n') 
              
    # Find rank of a matrix 
    def rankOfMatrix(self):
        matrix = self.matrix
        rank = self.columns 
        for row in range(0, rank): 
              
            # Before we visit current row  
            # 'row', we make sure that  
            # mat[row][0],....mat[row][row-1]  
            # are 0.  
      
            # Diagonal element is not zero 
            if matrix[row][row] != 0: 
                for col in range(0, self.rows): 
                    if col != row: 
                          
                        # This makes all entries of current  
                        # column as 0 except entry 'mat[row][row]'  
                        multiplier = (matrix[col][row] / matrix[row][row]) 
                        for i in range(rank): 
                            matrix[col][i] -= (multiplier * matrix[row][i]) 
                                                  
            # Diagonal element is already zero.  
            # Two cases arise:  
            # 1) If there is a row below it  
            # with non-zero entry, then swap  
            # this row with that row and process  
            # that row  
            # 2) If all elements in current  
            # column below mat[r][row] are 0,  
            # then remvoe this column by  
            # swapping it with last column and  
            # reducing number of columns by 1.  
            else: 
                reduce = True
                  
                # Find the non-zero element  
                # in current column  
                for i in range(row + 1, self.rows): 
                      
                    # Swap the row with non-zero  
                    # element with this row. 
                    if matrix[i][row] != 0: 
                        self.swap(row, i, rank) 
                        reduce = False
                        break
                          
                # If we did not find any row with  
                # non-zero element in current  
                # columnm, then all values in  
                # this column are 0. 
                if reduce: 
                      
                    # Reduce number of columns  
                    rank -= 1
                      
                    # copy the last column here 
                    for i in range(0, self.rows): 
                        matrix[i][row] = matrix[i][rank] 
                          
                # process this row again 
                row -= 1
                    
        return (rank) 
