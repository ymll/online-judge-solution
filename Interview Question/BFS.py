import queue
def get_maze_value(x ,y):
    if x < 0 or x >= len(maze):
        return None
    if y < 0 or y >= len(maze[0]):
        return None
    return maze[x][y]

def is_visited(node, visited):
    return node in visited

def check_valid_neighbour(node, visited):
    return get_maze_value(node[0], node[1]) == 0 and not is_visited(node, visited)

def get_neighbours(x, y, visited):
    neighbours = []
    top = (x, y-1)
    left = (x-1, y)
    right = (x+1, y)
    down = (x, y+1)
    for node in [top, left, right, down]:
        if check_valid_neighbour(node, visited):
            neighbours.append(node)
    return neighbours

def escape(maze, startX, startY, goalX, goalY):
    start = maze[startX][startY]
    end = maze[goalX][goalY]
    if start == 1 or end == 1:
	    return -1
    #BFS
    q = queue.Queue()
    steps = 0
    q.put((startX, startY, steps))
    visited = []
    while not q.empty():
        current_node_x, current_node_y, steps = q.get()
        visited.append((current_node_x, current_node_y))
        # get nearby nodes and put into the queue
        neighbours = get_neighbours(current_node_x, current_node_y, visited)
        if neighbours:
            for neighbour in neighbours:
                if neighbour[0] == goalX and neighbour[1] == goalY:
                    return steps+1
                q.put(neighbour + (steps+1, ))
    return -1
#  0123
#0|0010
#1|0000
#2|1110
#3|0000

maze = [[0, 0, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0], [0, 0, 0, 0]]
print("shortest path: ", escape(maze, 0, 0, 0, 3))

