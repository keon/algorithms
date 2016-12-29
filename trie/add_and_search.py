"""
We are asked to design an efficient data structure
that allows us to add and search for words.
The search can be a literal word or regular expression
containing “.”, where “.” can be any letter.

Example:
addWord(“bad”)
addWord(“dad”)
addWord(“mad”)
search(“pad”) -> false
search(“bad”) -> true
search(“.ad”) -> true
search(“b..”) -> true
"""

class TrieNode(object):
    def __init__(self, letter, isTerminal=False):
        self.children = dict()
        self.letter = letter
        self.isTerminal = isTerminal

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode(letter)
            cur = cur.children[letter]
        cur.isTerminal = True

    def search(self, word, node=None):
        cur = node
        if not cur:
            cur = self.root
        for i, letter in enumerate(word):
            # if dot
            if letter == ".":
                if i == len(word) - 1: # if last character
                    for child in cur.children.itervalues():
                        if child.isTerminal:
                            return True
                    return False
                for child in cur.children.itervalues():
                    if self.search(word[i+1:], child) == True:
                        return True
                return False
            # if letter
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.isTerminal

