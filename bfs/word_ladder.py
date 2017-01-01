"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
.
Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""
def ladderLength(beginWord, endWord, wordList):
    """
    Bidirectional BFS!!!
    :type beginWord: str
    :type endWord: str
    :type wordList: Set[str]
    :rtype: int
    """
    beginSet = set()
    endSet = set()
    beginSet.add(beginWord)
    endSet.add(endWord)
    result = 2
    while len(beginSet) != 0 and len(endSet) != 0:
        if len(beginSet) > len(endSet):
            beginSet, endSet = endSet, beginSet
        nextBeginSet = set()
        for word in beginSet:
            for ladderWord in wordRange(word):
                if ladderWord in endSet:
                    return result
                if ladderWord in wordList:
                    nextBeginSet.add(ladderWord)
                    wordList.remove(ladderWord)
        beginSet = nextBeginSet
        result += 1
        print(beginSet)
        print(result)
    return 0

def wordRange(word):
    for ind in range(len(word)):
        tempC = word[ind]
        for c in [chr(x) for x in range(ord('a'), ord('z')+1)]:
            if c != tempC:
                yield word[:ind] + c + word[ind+1:]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(ladderLength(beginWord, endWord, wordList))
