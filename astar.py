import copy

class Node:
    def __init__(self, state, parent, gscore, hscore, move):
        self.state = state #The Board
        self.parent = parent #Parent Node
        self.gscore = gscore #Integer representing G Score
        self.hscore = hscore #Integer Representing H Score
        #the direction the 0 moved in the parent state to produce this state
        self.move = move

#finds the x y coordinate of a specific valued tile
def find_tile(state, value):
    for i in range(3):
        for k in range(3):
            if state[i][k] == value:
                return [i, k]
    return[0,0]

#calculates the h score using the manhattan heuristic
def calculate_manhattan_hscore(state, goal):
    hscore = 0
    for i in range(3):
        for k in range(3):
            if state[i][k] != 0:
                goal_pos = find_tile(goal, state[i][k])
                hscore += abs(i - goal_pos[0])
                hscore += abs(k - goal_pos[1])
    return(hscore)

#calculates hscore +1 for each tile that is not in the solution position
def calculate_wrong_tiles_hscore(state, goal):
    hscore = 0
    for i in range(3):
        for k in range(3):
            if state[i][k] != 0:
                goal_pos = find_tile(goal, state[i][k])
                if goal_pos[0] != i or goal_pos[1] != k:
                    hscore += 1
    return(hscore)

#build a board from user input    
def get_array(num):
    empty_array = [[], [], []]
    input_values = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,"6": 0, "7": 0, "8": 0,}
    remaining_values = ["0, ","1, ","2, ","3, ","4, ","5, ","6, ","7, ","8", ]
    if num == 0:
        print("Please provide the order of how the tiles will start, starting with the top row, going from left to right, no duplicate tiles, ranging from 0-8 with 0 being the empty space")
        for i in range(3):
            for k in range(3):
                while True:
                    print(f"remaining values {remaining_values[0]}{remaining_values[1]}{remaining_values[2]}{remaining_values[3]}{remaining_values[4]}{remaining_values[5]}{remaining_values[6]}{remaining_values[7]}{remaining_values[8]}")
                    value = input(f"""current board:\n
                        {empty_array[0]}\n
                        {empty_array[1]}\n
                        {empty_array[2]}\n
                        next tile: """)
                    if value not in input_values:
                        print(f"{value} is not between 0-8, please provide a valid value")
                    elif input_values[value] == 0:
                        input_values[value] = 1
                        empty_array[i].append(int(value))
                        remaining_values[int(value)] = ""
                        break
                    elif input_values[value] == 1:
                        print(f"{value} is already on the board, please provide unique values for each tile")
    if num == 1:
        print("Please provide the order of how the tiles should end, starting with the top row, going from left to right, no duplicate tiles, ranging from 0-8 with 0 being the empty space")
        for i in range(3):
            for k in range(3):
                while True:
                    print(f"remaining values {remaining_values[0]}{remaining_values[1]}{remaining_values[2]}{remaining_values[3]}{remaining_values[4]}{remaining_values[5]}{remaining_values[6]}{remaining_values[7]}{remaining_values[8]}")
                    value = input(f"""current board:\n
                        {empty_array[0]}\n
                        {empty_array[1]}\n
                        {empty_array[2]}\n
                        next tile: """)
                    if value not in input_values:
                        print(f"{value} is not between 0-8, please provide a valid value")
                    elif input_values[value] == 0:
                        input_values[value] = 1
                        empty_array[i].append(int(value))
                        remaining_values[int(value)] = ""
                        break
                    elif input_values[value] == 1:
                        print(f"{value} is already on the board, please provide unique values for each tile")
    print(f"""\n
        {empty_array[0]}\n
        {empty_array[1]}\n
        {empty_array[2]}\n""")    
    return empty_array

def add_to_frontier(node, frontier):
    if len(frontier) == 0:
        frontier.append(node)
        return
    for i in range(len(frontier)):
        if (node.hscore + node.gscore) <= (frontier[i].hscore + frontier[i].gscore):
            frontier.insert(i, node)
            return
    frontier.append(node)

# walk back up the tree to construct the work path
def solution_path(node):
    if node.move == None:
        return ""
    solution = f"{node.move}"
    next_node = copy.deepcopy(node.parent)
    while True:
        if next_node.parent == None:
            return solution
        solution = next_node.move + "->" + solution
        next_node = copy.deepcopy(next_node.parent)
        
#function to print out solution information
def print_solution(current_node, goal):
    print("current node below")
    print(f"""
    {current_node.state[0]}\n
    {current_node.state[1]}\n
    {current_node.state[2]}\n""")
    print("goal state")
    print(f"""\n
        {goal[0]}\n
        {goal[1]}\n
        {goal[2]}\n""")
    print("solution found")

