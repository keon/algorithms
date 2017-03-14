# a -> Adam -> Book -> 4
# b -> Bill -> Computer -> 5
          # -> TV -> 6
     # Jill -> Sports -> 1
# c -> Bill -> Sports -> 3
# d -> Adam -> Computer -> 3
     # Quin -> Computer -> 3
# e -> Quin -> Book -> 5
          # -> TV -> 2
# f -> Adam -> Computer -> 7

def treePrint(tree):
    for key in tree:
        print key, # comma prevents a newline character
        treeElem = tree[key] # multiple lookups is expensive, even amortized O(1)!
        for subElem in treeElem:
            print " -> ", subElem,
            if type(subElem) != str: # OP wants indenting after digits
                print "\n " # newline and a space to match indenting
        print "" # forces a newline
