# def lengthLongestPath(input):
#     maxlen = 0
#     pathlen = {0: 0}
#     for line in input.splitlines():
#         print("---------------")
#         print("line:", line)
#         name = line.strip('\t')
#         print("name:", name)
#         depth = len(line) - len(name)
#         print("depth:", depth)
#         if '.' in name:
#             maxlen = max(maxlen, pathlen[depth] + len(name))
#         else:
#             pathlen[depth + 1] = pathlen[depth] + len(name) + 1
#         print("maxlen:", maxlen)
#     return maxlen

# def lengthLongestPath(input):
#     paths = input.split("\n")
#     level = [0] * 10
#     maxLength = 0
#     for path in paths:
#         print("-------------")
#         levelIdx = path.rfind("\t")
#         print("Path: ", path)
#         print("path.rfind(\\t)", path.rfind("\t"))
#         print("levelIdx: ", levelIdx)
#         print("level: ", level)
#         level[levelIdx + 1] = level[levelIdx] + len(path) - levelIdx + 1
#         print("level: ", level)
#         if "." in path:
#             maxLength = max(maxLength, level[levelIdx+1] - 1)
#             print("maxlen: ", maxLength)
#     return maxLength

def length_longest_path(input):
    """
    :type input: str
    :rtype: int
    """
    curr_len, max_len = 0, 0    # running length and max length
    stack = []    # keep track of the name length
    for s in input.split('\n'):
        print("---------")
        print("<path>:", s)
        depth = s.count('\t')    # the depth of current dir or file
        print("depth: ", depth)
        print("stack: ", stack)
        print("curlen: ", curr_len)
        while len(stack) > depth:    # go back to the correct depth
            curr_len -= stack.pop()
        stack.append(len(s.strip('\t'))+1)   # 1 is the length of '/'
        curr_len += stack[-1]    # increase current length
        print("stack: ", stack)
        print("curlen: ", curr_len)
        if '.' in s:    # update maxlen only when it is a file
            max_len = max(max_len, curr_len-1)    # -1 is to minus one '/'
    return max_len


st = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdirectory1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
st2 = "a\n\tb1\n\t\tf1.txt\n\taaaaa\n\t\tf2.txt"
print("path:", st2)

print("answer:", length_longest_path(st2))
