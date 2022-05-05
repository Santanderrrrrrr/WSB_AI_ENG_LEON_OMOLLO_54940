import pygad
import numpy
import time

start = time.time()
print("timer started")

#######################################

item_names = ["clock", "painting_nature", "painting_portrait", "radio", "laptop", "lamp", "silver_cutlery", "porcerlain_cups", "bronze_statue", "leather_bag", "vacuum_cleaner"]
item_values = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
item_weights = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]
desired_output = 25
# define all possible genes
gene_space = [0, 1]
S=item_weights

#define the number of genes in a chromosome/solution
num_genes = len(S)

# define the fitness function
# how to grade chromosomes?
def fitness_func(solution, solution_idx):
    sum1 = numpy.sum(solution * S)
    solution_invert = 1 - solution
    sum2 = numpy.sum(solution_invert * S)
    # fitness = -numpy.abs(sum1-sum2)
    fitness = 1/(1 + numpy.abs(sum1-desired_output))
    return fitness

fitness_function = fitness_func

# size of the population
sol_per_pop = 10

# percentage of the population to become parents * 0.1
num_parents_mating = 5

# percentage of parents reproducing to live with children * 0.1
keep_parents = 3

# maximal number of generations
num_generations = 1000


# type of selection
parent_selection_type = "sss"

# type of crossover
crossover_type = "single_point"

# how should mutation work?
# set the percentage to: round_up(100/num_genes)
mutation_type = "random"
mutation_percent_genes = 10

# initiate the algorithm, give all the parameters from above
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
                       stop_criteria=["reach_1"])



# run the algorithm, it will start the generation cycle
while True:
    ga_instance.run()
        # if numpy.sum(ga_instance.best_solution().solution * item_values)==1630:
        #     break


    # summary: we return the solution
    solution, solution_fitness, solution_idx = ga_instance.best_solution()

    iteration = 0
    summer = 0

    def summation (iteration, solution, summer):
        for x in solution:
            summer += item_values[iteration]*x
            iteration += 1
        return summer

    while summation != 1630:
        ga_instance.run()

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

