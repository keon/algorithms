"""
The Boyer–Moore–Horspool-Sunday (BMHS) algorithm or Horspool's algorithm is an algorithm for finding substrings in strings.

The complexity of time and space for
the preprocessing is O (m + c).

For the research phase, the worst case of
algorithm is O (nm), the best case is O (n / m) and
the expected case is O (n / m), if c is not
small and m is not very large.

* @param text: 
      - text: text where the presence of a pattern
      - pattern: pattern which will be checked
* @return:
      - occurrences: list with position of Pattern Matching

* @example: 
      - bmh("Can you can a can as a canner can can a can?", "can")
      - >>> [8, 14, 23, 30, 34, 40]
"""

def bmhs(text, pattern):
  
  maxChar = 255
  alphabet = []
  occurrence = []
  for j in range(maxChar):
    alphabet.append(len(pattern) + 1)
  for j in range(len(pattern)):
    alphabet[ord(pattern[j])] = len(pattern) - j
  i = len(pattern) - 1;

  while ( i < len(text)):
    k = i
    j = len(pattern) - 1
    while (( j >= 0) and (text[k] == pattern[j] ) ):
      j -= 1
      k-= 1 
    if(j < 0):
      occurrence.append(k+1)
    if(i < (len(text) - 1)):
      i = i + alphabet[ord(text[ i + 1])]
    else:
      i = i + len(pattern) + 1
  return occurrence
