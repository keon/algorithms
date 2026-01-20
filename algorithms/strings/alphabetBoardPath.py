"""
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

board = [
"abcde", 
"fghij", 
"klmno", 
"pqrst", 
"uvwxy", 
"z"]

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

Example:
Input: target = "code"
Output: "RR!DDRR!UUL!R!"

Time complexity: O(n)

Space complextity: O(n)
"""

def alphabetBoardPath(self, target: str) -> str:

    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    dct = {}
    # mapping each letter to its position in the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            dct[board[i][j]] = (i, j)
    curPos = (0, 0)
    # iterate through every char in target, keeping track of current letter and destination
    # add path from current letter to destination to path
    
    path = ''
    for letter in target:
      
        if curPos == dct[letter]:
            path += '!'
            
        else:
            ver = curPos[0] - dct[letter][0]
            hor = curPos[1] - dct[letter][1]
            yMove = 'U' * ver if ver > 0 else 'D' * (-1 * ver)
            xMove = 'L' * hor if hor > 0 else 'R' * (-1 * hor)
            
            # traversal if destination == 'z': horizontal -> vertical else vertical -> horizontal
            
            if letter == 'z':
                path  += xMove + yMove + '!'
            else:
                path += (yMove + xMove + '!')
            curPos = dct[letter]
            
    return path
