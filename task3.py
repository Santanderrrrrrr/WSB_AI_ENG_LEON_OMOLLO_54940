import pygad
import numpy
import time
start = time.time()
print("timer started")


S = [1, 2, 4, 6, 10, 19, 25, 29, 30, 41, 51, 60, 70, 79, 80, 5, 22, 33, 66, 11, 18, 26, 9, 31, 40, 45, 61, 69, 77, 12, 14, 58, 63, 72, 20, 88, 66, 28, 34, 16, 18, 17]

# define all possible genes
gene_space = [0, 1]

#define the number of genes in a chromosome/solution
num_genes = len(S)

# define the fitness function
# how to grade chromosomes?
def fitness_func(solution, solution_idx):
    sum1 = numpy.sum(solution * S)
    solution_invert = 1 - solution
    sum2 = numpy.sum(solution_invert * S)
    fitness = -numpy.abs(sum1-sum2)
    #other possible formula: fitness = 1.0 / (1.0 + numpy.abs(sum1-sum2))
    return fitness

fitness_function = fitness_func

# size of the population
sol_per_pop = 10

# percentage of the population to become parents * 0.1
num_parents_mating = 5

# percentage of parents reproducing to live with children * 0.1
keep_parents = 2

# maximal number of generations
num_generations = 300


# type of selection
parent_selection_type = "sss"

# type of crossover
crossover_type = "single_point"

# how should mutation work?
# set the percentage to: round_up(100/num_genes)
mutation_type = "random"
mutation_percent_genes = 3

# initiate the algorithm, gice all the parameters from above
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=["reach_0"])

# run the algorithm, it will start the generation cycle
ga_instance.run()

# summary: we return the solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

# we can additionaly give the best fitness
prediction = numpy.sum(S*solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

end = time.time()
print("amount of time taken is: ", end - start)

# show a plot of the best solution fitness throughout the generations
ga_instance.plot_fitness()

