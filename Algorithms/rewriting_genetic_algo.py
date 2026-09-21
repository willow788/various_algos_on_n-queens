#i wanted to rewrite the algo
import random

#first defining the function to create a random chromosome
def random_chromosome(size):
    chromosome = [random.randint(1, nq) for _ in range(nq)]

    return chromosome

def fitness(chromosome):
    n = len(chromosome)

    #horizontal collisions
    hor_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2

    #vertical collisions
    vert_collisions = 0

    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n

    for i in range(n):

        #left diagonal will be the sum of the row and column indices
        left_diagonal[i + chromosome[i] - 1] += 1

        #right diagonal[n- i + chromosome[i] - 2] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1
#now we will calculate the number of collisions in the diagonals
    for i in range(2 * n - 1):

        #initializing the counter to 0
        counter = 0

        #if the diagonal has more than one queen -- it is a collision
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
            #
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1

        #total number of collisions in the diagonals
        diagonal_collisions += counter / (n - abs(i - n + 1))

    return int(maxFitness - (hor_collisions + diagonal_collisions))


def probability(chromosome, fitness):

    prob = fitness(chromosome) / maxFitness
    return prob

def random_pick(population, probabilities):

    #defing population with probability
    population_with_probability = zip(population, probabilities)

    #total weight of the population
    total = sum(w for c, w in population_with_probability)

    #randomly picking a number between 0 and total weight
    r = random.uniform(0, total)

    #initializing the counter to 0
    counter = 0

    #iterating through the population and their probabilities
    for people, weight in zip(population, probabilities):

        #if the counter and weight together is greater than r 
        #then return the chromosome -- why?
        #because probabilty of that chromosome is greater than the random number generated
        #which means it is more likely to be selected -- more fit chromosome
        if counter + weight >= r:
            return people
        else:
            #not selected -- add the weight to the counter and continue
            counter += weight

    assert False, "Shouldn't get here"

#now we will cross over two chromosomes to create a new chromosome
def reproduce(chromosome_1, chromosome_2):

    #length = len(chromosome_1)
    l = len(chromosome_1)

    #chose a random index to cross over like the position of the queen in the row
    c = random.randint(0, l - 1)

    #now cross over
    newChromosome = chromosome_1[0:c] + chromosome_2[c:l]

    return newChromosome

#mutating a chromosome by changing the position of a queen in a row
def mutate(chromosome):
    #length = len(chromosome)
    l = len(chromosome)

    #chose a random index to mutate like the position of the queen in the row
    c = random.randint(0, l - 1)

    #chose a random value to mutate like the position of the queen in the column
    m = random.randint(1, l)

    #mutate the chromosome
    chromosome[c] = m

    return chromosome

#now creating the genetic algorithm function
def genetic_queen(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities) #best chromosome 1
        y = random_pick(population, probabilities) #best chromosome 2
        child = reproduce(x, y) #creating two new chromosomes from the best 2 chromosomes
        if random.random() < mutation_probability:
            child = mutate(child)

        new_population.append(child)
        if fitness(child) == maxFitness: break

        return new_population


def print_chromosome(chromosome):
    print("Chromosome = {},  Fitness = {}".format(str(chromosome), fitness(chromosome)))

if __name__ == "__main__":
    nq = int(input("Enter Number of Queens: ")) #say N = 8
    maxFitness = (nq*(nq-1))/2  # 8*7/2 = 28
    population = [random_chromosome(nq) for _ in range(100)]
    
    generation = 1
    
    while not maxFitness in [fitness(chrom) for chrom in population]:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population, fitness)
        print("")
        print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1
    chrom_out = []
    print("Solved in Generation {}!".format(generation-1))
    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("")
            print("One of the solutions: ")
            chrom_out = chrom
            print_chromosome(chrom)
    
    board = []
    
    for x in range(nq):
        board.append(["x"] * nq)
    
    for i in range(nq):
        board[nq-chrom_out[i]][i]="Q"
    
    
    def print_board(board):
        for row in board:
            print (" ".join(row))
    
    print()
    print_board(board)
    
    
    
    
    
