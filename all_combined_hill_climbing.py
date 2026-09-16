# All Combined Hill Climbing
#we will be combining random walk and hill climbing to solve the n-queens problem and also random state too

"""combined approach of random walk and hill climbing to solve the n-queens problem
if no conflict found -- then return the solution
else if a local optima is encountered -- then we will with some probability either do a random walk or a restart.
 """

import random
import matplotlib.pyplot as plt
import time

def is_Conflict(state_1, state_2, board):
    row_1 = state_1
    row_2 = state_2
    col_1 = board[state_1]
    col_2 = board[state_2]

    #conflict conditions
    #same row , col or diagonal
    if row_1 == row_2:
        return True
    elif col_1 == col_2:
        return True
    elif abs(row_1 - row_2) == abs(col_1 - col_2):
        return True
    else:  
        return False

def and_my_heuristic_is(state):
    #counting the number of conflicts in the state
    problems = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if is_Conflict(i,j, state):
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

def all_combined_hill_climbing(n, max_restarts = 1000):

    for restart_no in range(1, max_restarts+1):
        steps = 0

        #generating a random state for n queens
        current_State = random.sample(range(n), n)

        #heuristic value of the current state
        current_heuristic = and_my_heuristic_is(current_State)

        #printing the current state and its heuristic value
        print(f"Restart {restart_no}")
        print(f"current state : {current_State}")
        print(f"current heuristic : {current_heuristic}")

        while True:
            steps += 1
            if steps > n * n:
                print(f"step limit reached for restart {restart_no}, moving to the next restart")
                break

            #checking if the current state is a solution
            if current_heuristic == 0:
                print(f"Solution found after {restart_no} restarts")
                print(f"solution : {current_State}")
                return current_State

            #else finding the neighbours of the current state
            neighbours = generating_neighbours(current_State)

            #finding the neighbour with the least heuristic value
            best_neighbour = min(neighbours, key=and_my_heuristic_is)

            #generating the heuristic value of the best neighbour
            best_Neighbour_Heuristic = and_my_heuristic_is(best_neighbour)

            if current_heuristic <= best_Neighbour_Heuristic:
                print(f"we are stuck at a local optima!")

                #now we generate a probability to either do a random walk or a restart
                prob_To_Do_random_walk = random.randint(0, 1)

                if prob_To_Do_random_walk == 1:
                    print(f"doing a random walk!")
                    print(f"value of prob_To_Do_random_walk : {prob_To_Do_random_walk}")

                    #generating a random neighbour of the current state
                    random_neighbour = random.choice(neighbours)
                    current_State = random_neighbour
                    current_heuristic = and_my_heuristic_is(current_State)
                    print(f"current state after random walk : {current_State}")
                    print(f"current heuristic after random walk : {current_heuristic}")
                else:
                    print(f"doing a random restart!")

                    #generating a random state for n queens
                    random_state = random.sample(range(n), n)
                    current_State = random_state
                    current_heuristic = and_my_heuristic_is(current_State)
                    print(f"current state after random restart : {current_State}")
                    print(f"current heuristic after random restart : {current_heuristic}")
                    break

        print(f"no solution found in this restart, moving to next restart")
    print(f"no solution found in any of the restarts")

    return None, max_restarts

def print_board(state):
    n = len(state)
    for i in range(n):
        row = ['.'] * n
        row[state[i]] = 'Q'
        print(' '.join(row))

def main():
    n = int(input("Enter the number of queens: "))
    if n <= 3:
        print("No solution exists for n <= 3")
        return
    else:
        soln = all_combined_hill_climbing(n)
        if soln is not None:
            print("Solution found:")
            print_board(soln)
        else:
            print("No solution found.")

if __name__ == "__main__":
    main()
            
            

  

