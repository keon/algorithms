def topView(head, dis, level, dict):

    if head is None:
        return

    if dis not in dict or level < dict[dis][1]:
        dict[dis] = (head.key, level)
    topView(head.left, dis - 1, level + 1, dict)
    topView(head.right, dis + 1, level + 1, dict)

def printTopView(head):
    dict = {}

    topView(head, 0, 0, dict)
    for key in sorted(dict.keys()):
        print(dict.get(key)[0], end=' ')