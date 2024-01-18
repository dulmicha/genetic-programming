from MiniLang.MGlib import *
from read_data import read_data
from parameters import Params


example = "1_1_A"
file_name = f"../antlr/test/example_{example}.txt"
params = Params(
    max_depth=2,
    max_width=2,
    population_size=10,
    generations=5,
    tournament_size=3,
    crossover_prob=0.7,
    mutation_prob=0.1,
)
inputs, outputs = read_data(file_name)
print("inputs: ", inputs)
print("outputs: ", outputs)
mglib = MGlib(inputs=inputs, outputs=outputs, parameters=params, example=example)
mglib.display_population_fitness()
mglib.run()
