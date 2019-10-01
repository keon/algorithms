
"""
With a deterministic finite automaton we can verify whether or not there is a marriage for the pattern in the text.

complexity: The cost of the Shift-And algorithm is O (n), since operations can be performed on O (1) and the standard fits on a few computer words.

* @param text: 
      - text: text where the presence of a pattern
      - pattern: pattern which will be checked
* @return:
      - occurrences: list with position of Pattern Matching

* @example: 
      - shift_and("Can you can a can as a canner can can a can?", "can")
      - >>> [8, 14, 23, 30, 34, 40]
"""

def shift_and(text, pattern):
  char = []
  occurrences = []
  r = 0
  for i in range(256):
    char.append(0)
   
  k = 1
  for j in range(len(pattern)):
    a=pattern[j]          
    char[ord(a)] = char[ord(a)] | k            
    lastbit=k
    k<<=1
  for i in range(len(text)):
    r=((r<<1) | 1) & char[ord(text[i])]
    if ((r & lastbit)!=0):
      occurrences.append(i - len(pattern) + 1)
  return occurrences