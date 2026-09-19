#we will try bfs on n queens problem
#BFS is a complete algorithm and will always find a solution if it exists
#bfs will work but it will take a lot of time and space to find a solution for large n

import queue
import random
import time
from collections import deque
import matplotlib.pyplot as plt

# Define a function to check if a position is valid
def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


# Define a function to generate heuristic value of a state
def heuristic_function(state):
    problems = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            same_column = state[i] == state[j]
            same_diagonal = abs(state[i] - state[j]) == abs(i - j)
            if same_column or same_diagonal:
                problems += 1
    return problems

#defining if it is the goal state or not
def is_goal_state(state, n):

    #find the heuristic value of the state
    state_heuristic_value = heuristic_function(state)
    if len(state) == n and state_heuristic_value == 0:
        return True
    else:
        return False

#generating all possible neighbours of a state
def generating_neighbours(state, n):

    #initialise an empty list
    neighbours = []

    row = len(state)
    for col in range(n):

        #if the row is valid  then we will add it
        if is_valid(state, row, col):

            new_State = state.copy()
            new_State.append(col)

            neighbours.append(new_State)

    return neighbours

#defining the n queens bfs function
def bfs_n_queens(n):
    initial_state = []

    queue = deque()
    queue.append(initial_state)

    while queue:

        #pop the first state from the queue
        #then check if it is the goal state or not
        #if  goal then return the state
        #if not -- generate tge neighbours and add them to the queue
        #then repeat the process untill queue is empty

        #step_1: generate the current state
        current_State = queue.popleft()

        #step_2: check if it is the goal state or not
        if is_goal_state(current_State, n):
            return current_State
        else:
            #step_3: generate the neighbours of the current state
            neighbours = generating_neighbours(current_State, n)

            #step_4: ad the neighbours to the queue
            for next_queen in neighbours:
                queue.append(next_queen)

        #step_5: repeat the process until the queue is empty

    return None

def print_board(state):
    n = len(state)
    for i in range(n):
        row = ['.'] * n
        row[state[i]] = 'Q'
        print(' '.join(row))
    print()


#defining the main function to run the bfs on n queens problem
def main():
    """
    n = int(input("enter the value of n: "))

    if n <= 3:
        print("No solution exists for n <= 3")
        return
    else:
        print(f"we can find a solution for n = {n} using bfs")
        soln = bfs_n_queens(n)
        if soln:
            print(f"solution found for n = {n} is : {soln}")
            print_board(soln)
        else:
            print(f"no solution found for n = {n}")
    """

    #NOW WE WILL OBSERVE THE BEHAVIOR
    i = list(range(4, 15))
    time_taken_values = []

    #we will see how long it takes to find a solution for different values of n
    for n in i:

        starting_time = time.time()

        #find a solution for n queens problem using bfs
        soln = bfs_n_queens(n)

        ending_time = time.time()

        time_taken = ending_time - starting_time
        time_taken_values.append(time_taken)
        print(f"Time taken for n = {n}: {time_taken:.2f} seconds")

    # Plot the time taken to find a solution for each value of n.
    plt.plot(i, time_taken_values, marker='o', label='Time taken')
    plt.xlabel('Number of queens (n)')
    plt.ylabel('time taken (seconds)')
    plt.title('BFS on N-Queens')
    plt.grid()
    plt.legend()
    plt.show()
        



if __name__ == "__main__":
    main()
    


    

 





    

