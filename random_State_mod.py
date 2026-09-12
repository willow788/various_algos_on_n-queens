
import random
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

def random_state_n_queens_with_memory(n, max_steps=100000):

    #init the board with random positions
    
    steps = 0
    database = set()

    #checckinng if this state is previusly present in the data
    while(steps< max_steps):
        curr_state = tuple(random.sample(range(n), n))

        #we will check if it is in the database or not
        if curr_state in database:
            print('this state has been previously generated and no soln is obtained from it')
        else:
            print('this state has not been previously generated!')
            database.add(curr_state)
            steps += 1
            conflict_present = conflicting_queens(curr_state)

            if not conflict_present:
                print('Solution found')
                print(f"final state obtained: {curr_state} in total steps: {steps}")
                return curr_state, steps
            print("conflict is present thus will will be generating a new state")
            curr_state = tuple(random.sample(range(n), n))
            steps += 1
    print('no soln foound!')
    return None, steps


def print_board(state):
    n = len(state)
    for i in range(n):
        row = ['.'] * n
        row[state[i]] = 'Q'
        print(' '.join(row))

def main():
   soln = random_state_n_queens_with_memory(8)
   
   print(soln)
   


if __name__ == "__main__":
    main()

            

