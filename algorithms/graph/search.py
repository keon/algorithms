# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to Clemson University and the authors.
# 
# Authors: Pei Xu (peix@g.clemson.edu) and Ioannis Karamouzas (ioannis@g.clemson.edu)
#

"""
 In this assignment, the task is to implement different search algorithms to find 
 a path from a given start cell to the goal cell in a 2D grid map.

 To complete the assignment, you must finish three functions:
   depth_first_search (line 148), uniform_cost_search (line 224), 
   and astar_search (line 264).

 During the search, a cell is represented using a tuple of its location
 coordinates.
 For example:
   the cell at the left-top corner is (0, 0);
   the cell at the first row and second column is (0, 1);
   the cell at the second row and first column is (1, 0).
 You need put these tuples into the open set or/and closed set properly
 during searching.
"""

# ACTIONS defines how to reach an adjacent cell from a given cell
# Important: please check that a cell within the bounds of the grid
# when try to access it.
ACTIONS = (
    (-1,  0), # go up
    ( 0, -1), # go left
    ( 1,  0), # go down
    ( 0,  1)  # go right
)

from utils.search_app import OrderedSet, Stack, Queue, PriorityQueue
"""
 Four different structures are provided as the containers of the open set
 and closed set.

 OrderedSet is an ordered collections of unique elements.

 Stack is an LIFO container whose `pop()` method always pops out the last
 added element. 

 Queue is an FIFO container whose `pop()` method always pops out the first
 added element.

 PriorityQueue is a key-value container whose `pop()` method always pops out
 the element whose value has the highest priority.

 All of these containers are iterable but not all of them are ordered. Use
 their pop() methods to ensure elements are popped out as expected.


 Common operations of OrderedSet, Stack, Queue, PriorityQueue
   len(s): number of elements in the container s
   x in s: test x for membership in s
   x not in s: text x for non-membership in s
   s.clear(): clear s
   s.remove(x): remove the element x from the set s;
                nothing will be done if x is not in s


 Unique operations of OrderedSet:
   s.add(x): add the element x into the set s;
             nothing will be done if x is already in s
   s.pop(): return and remove the LAST added element in s;
            raise IndexError if s is empty 
   s.pop(last=False): return and remove the FIRST added element in s;
            raise IndexError if s is empty 
 Example:
   s = Set()
   s.add((1,2))    # add a tuple element (1,2) into the set
   s.remove((1,2)) # remove the tuple element (1,2) from the set
   s.add((1,1))
   s.add((2,2))
   s.add((3,3))
   x = s.pop()
   assert(x == (3,3))
   assert((1,1) in s and (2,2) in s)
   assert((3,3) not in s)
   x = s.pop(last=False)
   assert(x == (1,1))
   assert((2,2) in s)
   assert((1,1) not in s)
   

 Unique operations of Stack:
   s.append(x): add the element x into the back of the stack s
   s.pop(): return and remove the LAST added element in the stack s;
            raise IndexError if s is empty
 Example:
   s = Stack()
   s.add((1,1))
   s.add((2,2))
   x = s.pop()
   assert(x == (2,2))
   assert((1,1) in s)
   assert((2,2) not in s)


 Unique operations of Queue:
   s.append(x): add the element x into the back of the queue s
   s.pop(): return and remove the FIRST added element in the queue s;
            raise IndexError if s is empty
 Example:
   s = Queue()
   s.add((1,1))
   s.add((2,2))
   x = s.pop()
   assert(x == (1,1))
   assert((2,2) in s)
   assert((1,1) not in s)


 Unique operations of PriorityQueue:
   PriorityQueue(order="min", f=lambda v: v): build up a priority queue
       using the function f to compute the priority based on the value
       of an element
   s.put(x, v): add the element x with value v into the queue
                update the value of x if x is already in the queue
   s.get(x): get the value of the element x
            raise KeyError if x is not in s
   s.pop(): return and remove the element with highest priority in s;
            raise IndexError if s is empty
            if order is "min", the element with minimum f(v) will be popped;
            if order is "max", the element with maximum f(v) will be popped.
 Example:
   s = PriorityQueue(order="max", f=lambda v: abs(v))
   s.put((1,1), -1)
   s.put((2,2), -20)
   s.put((3,3), 10)
   x, v = s.pop()  # the element with maximum value of abs(v) will be popped
   assert(x == (2,2) and v == -20)
   assert(x not in s)
   assert(x.get((1,1)) == -1)
   assert(x.get((3,3)) == 10)
"""


# use math library if needed
import math

