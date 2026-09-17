#now we will be adding side ways walk to the hill climbing algorithms in order to escape from plateaus
import random
import time
import matplotlib.pyplot as plt



def is_conflict(state_1, state_2, board):
    row_1 = state_1
    row_2 = state_2
    col_1 = board[row_1]
    col_2 = board[row_2]

    #conflict conditions
    if row_1 == row_2:
        return True
    elif col_1 == col_2:
        return True
    elif abs(row_1 - row_2) == abs(col_1-col_2):
        return True
    else:
        return False

#defining the heuristic function
def heuristic_function(state):

    #counting the no of conflicts
    problems = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if is_conflict(i,j,state):
                problems += 1

    return problems

def generating_neighbours(state):
    #initialising an empty list to store the neighbours
    neighbours = []
    
    #how many queens we have 
    queens_no = len(state)
    
    for first_Col in range(queens_no):
        for second_Col in range(first_Col + 1, queens_no):
                new_State = state.copy()
                new_State[first_Col], new_State[second_Col] = (
                    new_State[second_Col],
                    new_State[first_Col],
                )
                neighbours.append(new_State)
    
    return neighbours

def hill_climbing_with_sidewise_walk_added(n, max_restarts=10000, max_steps=1000, max_sideways_moves=100):

    # if the max steps is none then take 2n steps with n being the no of queens
    if max_steps is None:
        max_steps = 2 * n

    for restart_number in range(1, max_restarts + 1):
        steps = 0
        sideways_move_count = 0

        # generating a random state
        current_State = random.sample(range(n), n)
        current_State_heuristic = heuristic_function(current_State)

        # printing the current state and its heuristic value
        print(f"Current state  = {current_State}")
        print(f"Current state's heuristic function value : {current_State_heuristic}")
        print(f"Current restart number: {restart_number}")

        while steps < max_steps:
            steps += 1

            # if the current state is the soln then return it
            if current_State_heuristic == 0:
                print("we have got a solution!")
                print("the current state is the solution!")
                print(f"current solution : {current_State}")
                print(f"current state's heuristic value: {current_State_heuristic} with {restart_number} restarts")
                return current_State

            neighbours = generating_neighbours(current_State)
            best_neigbour = min(neighbours, key=heuristic_function)
            best_neigbour_heuristic = heuristic_function(best_neigbour)

            # main conditions
            if best_neigbour_heuristic < current_State_heuristic:
                current_State = best_neigbour
                current_State_heuristic = best_neigbour_heuristic
                sideways_move_count = 0

            elif best_neigbour_heuristic > current_State_heuristic:
                print('we may be stuck in a local optima')
                random_neigbor = random.choice(neighbours)
                current_State = random_neigbor
                current_State_heuristic = heuristic_function(random_neigbor)
                sideways_move_count = 0
                print(f"After random restart due to local optima we are doing random walk to a random neighbour.")
                print(f"The current state now will be {current_State} with heuristic {current_State_heuristic}")

            else:
                if sideways_move_count < max_sideways_moves:
                    print('We will perform a sideways move to any of the neighbours and do hill climbing again.')
                    current_State = best_neigbour
                    current_State_heuristic = best_neigbour_heuristic
                    sideways_move_count += 1
                else:
                    print('You have reached the maximum number of sideways moves.. restarting with a new random state')
                    break

        print('NO SOLUTION FOUND IN THIS RESTART.. MOVING TO THE NEXT ONE!')

    print("No solution found from any of the restarts we will be returning None")
    return None, restart_number

def print_board(state):
    n = len(state)
    for i in range(n):
        row = ['.'] * n
        row[state[i]] = 'Q'
        print(' '.join(row))

def main():
    

    n = list(range(4, 20))
    time_taken = []
    
    for i in n:
    
        start_time = time.time()
        soln = hill_climbing_with_sidewise_walk_added(i)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_taken.append(elapsed_time)
        print(f"Time taken to find solution for n = {i} is {elapsed_time} seconds")
    
    plt.plot(n, time_taken)
    plt.title('Time taken to find solution for n-Queens problem')
    plt.xlabel('Number of Queens')
    plt.ylabel('Time taken (seconds)')
    plt.grid(True)
    plt.title('time taken to find solution for n- Queens problem')
    plt.savefig('time_taken_sideways_hill_climbing.png')
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()
