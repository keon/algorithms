"""
given input word, return the list of abbreviations.
ex)
word => ['word', 'wor1', 'wo1d', 'wo2', 'w1rd', 'w1r1', 'w2d', 'w3', '1ord', '1or1', '1o1d', '1o2', '2rd', '2r1', '3d', '4']
"""


def generate_abbreviations(word):

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

    result = []
    backtrack(result, word, 0, 0, "")
    return result
