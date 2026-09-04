import random

#we will implement random state algo 
#very similar to random walk
#steps -->
#first define the conflict function -->
#then define the queen conflict function -->
#then implement the random state algo -->
#main function

def is_conflict(state_1, state_2, board):
    #conflict when two queens on same row or col or diagonal
    row_1 = state_1
    row_2 = state_2
    col_1 = board[state_1] 
    col_2 = board[state_2]

    if row_1 == row_2:
        return True
    elif col_1 == col_2:
        return True
    elif abs(row_1 - row_2) == abs(col_1 - col_2):
        return True
    else:
        return False


#defining the function to find the conflicted queens
def conflicting_queens(state):
    problems = []
    l = len(state)
    for i in range(l):
        
        for j in range(l):
            
            if i != j and is_conflict(i,j, state):
                problems.append(i)
                break

    return problems

def random_state_n_queens(n, max_steps=100000):

    #init the board with random positions
    curr_state = random.sample(range(n), n)
    steps = 0
    
    while (steps < max_steps):

        #counting the number of conflicts
        conflicts = conflicting_queens(curr_state)

        if not conflicts:
            print('the solution has been found!')
            print('final state: ', curr_state)
            print('steps taken: ', steps
                  )
            return curr_state, steps
        else:

            #if soln is not found then randomly generate a new state
            #and try again
            print('conflicts found: ', conflicts)
            print('current state: ', curr_state)
            print('we are generating a new state...')
            curr_state = random.sample(range(n), n)
            steps += 1

    print('no solution found in ', max_steps, ' steps') 
    print('final state: ', curr_state)
    return None, steps


def print_board(state):
    n = len(state)
    for i in range(n):
        row = ['.'] * n
        row[state[i]] = 'Q'
        print(' '.join(row))

def finding_Avg_steps():
    iters = 100
    steps_list = []
    for _ in range(iters):
        soln = random_state_n_queens(8)
        if soln:
            steps_list.append(soln[1])
    if not steps_list:
        return None
    return sum(steps_list) / len(steps_list)


def main():
   print("Average steps:", finding_Avg_steps())

if __name__ == "__main__":
    main()

            
