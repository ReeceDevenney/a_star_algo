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

def solve_puzzle():
    start = get_array(0)
    goal = get_array(1)
    frontier = []
    expanded = 0
    frontier.append(Node(start, None, 0, calculate_manhattan_hscore(start, goal), None))
    
    print(frontier[0].hscore)

print(get_array(0))
