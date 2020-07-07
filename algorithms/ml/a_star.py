import random


class Node:
    """ Simple node class for A* pathfinding """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.f = 0
        self.h = 0

    def __eq__(self, other):
        self.position == other.position


def make(n):
    maze = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            x = random.random()
            if x > 0.7:
                maze[i][j] = 1

    return maze


def astar(maze, start, end):
    """ Returns a list of tuples as a path from the given end in the given maze"""

    # Defining a start and end Node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.f = end_node.h = 0

    # Initialize open and closed list
    open_list = []
    closed_list = []

    # Adding the start node in open list
    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            # lower f means better path
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Popping the current index off the open list and adding the node in closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal? Cool. Now backtrack
        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Generate Children

        children = []
        for new_position in [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]:  # Adjacent squares

            # Getting node position
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1],
            )

            # Checking if in-range or not :
            if (
                node_position[0] > (len(maze) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(maze[len(maze) - 1]) - 1)
                or node_position[1] < 0
            ):
                continue

            # See if walkable or not
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Creating new node
            new_node = Node(current_node, node_position)

            # Confirming the Child
            children.append(new_node)

        # Now, Loop through the children
        for child in children:

            # Child is on the closed list?
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # If not? start making f,g and h values
            child.g = current_node.g + 1  ## why not child.parent.g?
            ## Eucledian heuristic without sqrt? Genius
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                (child.position[1] - end_node.position[1]) ** 2
            )
            child.f = child.h + child.g

            # Child Already in Open List?
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            # Add the child in the open list
            open_list.append(child)


def showPath(maze, path, n, start, end):
    dupMaze = maze
    # General Display
    for i in range(n):
        for j in range(n):
            if dupMaze[i][j] == 1:
                dupMaze[i][j] = "|"
            elif dupMaze[i][j] == 0:
                dupMaze[i][j] = " "

    dupMaze[start[0]][start[1]] = "S"
    dupMaze[end[0]][end[1]] = "E"
    for i in path[1:-1]:
        dupMaze[i[0]][i[1]] = "."

    return dupMaze


def main():
    print("Started!")
    maze = make(random.randint(3, 10))

    print(" You maze is")
    for i in maze:
        for j in i:
            print(j)
        print()

    start = tuple(map(int, input("Please Enter the starting Coordinates: ").split()))
    end = tuple(map(int, input("Please Enter the ending Coordinates: ").split()))

    path = astar(maze, start, end)

    display = showPath(maze, path, len(maze[0]), start, end)
    print("\n\n")
    for i in display:
        for j in i:
            print(j)
        print()

    print("The Perfect Path will be {}".format(path))


if __name__ == "__main__"
:
    main()

#By cosmos

