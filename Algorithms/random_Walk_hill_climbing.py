#now we will combine random walk to hill climbing to create a new algo that may find the optimal soln as in the global optima
"""random walk + hill climbing
when we find a local optima we will do a random walk to any of the neighbour and start hill climbing again
this may help us to prevent landing in a local optima and help us to find the global optima
as the algo (random walk) is asymptotically convergent to the global optima

in a few lines: 
 if getting soln -  as in the heuristic is 0 then we return the soln
 else we if we stuck in local optima -- randomly walk to any of the neighbour and start hill climbing again
"""

import random
import time
import matplotlib.pyplot as plt

#we will be implementing this algo on a n queens problem

#is conflict function
def is_conflict(state_1, state_2, board):
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
    
#heuristic function
def heuristic_function(state):
    #counting the number of conflicts in the state
    problems = 0 
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if is_conflict(i,j, state):
                problems += 1
    return problems


#generating neighbours function
def generating_neighbours(state):
    #initialising an empty list to store the neighbours
    neighbours = []

    #how many queens we have
    n = len(state)

    #generating all possible neighbours of a state
    for first_Col in range(n):
        for second_Col in range(first_Col + 1, n):
                new_State = state.copy()
                new_State[first_Col], new_State[second_Col] = (
                    new_State[second_Col],
                    new_State[first_Col],
                )
                neighbours.append(new_State)

    return neighbours

#main algo
def random_walk_combined_hill_climbing(n, max_restarts = 1000):
    for restart_no in range(1, max_restarts+1):

        #generating a random state
        current_State = random.sample(range(n), n)

        #getting the heuristic value of the current state
        current_heuristic = heuristic_function(current_State)

        #printing the details of the current state and heuristic value
        print(f"restart number : {restart_no}")
        print(f"current state : {current_State}")
        print(f"current heuristic : {current_heuristic}")

        while True:

            if current_heuristic == 0:
                print(f"solution found : {current_State}")
                print(f"total restarts : {restart_no}")
                return current_State

            #now we generating the neighbours of the current state
            neighbours = generating_neighbours(current_State)

            #choose the neighbour with the least heuristic value
            best_neighbour = min(neighbours, key=heuristic_function)    

            #gettinhg the heuristic value of the best neighbour
            best_neighbour_heuristic = heuristic_function(best_neighbour)
            print(f"best neighbour : {best_neighbour}")
            print(f"best neighbour heuristic : {best_neighbour_heuristic}")

            #if we encounter a local optima
            if best_neighbour_heuristic >= current_heuristic:
                print('local optima encountered.. walking randomly to a neighbour and starting hill climbing again')
                lucky_neighbour = random.choice(neighbours)
                current_State = lucky_neighbour
                current_heuristic = heuristic_function(current_State)
                restart_no += 1
                if restart_no > max_restarts:
                    print('maximum restarts reached without finding a solution')
                    return None
                print(f"restart number : {restart_no}")
                print(f"current state : {current_State}")
            else:
                #moving to the best neighbour
                current_State = best_neighbour
                current_heuristic = best_neighbour_heuristic
                print('we did not encounter a local optima.. moving to the best neighbour')
                print(f"current state without a random walk to a neighbour : {current_State}")
                print(f"current heuristic value : {current_heuristic}")

        print('no solution found in this restart, moving to next restart')
    print('no solution found in any of the restarts')
    return None, max_restarts

def print_board(state):
    n = len(state)
    for i in range(n):
        row = ['.'] * n
        row[state[i]] = 'Q'
        print(' '.join(row))


def main():
    """

    no_of_queens = int(input("Enter the number of queens: "))

    if no_of_queens <= 3:
        print("No solution exists for 3 or fewer queens.")
        return

    soln = random_walk_combined_hill_climbing(no_of_queens)
    if soln is not None:
        print("Solution found:")
        print_board(soln)
    else:
        print("No solution found.")"""


   #we want to generate n queens soln for n = 4 to n = 20 and print the time taken to find the soln for each n
   #and we want to plot the time taken to find the soln for each n

    n = list(range(4, 21))
    time_taken = []

    for i in n:
        start_Time = time.time()
        soln = random_walk_combined_hill_climbing(i)
        end_Time = time.time()
        time_taken.append(end_Time - start_Time)
        print(f"Time taken for {i} queens: {end_Time - start_Time:.2f} seconds")

    #now plotting the time taken to find the soln for each n
    plt.plot(n, time_taken)
    plt.xlabel('Number of Queens')
    plt.ylabel('Time taken (seconds)')
    plt.title('Time taken to find solution for n-Queens problem ')
    plt.grid()
    plt.tight_layout()
    plt.savefig('time_taken_random_walk_hill_climbing.png')
    plt.show()
    plt.close()




if __name__ == "__main__":
    main()

            

