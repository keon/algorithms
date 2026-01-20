
import collections


def removeWhitespace(string):
    return "".join(string.split())


"""
    Checks if two strings are anagrams of each other, ignoring any whitespace.
    
    First remove any whitespace and lower all characters of both strings.
    Then create dictionaries of the counts of every character in each string.
    As well as keep a set of all characters used in both strings.
    Check to ensure every unique character are used in both strings the
        same number of times.
"""


def isAnagram(string1, string2):
    charCount1 = collections.Counter(removeWhitespace(string1.lower()))
    charCount2 = collections.Counter(removeWhitespace(string2.lower()))

    allChars = set(charCount1.keys())
    allChars = allChars.union(charCount2.keys())

    for c in allChars:
        if charCount1[c] != charCount2[c]:
            return False

    return True


assert isAnagram("anagram", "not a gram") == False
assert isAnagram("anagram", "na a marg") == True
assert isAnagram("William Shakespeare", "I am \t a weakish speller") == True
assert isAnagram("Madam Curie", "Radium came") == True
assert isAnagram("notagram", "notaflam") == False

#By OpenGenus
