from collections import deque

'''
BFS time complexity : O(|E| + |V|)
BFS space complexity : O(|E| + |V|)

do BFS from (0,0) of the grid and get the minimum number of steps needed to get to the lower right column

only step on the columns whose value is 1

if there is no path, it returns -1

Ex 1)
If grid is
[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]], 
the answer is: 14

Ex 2)
If grid is
[[1,0,0],
 [0,1,1],
 [0,1,1]], 
the answer is: -1
'''

def maze_search(maze):
    flags = [False for i in range(10)]
    BLOCKED, ALLOWED = 0, 1
    UNVISITED, VISITED = 0, 1

    initial_x, initial_y = 0, 0

    if maze[initial_x][initial_y] == BLOCKED:
        flags[0] = True
        print(flags)
        print(len(list(filter(lambda x:(x == True) ,  flags))) / len(flags))   
        return -1
    
    else:
        flags[1] = True 
    
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    height, width = len(maze), len(maze[0])

    target_x, target_y = height - 1, width - 1

    queue = deque([(initial_x, initial_y, 0)])

    is_visited = [[UNVISITED for w in range(width)] for h in range(height)]
    is_visited[initial_x][initial_y] = VISITED

    while queue:
        flags[2] = True
        x, y, steps = queue.popleft()

        if x == target_x and y == target_y:
            flags[3] = True
            print(flags)
            print(len(list(filter(lambda x:(x == True) ,  flags))) / len(flags))                       
            return steps
        else:
            flags[4] = True
        for dx, dy in directions:
            flags[5] = True
            new_x = x + dx
            new_y = y + dy
            if not (0 <= new_x < height and 0 <= new_y < width):
                flags[6] = True
                continue
            else:
                flags[7]

            if maze[new_x][new_y] == ALLOWED and is_visited[new_x][new_y] == UNVISITED:
                flags[8] = True
                queue.append((new_x, new_y, steps + 1))
                is_visited[new_x][new_y] = VISITED
            else:
                flags[9] = True     
    print(len(list(filter(lambda x:(x == True) ,  flags))) / len(flags))                       
    print(flags)
    return -1 

if __name__ ==  "__main__":
    print("Coverages for ex1")
    ex1 = [[1,0,0],
            [0,1,1],
            [0,1,1]] 
    maze_search(ex1)
    print("Coverages for ex2")
    ex2 = [[1,0,1,1,1,1],
        [1,0,1,0,1,0],
        [1,0,1,0,1,1],
        [1,1,1,0,1,1]]
    maze_search(ex2)


 