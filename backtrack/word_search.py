'''
Given a matrix of words and a list of words to search, return a list of words that exists in the board
This is Word Search II on LeetCode

board = [
         ['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v']
         ]

words = ["oath","pea","eat","rain"]

print findWords(board, words)
'''

def findWords(board, words):
    #make trie
    trie = {}
    for word in words:
        curr_trie = trie
        for char in word:
            if char not in curr_trie:
                curr_trie[char] = {}
            curr_trie = curr_trie[char]
        curr_trie['#'] = '#'

    result = set()
    used = [[False]*len(board[0]) for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            find(board, i, j, trie, '', used, result)
    return list(result)

def find(board, i, j, trie, pre, used, result):
    if '#' in trie:
        result.add(pre)
    
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    
    if not used[i][j] and board[i][j] in trie:
        used[i][j]=True
        find(board,i+1,j,trie[board[i][j]],pre+board[i][j], used, result)
        find(board,i,j+1,trie[board[i][j]],pre+board[i][j], used, result)
        find(board,i-1,j,trie[board[i][j]],pre+board[i][j], used, result)
        find(board,i,j-1,trie[board[i][j]],pre+board[i][j], used, result)
        used[i][j]=False
