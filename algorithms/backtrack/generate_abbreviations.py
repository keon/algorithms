"""
given input word, return the list of abbreviations.
ex)
word => [1ord, w1rd, wo1d, w2d, 3d, w3 ... etc]
"""


def generate_abbreviations(word):
    result = []
    backtrack(result, word, 0, 0, "")
    return result


def backtrack(result, word, pos, count, cur):
    if pos == len(word):
        if count > 0:
            cur += str(count)
        result.append(cur)
        return

    if count > 0:  # add the current word
        backtrack(result, word, pos+1, 0, cur+str(count)+word[pos])
    else:
        backtrack(result, word, pos+1, 0, cur+word[pos])
    # skip the current word
    backtrack(result, word, pos+1, count+1, cur)
