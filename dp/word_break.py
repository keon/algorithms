def word_break(s, word_dict):
  """
  :type s: str
  :type word_dict: Set[str]
  :rtype: bool
  """
  f = [False] * (len(s)+1)
  f[0] = True
  for i in range(1, len(s)+1):
      for j in range(0, i):
        if f[j] and s[j:i] in word_dict:
            f[i] = True
            break
  return f[-1]

s = "keonkim"
dic = ["keon", "kim"]

print(word_break(s, dic))
