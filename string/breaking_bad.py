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
worked. But I didn't make it through the interview, I am guessing my solution
was O(n^2) and they expected an efficient algorithm.


note:
This approach didn't pass interview because it did wrong in conditions like:

input:
chemicals = ['Amazon', 'Microsoft', 'Google']
symbols = ['I', 'Am', 'cro', 'Na', 'le', 'abc', 'o']  # add 'o' here

expected:
['[am]azon', 'mi[cro]soft', 'goog[le]']

exact output:
['[Am]azon', 'Mi[cro]soft', 'Goog[le]', 'Amaz[o]n', 'Micr[o]s[o]ft', 'G[o][o]gle']
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

print(match_symbol(chemicals, symbols))



"""
An improved version of above, get right output.

symbols = ['I', 'Am', 'cro', 'Na', 'le', 'abc', 'o']
words = ['Amazon', 'Microsoft', 'Google']
print(match_symbol_1(symbols, words))
>>> ['[Am]azon', 'Mi[cro]soft', 'Goog[le]']

O(mn) time
m = len(symbols), n = len(words)
Assuming re.findall(s, w) is O(1) time.
"""

def match_symbol_1(symbols, words):
    import re
    bracketed_list = []
    for w in words:
        longest_match=''
        for s in symbols:
            matchs = re.findall(s, w)
            for m in matchs:
                longest_match = m if len(longest_match) < len(m) else longest_match
        bracketed.append(re.sub(longest_match, '[{}]'.format(longest_match), w))
    return bracketed_list



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
