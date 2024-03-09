"""
Given a non-empty string s and a dictionary wordDict
containing a list of non-empty words,
determine if word can be segmented into a space-separated
sequence of one or more dictionary words.
You may assume the dictionary does not contain duplicate words.

For example, given
word = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

word = abc word_dict = ["a","bc"]
True False False False

"""


# TC: O(N^2)  SC: O(N)
def word_break(word, word_dict):
    """
    :type word: str
    :type word_dict: Set[str]
    :rtype: bool
    """
    dp_array = [False] * (len(word)+1)
    dp_array[0] = True
    for i in range(1, len(word)+1):
        for j in range(0, i):
            if dp_array[j] and word[j:i] in word_dict:
                dp_array[i] = True
                break
    return dp_array[-1]


if __name__ == "__main__":
    STR = "keonkim"
    dic = ["keon", "kim"]

    print(word_break(str, dic))
