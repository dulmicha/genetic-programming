from MiniLang.MGlib import *
from read_data import read_data
from parameters import Params
from fitness_functions import *

file_name = '../antlr/test/example_1_1_A.txt'
params = Params(max_depth=2, max_width=2, population_size=10, generations=5, tournament_size=3,
                crossover_prob=0.7, mutation_prob=0.1)
inputs, outputs = read_data(file_name)
print("inputs: ", inputs)
print("outputs: ", outputs)
mglib = MGlib(inputs=inputs, outputs=outputs, parameters=params)
mglib.display_population_fitness()
mglib.run()
