GRAY, BLACK = 0, 1

def top_sort_recursive(graph):
    """ Time complexity is the same as DFS, which is O(V + E)
        Space complexity: O(V)
    """
    order, enter, state = [], set(graph), {}
    
    def dfs(node):
        state[node] = GRAY
        #print(node)
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY:
                raise ValueError("cycle")
            if sk == BLACK:
                continue
            enter.discard(k)
            dfs(k)
        order.append(node)
        state[node] = BLACK
        
    while enter: dfs(enter.pop())
    return order

def top_sort(graph):
    """ Time complexity is the same as DFS, which is O(V + E)
        Space complexity: O(V)
    """
    order, enter, state = [], set(graph), {}
    
    def is_ready(node):
        lst = graph.get(node, ())
        if len(lst) == 0:
            return True
        for k in lst:
            sk = state.get(k, None)
            if sk == GRAY: 
                raise ValueError("cycle")
            if sk != BLACK:
                return False
        return True
        
    while enter:
        node = enter.pop()
        stack = []
        while True:
            state[node] = GRAY
            stack.append(node)
            for k in graph.get(node, ()):
                sk = state.get(k, None)
                if sk == GRAY: 
                    raise ValueError("cycle")
                if sk == BLACK: 
                    continue
                enter.discard(k)
                stack.append(k)
            while stack and is_ready(stack[-1]):
                node = stack.pop()
                order.append(node)
                state[node] = BLACK
            if len(stack) == 0:
                break
            node = stack.pop()
        
    return order
