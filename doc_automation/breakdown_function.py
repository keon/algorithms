import inspect


def dfs(root, sum, ls, res):
    if root.left is None and root.right is None and (root.val == sum):
        ls.append(root.val)
        res.append(ls)
    if root.left is not None:
        dfs(root.left, sum - root.val, ls + [root.val], res)
    if root.right is not None:
        dfs(root.right, sum - root.val, ls + [root.val], res)


def create_control_graph(func):
    lines = inspect.getsource(func).split('\n')
    nodes = []
    edges = []
    for i, line in enumerate(lines):
        if line.startswith('if'):
            nodes.append(line.strip())
            if ':' in lines[i + 1]:
                edges.append((line.strip(), lines[i + 1].strip()))
            else:
                edges.append((line.strip(), lines[i + 2].strip()))
        elif line.strip():
            nodes.append(line.strip())
    graph = 'digraph G {\n'
    for node in nodes:
        if node.startswith('if'):
            graph += f'    "{node}" [shape=diamond];\n'
        else:
            graph += f'    "{node}" [shape=box];\n'
    for src, dest in edges:
        graph += f'    "{src}" -> "{dest}";\n'
    graph += '}'
    return graph


if __name__ == '__main__':
    print(create_control_graph(dfs))
