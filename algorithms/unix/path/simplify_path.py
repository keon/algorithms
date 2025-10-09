"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

Reference: https://leetcode.com/problems/simplify-path/description/
"""

branch_coverage = {
    "for": False,
    "if": False,
    "elif": False,
}

import os
def simplify_path_v1(path):
    return os.path.abspath(path)

def simplify_path_v2(path):
    stack, tokens = [], path.split("/")
    for token in tokens:
        branch_coverage["for"] = True
        if token == ".." and stack:
            branch_coverage["if"] = True
            stack.pop()
        elif token != ".." and token != "." and token:
            branch_coverage["elif"] = True
            stack.append(token)

    return "/" + "/".join(stack)

def print_coverage():
    covered = 0
    print("branch coverage for `simplify_path_v2`:")
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
        if hit: covered += 1;
    print(f"Branch coverage: {covered / len(branch_coverage) * 100}")
    

# simplify_path_v2(".")
# simplify_path_v2("/../")
# simplify_path_v2("/home//foo/")
# simplify_path_v2("")
# simplify_path_v2("/home/../")
print_coverage()