def solve_puzzle(start, goal, h_function):
    #start = get_array(0)
    #goal = get_array(1)
    #frontier to store all created nodes
    frontier = []
    #counter for how many nodes were expanded
    expanded = 0
    generatedNodes = 1
    frontier.append(Node(start, None, 0, h_function(start, goal), None))
    if frontier[0].hscore == 0:
                print_solution(frontier[0], goal)
                print(f"expanded: {expanded}")
                print(f"total nodes: {expanded + len(frontier)}")
                print(solution_path(frontier[0]))
                return

    
    for i in range(100000):
        if i == 99999:
            print("no solution found")
            return 0

        current_node = frontier.pop(0)
        print(f"""\n
        {current_node.state[0]}\n
        {current_node.state[1]}\n
        {current_node.state[2]}\n""") 
        print(f"F Value: {current_node.hscore + current_node.gscore}")
        expanded += 1
        zero_loc = find_tile(current_node.state, 0)
        #Logic to see if 0 can be moved north
        if zero_loc[0] - 1 != -1:

            #Adding 1 to the total node count!
            generatedNodes += 1

            new_North_state = copy.deepcopy(current_node.state)
            new_North_state[zero_loc[0]][zero_loc[1]] = new_North_state[zero_loc[0] - 1][zero_loc[1]] #WHAT IS GOING ON WITH POINTERS HERE
            new_North_state[zero_loc[0] - 1][zero_loc[1]] = 0
            
            new_North_node = Node(new_North_state, current_node, copy.deepcopy(current_node.gscore) + 1, h_function(new_North_state, goal), "N")
            
            if new_North_node.hscore == 0:
                print_solution(new_North_node, goal)
                print(f"expanded: {expanded}")
                print(f"total nodes: {generatedNodes}")
                print(solution_path(new_North_node))
                return

            add_to_frontier(new_North_node, frontier)
        #Logic to see if 0 can be moved south
        if zero_loc[0] + 1 != 3:

            generatedNodes += 1

            new_South_state = copy.deepcopy(current_node.state)
            new_South_state[zero_loc[0]][zero_loc[1]] = new_South_state[zero_loc[0] + 1][zero_loc[1]]
            new_South_state[zero_loc[0] + 1][zero_loc[1]] = 0
            
            new_South_node = Node(new_South_state, current_node, copy.deepcopy(current_node.gscore) + 1, h_function(new_South_state, goal), "S")
            
            if new_South_node.hscore == 0:
                print_solution(new_South_node, goal)
                print(f"expanded: {expanded}")
                print(f"total nodes: {generatedNodes}")
                print(solution_path(new_South_node))
                return

            add_to_frontier(new_South_node, frontier)
        #Logic to see if 0 can be moved east
        if zero_loc[1] + 1 != 3:

            generatedNodes += 1

            new_East_state = copy.deepcopy(current_node.state)
            new_East_state[zero_loc[0]][zero_loc[1]] = new_East_state[zero_loc[0]][zero_loc[1] + 1]
            new_East_state[zero_loc[0]][zero_loc[1] + 1] = 0
            
            new_East_node = Node(new_East_state, current_node, copy.deepcopy(current_node.gscore) + 1, h_function(new_East_state, goal), "E")
            
            if new_East_node.hscore == 0:
                print_solution(new_East_node, goal)
                print(f"expanded: {expanded}")
                print(f"total nodes: {generatedNodes}")
                print(solution_path(new_East_node))
                return

            add_to_frontier(new_East_node, frontier)
        #Logic to see if 0 can be moved west
        if zero_loc[1] - 1 != -1:

            generatedNodes += 1

            new_West_state = copy.deepcopy(current_node.state)
            new_West_state[zero_loc[0]][zero_loc[1]] = new_West_state[zero_loc[0]][zero_loc[1] - 1]
            new_West_state[zero_loc[0]][zero_loc[1] - 1] = 0
            
            new_West_node = Node(new_West_state, current_node, copy.deepcopy(current_node.gscore) + 1, h_function(new_West_state, goal), "W")
            
            if new_West_node.hscore == 0:
                print_solution(new_West_node, goal)
                print(f"expanded: {expanded}")
                print(f"total nodes: {generatedNodes}")
                print(solution_path(new_West_node))
                return

            add_to_frontier(new_West_node, frontier)
start = [[2,0,3],
         [1,8,4],
         [7,6,5]]


goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]


solve_puzzle(start, goal, calculate_wrong_tiles_hscore)

