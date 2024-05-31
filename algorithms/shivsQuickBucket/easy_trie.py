from collections import deque
'''
You may also try to make a treenode in cases where you need to store metadata
for a particular children of the node like this - 
class TreeNode:
def __init__(self):
    self.children = {}
    self.metadata = String | Number | Boolean
'''
# Trie Template for adding words checking if a prefix is valid in trie and returning list of words with that prefix

trie = {}
def add_word(curr, word):
    for c in word:
        if c not in curr: curr[c] = {}
        curr = curr[c]
    curr['#'] = {}

def has_word(curr, word):
    for c in word:
        if c in curr: curr = curr[c]
        else: return False
    return '#' in curr

def has_prefix(curr, pre):
    for c in pre:
        if c in curr: curr = curr[c]
        else: return False
    return curr

def get_words_using_prefix(head, pre):
    curr = has_prefix(head, pre)
    if not curr: return []

    #BFS
    words = []
    q = deque([(curr, pre)])
    while q:
        size = len(q)
        for _ in range(size):
            curr, pre = q.popleft()
            if '#' in curr: words.append(pre)
            for nei in curr:
                q.append((curr[nei], pre + nei))
    return words

words = ['abcd', 'defg']
prefixes = ['a', 'def']
for word in words:
    add_word(trie, word)
for pre in prefixes:
    print(get_words_using_prefix(trie, pre))