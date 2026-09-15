#we will be combining the hill climbing algorithm with random restarts when we dont get a soln
import random

"""random state hill climbing algorithm for n queens problem
if we get a soln--- then good!
otherwise we will generate a new random state and start the hill climbing algorithm again
pretty simple to implement and understand
as we know that random states algorithms are asymptotically complete and hill climbing is not, thus we will be combining the two to get a better solution"""


def is_conflict(state_1, state_2, board):

    row_1 = state_1
    row_2 = state_2
    col_1 = board[state_1]
    col_2 = board[state_2]

    #conflict conditions
    #the second condition is never true by the way -- because of the way we are sampling


    if row_1 == row_2:
        return True
    elif col_1 == col_2:
        return True
    elif abs(row_1 - row_2) == abs(col_1 - col_2):
        return True
    else:
        return False

def heuristic_function(state):

    problems = 0 
    for i in range(len(state)):
        for j in range( i+1, len(state)):
            if is_conflict(i,j, state):
                problems += 1

    return problems

#generating all possible neighbours of a state
def generating_neighbours(state):
    #initialising an empty list to store the neighbours
    neighbours = []
    n = len(state)
    for first_column in range(n):
        for second_column in range(first_column + 1, n):
            new_state = state.copy()
            new_state[first_column], new_state[second_column] = (
                new_state[second_column],
                new_state[first_column],
            )
            neighbours.append(new_state)

    return neighbours

def random_states_hill_climbing(n, max_restarts = 1000):
    for restart_number in range(1, max_restarts + 1):

        #generating a random state
        curr_state = random.sample(range(n), n)

        #getting the heuristic value of the current state
        current_heuristic = heuristic_function(curr_state)

        print(f"restart number : {restart_number}")
        print(f"current state : {curr_state}")
        print(f"the heuristic value of the current state is : {current_heuristic}")

        while True:

            #if soln is found
            if current_heuristic == 0:
                print("we got a solution!")
                print(f"final state obtained : {curr_state} in total restarts : {restart_number}")
                return curr_state, restart_number

            neighbours = generating_neighbours(curr_state)

            #finding the neighbour with the least heuristic value
            best_neighbour = min(neighbours, key = heuristic_function)

            #checkning if neighbour si better or not
            heuristic_Neighbour = heuristic_function(best_neighbour)

            if heuristic_Neighbour >= current_heuristic:
                print('terminal case!..  restarting!')
                break
            else:

                #move up to the neighbour
                curr_state = best_neighbour
                current_heuristic = heuristic_Neighbour
                print(f"current state : {curr_state}")
                print(f"current state heuristic value : {current_heuristic}")

        print('no solution found in this restart, moving to next restart')

    print('max restarts reached, no solution found!')
    return None, max_restarts


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
    soln = random_states_hill_climbing(8)
    if soln[0] is not None:
        print(f"solution found : {soln[0]} in total restarts : {soln[1]}")
        print_board(soln[0])
    else:
        print('no solution found!')

if __name__ == "__main__":
    main()
    
    