"""
Given an api which returns an array of chemical names and an array of chemical
symbols, display the chemical names with their symbol surrounded by square
brackets:

Ex:
Chemicals array: ['Amazon', 'Microsoft', 'Google']
Symbols: ['I', 'Am', 'cro', 'Na', 'le', 'abc']

Output:
[Am]azon, Mi[cro]soft, Goog[le]

If the chemical string matches more than one symbol, then choose the one with
longest length. (ex. 'Microsoft' matches 'i' and 'cro')

My solution:
(I sorted the symbols array in descending order of length and ran loop over
chemicals array to find a symbol match(using indexOf in javascript) which
worked. But I din't make it through the interview, I am guessing my solution
was O(n2) and they expected an efficient algorithm.
"""

chemicals = ['Amazon', 'Microsoft', 'Google']
symbols = ['I', 'Am', 'cro', 'le', 'abc']

def match_symbol(chemicals, symbols):
    import re
    combined = []

    for s in symbols:
        for c in chemicals:
            r = re.search(s, c)
            if r:
                combined.append(re.sub(s, "[{}]".format(s), c))

    return combined


print match_symbol(chemicals, symbols)

"""
One approach is to use a Trie for the dictionary (the symbols), and then match
brute force. The complexity will depend on the dictionary;
if all are suffixes of the other, it will be n*m
(where m is the size of the dictionary). For example, in Python:
"""

from functools import reduce

class TrieNode:
    def __init__(self):
        self.c = dict()
        self.sym = None

def bracket(words, symbols):
    root = TrieNode()
    for s in symbols:
        t = root
        for char in s:
            if char not in t.c:
                t.c[char] = TrieNode()
            t = t.c[char]
        t.sym = s
    result = dict()
    for word in words:
        i = 0
        symlist = list()
        while i < len(word):
            j, t = i, root
            while j < len(word) and word[j] in t.c:
                t = t.c[word[j]]
                if t.sym is not None:
                    symlist.append((j+1-len(t.sym), j+1, t.sym))
                j += 1
            i += 1
        if len(symlist) > 0:
            sym = reduce(lambda x, y: x if x[1]-x[0] >= y[1]-y[0] else y, symlist)
            result[word] = "{}[{}]{}".format(word[:sym[0]], sym[2], word[sym[1]:])
    return tuple(word if word not in result else result[word] for word in words)

bracket(['amazon', 'microsoft', 'google'], ['i', 'am', 'cro', 'na', 'le', 'abc'])
>>> ('[am]azon', 'mi[cro]soft', 'goog[le]')
