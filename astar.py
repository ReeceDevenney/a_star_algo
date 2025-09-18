class Node:
    def __init__(self, state, parent, gscore, hscore, move):
        self.state = state
        self.parent = parent
        self.gscore = gscore
        self.hscore = hscore
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
    for i in range(len(frontier)):
        if (node.hscore + node.gscore) <= (frontier[i].hscore + frontier[i].gscore):
            frontier.insert(i, node)
            break

start = [[0,1,3], [4,2,5], [7,8,6]]

goal =[[1,2,0], 
        [4,5,3], 
        [7,8,6]]
 
start2 = [[1,2,3], 
        [4,5,6], 
        [7,8,0]]


def print_solution(current_node, goal):
    print("current node")
    print(f"""\n
    {current_node.state[0]}\n
    {current_node.state[1]}\n
    {current_node.state[2]}\n""")
    print("goal state")
    print(f"""\n
        {goal[0]}\n
        {goal[1]}\n
        {goal[2]}\n""")
    print("solution found")

def solve_puzzle(start, goal):
    #start = get_array(0)
    #goal = get_array(1)
    frontier = []
    expanded = 0
    frontier.append(Node(start, None, 0, calculate_manhattan_hscore(start, goal), None))
    
    for i in range(100):
        current_node = frontier.pop(0)
        print(f"""\n
        {current_node.state[0]}\n
        {current_node.state[1]}\n
        {current_node.state[2]}\n""") 
        print(current_node.hscore)
        expanded += 1
        zero_loc = find_tile(current_node.state, 0)
        #North
        if current_node.state[zero_loc[0] - 1][zero_loc[1]]:
            new_state = current_node.state
            new_state[zero_loc[0]][zero_loc[1]] = new_state[zero_loc[0] - 1][zero_loc[1]]
            new_state[zero_loc[0] - 1][zero_loc[1]] = 0
            
            new_node = Node(new_state, current_node, current_node.gscore + 1, calculate_manhattan_hscore(new_state, goal), "N")
            
            if new_node.hscore == 0:
                print_solution(current_node, goal)
                return

            add_to_frontier(new_node, frontier)
        #South

        #East
        #West
    
solve_puzzle(start2, goal)
