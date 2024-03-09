# a -> Adam -> Book -> 4
# b -> Bill -> Computer -> 5
#           -> TV -> 6
#      Jill -> Sports -> 1
# c -> Bill -> Sports -> 3
# d -> Adam -> Computer -> 3
#      Quin -> Computer -> 3
# e -> Quin -> Book -> 5
#           -> TV -> 2
# f -> Adam -> Computer -> 7

from __future__ import print_function


def tree_print(tree):
    for key in tree:
        print(key, end=' ')  # end=' ' prevents a newline character
        tree_element = tree[key]  # multiple lookups is expensive, even amortized O(1)!
        for subElem in tree_element:
            print(" -> ", subElem, end=' ')
            if type(subElem) != str:  # OP wants indenting after digits
                print("\n ")  # newline and a space to match indenting
        print()  # forces a newline
