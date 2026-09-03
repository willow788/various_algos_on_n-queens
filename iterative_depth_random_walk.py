import random
#we will implement the trival algo first

def is_conflict(i, j, board):

    #queen in the same row
    row1 = i
    row2 = j
    col1 = board[i]
    col2 = board[j]

    if row1 == row2:
        return True
    elif col1 == col2:
        return True
    elif abs(row1 - row2) == abs(col1 - col2):
        return True
    else:
        return False

def conflicted_queens(state):
    problems = []
    l = len(state)
    for i in range(l):
        for j in range(l):
            if i != j and is_conflict(i, j, state):
                problems.append(i)
                break
    return problems

def random_walk_n_queens(n, max_steps):
    #initialize the board with random positions
    #we will increase the max_steps iteraticely if we do not find a solution
    
    current_max_steps = max_steps
    while True:
        state = [random.randrange(n) for _ in range(n)]
        steps = 0

        while (steps < current_max_steps):

            #count the number of conflicts
            conflicts = conflicted_queens(state)
            if not conflicts:
                print("Solution found in ", steps, " steps")
                print("Final state: ", state)
                return state

            #if conflicts exist, randomly select a queen and move it to a new position
            victim_queen = random.choice(conflicts)
            victim_index = victim_queen

            #randomly select a new position for the victim queen
            new_pos_for_victim = random.randrange(n)

            #move the victim queen to the new position
            state[victim_index] = new_pos_for_victim

            steps += 1

        print("No solution found in ", current_max_steps, " steps")
        current_max_steps += 1
        print("Increasing max_steps and trying again...")
        print("New max_steps: ", current_max_steps)

def print_board(state):
    n = len(state)
    for i in range(n):
        row = ['.'] * n
        row[state[i]] = 'Q'
        print(' '.join(row))

if __name__ == "__main__":
    sol = random_walk_n_queens(8, 1)
    if sol:
        print_board(sol)
    else:
        print("No solution found")



        






