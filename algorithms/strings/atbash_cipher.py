"""
Atbash cipher is mapping the alphabet to it's reverse.
So if we take "a" as it is the first letter, we change it to the last - z.

Example:
Attack at dawn --> Zggzxp zg wzdm

Complexity: O(n)
"""

def atbash(s):
    translated = ""
    for i in range(len(s)):
        n = ord(s[i])
        
        if s[i].isalpha():
            
            if s[i].isupper():
                x = n - ord('A')
                translated += chr(ord('Z') - x)
            
            if s[i].islower():
                x = n - ord('a')
                translated += chr(ord('z') - x)
        else:
            translated += s[i]
    return translated