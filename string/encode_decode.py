# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded
# back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
  # // ... your code
  # return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
  # //... your code
  # return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

def encode(strs):
    """Encodes a list of strings to a single string.
    :type strs: List[str]
    :rtype: str
    """
    res = ''
    for string in strs.split():
        res += str(len(string)) + ":" + string
    return res

def decode(s):
    """Decodes a single string to a list of strings.
    :type s: str
    :rtype: List[str]
    """
    strs = []
    i = 0
    while i < len(s):
        index = s.find(":", i)
        size = int(s[i:index])
        strs.append(s[index+1: index+1+size])
        i = index+1+size
    return strs

strs = "keon is awesome"
print(strs)
enc = encode(strs)
print(enc)
dec = decode(enc)
print(dec)
