import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

# Evolve the whole genetic algorithm until termination has been reached
# consider_termination is defaulted to True
ga.evolve()

# Print out the current generation and the population
ga.print_generation()
ga.print_population()

# set generations
ga2 = EasyGA.GA()

ga2.evolve(number_of_generations=200, consider_termination=False)

# Print out the current generation and the population
ga2.print_generation()
ga2.print_population()

# set generations
ga3 = EasyGA.GA()

ga3.evolve(consider_termination=False)

# Print out the current generation and the population
ga3.print_generation()
ga3.print_population()
