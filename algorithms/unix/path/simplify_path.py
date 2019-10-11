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

import os
def simplify_path_v1(path):
    return os.path.abspath(path)

def simplify_path_v2(path):
    stack, tokens = [], path.split("/")
    for token in tokens:
        if token == ".." and stack:
            stack.pop()
        elif token != ".." and token != "." and token:
            stack.append(token)
    return "/" + "/".join(stack)
