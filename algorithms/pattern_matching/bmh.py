"""
The Boyer–Moore–Horspool algorithm or Horspool's algorithm is an algorithm for finding substrings in strings. 

complexity: The algorithm trades space for time in order to obtain an average-case complexity of O(n) on random text, although it has O(nm) in the worst case, where the length of the pattern is m and the length of the search string is n.

* @param text: 
      - text: text where the presence of a pattern
      - pattern: pattern which will be checked
* @return:
      - occurrences: list with position of Pattern Matching

* @example: 
      - bmh("Can you can a can as a canner can can a can?", "can")
      - >>> [8, 14, 23, 30, 34, 40]
"""
def bmh(text, pattern):
  skip = []
  occurrences = []
  for k in range(256):
    skip.append(len(pattern))

  for k in range(len(pattern)-1):
    skip[ord(pattern[k])] = len(pattern) - k -1

  i = len(pattern) - 1
  while(i < len(text)):
    k = i
    j = len(pattern) - 1
    while(j >= 0 and (text[k] == pattern[j])):
      k -= 1
      j -= 1
    if(j == -1):
      occurrences.append(k+1)
    i += skip[ord(text[i])]
  return occurrences