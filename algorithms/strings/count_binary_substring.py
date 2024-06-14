"""
Give a string s, count the number of non-empty (contiguous) substrings that have
 the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Reference: https://leetcode.com/problems/count-binary-substrings/description/
"""
branch_coverage = {
    "check_5": False,
    "check_6": False,
    "check_7": False,
}

def count_binary_substring(s):
    global branch_coverage
    cur = 1
    pre = 0
    count = 0
    for i in range(1, len(s)):
        branch_coverage["check_5"] = True
        if s[i] != s[i - 1]:
            branch_coverage["check_6"] = True
            count = count + min(pre, cur)
            pre = cur
            cur = 1
        else:
            branch_coverage["check_7"] = True
            cur = cur + 1
    count = count + min(pre, cur)
    return count


def print_coverage():
    total = len(branch_coverage)
    reached_branches = sum(branch_coverage.values())
    percentage = (reached_branches / total) * 100
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
    print(f"total Coverage: {percentage}%")

count = count_binary_substring("01100110")

print_coverage()
