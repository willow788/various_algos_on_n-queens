import random

#we will be implementing a hil climbing algorithm to solve the n queens problem
"""steps: 
1. Generate a random state of n queens on the board.
2. Check if the state is a solution (no conflicts).
3. If it is a solution, return the state.
4. If it is not a solution, generate all possible neighboring states by moving one queen to a different row in its column.
5. Evaluate the neighboring states and select the one with the fewest conflicts.
6. Repeat steps 2-5 until a solution is found or a maximum number of iterations is reached.
"""

def is_conflict(i, j, state):
    #check if two queens are in conflict
    row_1 = i
    row_2 = j
    col_1 = state[i]
    col_2 = state[j]

    #two queens should not be in the same row, column or diagonal
    if row_1 == row_2:
        return True
    elif col_1 == col_2:
        return True #this check is kinda useless
    elif abs(row_1 - row_2) == abs(col_1 - col_2):
        return True #same diagonal check
    else:
        return False

    

def heuristic_function(state):

    problems = 0 
    for i in range(len(state)):
        for j in range( i+1, len(state)):

            if is_conflict(i,j, state):
                problems += 1

    return problems

#need to generate all possible neighbours
def generating_neighbours(state):

    #initialising an empty list to store the neighbours
    neighbours = []

    #whats the value of n
    n = len(state)

    for col in range(n):

        for row in range(n):

            #if row is equal to the current row then dont move
            #we cant have our neighbour as self
            if row != state[col]:
                new_state = state.copy()

                #move the queen to new state
                new_state[col] = row

                neighbours.append(new_state)
    return neighbours

def hill_climbing_on_n_queens(n, max_steps = 1000):
    steps = 0

    while (steps < max_steps):
        steps += 1

        #starting with a random state
        current_State = random.sample(range(n), n)

        #printing the current state and its heuristic value
        print(f"current state : {current_State}")
        print(f"the heuristic value of the current state is : {heuristic_function(current_State)}")

        while True:

            #if there is no conflict then we have found a solution
            if heuristic_function(current_State) == 0:
                print("we got a solution!")
                print(f"final state obtained: {current_State} in total steps: {steps}")
                return current_State, steps

            #otherwise generate all possible neighbours
            neighbours = generating_neighbours(current_State)

            #finding the neighbour with the least heuristic value
            #as lower heuristic value means less conflicts
            next_state = min(neighbours, key=heuristic_function)

            #comparing current state with the next state
            current_heuristic = heuristic_function(current_State)
            next_neighbour_heuristic = heuristic_function(next_state)

            if current_heuristic >= next_neighbour_heuristic:
                print('we encountered a local maxima or a plateau')
                print(f"current state : {current_State} with heuristic value : {current_heuristic}")
                return None, steps

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)

def main():
            #we will run the hill climbing algorithm on n queens problem
    soln = hill_climbing_on_n_queens(8)
    if soln[0] is not None:
                
        print(f"solution obtained: {soln[0]} in total steps: {soln[1]}")
        print(f"final heuristic value of the solution is : {heuristic_function(soln[0])}")
        print("Final board:")
        print_board(soln[0])

if __name__ == "__main__":
    main()

    #this is just the basic hill climbing algorithm and it can be improved by using random restarts or simulated annealing to avoid local maxima and plateaus.
            