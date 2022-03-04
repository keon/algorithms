"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

* Did you consider the case where path = "/../"?
    In this case, you should return "/".
* Another corner case is the path might contain multiple slashes '/' together,
    such as "/home//foo/". In this case, you should ignore redundant
    slashes and return "/home/foo".
"""
def simplify_path(path):
    """
    :type path: str
    :rtype: str
    """
    skip = {'..', '.', ''}
    stack = []
    paths = path.split('/')
    for tok in paths:
        if tok == '..':
            if stack:
                stack.pop()
        elif tok not in skip:
            stack.append(tok)
    return '/' + '/'.join(stack)