def depth_first_search(grid_size, start, goal, obstacles, costFn, logger):
    """
    DFS algorithm finds the path from the start cell to the
    goal cell in the 2D grid world.
    
    Parameters
    ----------
    grid_size: tuple, (n_rows, n_cols)
        (number of rows of the grid, number of cols of the grid)
    start: tuple, (row, col)
        location of the start cell;
        row and col are counted from 0, i.e. the 1st row is 0
    goal: tuple, (row, col)
        location of the goal cell
    obstacles: tuple, ((row, col), (row, col), ...)
        locations of obstacles in the grid
        the cells where obstacles are located are not allowed to access 
    costFn: a function that returns the cost of landing to a cell (x,y)
         after taking an action. The default cost is 1, regardless of the
         action and the landing cell, i.e. every time the agent moves NSEW
         it costs one unit. 
    logger: a logger to visualize the search process.
         Do not do anything to it.

   

    Returns
    -------
    movement along the path from the start to goal cell: list of actions
        The first returned value is the movement list found by the search
        algorithm from the start cell to the end cell.
        The movement list should be a list object who is composed of actions
        that should made moving from the start to goal cell along the path
        found the algorithm.
        For example, if nodes in the path from the start to end cell are:
            (0, 0) (start) -> (0, 1) -> (1, 1) -> (1, 0) (goal)
        then, the returned movement list should be
            [(0,1), (1,0), (0, -1)]
        which means: move right, down, left.

        Return an EMPTY list if the search algorithm fails finding any
        available path.
        
    closed set: list of location tuple (row, col)
        The second returned value is the closed set, namely, the cells are expanded during search.
    """
    n_rows, n_cols = grid_size
    start_row, start_col = start
    goal_row, goal_col = goal

    ##########################################
    # Choose a proper container yourself from
    # OrderedSet, Stack, Queue, PriorityQueue
    # for the open set and closed set.
    open_set = Stack()
    closed_set = OrderedSet()
    list_store = Stack()
    ##########################################

    ##########################################
    # Set up visualization logger hook
    # Please do not modify these four lines
    closed_set.logger = logger
    logger.closed_set = closed_set
    open_set.logger = logger
    logger.open_set = open_set
    ##########################################

    movement = []
    # ----------------------------------------
    # finish the code below
    # ----------------------------------------
#############################################################################
    import numpy
    open_set.add((start_row, start_col))
    #stack to find path
    list_store.add((start, [start]))
    while len(open_set) != 0:
        x = open_set.pop()
        node, path = list_store.pop()
        if x == goal:
        	break
        closed_set.add(x)
        #N, W, S, E
        children = [(x[0]-1, x[1]), (x[0], x[1]-1), (x[0]+1, x[1]), (x[0], x[1]+1)]
        for child in children:
            #check for out of bounds or obstacle
        	if child[0] >= n_rows or child[0] < 0 or child[1] >= n_cols or child[1] < 0:
        		continue
        	if child in obstacles:
        		continue
            #check if not in open or closed
        	if child not in closed_set:
        	    open_set.add(child)
        	    #adding to final path
        	    list_store.add((child, path+[child]))
    #calculating movement tuples 	    
    x = path.pop()
    while len(path) != 0:
    	y = path.pop()
    	move = ((x[0]-y[0]), (x[1]-y[1]))
    	x = y
    	movement.append(move)
    movement.reverse()
    
#############################################################################
    return movement, closed_set

def uniform_cost_search(grid_size, start, goal, obstacles, costFn, logger):
    """
    Uniform-cost search algorithm finds the optimal path from 
    the start cell to the goal cell in the 2D grid world. 
    
    After expanding a node, to retrieve the cost of a child node at location (x,y), 
    please call costFn((x,y)). In all of the grid maps, the cost is always 1.

    See depth_first_search() for details.
    """
    n_rows, n_cols = grid_size
    start_row, start_col = start
    goal_row, goal_col = goal

    ##########################################
    # Choose a proper container yourself from
    # OrderedSet, Stack, Queue, PriorityQueue
    # for the open set and closed set.
    #open_set = OrderedSet()
    open_set = PriorityQueue(order="min", f=lambda v: v)
    closed_set = PriorityQueue(order="min", f=lambda v: v)
    list_store = PriorityQueue(order="min", f=lambda v: v)
    ##########################################

    ##########################################
    # Set up visualization logger hook
    # Please do not modify these four lines
    closed_set.logger = logger
    logger.closed_set = closed_set
    open_set.logger = logger
    logger.open_set = open_set
    ##########################################
    import numpy
    movement = []
    costs = numpy.empty([n_rows, n_cols])
    # ----------------------------------------
    # finish the code below
    # ----------------------------------------
