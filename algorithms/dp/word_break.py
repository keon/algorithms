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
branch_coverage = {
    "check_5": False,  
    "check_6": False,   
    "check_7": False,
    "check_8": False,
    
}
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
        branch_coverage["check_5"] = True
        for j in range(0, i):
            branch_coverage["check_6"] = True
            if dp_array[j] and word[j:i] in word_dict:
                branch_coverage["check_7"] = True
                dp_array[i] = True
                break
            branch_coverage["check_8"] = True
    return dp_array[-1]


def print_coverage():
    total = len(branch_coverage)
    reached = sum(branch_coverage.values())
    coverage_percentage = (reached / total) * 100
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
    print(f"coverage_percentage: {coverage_percentage}%")


result = word_break("keonkim", {"keon", "kim"})
print_coverage()