#############################################################################
    costs[start_row][start_col] = 0
    open_set.put(start, costs[start_row][start_col])
    #list_store.put((start, [start]), costs[start_row][start_col])
    while len(open_set) != 0:
    	x = open_set.pop()
    	if x[0] == goal:
    		break
    	closed_set.put(x[0], x[1])
    	children = [(x[0][0]-1, x[0][1]), (x[0][0], x[0][1]-1), 
    		(x[0][0]+1, x[0][1]), (x[0][0], x[0][1]+1)]
    	for child in children:
        	if child[0] >= n_rows or child[0] < 0 or \
        		child[1] >= n_cols or child[1] < 0:
        		continue
        	if child in obstacles:
        		continue
            #check if not in open or closed
        	if child not in closed_set:
        		costs[child[0]][child[1]]=costs[x[0][0]][x[0][1]]+costFn(child)
        		open_set.put(child, costs[child[0]][child[1]])
    #populate movement
    x = goal
    mini = costs[x[0]][x[1]]
    path = [goal]
    while x != start:
    	children = [(x[0]-1, x[1]), (x[0], x[1]-1), (x[0]+1, x[1]), (x[0], x[1]+1)]
    	for child in children:
    		#ignoring nodes not in closed_set
    		if child not in closed_set:
    			continue
    		#ignoring out of bounds
    		if child[0] >= n_rows or child[0] < 0 or \
    			child[1] >= n_cols or child[1] < 0:
        		continue
        	#ignoring obstacles
    		if child in obstacles:
    			continue
    		if costs[child[0]][child[1]] < mini:
    			mini = costs[child[0]][child[1]]
    			mini_node = child
    	#adding to final path
    	path = path + [mini_node]
    	x = mini_node
    #calculating movement tuples
    x = path.pop()
    while len(path) != 0:
    	y = path.pop()
    	move = ((y[0]-x[0]), (y[1]-x[1]))
    	x = y
    	movement.append(move)

#############################################################################
    return movement, closed_set

def astar_search(grid_size, start, goal, obstacles, costFn, logger):
    """
    A* search algorithm finds the optimal path from the start cell to the
    goal cell in the 2D grid world.

    After expanding a node, to retrieve the cost of a child node at location (x,y), 
    please call costFn((x,y)). In all of the grid maps, the cost is always 1.  

    See depth_first_search() for details.    
    """
    n_rows, n_cols = grid_size
    start_row, start_col = start
    goal_row, goal_col = goal

    ##########################################
    # Choose a proper container yourself from
    # OrderedSet, Stack, Queue, PriorityQueue
    # for the open set and closed set.
    open_set = PriorityQueue(order="min", f=lambda v: v)
    closed_set = PriorityQueue(order="min", f=lambda v: v)
    ##########################################

    ##########################################
    # Set up visualization logger hook
    # Please do not modify these four lines
    closed_set.logger = logger
    logger.closed_set = closed_set
    open_set.logger = logger
    logger.open_set = open_set
    ##########################################
    import numpy
    movement = []
    #g(n)
    costs = numpy.empty([n_rows, n_cols])
    #costs = [None] * (n_rows * n_cols)
    #y*cols+x
    # ----------------------------------------
    # finish the code below to implement a Manhattan distance heuristic
    # ----------------------------------------
    def heuristic(row, col):
    	#calculate Manhattan distance
    	distance = abs((goal_row-row)) + abs((goal_col-col))
    	return distance
#############################################################################
    distance = heuristic(start_row, start_col)
    costs[start_row, start_col] = 0
    open_set.put(start, distance)
    while len(open_set) != 0:
    	x = open_set.pop()
    	if x[0] == goal:
    		break
    	closed_set.put(x[0], x[1])
    	children = [(x[0][0]-1, x[0][1]), (x[0][0], x[0][1]-1), 
    		(x[0][0]+1, x[0][1]), (x[0][0], x[0][1]+1)]
    	for child in children:
    		if child[0] >= n_rows or child[0] < 0 or \
    			child[1] >= n_cols or child[1] < 0:
        		continue
    		if child in obstacles:
        		continue
            #check if not in open or closed
    		if child not in closed_set:
    			#update g(n)
    			costs[child[0]][child[1]] = costs[x[0][0]][x[0][1]] + 1
    			distance = heuristic(child[0], child[1])
    			distance = distance + costs[child[0]][child[1]]
    			open_set.put(child, distance)
    #finding movements
    x = goal
    mini = costs[x[0]][x[1]]
    path = [goal]
    while x != start:
    	#finding nearest node with lowest priority
    	children = [(x[0]-1, x[1]), (x[0], x[1]-1), (x[0]+1, x[1]), (x[0], x[1]+1)]
    	for child in children:
    		#ignoring nodes not in closed_set
    		if child not in closed_set:
    			continue
    		#ignoring out of bounds 
    		if child[0] >= n_rows or child[0] < 0 or \
    			child[1] >= n_cols or child[1] < 0:
       			continue
       		#ignoring obstacles
    		if child in obstacles:
    			continue
    		if costs[child[0]][child[1]] < mini:
    			mini = costs[child[0]][child[1]]
    			mini_node = child
    	#adding to final path
    	path = path + [mini_node]
    	x = mini_node
    	print(x)

    #calculating for movement tuples
    x = path.pop()
    while len(path) != 0:
    	y = path.pop()
    	move = ((y[0]-x[0]), (y[1]-x[1]))
    	x = y
    	movement.append(move)
    	


#############################################################################
    return movement, closed_set

if __name__ == "__main__":
    # make sure actions and cost are defined correctly
    from utils.search_app import App
    assert(ACTIONS == App.ACTIONS)

    import tkinter as tk

    algs = {
        "Depth-First": depth_first_search,
        "Uniform Cost Search": uniform_cost_search,
        "A*": astar_search
    }

    root = tk.Tk()
    App(algs, root)
    root.mainloop()

